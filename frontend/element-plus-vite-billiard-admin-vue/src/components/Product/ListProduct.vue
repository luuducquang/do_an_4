<template>
    <el-card class="card_content" v-loading="loading">
        <div class="button_add">
            <el-button @click="handlerAdd" type="primary"
                ><el-icon><CirclePlus /></el-icon>
            </el-button>
        </div>
        <el-table :data="tableData" class="table_content">
            <el-table-column label="Sản phẩm" align="center" prop="tenSanPham">
                <template #default="scope">
                    <span :title="scope.row.tenSanPham" class="name_product">{{
                        scope.row.tenSanPham
                    }}</span>
                </template></el-table-column
            >
            <el-table-column label="Hình ảnh" align="center" prop="anhDaiDien">
                <template #default="scope">
                    <img
                        :src="apiImage + scope.row.anhDaiDien"
                        alt="Hình ảnh sản phẩm"
                        class="img_item"
                    /> </template
            ></el-table-column>
            <el-table-column label="Giá bán" align="center" prop="giaGiam">
                <template #default="scope">
                    <span>{{
                        parseInt(scope.row.giaGiam).toLocaleString("en-US")
                    }}</span>
                </template>
            </el-table-column>
            <el-table-column label="Số lượng" align="center" prop="soLuong" />
            <el-table-column label="Lượt bán" align="center" prop="luotBan" />
            <el-table-column label="Đánh giá" align="center" prop="danhGia">
                <template #default="scope">
                    <span class="rate_product" :title="scope.row.danhGia"
                        ><span>{{ scope.row.danhGia }}</span
                        ><el-icon class="rate_product_star"
                            ><StarFilled /></el-icon
                    ></span>
                </template>
            </el-table-column>
            <el-table-column
                label="Trọng lượng"
                align="center"
                prop="trongLuong"
            />
            <el-table-column
                label="Danh mục"
                align="center"
                prop="tenDanhMuc"
            />
            <el-table-column
                label="Ưu đãi"
                align="center"
                prop="tendanhmucuudai"
            />
            <el-table-column label="Trạng thái" align="center" prop="trangThai">
                <template #default="scope">
                    <p
                        :style="{
                            color:
                                scope.row.trangThai === true
                                    ? '#33CC33'
                                    : '#CC3333',
                        }"
                    >
                        {{ scope.row.trangThai === true ? "Hoạt động" : "Tắt" }}
                    </p>
                </template></el-table-column
            >
            <el-table-column align="right">
                <template #header>
                    <el-input
                        v-model="search"
                        size="small"
                        placeholder="Nhập tên sản phẩm"
                    />
                </template>
                <template #default="scope">
                    <el-button
                        size="small"
                        @click="handleEdit(scope.$index, scope.row)"
                    >
                        Edit
                    </el-button>

                    <el-popconfirm
                        confirm-button-text="Yes"
                        cancel-button-text="No"
                        icon-color="#626AEF"
                        title="Bạn có muốn xoá không?"
                        @confirm="() => confirmEvent(scope.row.maSanPham)"
                    >
                        <template #reference>
                            <el-button size="small" type="danger">
                                Delete
                            </el-button>
                        </template>
                    </el-popconfirm>
                </template>
            </el-table-column>
        </el-table>
        <div class="pagination_wrapper">
            <el-pagination
                background
                layout="prev, pager, next"
                v-model:current-page="currentPage"
                :total="totalItemPage"
            />
        </div>
    </el-card>
</template>

<script lang="ts" setup>
import { computed, onMounted, ref, watch } from "vue";
import { useUserStore } from "~/store";
import { CirclePlus, StarFilled } from "@element-plus/icons-vue";
import { apiImage } from "~/constant/request";
import { deleteProduct, searchProduct } from "~/services/product.service";
import debounce from "~/utils/debounce";
import { Product } from "~/constant/api";
import router from "~/router";
import { ElMessage } from "element-plus";

const Notification = (
    message: string,
    type: "success" | "warning" | "error"
) => {
    ElMessage({
        message: message,
        type: type,
    });
};

const search = ref("");
const loading = ref(false);

const tableData = ref<Product[]>([]);

const currentPage = ref(1);
const totalItemPage = ref(0);

watch(currentPage, (newPage: number, oldPage: number) => {
    if (newPage !== oldPage) {
        fetchData(search.value);
    }
});

const handleEdit = (index: number, row: Product) => {
    router.push(`/product/edit/${row.maSanPham}`);
};

const confirmEvent = async (Id: number) => {
    try {
        await deleteProduct([Id]);
        Notification("Xoá thành công", "success");
        fetchData(search.value);
    } catch (error) {
        console.error("Error deleting =:", error);
        Notification("Lỗi khi xoá =", "error");
    }
};

const fetchData = async (searchTerm = "") => {
    loading.value = true;
    try {
        const payLoad = {
            page: currentPage.value,
            pageSize: 10,
            TenSanPham: searchTerm,
        };
        const res = await searchProduct(payLoad);
        totalItemPage.value = res.totalItems;
        tableData.value = res.data;
    } catch (error) {
        console.error("Error fetching:", error);
        tableData.value = [];
    } finally {
        loading.value = false;
    }
};

const debouncedFetchData = debounce(fetchData, 300);

watch(search, (newSearch) => {
    debouncedFetchData(newSearch);
});

onMounted(() => {
    fetchData(search.value);
});

const handlerAdd = () => {
    router.push("/product/add");
};
</script>

<style scoped>
.card_content {
    max-width: 100wh;
}

.button_add {
    display: flex;
    justify-content: flex-end;
    padding: 0 0 10px 7px;
}

.table_content {
    width: 100%;
}

.img_item {
    width: 70px;
    height: 70px;
    object-fit: cover;
}
.name_product {
    cursor: pointer;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.rate_product {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    gap: 2px;
}

.rate_product_star {
    color: #ffcc00;
    font-size: 20px;
}

.pagination_wrapper {
    width: 100%;
    display: flex;
    justify-content: center;
    padding: 10px 0;
}
</style>
