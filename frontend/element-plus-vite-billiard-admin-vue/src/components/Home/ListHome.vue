<template>
    <el-card class="card_content" v-loading="loading">
        <el-row :gutter="20">
            <el-col
                v-for="(table) in tableData"
                :key="table._id"
                :span="6"
                @click="handleEdit(String(table._id))"
                ><div
                    class="grid-content ep-bg-purple"
                >
                    <h1>{{ table.table_number }}</h1>
                    <p
                        :class="
                            table.status ? 'status-in-use' : 'status-available'
                        "
                        class="m-0"
                    >
                        {{
                            table.status === true
                                ? "Đang sử dụng"
                                : "Đang trống"
                        }}
                    </p>
                </div></el-col
            >
        </el-row>
    </el-card>
</template>

<script lang="ts" setup>
import { getAllTable } from "~/services/home.service";
import { Tables } from "~/constant/api";
import { ref, onMounted } from "vue";
import router from '~/router'

const tableData = ref<Tables[]>([]);
const loading = ref(true);

const handleEdit = (id:string) => {
    router.push(`/${id}`);
};

const fetchData = async () => {
    try {
        const res = await getAllTable();
        tableData.value = res;
    } catch (error) {
        console.error("Error fetching:", error);
        tableData.value = [];
    } finally {
        loading.value = false;
    }
};

onMounted(() => {
    fetchData();
});
</script>

<style scoped>
.grid-content {
    height: 200px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: bold;
    margin-bottom: 10px;
    cursor: pointer;
}

.grid-content > h1 {
    font-size: 50px;
}

/* .grid-content > p {
    margin: 0;
} */

.ep-bg-purple {
    background-color: #3d4d44;
}
.ep-bg-green {
    background-color: #27ae60;
    height: 100%;
}
.status-in-use {
    color: #ff3333;
}
.status-available {
    color: #00bb00;
}
.active_table {
    background-color: #000000;
}
</style>
