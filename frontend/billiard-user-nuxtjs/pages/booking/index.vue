<template>
    <div class="container">
        <div class="type">
            <NuxtLink to="/">TRANG CHỦ</NuxtLink>
            <i class="fa-solid fa-arrow-right"></i>
            <NuxtLink to="/booking">Đặt bàn</NuxtLink>
        </div>
    </div>
    <div class="container py-4">
        <div class="row g-3">
            <div
                class="col-6 col-md-4 col-lg-3"
                v-for="table in tableData"
                :key="table._id"
            >
                <div
                    class="card text-center p-3 position-relative"
                    :class="table.status ? 'bg-danger' : 'bg-success'"
                >
                        <h1 class="text-white">{{ table.table_number }}</h1>
                        <p class="m-0 text-white">
                            {{ table.status ? "Đang sử dụng" : "Đang trống" }}
                        </p>
                    <button
                        class="btn btn-primary btn-booking"
                        v-if="!table.status"
                        @click="handleBooking(table._id)"
                    >
                        Đặt bàn
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { getAllTable } from "~/services/booking.service";
import { type Tables } from "~/constant/api";

const tableData = ref<Tables[]>([]);
const loading = ref(true);
const router = useRouter();

const handleBooking = (id: string) => {
    alert(`Đặt bàn có ID: ${id}`);
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

<style lang="css" scoped>
.type {
    background: linear-gradient(90deg, var(--color-primary) 0%, #001815 100%) 0%
        0% no-repeat;
    padding: 10px;
    color: #fff;
    margin-top: 10px;
}

.type a {
    text-decoration: none;
    color: #ddd;
    font-size: 14px;
    text-transform: uppercase;
}

.type i {
    color: #fff;
    font-size: 10px;
    padding: 0 10px;
}
.card {
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.2s ease, opacity 0.2s ease;
    position: relative;
    overflow: hidden;
}

.card:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.card:hover h1,
.card:hover p {
    opacity: 0.1; 
    transition: opacity 0.2s ease;
}

.btn-booking {
    position: absolute;
    left: 50%;
    transform: translate(-50%, 50%);
    opacity: 0;
    visibility: hidden;
    transition: all 0.3s ease;
    background: linear-gradient(90deg, #4caf50, #81c784); 
    color: #fff;
    font-size: 1rem;
    font-weight: bold;
    border: none;
    border-radius: 20px; 
    padding: 10px 20px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3); 
    cursor: pointer;
}

.btn-booking:hover {
    background: linear-gradient(90deg, #388e3c, #66bb6a); 
    box-shadow: 0 6px 8px rgba(0, 0, 0, 0.4); 
    transform: translate(-50%, 60%) scale(1.05); 
}

.card:hover .btn-booking {
    opacity: 1; 
    visibility: visible;
}

.card h1 {
    font-size: 3rem;
    font-weight: bold;
    transition: opacity 0.2s ease;
}

.card p {
    font-size: 1.2rem;
    transition: opacity 0.2s ease;
}

.bg-danger {
    background-color: #e74c3c !important;
}

.bg-success {
    background-color: #2ecc71 !important;
}
</style>
