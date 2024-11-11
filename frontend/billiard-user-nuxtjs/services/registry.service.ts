import type { Account } from "~/constant/api";
import { AccountUrl } from "~/constant/endpoints";
import { apiClient } from "~/constant/request";

export const checkUserNameIsEmpty = async (): Promise<Account> => {
    const res = await apiClient?.get(`${AccountUrl}/get-alltaikhoan`);
    return res?.data;
};

export const registryUser = async (
    data: Record<string, string | number>
): Promise<Account> => {
    const res = await apiClient?.post(`${AccountUrl}/create-taikhoan`, data);
    return res?.data;
};
