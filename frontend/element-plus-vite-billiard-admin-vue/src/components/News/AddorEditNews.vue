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
            <el-form-item label="Tiêu đề" prop="tieuDe">
                <el-input v-model="ruleForm.tieuDe" :rows="4" type="textarea" />
            </el-form-item>

            <el-form-item label="Ảnh sản phẩm" prop="hinhAnh">
                <el-upload
                    :file-list="fileListImg"
                    class="upload-demo"
                    :action="uploadProps.action"
                    :on-remove="handleRemoveImg"
                    :on-change="handlerChange"
                    list-type="picture-card"
                >
                    <el-icon><Plus /></el-icon>
                </el-upload>
            </el-form-item>

            <el-form-item label="Trạng thái" prop="trangThai">
                <el-select
                    v-model="ruleForm.trangThai"
                    placeholder="Vui lòng chọn"
                >
                <el-option label="Hiện" value="Hiện" />
                    <el-option label="Ẩn" value="Ẩn" />
                </el-select>
            </el-form-item>

            <el-form-item label="Nội dung" prop="noiDung">
                <ckeditor :editor="editor" v-model="ruleForm.noiDung" />
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
import { useUserStore } from "~/store";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";
import { ElMessage } from "element-plus";
import router from "~/router";
import { useRoute } from "vue-router";
import { News } from "~/constant/api";
import { apiImage } from "~/constant/request";
import { createNew, getbyIdNews, updateNew } from "~/services/news.service";

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

const ruleForm = reactive<News>({
    tieuDe: "",
    hinhAnh: "",
    trangThai: "Hiện",
    noiDung: "",
});

const rules = reactive<FormRules>({
    tieuDe: [
        {
            required: true,
            message: "Vui lòng nhập tiêu đề",
            trigger: "blur",
        },
    ],
    hinhAnh: [
        {
            required: true,
            message: "Vui lòng chọn ảnh",
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
    noiDung: [
        {
            required: true,
            message: "Vui lòng nhập nội dung",
            trigger: "blur",
        },
    ],
});

const uploadProps = {
    name: "file",
    action: `${apiImage}/api-admin/Image/upload`,
    headers: {
        authorization: `Bearer ${token}`,
    },
};

const fileListImg = ref<UploadUserFile[]>([]);

const handlerChange = (file: UploadUserFile, fileList: UploadUserFile[]) => {
    fileListImg.value = fileList.slice(-1);
    ruleForm.hinhAnh = "/img/" + fileListImg.value[0].name;
};

const handleRemoveImg: UploadProps["onRemove"] = (uploadFile, uploadFiles) => {
    ruleForm.hinhAnh = "";
};

const fetchById = async (id: number) => {
    const resNewId = await getbyIdNews(id);
    ruleForm.tieuDe = resNewId?.tieuDe;
    ruleForm.hinhAnh = resNewId?.hinhAnh;
    ruleForm.trangThai = resNewId?.trangThai;
    ruleForm.noiDung = resNewId?.noiDung;

    fileListImg.value = [
        {
            name: resNewId.hinhAnh,
            url: apiImage + resNewId.hinhAnh,
        },
    ];
};

onMounted(() => {
    if (route.params.id) {
        fetchById(Number(route.params.id));
    }
});

const submitForm = async (formEl: FormInstance | undefined) => {
    if (!formEl) return;

    try {
        const valid = await formEl.validate();
        if (valid) {
            if (route.params.id) {
                await updateNew({
                    MaTinTuc: Number(route.params.id),
                    TieuDe: ruleForm.tieuDe,
                    NoiDung: ruleForm.noiDung,
                    HinhAnh: ruleForm.hinhAnh,
                    MaTaiKhoan: useStore.user.mataikhoan,
                    TrangThai: ruleForm.trangThai,
                });
                Notification("Cập nhật thành công", "success");
                router.push("/news");
            } else {
                await createNew({
                    TieuDe: ruleForm.tieuDe,
                    NoiDung: ruleForm.noiDung,
                    HinhAnh: ruleForm.hinhAnh,
                    MaTaiKhoan: useStore.user.mataikhoan,
                    TrangThai: ruleForm.trangThai,
                });
                Notification("Thêm thành công", "success");
                router.push("/news");
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
    fileListImg.value = [];
};
</script>
