import { News, ResponseData } from "~/constant/api";
import { NewUrl } from "~/constant/endpoints";
import { apiClient } from "~/constant/request";

export const searchNews = async (
    data: Record<string, string | number>
): Promise<ResponseData<News>> => {
    const res = await apiClient?.post(`${NewUrl}/search-tintuc`, data);
    return res?.data;
};

export const createNew = async (
    data: Record<string, string | number>
): Promise<News> => {
    const res = await apiClient?.post(`${NewUrl}/create-tintuc`, data);
    return res?.data;
};

export const updateNew = async (
    data: Record<string, string | number>
): Promise<any> => {
    const res = await apiClient?.put(`${NewUrl}/update-tintuc`, data);
    return res?.data;
};

export const deleteNew = async (data: Array<number>): Promise<News> => {
    const res = await apiClient?.delete(`${NewUrl}/delete-tintuc`, {
        data: data,
    });
    return res?.data;
};

export const getbyIdNews = async (maTinTuc: number): Promise<any> => {
    const res = await apiClient?.get(`${NewUrl}/getbyid-tintuc/` + maTinTuc);
    return res?.data;
};
