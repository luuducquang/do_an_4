import type { News, ResponseData } from "~/constant/api";
import { NewUrl } from "~/constant/endpoints";
import { apiClient } from "~/constant/request";

export const getNews = async (
    data: Record<string, string | number>
): Promise<ResponseData<News>> => {
    const res = await apiClient?.post(`${NewUrl}/search-tintuc`, data);
    return res?.data;
};

export const getNewById = async (id: number): Promise<News> => {
    const res = await apiClient?.get(`${NewUrl}/getbyid-tintuc/` + id);
    return res?.data;
};
