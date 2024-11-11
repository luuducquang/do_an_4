import { apiClient } from "~/constant/request";
import type { Cart } from "~/constant/api";
import { CartUrl } from "~/constant/endpoints";

export const getGioHangByIdTaiKhoan = async (id: number): Promise<Cart[]> => {
    const res = await apiClient?.get(
        `${CartUrl}/getbyidtaikhoan-giohang/` + id
    );
    return res?.data;
};

export const createCart = async (
    data: Record<string, string | number | boolean>
): Promise<Cart> => {
    const res = await apiClient?.post(`${CartUrl}/create-giohang`, data);
    return res?.data;
};

export const updateCart = async (
    data: Record<string, string | number | boolean>
): Promise<Cart> => {
    const res = await apiClient?.put(`${CartUrl}/update-giohang`, data);
    return res?.data;
};

export const updateCartsFalse = async (mataikhoan: number): Promise<Cart> => {
    const res = await apiClient?.put(
        `${CartUrl}/update-giohangfalse?mataikhoan=${mataikhoan}`
    );
    return res?.data;
};

export const deleteCarts = async (data: Array<number>): Promise<Cart> => {
    const res = await apiClient?.delete(`${CartUrl}/delete-giohang`, {
        data: data,
    });
    return res?.data;
};
