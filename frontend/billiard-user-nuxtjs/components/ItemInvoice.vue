<template>
    <div class="accordion" id="accordionExample">
        <div
            class="accordion-item"
            v-for="(value, index) in billsell"
            :key="index"
        >
            <h2 class="accordion-header" :id="`heading${value?.maHoaDon}`">
                <button
                    class="accordion-button collapsed"
                    type="button"
                    data-bs-toggle="collapse"
                    :data-bs-target="`#collapse${value?.maHoaDon}`"
                    aria-expanded="false"
                    :aria-controls="`collapse${value?.maHoaDon}`"
                >
                    {{
                        `${value?.tenKH} | ${
                            value?.tongGia > 0
                                ? value?.tongGia.toLocaleString("DE-de")
                                : 0
                        }đ | ${value?.diaChiGiaoHang} | ${value?.trangThai}`
                    }}
                </button>
            </h2>
            <div
                :id="`collapse${value?.maHoaDon}`"
                class="accordion-collapse collapse"
                :aria-labelledby="`heading${value?.maHoaDon}`"
                data-bs-parent="#accordionExample"
                style=""
            >
                <div
                    class=""
                    v-for="(item, index) in detailBillSells"
                    :key="index"
                >
                    <div
                        v-if="item.maHoaDon === value?.maHoaDon"
                        class="d-flex accordion-body"
                    >
                        <img
                            :src="apiImage + item.anhDaiDien"
                            alt="image"
                            width="200"
                            height="200"
                        />
                        <div class="p-3">
                            <h5>{{ item.tenSanPham }}</h5>
                            <div>
                                Số lượng:
                                {{ item.soLuong }}
                            </div>
                            <div>
                                Đơn giá:
                                {{
                                    item.donGia > 0
                                        ? item.donGia.toLocaleString("De-de")
                                        : 0
                                }}đ
                            </div>
                            <div>
                                Tổng giá:
                                {{
                                    (
                                        Number(item.soLuong) *
                                        Number(item.donGia)
                                    ).toLocaleString("De-de")
                                }}đ
                            </div>
                        </div>
                    </div>
                </div>
                <!-- <div
                    v-if="value.trangThai === 'Đang xử lý'"
                    class="text-center"
                >
                    <button
                        @click="cancelOrder(Number(value.maHoaDon))"
                        class="btn btn_cancel"
                    >
                        Huỷ đơn
                    </button>
                </div> -->
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref, nextTick } from "vue";
import type { BillSell, TableBillSell } from "~/constant/api";
import { apiImage } from "~/constant/request";
import { getInvoiceById } from "~/services/invoice.servie";

const props = defineProps<{
    billsell: BillSell[];
}>();

const detailBillSells = ref<TableBillSell[]>([]);

// onMounted(async () => {
//     await nextTick();
//     console.log(props.billsell);
// });

const fetchData = () => {
    setTimeout(async () => {
        const listDetail = await Promise.all(
            props.billsell.map(async (value) => {
                const dataDetail = await getInvoiceById(Number(value.maHoaDon));
                return dataDetail;
            })
        );
        detailBillSells.value = listDetail.flat();
        console.log(detailBillSells.value);
    }, 1000);
};

onMounted(() => {
    fetchData();
});

const cancelOrder = (id: number) => {
    console.log(id);
};
</script>

<style lang="css" scoped>
.btn_cancel {
    border: none;
    padding: 7px 10px;
    background-color: #ff0033;
    outline: none;
    color: #fff;
    margin-bottom: 10px;
}

.btn_cancel:hover {
    opacity: 0.8;
}
</style>
