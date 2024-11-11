import type { Account } from "~/constant/api";
import { AccountUrl } from "~/constant/endpoints";
import { apiClient } from "~/constant/request";

export const getInformation = async (id: number): Promise<Account[]> => {
    const res = await apiClient?.get(
        `${AccountUrl}/getbyid-taikhoan-chitiettaikhoan/` + id
    );
    return res?.data;
};

export const updateInformation = async (
    data: Record<string, string | [object]>
): Promise<Account> => {
    const res = await apiClient?.put(`${AccountUrl}/update-taikhoan`, data);
    return res?.data;
};
