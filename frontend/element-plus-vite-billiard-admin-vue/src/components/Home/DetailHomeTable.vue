<template>
    <el-card class="card-container">
        <el-row :gutter="20">
            <el-col :span="8">
                <div class="content">
                    <h1 class="m-0">
                        Bàn số : {{ dataDetailTable?.table_number }}
                    </h1>
                    <p>Thời gian sử dụng: {{ formatTime(timeElapsed) }}</p>
                    <p>
                        Giá 1h:
                        {{
                            ConvertPrice(
                                Number(
                                    dataDetailTable?.pricingrule?.rate_per_hour
                                )
                            ) || "Chưa có dữ liệu"
                        }}
                    </p>
                    <p>Tạm tính: {{ ConvertPrice(Number(totalPrice)) }}</p>
                    <p>
                        Tiền dịch vụ: {{ ConvertPrice(Number(service_price)) }}
                    </p>
                    <h2>
                        Tổng tiền :
                        {{
                            ConvertPrice(
                                Number(service_price) + Number(totalPrice)
                            )
                        }}
                    </h2>
                </div>
                <div class="button-container">
                    <div v-if="dataDetailTable?.status === true">
                        <el-popconfirm
                            confirm-button-text="Yes"
                            cancel-button-text="No"
                            icon-color="#626AEF"
                            title="Bạn có muốn thanh toán không?"
                            @confirm="StartAndPay"
                        >
                            <template #reference>
                                <el-button type="primary">
                                    Thanh Toán
                                </el-button>
                            </template>
                        </el-popconfirm>
                    </div>

                    <el-button v-else type="primary" @click="toggleTimer">
                        Bắt đầu
                    </el-button>
                </div>
            </el-col>
            <el-col v-show="dataDetailTable?.status === true" :span="16">
                <div class="button_add">
                    <el-button
                        type="success"
                        @click="
                            () => {
                                dialogFormMenuItemVisible = true;
                                resetForm(ruleFormRef);
                            }
                        "
                        >Đồ ăn</el-button
                    >
                    <el-button
                        type="info"
                        @click="
                            () => {
                                dialogFormRentalItemVisible = true;
                                resetForm(ruleFormRef);
                            }
                        "
                        >Thuê gậy</el-button
                    >
                </div>
                <el-table
                    :data="tableDataMenuItem"
                    class="table_content"
                    v-show="tableDataMenuItem.length > 0"
                >
                    <el-table-column
                        label="Sản phẩm"
                        align="center"
                        prop="menuitem.image"
                    >
                        <template #default="scope">
                            <img
                                :src="apiImage + scope.row.menuitem.image"
                                alt="Hình ảnh sản phẩm"
                                class="img_item"
                            /> </template
                    ></el-table-column>
                    <el-table-column
                        label="Số lượng"
                        align="center"
                        prop="quantity"
                    >
                        <template #default="scope">
                            <el-input-number
                                v-model="scope.row.quantity"
                                :min="1"
                                :max="100"
                                @change="
                                    (value) =>
                                        handleQuantityMenuItemChangeApi(
                                            value,
                                            scope.row
                                        )
                                "
                                class="custom-input-number"
                            />
                        </template>
                    </el-table-column>
                    <el-table-column
                        label="Giá"
                        align="center"
                        prop="unit_price"
                    >
                        <template #default="scope">
                            <span>{{
                                ConvertPrice(scope.row.unit_price)
                            }}</span>
                        </template>
                    </el-table-column>
                    <el-table-column
                        label="Tổng giá"
                        align="center"
                        prop="total_price"
                    >
                        <template #default="scope">
                            <span>{{
                                ConvertPrice(scope.row.total_price)
                            }}</span>
                        </template>
                    </el-table-column>
                    <el-table-column align="right">
                        <template #default="scope">
                            <el-popconfirm
                                confirm-button-text="Yes"
                                cancel-button-text="No"
                                icon-color="#626AEF"
                                title="Bạn có muốn xoá không?"
                                @confirm="
                                    () => confirmEventMenuItem(scope.row._id)
                                "
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
                <!-- RentalItemmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm -->
                <el-table
                    :data="tableDataRentalItem"
                    class="table_content"
                    v-show="tableDataRentalItem.length > 0"
                >
                    <el-table-column align="center" prop="rentalitem.image">
                        <template #default="scope">
                            <img
                                :src="apiImage + scope.row.rentalitem.image"
                                alt="Hình ảnh sản phẩm"
                                class="img_item"
                            /> </template
                    ></el-table-column>
                    <el-table-column align="center" prop="start_time">
                        <template #default="scope">
                            <span>{{
                                formatTime(checkSeconds(scope.row.start_time))
                            }}</span>
                        </template>
                    </el-table-column>
                    <el-table-column align="center" prop="unit_price">
                        <template #default="scope">
                            <span
                                >{{
                                    ConvertPrice(scope.row.unit_price)
                                }}/h</span
                            >
                        </template>
                    </el-table-column>
                    <el-table-column align="center">
                        <template #default="scope">
                            <span>{{
                                ConvertPrice(
                                    (scope.row.unit_price / 60 / 60) *
                                        checkSeconds(scope.row.start_time)
                                )
                            }}</span>
                        </template>
                    </el-table-column>
                    <el-table-column align="right">
                        <template #default="scope">
                            <el-popconfirm
                                confirm-button-text="Yes"
                                cancel-button-text="No"
                                icon-color="#626AEF"
                                title="Bạn có muốn xoá không?"
                                @confirm="
                                    () => confirmEventRentalItem(scope.row._id)
                                "
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
            </el-col>
        </el-row>
    </el-card>
    <el-dialog
        v-model="dialogFormMenuItemVisible"
        title="Thêm đồ ăn"
        width="500"
    >
        <el-form :model="form" :rules="rules" ref="ruleFormRef">
            <el-form-item
                label="Sản phẩm"
                :label-width="formLabelWidth"
                prop="item_id"
            >
                <el-select
                    v-model="form.item_id"
                    filterable
                    placeholder="Vui lòng chọn"
                    @change="handleMenuItemChange"
                >
                    <el-option
                        v-for="item in optionListMenuItems"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value"
                    />
                </el-select>
            </el-form-item>
            <el-form-item
                label="Số lượng"
                :label-width="formLabelWidth"
                prop="quantity"
            >
                <el-input-number
                    v-model="form.quantity"
                    :min="1"
                    :max="100"
                    @change="handleChangeQuantityMenuItem"
                />
            </el-form-item>
            <el-form-item
                label="Giá bán"
                :label-width="formLabelWidth"
                prop="unit_price"
            >
                <el-input
                    v-model="form.unit_price"
                    autocomplete="off"
                    disabled
                />
            </el-form-item>
            <el-form-item
                label="Tổng giá"
                :label-width="formLabelWidth"
                prop="total_price"
            >
                <el-input
                    v-model="form.total_price"
                    autocomplete="off"
                    disabled
                />
            </el-form-item>
            <el-form-item>
                <div class="button_item">
                    <el-button @click="dialogFormMenuItemVisible = false"
                        >Cancel</el-button
                    >
                    <el-button
                        type="primary"
                        @click="submitFormMenuItem(ruleFormRef)"
                    >
                        Thêm
                    </el-button>
                </div>
            </el-form-item>
        </el-form>
    </el-dialog>
    <el-dialog
        v-model="dialogFormRentalItemVisible"
        title="Thuê gậy"
        width="500"
    >
        <el-form :model="form" :rules="rules" ref="ruleFormRef">
            <el-form-item
                label="Sản phẩm"
                :label-width="formLabelWidth"
                prop="item_id"
            >
                <el-select
                    v-model="form.item_id"
                    filterable
                    placeholder="Vui lòng chọn"
                    @change="handleRentalItemChange"
                >
                    <el-option
                        v-for="item in optionListRenTalItems"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value"
                    />
                </el-select>
            </el-form-item>
            <el-form-item
                label="Giá thuê/1h"
                :label-width="formLabelWidth"
                prop="unit_price"
            >
                <el-input
                    v-model="form.unit_price"
                    autocomplete="off"
                    disabled
                />
            </el-form-item>
            <el-form-item
                label="Tổng giá"
                :label-width="formLabelWidth"
                prop="total_price"
            >
                <el-input
                    v-model="form.total_price"
                    autocomplete="off"
                    disabled
                />
            </el-form-item>
            <el-form-item>
                <div class="button_item">
                    <el-button @click="dialogFormRentalItemVisible = false"
                        >Cancel</el-button
                    >
                    <el-button
                        type="primary"
                        @click="submitFormRentalItem(ruleFormRef)"
                    >
                        Thêm
                    </el-button>
                </div>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<script lang="ts" setup>
import axios from "axios";
import { ElMessage, FormInstance, FormRules } from "element-plus";
import { onMounted, onUnmounted } from "vue";
import { ref, computed, reactive } from "vue";
import { useRoute } from "vue-router";
import {
    OptionSelect,
    TableMenuItems,
    TableRentalItems,
    Tables,
} from "~/constant/api";
import {
    createTableMenuItem,
    createTableRentalItem,
    deleteMenuItem,
    deleteRentalItem,
    getbyIdTable,
    getbyIdTableMenuItem,
    getbyIdTableRentalItem,
    updateTable,
    updateTableMenuItem,
} from "~/services/home.service";
import { getAllMenuItem } from "~/services/menuitem.service";
import ConvertPrice from "~/utils/convertprice";
import { apiImage } from "~/constant/request";
import { getAllRentalItem } from "~/services/rentalitem.service";

const route = useRoute();
const dataDetailTable = ref<Tables | null>(null);

const timeElapsed = ref(0);
const startTime = ref<string | null>(null);
let timer: NodeJS.Timeout | null = null;

const ruleFormRef = ref<FormInstance>();

const optionListMenuItems = ref<OptionSelect[]>();
const optionListRenTalItems = ref<OptionSelect[]>();

const dialogFormMenuItemVisible = ref(false);
const dialogFormRentalItemVisible = ref(false);
const formLabelWidth = "140px";

const tableDataMenuItem = ref<TableMenuItems[]>([]);
const tableDataRentalItem = ref<TableRentalItems[]>([]);

const Notification = (
    message: string,
    type: "success" | "warning" | "error"
) => {
    ElMessage({
        message: message,
        type: type,
    });
};

const form = reactive({
    item_id: "",
    quantity: 1,
    unit_price: 0,
    total_price: 0,
});

const rules = reactive<FormRules>({
    item_id: [
        {
            required: true,
            message: "Vui lòng chọn sản phẩm",
            trigger: "change",
        },
    ],
    quantity: [
        {
            required: true,
            message: "Vui lòng chọn số lượng",
            trigger: "change",
        },
        {
            pattern: /^[0-9]+$/,
            message: "Vui lòng nhập số tự nhiên",
            trigger: "change",
        },
    ],
    unit_price: [
        {
            required: true,
            message: "Vui lòng nhập giá bán",
            trigger: "change",
        },
    ],
    total_price: [
        {
            required: true,
            message: "Vui lòng nhập tổng giá",
            trigger: "change",
        },
    ],
});

const handleMenuItemChange = (value: string) => {
    if (optionListMenuItems.value) {
        const selectedProduct = optionListMenuItems.value.find(
            (item: OptionSelect) => item.value === value
        );

        if (selectedProduct) {
            form.unit_price = Number(selectedProduct.price);
        }
        if (form.item_id !== "") {
            form.total_price = Number(form.quantity) * Number(form.unit_price);
        }
    }
};

const handleRentalItemChange = (value: string) => {
    if (optionListRenTalItems.value) {
        const selectedProduct = optionListRenTalItems.value.find(
            (item: OptionSelect) => item.value === value
        );

        if (selectedProduct) {
            form.unit_price = Number(selectedProduct.price);
        }
        if (form.item_id !== "") {
            form.total_price = Number(form.quantity) * Number(form.unit_price);
        }
    }
};

const handleChangeQuantityMenuItem = (
    cur: number | undefined,
    prev: number | undefined
) => {
    if (form.item_id !== "") {
        form.total_price = Number(cur) * Number(form.unit_price);
    }
};

const handleQuantityMenuItemChangeApi = async (
    value: number | undefined,
    item: TableMenuItems
) => {
    await updateTableMenuItem({
        _id: String(item._id),
        table_id: String(item.table_id),
        item_id: String(item.item_id),
        quantity: Number(value),
        unit_price: String(item.unit_price),
        total_price: Number(value) * Number(item.unit_price),
    });
    fetchById(String(route.params.id));
};

const confirmEventMenuItem = async (Id: string) => {
    try {
        await deleteMenuItem(Id);
        Notification("Xoá thành công", "success");
        fetchById(String(route.params.id));
    } catch (error) {
        console.error("Error deleting =:", error);
        Notification("Lỗi khi xoá =", "error");
    }
};

const confirmEventRentalItem = async (Id: string) => {
    try {
        await deleteRentalItem(Id);
        Notification("Xoá thành công", "success");
        fetchById(String(route.params.id));
    } catch (error) {
        console.error("Error deleting =:", error);
        Notification("Lỗi khi xoá =", "error");
    }
};

const submitFormMenuItem = async (formEl: FormInstance | undefined) => {
    if (!formEl) return;

    try {
        const valid = await formEl.validate();
        if (valid) {
            try {
                await createTableMenuItem({
                    table_id: String(route.params.id),
                    item_id: form.item_id,
                    quantity: form.quantity,
                    unit_price: form.unit_price,
                    total_price:
                        Number(form.quantity) * Number(form.unit_price),
                });
                Notification("Thêm thành công", "success");
                dialogFormMenuItemVisible.value = false;
                fetchById(String(route.params.id));
            } catch (error) {
                if (axios.isAxiosError(error)) {
                    Notification(error.response?.data.detail, "warning");
                }
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

const submitFormRentalItem = async (formEl: FormInstance | undefined) => {
    if (!formEl) return;

    try {
        const valid = await formEl.validate();
        if (valid) {
            try {
                await createTableRentalItem({
                    table_id: String(route.params.id),
                    item_id: form.item_id,
                    unit_price: form.unit_price,
                    start_time: getLocalISOString(),
                });
                Notification("Thêm thành công", "success");
                dialogFormRentalItemVisible.value = false;
                fetchById(String(route.params.id));
            } catch (error) {
                if (axios.isAxiosError(error)) {
                    Notification(error.response?.data.detail, "warning");
                }
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

function getLocalISOString() {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, "0");
    const day = String(now.getDate()).padStart(2, "0");
    const hours = String(now.getHours()).padStart(2, "0");
    const minutes = String(now.getMinutes()).padStart(2, "0");
    const seconds = String(now.getSeconds()).padStart(2, "0");
    return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
}

async function toggleTimer() {
    const tableDetail = await getbyIdTable(String(route.params.id));

    if (tableDetail.status === false) {
        if (timer) {
            clearInterval(timer);
            timer = null;
            startTime.value = null;
        } else {
            startTime.value = getLocalISOString();
            timer = setInterval(updateElapsed, 1000);
        }
        await updateTable({
            _id: String(route.params.id),
            table_number: Number(dataDetailTable.value?.table_number),
            table_type_id: String(dataDetailTable.value?.table_type_id),
            status: Boolean(!dataDetailTable.value?.status),
            start_date: String(startTime.value),
            end_date: String(startTime.value),
        });
        fetchById(String(route.params.id));
    } else {
        Notification("Bàn này đã được dùng", "warning");
    }
}

function updateElapsed() {
    if (startTime.value) {
        const start = new Date(startTime.value).getTime();
        timeElapsed.value = Math.floor((Date.now() - start) / 1000);
    }
}

function checkSeconds(time: string | Date): number {
    let dateTime: Date;

    if (typeof time === "string") {
        dateTime = new Date(time);
    } else if (time instanceof Date) {
        dateTime = time;
    } else {
        throw new Error("Invalid input: time must be a string or Date object.");
    }

    if (isNaN(dateTime.getTime())) {
        throw new Error("Invalid input: time is not a valid date.");
    }

    return Math.floor((Date.now() - dateTime.getTime()) / 1000);
}

const formatTime = (s: number): string => {
    const hours = Math.floor(s / 3600);
    const minutes = Math.floor((s % 3600) / 60);
    const seconds = s % 60;

    return `${String(hours).padStart(2, "0")}:${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`;
};

const fetchById = async (id: string) => {
    const resIdTable = await getbyIdTable(id);
    dataDetailTable.value = resIdTable;

    const resTableMenuItem = await getbyIdTableMenuItem(id);
    tableDataMenuItem.value = resTableMenuItem;

    if (dataDetailTable.value?.status === true) {
        startTime.value = String(dataDetailTable.value?.start_date);
        timer = setInterval(async () => {
            updateElapsed();
            const resTableRentalItem = await getbyIdTableRentalItem(id);
            tableDataRentalItem.value = resTableRentalItem;
        }, 1000);
    }
    const resListMenuItem = await getAllMenuItem();
    optionListMenuItems.value = resListMenuItem?.map(function ({
        _id,
        name,
        price,
    }) {
        return {
            value: _id || 0,
            label: name || "",
            price: price || 0,
        };
    });

    const resListRentalItem = await getAllRentalItem();
    optionListRenTalItems.value = resListRentalItem?.map(function ({
        _id,
        item_name,
        rental_price_hours,
    }) {
        return {
            value: _id || 0,
            label: item_name || "",
            price: rental_price_hours || 0,
        };
    });
};

const totalPrice = computed(() => {
    const ratePerHour = dataDetailTable.value?.pricingrule?.rate_per_hour || 0;
    const timeInHours = timeElapsed.value / 3600;
    return (ratePerHour * timeInHours).toFixed(2);
});

const service_price = computed(() => {
    const menuItemTotal = tableDataMenuItem.value.reduce((total, item) => {
        return total + item.quantity * item.unit_price;
    }, 0);

    const rentalItemTotal = tableDataRentalItem.value.reduce((total, item) => {
        return (
            total + checkSeconds(item.start_time) * (item.unit_price / 60 / 60)
        );
    }, 0);

    return menuItemTotal + rentalItemTotal;
});

const StartAndPay = () => {
    console.log("1");
};

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
.img_item {
    width: 70px;
    height: 70px;
    object-fit: cover;
}
.button_item {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
}

.button_add {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
}
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
    background-color: #f9f9f9;
}
.custom-input-number {
    width: 100px;
}

.ep-table th.ep-table__cell.is-leaf,
.ep-table td.ep-table__cell {
    border-bottom: 0px solid #000 !important;
}

.ep-button + .ep-button {
    margin-left: 0px;
}
.ep-button {
    margin: 2px;
}
</style>
