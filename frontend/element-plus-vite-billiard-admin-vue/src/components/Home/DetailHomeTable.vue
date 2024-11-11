<template>
    <el-card class="card-container">
        <div class="content">
            <p>Thời gian sử dụng: {{ formattedTime }}</p>
            <p>
                Giá 1h:
                {{
                    ConvertPrice(
                        Number(dataDetailTable?.pricingrule?.rate_per_hour)
                    ) || "Chưa có dữ liệu"
                }}
            </p>
            <p>Tạm tính: {{ ConvertPrice(Number(totalPrice)) }}</p>
        </div>
        <div class="button-container">
            <el-button type="primary" @click="startTimer">{{
                timer ? "Dừng" : "Bắt đầu"
            }}</el-button>
        </div>
    </el-card>
</template>

<script lang="ts" setup>
import { onMounted, onUnmounted } from "vue";
import { ref, computed } from "vue";
import { useRoute } from "vue-router";
import { Tables } from "~/constant/api";
import { getbyIdTable } from "~/services/home.service";
import ConvertPrice from "~/utils/convertprice";

const route = useRoute();

const timeElapsed = ref(0);
let timer: NodeJS.Timeout | null = null;
const dataDetailTable = ref<Tables | null>(null);

function startTimer() {
    if (timer) {
        clearInterval(timer);
        timer = null;
    } else {
        timer = setInterval(() => {
            timeElapsed.value += 1;
        }, 1000);
    }
}

const formattedTime = computed(() => {
    const hours = Math.floor(timeElapsed.value / 3600);
    const minutes = Math.floor((timeElapsed.value % 3600) / 60);
    const seconds = timeElapsed.value % 60;

    return `${String(hours).padStart(2, "0")}:${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`;
});

const fetchById = async (id: string) => {
    const resIdTable = await getbyIdTable(id);
    dataDetailTable.value = resIdTable;
};

const totalPrice = computed(() => {
    const ratePerHour = dataDetailTable.value?.pricingrule?.rate_per_hour || 0;
    const timeInHours = timeElapsed.value / 3600;
    return (ratePerHour * timeInHours).toFixed(2);
});

onMounted(() => {
    if (route.params.id) {
        fetchById(String(route.params.id));
    }
});

onUnmounted(() => {
    if (timer) clearInterval(timer);
});
</script>

<style scoped>
.card-container {
    display: flex;
    flex-direction: column;
    height: 100vh;
}

.content {
    flex: 1;
    overflow-y: auto;
}

.button-container {
    display: flex;
    justify-content: center;
    padding: 16px;
    border-top: 1px solid #e0e0e0;
    background-color: #f9f9f9;
}
</style>
