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
            <el-form-item label="Danh mục" prop="category_name">
                <el-input v-model="ruleForm.category_name" />
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
import type { ComponentSize, FormInstance, FormRules } from "element-plus";
import { Plus } from "@element-plus/icons-vue";
import { ElMessage } from "element-plus";
import router from "~/router";
import { useRoute } from "vue-router";
import { Categorys, News } from "~/constant/api";
import { apiImage } from "~/constant/request";
import {
    createCategory,
    getbyIdCategory,
    updateCategory,
} from "~/services/categorymenuitem.service";

const formSize = ref<ComponentSize>("default");
const ruleFormRef = ref<FormInstance>();
const route = useRoute();

const Notification = (
    message: string,
    type: "success" | "warning" | "error"
) => {
    ElMessage({
        message: message,
        type: type,
    });
};

const ruleForm = reactive<Categorys>({
    category_name: "",
});

const rules = reactive<FormRules>({
    category_name: [
        {
            required: true,
            message: "Vui lòng nhập tên danh mục",
            trigger: "blur",
        },
    ],
});

const fetchById = async (id: string) => {
    const resNewId = await getbyIdCategory(id);
    ruleForm.category_name = resNewId?.category_name;
};

onMounted(() => {
    if (route.params.id) {
        fetchById(String(route.params.id));
    }
});

const submitForm = async (formEl: FormInstance | undefined) => {
    if (!formEl) return;

    try {
        const valid = await formEl.validate();
        if (valid) {
            if (route.params.id) {
                await updateCategory({
                    _id: String(route.params.id),
                    category_name: ruleForm.category_name,
                });
                Notification("Cập nhật thành công", "success");
                router.push("/categorymenuitem");
            } else {
                await createCategory({
                    category_name: ruleForm.category_name,
                });
                Notification("Thêm thành công", "success");
                router.push("/categorymenuitem");
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
};
</script>
