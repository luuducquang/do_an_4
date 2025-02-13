<template>
    <el-card title="Login Admin" class="login-card">
        <el-form
            :model="formState"
            @submit.native.prevent="handleSubmit"
            label-position="top"
        >
            <el-form-item
                label="Tài khoản"
                :error="username.errorMsg"
                :status="username.validateStatus"
            >
                <el-input
                    v-model="formState.username"
                    placeholder="Vui lòng nhập tài khoản"
                    type="text"
                />
            </el-form-item>

            <el-form-item
                label="Mật khẩu"
                :error="password.errorMsg"
                :status="password.validateStatus"
            >
                <el-input
                    v-model="formState.password"
                    placeholder="Vui lòng nhập mật khẩu"
                    type="password"
                />
            </el-form-item>

            <el-form-item>
                <el-button
                    type="primary"
                    native-type="submit"
                    :loading="loading"
                    block
                    >Login</el-button
                >
            </el-form-item>
        </el-form>
    </el-card>
</template>

<script setup lang="ts">
import { ref, reactive } from "vue";
import { useRouter } from "vue-router";
import { ElMessage } from "element-plus";
import { login } from "~/services/login.service";
import { useUserStore } from "~/store";

const Notification = (
    message: string,
    type: "success" | "warning" | "error"
) => {
    ElMessage({
        message: message,
        type: type,
    });
};

const formState = reactive({
    username: "",
    password: "",
});

const username = ref({
    validateStatus: "",
    errorMsg: "",
});

const password = ref({
    validateStatus: "",
    errorMsg: "",
});

const loading = ref(false);
const userStore = useUserStore();
const router = useRouter();

const validateForm = () => {
    let isValid = true;
    if (!formState.username) {
        username.value.validateStatus = "error";
        username.value.errorMsg = "Vui lòng nhập tài khoản";
        isValid = false;
    } else {
        username.value.validateStatus = "";
        username.value.errorMsg = "";
    }

    if (!formState.password) {
        password.value.validateStatus = "error";
        password.value.errorMsg = "Vui lòng nhập mật khẩu";
        isValid = false;
    } else {
        password.value.validateStatus = "";
        password.value.errorMsg = "";
    }

    return isValid;
};

const handleSubmit = async () => {
    if (validateForm()) {
        loading.value = true;
        try {
            setTimeout(async function () {
                try {
                    const res = await login({
                        username: formState.username,
                        password: formState.password,
                    });
                    if (res?.role_name === "ADMIN") {
                        loading.value = false;
                        userStore.setUser(res);
                        router.push("/");
                        Notification(
                            `Đăng nhập thành công. Xin chào, ${res?.fullname}`,
                            "success"
                        );
                    } else {
                        Notification(
                            "Tài khoản khách hàng không thể vào đây!",
                            "warning"
                        );
                        loading.value = false;
                    }
                } catch (error) {
                    Notification(
                        "Tài khoản hoặc mật khẩu không chính xác!",
                        "warning"
                    );
                    loading.value = false;
                }
            }, 1000);
        } catch (error) {
            console.error("Error submitting form:", error);
        }
    }
};
</script>

<style scoped>
.login-card {
    max-width: 400px;
    margin: 100px auto;
    padding: 20px;
}
</style>
