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
            <el-menu-item-group>
                <el-menu-item index="1-1">Trang chủ</el-menu-item>
            </el-menu-item-group>
        </el-sub-menu>

        <router-link to="/product">
            <el-menu-item index="2">
                <el-icon><Mug /></el-icon>
                <template #title>Thông tin sản phẩm</template>
            </el-menu-item>
        </router-link>

        <el-sub-menu index="3-4">
            <template #title>
                <el-icon><Tickets /></el-icon>
                <span>Hóa đơn</span>
            </template>
            <router-link to="/billsell">
                <el-menu-item index="3">Hoá đơn bán</el-menu-item>
            </router-link>
            <router-link to="/importbill">
                <el-menu-item index="4">Hoá đơn nhập</el-menu-item>
            </router-link>
        </el-sub-menu>

        <router-link to="/news">
            <el-menu-item index="5">
                <el-icon><Files /></el-icon>
                <template #title>Tin tức</template>
            </el-menu-item>
        </router-link>

        <router-link to="/rate">
            <el-menu-item index="6">
                <el-icon><ChatLineRound /></el-icon>
                <template #title>Đánh giá</template>
            </el-menu-item>
        </router-link>

        <el-sub-menu index="7-8">
            <template #title>
                <el-icon><CollectionTag /></el-icon>
                <span>Danh mục</span>
            </template>
            <router-link to="/category">
                <el-menu-item index="7">Danh mục đồ ăn</el-menu-item>
            </router-link>
        </el-sub-menu>

        <el-sub-menu index="9-10">
            <template #title>
                <el-icon><OfficeBuilding /></el-icon>
                <span>Nhà cung cấp</span>
            </template>
            <router-link to="/manufactor">
                <el-menu-item index="9">Hãng sản xuất</el-menu-item>
            </router-link>
            <router-link to="/distributor">
                <el-menu-item index="10">Nhà phân phối</el-menu-item>
            </router-link>
        </el-sub-menu>

        <el-sub-menu index="13-14">
            <template #title>
                <el-icon><User /></el-icon>
                <span>Tài khoản</span>
            </template>
            <router-link to="/typeaccount">
                <el-menu-item index="13">Loại tài khoản</el-menu-item>
            </router-link>
            <router-link to="/account">
                <el-menu-item index="14">Tài khoản</el-menu-item>
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
} from "@element-plus/icons-vue";

const isCollapse = ref(false);

const route = useRoute();

const activeIndex = computed(() => {
    const path = route.path;
    if (path === "/") return "1-1";
    if (path.startsWith("/product")) return "2";
    if (path.startsWith("/billsell")) return "3";
    if (path.startsWith("/importbill")) return "4";
    if (path.startsWith("/news")) return "5";
    if (path.startsWith("/rate")) return "6";
    if (path.startsWith("/category")) return "7";
    if (path.startsWith("/categoryoffer")) return "8";
    if (path.startsWith("/manufactor")) return "9";
    if (path.startsWith("/distributor")) return "10";
    if (path.startsWith("/advertisement")) return "11";
    if (path.startsWith("/slide")) return "12";
    if (path.startsWith("/typeaccount")) return "13";
    if (path.startsWith("/account")) return "14";

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
