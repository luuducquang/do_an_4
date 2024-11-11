<template>
    <AppSlide />
    <div class="container">
        <HeaderComponent title="Sản phẩm sale" link="" :isShowLink="false" />
        <div class="row" v-if="productSale">
            <div
                class="col-xl-2 col-lg-3 col-md-4 col-sm-4 col-6 mb-4 d-flex"
                v-for="product in productSale"
                :key="product.maSanPham"
            >
                <ItemProductHome :product="product" :isSale="true" />
            </div>
        </div>

        <HeaderComponent
            title="Sản phẩm ưa thích"
            link=""
            :isShowLink="false"
        />
        <div class="row" v-if="productFavourite">
            <div
                class="col-xl-2 col-lg-3 col-md-4 col-sm-4 col-6 mb-4 d-flex"
                v-for="product in productFavourite"
                :key="product.maSanPham"
            >
                <ItemProductHome :product="product" :isSale="false" />
            </div>
        </div>

        <HeaderComponent
            v-if="productSerum"
            title="Serum"
            :link="'/category/serum'"
            :isShowLink="true"
        />
        <div class="row" v-if="productSerum">
            <div
                class="col-xl-2 col-lg-3 col-md-4 col-sm-4 col-6 mb-4 d-flex"
                v-for="product in productSerum"
                :key="product.maSanPham"
            >
                <ItemProductHome :product="product" :isSale="false" />
            </div>
        </div>

        <HeaderComponent
            v-if="productCleanser"
            title="Sữa rửa mặt"
            :link="'/category/sữa rửa mặt'"
            :isShowLink="true"
        />
        <div class="row" v-if="productCleanser">
            <div
                class="col-xl-2 col-lg-3 col-md-4 col-sm-4 col-6 mb-4 d-flex"
                v-for="product in productCleanser"
                :key="product.maSanPham"
            >
                <ItemProductHome :product="product" :isSale="false" />
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { type Product } from "~/constant/api";
import { getProductFavourite, getProductHome } from "~/services/home.service";
import { onMounted, ref } from "vue";
import Cookies from "js-cookie";
import { getGioHangByIdTaiKhoan } from "~/services/cart.service";
import { useCartStore } from "~/store";

useHead({
    title: "Trang chủ",
});

const productSale = ref<Product[]>([]);
const productFavourite = ref<Product[]>([]);
const productSerum = ref<Product[]>([]);
const productCleanser = ref<Product[]>([]);
const store = useCartStore();

const { data: saleData, error: erSale } = await useAsyncData(
    "productSale",
    () =>
        getProductHome({
            page: 1,
            pageSize: 12,
            Tendanhmucuudai: "FlagSale",
        })
);

if (saleData.value) {
    productSale.value = saleData.value?.data;
} else if (erSale.value) {
    console.error("Error while fetching products:", erSale.value);
}

const { data: favouriteData, error: favouriteError } = await useAsyncData(
    "productFavourite",
    () => getProductFavourite()
);

if (favouriteData.value) {
    productFavourite.value = favouriteData.value;
} else if (favouriteError.value) {
    console.error(
        "Error while fetching favourite products:",
        favouriteError.value
    );
}

const { data: serumData, error: erSerum } = await useAsyncData(
    "productSerum",
    () =>
        getProductHome({
            page: 1,
            pageSize: 12,
            TenDanhMuc: "Serum",
        })
);

if (serumData.value) {
    productSerum.value = serumData.value?.data;
} else if (erSerum.value) {
    console.error("Error while fetching products:", erSale.value);
}

const { data: cleanserData, error: erCleanser } = await useAsyncData(
    "productCleanser",
    () =>
        getProductHome({
            page: 1,
            pageSize: 12,
            TenDanhMuc: "Sữa rửa mặt",
        })
);

if (cleanserData.value) {
    productCleanser.value = cleanserData.value?.data;
} else if (erCleanser.value) {
    console.error("Error while fetching products:", erSale.value);
}

onMounted(async () => {
    const customerData = Cookies.get("customer");
    if (customerData) {
        try {
            const customer = JSON.parse(customerData);
            const cart = await getGioHangByIdTaiKhoan(customer.mataikhoan);

            store.setCart(cart);
        } catch (error) {
            console.error("Failed to parse customer data from cookies:", error);
        }
    }
});
</script>
