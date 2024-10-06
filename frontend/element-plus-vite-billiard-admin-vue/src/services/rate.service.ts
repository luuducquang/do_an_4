import { Rate, ResponseData } from "~/constant/api";
import { apiClient } from "../constant/request";
import { RateUrl } from "~/constant/endpoints";

export const searchRate = async (
    data: Record<string, string | number>
): Promise<ResponseData<Rate>> => {
    const res = await apiClient?.post(`${RateUrl}/search-danhgia`, data);
    return res?.data;
};

export const editRate = async (
    data: Record<string, string | number>
): Promise<Rate> => {
    const res = await apiClient?.post(`${RateUrl}/update-danhgia`, data);
    return res?.data;
};

export const deleteRate = async (data: Array<number>): Promise<Rate> => {
    const res = await apiClient?.delete(`${RateUrl}/delete-danhgia`, {
        data: data,
    });
    return res?.data;
};

export const getbyIdRate = async (maDanhGia: number): Promise<any> => {
    const res = await apiClient?.get(`${RateUrl}/getbyid-danhgia/` + maDanhGia);
    return res?.data;
};
