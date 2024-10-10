import { Categorys, ResponseData } from "~/constant/api";
import { apiClient } from "../constant/request";
import { CategoryUrl } from "~/constant/endpoints";

export const searchCategory = async (
    data: Record<string, string | number>
): Promise<ResponseData<Categorys>> => {
    const res = await apiClient?.post(`${CategoryUrl}/search`, data);
    return res?.data;
};

export const createCategory = async (
    data: Record<string, string | number | boolean>
): Promise<Categorys> => {
    const res = await apiClient?.post(`${CategoryUrl}/add`, data);
    return res?.data;
};

export const updateCategory = async (
    data: Record<string, string | number | boolean>
): Promise<Categorys> => {
    const res = await apiClient?.put(`${CategoryUrl}/update`, data);
    return res?.data;
};

export const deleteCategory = async (id: String): Promise<Categorys> => {
    const res = await apiClient?.delete(`${CategoryUrl}/delete/` + id);
    return res?.data;
};

export const getbyIdCategory = async (
    category_name: string
): Promise<Categorys> => {
    const res = await apiClient?.get(`${CategoryUrl}/get/` + category_name);
    return res?.data;
};
