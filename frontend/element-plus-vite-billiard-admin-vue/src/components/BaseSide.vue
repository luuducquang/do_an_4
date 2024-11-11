<template>
    <el-menu
        :default-active="activeIndex"
        class="el-menu-vertical-demo"
        :collapse="isCollapse"
        @open="handleOpen"
        @close="handleClose"
    >
        <el-sub-menu index="1">
            <template #title>
                <el-icon><House /></el-icon>
                <span>Tổng quan</span>
            </template>
            <router-link to="/">
                <el-menu-item index="1-1">Trang chủ</el-menu-item>
            </router-link>
        </el-sub-menu>

        <el-sub-menu index="">
            <template #title>
                <el-icon><Box /></el-icon>
                <span>Quản lý bàn</span>
            </template>
            <router-link to="/tabletype">
                <el-menu-item index="3">Loại bàn</el-menu-item>
            </router-link>
            <router-link to="/table">
                <el-menu-item index="4">Bàn</el-menu-item>
            </router-link>
            <router-link to="/pricingrule">
                <el-menu-item index="5">Quy tắc giá</el-menu-item>
            </router-link>
        </el-sub-menu>

        <el-sub-menu index="">
            <template #title>
                <el-icon><Mug /></el-icon>
                <span>Sản phẩm</span>
            </template>
            <router-link to="/menuitem">
                <el-menu-item index="6">Đồ ăn</el-menu-item>
            </router-link>
            <router-link to="/rentalitem">
                <el-menu-item index="7">Đồ thuê</el-menu-item>
            </router-link>
        </el-sub-menu>

        <el-sub-menu index="3-4">
            <template #title>
                <el-icon><Ship /></el-icon>
                <span>Nhân viên</span>
            </template>
            <router-link to="/employeetype">
                <el-menu-item index="8">Loại nhân viên</el-menu-item>
            </router-link>
            <router-link to="/employee">
                <el-menu-item index="9">Nhân viên</el-menu-item>
            </router-link>
            <router-link to="/shift">
                <el-menu-item index="10">Ca làm việc</el-menu-item>
            </router-link>
            <router-link to="/employeepayment">
                <el-menu-item index="11">Lương</el-menu-item>
            </router-link>
        </el-sub-menu>

        <router-link to="/news">
            <el-menu-item index="12">
                <el-icon><Files /></el-icon>
                <template #title>Tin tức</template>
            </el-menu-item>
        </router-link>

        <el-sub-menu index="13-14">
            <template #title>
                <el-icon><CollectionTag /></el-icon>
                <span>Danh mục</span>
            </template>
            <router-link to="/categorymenuitem">
                <el-menu-item index="13">Danh mục đồ ăn</el-menu-item>
            </router-link>
            <router-link to="/categoryrentalitem">
                <el-menu-item index="14">Danh mục thuê</el-menu-item>
            </router-link>
        </el-sub-menu>

        <el-sub-menu index="">
            <template #title>
                <el-icon><OfficeBuilding /></el-icon>
                <span>Nhà cung cấp</span>
            </template>
            <router-link to="/manufactor">
                <el-menu-item index="15">Hãng sản xuất</el-menu-item>
            </router-link>
            <router-link to="/supplier">
                <el-menu-item index="16">Nhà phân phối</el-menu-item>
            </router-link>
        </el-sub-menu>

        <el-sub-menu index="">
            <template #title>
                <el-icon><User /></el-icon>
                <span>Tài khoản</span>
            </template>
            <router-link to="/typeaccount">
                <el-menu-item index="17">Loại tài khoản</el-menu-item>
            </router-link>
            <router-link to="/account">
                <el-menu-item index="18">Tài khoản</el-menu-item>
            </router-link>
        </el-sub-menu>
    </el-menu>
</template>

<script lang="ts" setup>
import { ref, computed } from "vue";
import { useRoute } from "vue-router";
import {
    House,
    Document,
    Menu as IconMenu,
    Tickets,
    Notebook,
    Files,
    ChatLineRound,
    CollectionTag,
    PriceTag,
    OfficeBuilding,
    School,
    CreditCard,
    Picture,
    Connection,
    User,
    Mug,
    Ship,
    Box,
} from "@element-plus/icons-vue";

const isCollapse = ref(false);

const route = useRoute();

const activeIndex = computed(() => {
    const path = route.path;
    if (path === "/") return "1-1";
    // if (path.startsWith("/product")) return "2";
    // if (path.startsWith("/billsell")) return "3";
    // if (path.startsWith("/importbill")) return "4";
    // if (path.startsWith("/news")) return "5";
    // if (path.startsWith("/rate")) return "6";
    // if (path.startsWith("/category")) return "7";
    // if (path.startsWith("/categoryoffer")) return "8";
    // if (path.startsWith("/manufactor")) return "9";
    // if (path.startsWith("/supplier")) return "10";
    // if (path.startsWith("/advertisement")) return "11";
    // if (path.startsWith("/slide")) return "12";
    // if (path.startsWith("/typeaccount")) return "13";
    // if (path.startsWith("/account")) return "14";

    return "0";
});

const handleOpen = (key: string, keyPath: string[]) => {
    // console.log(key, keyPath);
};
const handleClose = (key: string, keyPath: string[]) => {
    // console.log(key, keyPath);
};
</script>

<style lang="scss" scoped>
a {
    text-decoration: none;
    color: #333;
}

.el-menu-vertical-demo {
    min-width: 192px;
    overflow-y: scroll;
}
</style>
