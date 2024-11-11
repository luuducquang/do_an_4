import type { BillSell, TableBillSell } from "~/constant/api";
import { BillSellUrl } from "~/constant/endpoints";
import { apiClient } from "~/constant/request";

export const getInvoiceAll = async (id: number): Promise<BillSell[]> => {
    const res = await apiClient?.get(
        `${BillSellUrl}/getbytaikhoan-mahoadon-chitiethoadon/` + id
    );
    return res?.data;
};

export const getInvoiceById = async (id: number): Promise<TableBillSell[]> => {
    const res = await apiClient?.get(
        `${BillSellUrl}/getbyid-mahoadon-chitiethoadon/` + id
    );
    return res?.data;
};
