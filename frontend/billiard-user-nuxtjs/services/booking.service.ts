import type { Tables } from "~/constant/api";
import {
    TableUrl,
} from "~/constant/endpoints";
import { apiClient } from "~/constant/request";

export const getAllTable = async (): Promise<Tables[]> => {
    const res = await apiClient?.get(`${TableUrl}/get`);
    return res?.data;
};