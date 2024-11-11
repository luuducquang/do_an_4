<template>
    <div class="container mt-5">
        <form @submit.prevent="handleUpdateInformation">
            <div class="mb-3">
                <label for="avatar" class="form-label">Avatar</label>
                <input
                    type="file"
                    class="form-control"
                    id="avatar"
                    @change="handleAvatarChange"
                />
                <img
                    v-if="fileList.length"
                    :src="fileList[0].url"
                    class="img-thumbnail mt-2"
                    alt="avatar"
                />
                <img
                    v-else-if="formData.anhDaiDien"
                    :src="formData.anhDaiDien"
                    class="img-thumbnail mt-2"
                    alt="avatar"
                />
                <p v-if="formData.fileName">{{ formData.fileName }}</p>
            </div>
            <div class="mb-3">
                <label for="hoTen" class="form-label">Họ tên</label>
                <input
                    type="text"
                    class="form-control"
                    id="hoTen"
                    v-model="formData.hoTen"
                />
            </div>
            <div class="mb-3">
                <label for="soDienThoai" class="form-label"
                    >Số điện thoại</label
                >
                <input
                    type="text"
                    class="form-control"
                    id="soDienThoai"
                    v-model="formData.soDienThoai"
                />
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">Email</label>
                <input
                    type="email"
                    class="form-control"
                    id="email"
                    v-model="formData.email"
                />
            </div>
            <div class="mb-3">
                <label for="matKhau" class="form-label">Mật khẩu</label>
                <input
                    type="password"
                    class="form-control"
                    id="matKhau"
                    v-model="formData.matKhau"
                />
            </div>
            <div class="mb-3">
                <label for="diaChi" class="form-label">Địa chỉ</label>
                <textarea
                    class="form-control"
                    id="diaChi"
                    v-model="formData.diaChi"
                ></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Cập nhật</button>
        </form>
    </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from "vue";
import { useRouter } from "vue-router";
import Cookies from "js-cookie";
import axios from "axios";
import {
    getInformation,
    updateInformation,
} from "~/services/information.service";
import { apiImage } from "~/constant/request";
import { uploadImage } from "~/services/upload.service";
import { login } from "~/services/login.service";

interface FormData {
    hoTen: string;
    soDienThoai: string;
    email: string;
    diaChi: string;
    anhDaiDien: string;
    matKhau: string;
    fileName: string;
    file: File | null;
}

const router = useRouter();
const fileList = ref<{ url: string }[]>([]);
const formData = reactive<FormData>({
    hoTen: "",
    soDienThoai: "",
    email: "",
    diaChi: "",
    anhDaiDien: "",
    matKhau: "",
    fileName: "",
    file: null as File | null,
});

const handleAvatarChange = async (event: Event) => {
    const input = event.target as HTMLInputElement;
    const file = input.files?.[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = async (e) => {
            fileList.value = [{ url: e.target?.result as string }];
            formData.anhDaiDien = e.target?.result as string;
            formData.fileName = file.name;
            formData.file = file;
        };
        reader.readAsDataURL(file);
    }
};

const fetchDataCart = async () => {
    const customerData = Cookies.get("customer");
    if (customerData) {
        try {
            const customer = JSON.parse(customerData);
            const dataUser = await getInformation(customer.mataikhoan);
            console.log(dataUser);
            formData.hoTen = String(dataUser[0]?.hoTen);
            formData.soDienThoai = String(dataUser[0]?.soDienThoai);
            formData.email = String(dataUser[0]?.email);
            formData.diaChi = String(dataUser[0]?.diaChi);
            formData.matKhau = String(dataUser[0]?.matKhau);
            formData.anhDaiDien = apiImage + dataUser[0]?.anhDaiDien;
            formData.fileName = "";
            formData.file = null;
        } catch (error) {
            console.error("Failed to parse customer data from cookies:", error);
            Cookies.remove("customer");
            router.push("/login");
        }
    } else {
        router.push("/login");
    }
};

onMounted(async () => {
    fetchDataCart();
});

const handleUpdateInformation = async () => {
    try {
        const formData2 = new FormData();
        const customerData = Cookies.get("customer");
        if (customerData) {
            const customer = JSON.parse(customerData);
            const dataUser = await getInformation(customer.mataikhoan);

            if (formData.file) {
                formData2.append("file", formData.file);
                await uploadImage(formData2);
                await updateInformation({
                    MaTaiKhoan: customer.mataikhoan,
                    TenTaiKhoan: customer.taikhoan,
                    MatKhau: formData.matKhau,
                    Email: formData.email,
                    list_json_chitiet_taikhoan: [
                        {
                            MaChitietTaiKhoan: dataUser[0].maChitietTaiKhoan,
                            MaLoaitaikhoan: dataUser[0].maLoaitaikhoan,
                            AnhDaiDien: "/img/" + formData.fileName,
                            HoTen: formData.hoTen,
                            DiaChi: formData.diaChi,
                            SoDienThoai: formData.soDienThoai,
                            status: 2,
                        },
                    ],
                });
            } else {
                await updateInformation({
                    MaTaiKhoan: customer.mataikhoan,
                    TenTaiKhoan: customer.taikhoan,
                    MatKhau: formData.matKhau,
                    Email: formData.email,
                    list_json_chitiet_taikhoan: [
                        {
                            MaChitietTaiKhoan: dataUser[0].maChitietTaiKhoan,
                            MaLoaitaikhoan: dataUser[0].maLoaitaikhoan,
                            AnhDaiDien: dataUser[0].anhDaiDien,
                            HoTen: formData.hoTen,
                            DiaChi: formData.diaChi,
                            SoDienThoai: formData.soDienThoai,
                            status: 2,
                        },
                    ],
                });
            }
            const res = await login({
                username: String(dataUser[0].tenTaiKhoan),
                password: String(dataUser[0].matKhau),
            });
            Cookies.set("customer", JSON.stringify(res), { expires: 1 });
            window.location.reload();
        }
    } catch (error) {
        console.error("Lỗi khi cập nhật thông tin:", error);
    }
};
</script>

<style scoped>
.container {
    max-width: 600px;
}
.img-thumbnail {
    max-width: 150px;
    height: auto;
}
</style>
