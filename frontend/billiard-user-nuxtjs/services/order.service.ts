import type { BillSell } from "~/constant/api";
import { BillSellUrl } from "~/constant/endpoints";
import { apiClient } from "~/constant/request";

export const sendOrder = async (
    data: Record<string, string | object|number>
): Promise<BillSell> => {
    const res = await apiClient?.post(`${BillSellUrl}/create-hoadon`, data);
    return res?.data;
};
