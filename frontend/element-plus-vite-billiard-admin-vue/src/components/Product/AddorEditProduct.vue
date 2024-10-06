<template>
    <el-card class="card_body">
        <el-form
            ref="ruleFormRef"
            :model="ruleForm"
            :rules="rules"
            label-width="auto"
            class="demo-ruleForm"
            :size="formSize"
            status-icon
        >
            <el-form-item label="Danh mục" prop="maDanhMuc">
                <el-select
                    v-model="ruleForm.maDanhMuc"
                    filterable
                    placeholder="Vui lòng chọn"
                >
                    <el-option
                        v-for="item in optionsCategory"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value"
                    />
                </el-select>
            </el-form-item>

            <el-form-item label="Danh mục ưu đãi" prop="madanhmucuudai">
                <el-select
                    v-model="ruleForm.madanhmucuudai"
                    filterable
                    placeholder="Vui lòng chọn"
                >
                    <el-option
                        v-for="item in optionsCategoryOffer"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value"
                    />
                </el-select>
            </el-form-item>

            <el-form-item label="Tên sản phẩm" prop="tenSanPham">
                <el-input v-model="ruleForm.tenSanPham" type="textarea" />
            </el-form-item>

            <el-form-item label="Ảnh sản phẩm" prop="anhDaiDien">
                <el-upload
                    :file-list="fileListAvatar"
                    class="upload-demo"
                    :action="uploadProps.action"
                    :on-remove="handleRemoveAvatar"
                    :on-change="handlerChange"
                    list-type="picture-card"
                >
                    <el-icon><Plus /></el-icon>
                </el-upload>
            </el-form-item>

            <el-form-item label="Ảnh chi tiết sản phẩm" prop="anhChiTiet">
                <el-upload
                    :file-list="fileListImgDetail"
                    class="upload-demo"
                    :action="uploadProps.action"
                    :before-remove="beforeRemoveImgDetail"
                    :on-change="handlerChangeImgDetail"
                    :on-success="handleUploadSuccess"
                    list-type="picture-card"
                    :multiple="!route.params.id"
                >
                    <el-icon><Plus /></el-icon>
                </el-upload>
            </el-form-item>

            <el-form-item label="Giá nhập" prop="gianhap">
                <el-input v-model="ruleForm.gianhap" type="number" disabled />
            </el-form-item>

            <el-form-item label="Giá (Giá nhập + 50%)" prop="gia">
                <el-input v-model="ruleForm.gia" type="number" disabled />
            </el-form-item>

            <el-form-item label="Giá Giảm (Giá nhập + 30%)" prop="giaGiam">
                <el-input v-model="ruleForm.giaGiam" type="number" />
            </el-form-item>

            <el-form-item label="Số lượng" prop="soLuong">
                <el-input v-model="ruleForm.soLuong" type="number" disabled />
            </el-form-item>

            <el-form-item label="Trọng lượng" prop="trongLuong">
                <el-input v-model="ruleForm.trongLuong" type="text" />
            </el-form-item>

            <el-form-item label="Trạng thái" prop="trangThai">
                <el-select
                    v-model="ruleForm.trangThai"
                    placeholder="Vui lòng chọn"
                >
                    <el-option label="Hoạt động" :value="true" />
                    <el-option label="Tắt" :value="false" />
                </el-select>
            </el-form-item>

            <el-form-item label="Nhà sản xuất" prop="maNhaSanXuat">
                <el-select
                    v-model="ruleForm.maNhaSanXuat"
                    filterable
                    placeholder="Vui lòng chọn"
                >
                    <el-option
                        v-for="item in optionsManufactor"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value"
                    />
                </el-select>
            </el-form-item>

            <el-form-item label="Nhà phân phối" prop="maNhaPhanPhoi">
                <el-select
                    v-model="ruleForm.maNhaPhanPhoi"
                    filterable
                    placeholder="Vui lòng chọn"
                >
                    <el-option
                        v-for="item in optionsDistributor"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value"
                    />
                </el-select>
            </el-form-item>

            <el-form-item label="Xuất xứ" prop="xuatXu">
                <el-input v-model="ruleForm.xuatXu" type="text" />
            </el-form-item>

            <el-form-item label="Mô tả" prop="moTa">
                <el-input v-model="ruleForm.moTa" :rows="4" type="textarea" />
            </el-form-item>

            <el-form-item label="Chi tiết" prop="chiTiet">
                <ckeditor :editor="editor" v-model="ruleForm.chiTiet" />
            </el-form-item>

            <el-form-item>
                <el-button type="primary" @click="submitForm(ruleFormRef)">
                    {{ route.params.id ? "Update" : "Create" }}
                </el-button>
                <el-button @click="resetForm(ruleFormRef)">Reset</el-button>
            </el-form-item>
        </el-form>
    </el-card>
</template>

<script setup lang="ts">
import { reactive, ref, onMounted } from "vue";
import type {
    ComponentSize,
    FormInstance,
    FormRules,
    UploadFile,
    UploadProps,
    UploadUserFile,
} from "element-plus";
import { Plus } from "@element-plus/icons-vue";
import { FormProduct, ImgDetail, OptionSelect } from "~/constant/api";
import {
    createProduct,
    getbyIdProduct,
    getbyImgDetailProduct,
    getCategory,
    getCategoryOffer,
    getDistributor,
    getManufactor,
    updateProduct,
} from "~/services/product.service";
import { apiImage } from "~/constant/request";
import { useUserStore } from "~/store";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";
import { ElMessage } from "element-plus";
import router from "~/router";
import { useRoute } from "vue-router";

const formSize = ref<ComponentSize>("default");
const ruleFormRef = ref<FormInstance>();
const useStore = useUserStore();
const token = useStore.user.token;
const route = useRoute();

const editor = ClassicEditor;

const Notification = (
    message: string,
    type: "success" | "warning" | "error"
) => {
    ElMessage({
        message: message,
        type: type,
    });
};

const ruleForm = reactive<FormProduct>({
    maChiTietSanPham: 0,
    maDanhMuc: 1,
    madanhmucuudai: 1,
    tenSanPham: "",
    anhDaiDien: "",
    anhChiTiet: [],
    gianhap: 0,
    gia: 0,
    giaGiam: 0,
    soLuong: 0,
    luotBan: 0,
    danhGia: 0,
    trongLuong: "",
    trangThai: true,
    maNhaSanXuat: 1,
    maNhaPhanPhoi: 1,
    xuatXu: "",
    moTa: "",
    chiTiet: "",
});

const rules = reactive<FormRules>({
    maDanhMuc: [
        {
            required: true,
            message: "Vui lòng chọn danh mục",
            trigger: "blur",
        },
    ],
    madanhmucuudai: [
        {
            required: true,
            message: "Vui lòng chọn danh mục ưu đãi",
            trigger: "blur",
        },
    ],
    tenSanPham: [
        {
            required: true,
            message: "Vui lòng nhập tên sản phẩm",
            trigger: "blur",
        },
    ],
    anhDaiDien: [
        {
            required: true,
            message: "Vui lòng thêm ảnh sản phẩm",
            trigger: "blur",
        },
    ],
    anhChiTiet: [
        {
            required: true,
            message: "Vui lòng thêm ảnh chi tiết sản phẩm",
            trigger: "blur",
        },
    ],
    trongLuong: [
        {
            required: true,
            message: "Vui lòng nhập trọng lượng",
            trigger: "blur",
        },
    ],
    trangThai: [
        {
            required: true,
            message: "Vui lòng chọn trạng thái",
            trigger: "blur",
        },
    ],
    maNhaSanXuat: [
        {
            required: true,
            message: "Vui lòng chọn nhà sản xuất",
            trigger: "blur",
        },
    ],
    maNhaPhanPhoi: [
        {
            required: true,
            message: "Vui lòng nhập nhà phân phối",
            trigger: "blur",
        },
    ],
    xuatXu: [
        {
            required: true,
            message: "Vui lòng nhập xuất xứ",
            trigger: "blur",
        },
    ],
    moTa: [
        {
            required: true,
            message: "Vui lòng nhập mô tả sản phẩm",
            trigger: "blur",
        },
    ],
    chiTiet: [
        {
            required: true,
            message: "Vui lòng nhập chi tiết sản phẩm",
            trigger: "blur",
        },
    ],
});

const optionsCategoryOffer = ref<OptionSelect[]>();

async function fetchCategoryOffer() {
    const res = await getCategoryOffer();
    ruleForm.madanhmucuudai = Number(res[0].madanhmucuudai);
    optionsCategoryOffer.value = res.map(function (value: any) {
        return {
            value: value.madanhmucuudai,
            label: value.tendanhmucuudai,
        };
    });
}
onMounted(() => {
    fetchCategoryOffer();
});

const optionsCategory = ref<OptionSelect[]>();

async function fetchCategory() {
    const res = await getCategory();
    ruleForm.maDanhMuc = Number(res[0]?.maDanhMuc);
    optionsCategory.value = res.map(function (value: any) {
        return {
            value: value.maDanhMuc,
            label: value.tenDanhMuc,
        };
    });
}
onMounted(() => {
    fetchCategory();
});

const optionsManufactor = ref<OptionSelect[]>();

async function fetchManufactor() {
    const res = await getManufactor();
    ruleForm.maNhaSanXuat = Number(res[0]?.maNhaSanXuat);
    optionsManufactor.value = res.map(function (value: any) {
        return {
            value: value.maNhaSanXuat,
            label: value.tenHang,
        };
    });
}
onMounted(() => {
    fetchManufactor();
});

const optionsDistributor = ref<OptionSelect[]>();

async function fetchDistributor() {
    const res = await getDistributor();
    ruleForm.maNhaPhanPhoi = Number(res[0]?.maNhaPhanPhoi);
    optionsDistributor.value = res.map(function (value: any) {
        return {
            value: value.maNhaPhanPhoi,
            label: value.tenNhaPhanPhoi,
        };
    });
}
onMounted(() => {
    fetchDistributor();
});

const fetchImgDetail = async (id: number) => {
    const resDetailImg = await getbyImgDetailProduct(id);

    fileListImgDetail.value = resDetailImg.map((imgDetail: ImgDetail) => ({
        uid: imgDetail.id,
        name: imgDetail.linkAnh,
        url: apiImage + imgDetail.linkAnh,
    }));

    ruleForm.anhChiTiet = resDetailImg.map((imgDetail: ImgDetail) => ({
        uid: imgDetail.id,
        linkAnh: imgDetail.linkAnh,
        status: 4,
    }));
};

const getDetailProduct = async (id: number) => {
    const resDetaiProduct = await getbyIdProduct(id);
    ruleForm.maChiTietSanPham = resDetaiProduct?.maChiTietSanPham;
    ruleForm.maDanhMuc = resDetaiProduct?.maDanhMuc;
    ruleForm.madanhmucuudai = resDetaiProduct?.madanhmucuudai;
    ruleForm.tenSanPham = resDetaiProduct?.tenSanPham;
    ruleForm.anhDaiDien = resDetaiProduct?.anhDaiDien;
    ruleForm.gianhap = resDetaiProduct?.gianhap;
    ruleForm.gia = resDetaiProduct?.gia;
    ruleForm.giaGiam = resDetaiProduct?.giaGiam;
    ruleForm.soLuong = resDetaiProduct?.soLuong;
    ruleForm.luotBan = resDetaiProduct?.luotBan;
    ruleForm.danhGia = resDetaiProduct?.danhGia;
    ruleForm.trongLuong = resDetaiProduct?.trongLuong;
    ruleForm.trangThai = resDetaiProduct?.trangThai;
    ruleForm.maNhaSanXuat = resDetaiProduct?.maNhaSanXuat;
    ruleForm.maNhaPhanPhoi = resDetaiProduct?.maNhaPhanPhoi;
    ruleForm.xuatXu = resDetaiProduct?.xuatXu;
    ruleForm.moTa = resDetaiProduct?.moTa;
    ruleForm.chiTiet = resDetaiProduct?.chiTiet;

    fileListAvatar.value = [
        {
            name: resDetaiProduct.anhDaiDien,
            url: apiImage + resDetaiProduct.anhDaiDien,
        },
    ];

    fetchImgDetail(id);
};

onMounted(() => {
    if (route.params.id) {
        getDetailProduct(Number(route.params.id));
    }
});

const uploadProps = {
    name: "file",
    action: `${apiImage}/api-admin/Image/upload`,
    headers: {
        authorization: `Bearer ${token}`,
    },
};

const fileListAvatar = ref<UploadUserFile[]>([]);

const handlerChange = (file: UploadUserFile, fileList: UploadUserFile[]) => {
    fileListAvatar.value = fileList.slice(-1);
    ruleForm.anhDaiDien = "/img/" + fileListAvatar.value[0].name;
    console.log(ruleForm.anhDaiDien);
};

const handleRemoveAvatar: UploadProps["onRemove"] = (
    uploadFile,
    uploadFiles
) => {
    ruleForm.anhDaiDien = "";
};

const fileListImgDetail = ref<UploadUserFile[]>([]);

const handlerChangeImgDetail = async (
    file: UploadUserFile,
    fileList: UploadUserFile[]
) => {
    fileListImgDetail.value = fileList;

    ruleForm.anhChiTiet = fileList.map((file) => {
        return {
            linkAnh: "/img/" + file.name,
            status: 1,
        };
    });
};

const handleUploadSuccess = async (
    response: any,
    file: UploadFile,
    fileList: UploadUserFile[]
) => {
    if (route.params.id) {
        await updateProduct({
            MaSanPham: Number(route.params.id),
            MaDanhMuc: ruleForm.maDanhMuc,
            Madanhmucuudai: ruleForm.madanhmucuudai,
            TenSanPham: ruleForm.tenSanPham,
            AnhDaiDien: ruleForm.anhDaiDien,
            Gia: ruleForm.gia,
            GiaGiam: ruleForm.giaGiam,
            SoLuong: ruleForm.soLuong,
            TrongLuong: ruleForm.trongLuong,
            TrangThai: ruleForm.trangThai,
            XuatXu: ruleForm.xuatXu,
            list_json_chitiet_sanpham: [
                {
                    MaChiTietSanPham: ruleForm.maChiTietSanPham,
                    MaNhaSanXuat: ruleForm.maNhaSanXuat,
                    MoTa: ruleForm.moTa,
                    ChiTiet: ruleForm.chiTiet,
                    status: 2,
                },
            ],
            list_json_sanpham_nhaphanphoi: [
                {
                    MaSanPham: route.params.id,
                    MaNhaPhanPhoi: ruleForm.maNhaPhanPhoi,
                    status: 2,
                },
            ],
            list_json_anhsanpham: [
                {
                    LinkAnh: "/img/" + file.name,
                    status: 1,
                },
            ],
        });
        fetchImgDetail(Number(route.params.id));
        Notification("Thêm ảnh thành công", "success");
    }
};

const beforeRemoveImgDetail = async (
    file: UploadUserFile,
    fileList: UploadUserFile[]
) => {
    if (fileList.length <= 1) {
        Notification("Phải có ít nhất 1 ảnh", "warning");
        return false;
    }
    await updateProduct({
        MaSanPham: Number(route.params.id),
        MaDanhMuc: ruleForm.maDanhMuc,
        Madanhmucuudai: ruleForm.madanhmucuudai,
        TenSanPham: ruleForm.tenSanPham,
        AnhDaiDien: ruleForm.anhDaiDien,
        Gia: ruleForm.gia,
        GiaGiam: ruleForm.giaGiam,
        SoLuong: ruleForm.soLuong,
        TrongLuong: ruleForm.trongLuong,
        TrangThai: ruleForm.trangThai,
        XuatXu: ruleForm.xuatXu,
        list_json_chitiet_sanpham: [
            {
                MaChiTietSanPham: ruleForm.maChiTietSanPham,
                MaNhaSanXuat: ruleForm.maNhaSanXuat,
                MoTa: ruleForm.moTa,
                ChiTiet: ruleForm.chiTiet,
                status: 2,
            },
        ],
        list_json_sanpham_nhaphanphoi: [
            {
                MaSanPham: route.params.id,
                MaNhaPhanPhoi: ruleForm.maNhaPhanPhoi,
                status: 2,
            },
        ],
        list_json_anhsanpham: [
            {
                Id: file.uid,
                status: 3,
            },
        ],
    });
    Notification("Xoá ảnh thành công", "success");
    return true;
};

const submitForm = async (formEl: FormInstance | undefined) => {
    if (!formEl) return;

    try {
        const valid = await formEl.validate();
        if (valid) {
            if (route.params.id) {
                await updateProduct({
                    MaSanPham: Number(route.params.id),
                    MaDanhMuc: ruleForm.maDanhMuc,
                    Madanhmucuudai: ruleForm.madanhmucuudai,
                    TenSanPham: ruleForm.tenSanPham,
                    AnhDaiDien: ruleForm.anhDaiDien,
                    Gia: ruleForm.gia,
                    GiaGiam: ruleForm.giaGiam,
                    SoLuong: ruleForm.soLuong,
                    TrongLuong: ruleForm.trongLuong,
                    TrangThai: ruleForm.trangThai,
                    XuatXu: ruleForm.xuatXu,
                    list_json_chitiet_sanpham: [
                        {
                            MaChiTietSanPham: ruleForm.maChiTietSanPham,
                            MaNhaSanXuat: ruleForm.maNhaSanXuat,
                            MoTa: ruleForm.moTa,
                            ChiTiet: ruleForm.chiTiet,
                            status: 2,
                        },
                    ],
                    list_json_sanpham_nhaphanphoi: [
                        {
                            MaSanPham: route.params.id,
                            MaNhaPhanPhoi: ruleForm.maNhaPhanPhoi,
                            status: 2,
                        },
                    ],
                    list_json_anhsanpham: [
                        {
                            LinkAnh: "",
                            status: 0,
                        },
                    ],
                });
                Notification("Cập nhật thành công", "success");
                router.push("/product");
            } else {
                await createProduct({
                    MaDanhMuc: ruleForm.maDanhMuc,
                    Madanhmucuudai: ruleForm.madanhmucuudai,
                    TenSanPham: ruleForm.tenSanPham,
                    AnhDaiDien: ruleForm.anhDaiDien,
                    Gia: 0,
                    GiaGiam: 0,
                    SoLuong: 0,
                    TrongLuong: ruleForm.trongLuong,
                    TrangThai: ruleForm.trangThai,
                    XuatXu: ruleForm.xuatXu,
                    list_json_chitiet_sanpham: [
                        {
                            MaNhaSanXuat: ruleForm.maNhaSanXuat,
                            MoTa: ruleForm.moTa,
                            ChiTiet: ruleForm.chiTiet,
                        },
                    ],
                    list_json_sanpham_nhaphanphoi: [
                        {
                            MaNhaPhanPhoi: ruleForm.maNhaPhanPhoi,
                        },
                    ],
                    list_json_anhsanpham: ruleForm.anhChiTiet,
                });
                Notification("Thêm thành công", "success");
                router.push("/product");
            }
        } else {
            Notification("Bạn cần điền đủ thông tin", "warning");
            console.log("error submit!");
        }
    } catch (fields) {
        Notification("Bạn cần điền đủ thông tin", "warning");
        console.log("error submit!", fields);
    }
};

const resetForm = (formEl: FormInstance | undefined) => {
    if (!formEl) return;
    formEl.resetFields();
    fileListAvatar.value = [];
    fileListImgDetail.value = [];
};
</script>

<style>
.demo-ruleForm {
    max-width: 800px;
    margin: auto;
}

.ep-form-item__content {
    display: flex;
    justify-content: center;
}
</style>
