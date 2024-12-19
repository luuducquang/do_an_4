<template>
    <el-container>
        <el-main>
            <!-- Thống kê tổng quan -->
            <el-row :gutter="20" class="summary-row">
                <el-col
                    :span="6"
                    v-for="stat in summaryStats"
                    :key="stat.label"
                >
                    <el-card class="summary-card">
                        <h2 class="stat-label">{{ stat.label }}</h2>
                        <p class="stat-value">{{ stat.value }}</p>
                    </el-card>
                </el-col>
            </el-row>

            <!-- Biểu đồ doanh thu -->
            <el-row :gutter="20" class="chart-row">
                <el-col :span="24">
                    <el-card>
                        <h2>Biểu đồ Doanh Thu Theo Ngày</h2>
                        <el-tooltip
                            content="Số liệu doanh thu theo ngày"
                            placement="top"
                        >
                            <div id="revenueChart" style="height: 300px"></div>
                        </el-tooltip>
                    </el-card>
                </el-col>
            </el-row>
        </el-main>
    </el-container>
</template>

<script>
import * as echarts from "echarts";

export default {
    name: "StatisticsPage",
    data() {
        return {
            summaryStats: [
                { label: "Tổng số bàn", value: 12 },
                { label: "Bàn đang sử dụng", value: 5 },
                { label: "Bàn trống", value: 7 },
                { label: "Số lượng đặt bàn trong ngày", value: 8 },
                { label: "Số lượng hoá đơn bán", value: 50 },
                { label: "Số lượng hoá đơn nhập", value: 20 },
                { label: "Tổng số khách hàng", value: 150 },
                { label: "Khách hàng mới trong tháng", value: 10 },
                { label: "Đơn hàng bị huỷ", value: 2 },
                { label: "Đơn hàng chờ", value: 5 },
                { label: "Đơn hàng đang giao", value: 3 },
                { label: "Đơn hàng hoàn tất", value: 45 },
                { label: "Đơn hàng đổi trả", value: 1 },
                { label: "Tổng lượt xem sản phẩm", value: 2000 },
                {
                    label: "Tổng tiền nhập",
                    value: this.formatCurrency(5000000),
                },
                {
                    label: "Tổng doanh thu",
                    value: this.formatCurrency(12500000),
                },
            ],
            revenueData: [
                { date: "2024-12-01", revenue: 200000 },
                { date: "2024-12-02", revenue: 300000 },
                { date: "2024-12-03", revenue: 250000 },
                { date: "2024-12-04", revenue: 400000 },
                { date: "2024-12-05", revenue: 350000 },
            ],
        };
    },
    mounted() {
        this.renderRevenueChart();
    },
    methods: {
        formatCurrency(value) {
            return new Intl.NumberFormat("vi-VN", {
                style: "currency",
                currency: "VND",
            }).format(value);
        },
        renderRevenueChart() {
            const chart = echarts.init(document.getElementById("revenueChart"));
            const option = {
                xAxis: {
                    type: "category",
                    data: this.revenueData.map((item) => item.date),
                },
                yAxis: { type: "value" },
                series: [
                    {
                        data: this.revenueData.map((item) => item.revenue),
                        type: "line",
                        smooth: true,
                    },
                ],
                tooltip: { trigger: "axis" },
            };
            chart.setOption(option);
        },
    },
};
</script>

<style scoped>
.stat-label {
    font-size: 14px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 5px;
}

.stat-value {
    font-size: 16px;
    font-weight: bold;
    color: #409eff;
    text-align: center;
}

.summary-card {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 120px;
}

.summary-row {
    margin-bottom: 20px;
}

.chart-row {
    margin-top: 20px;
}
</style>
