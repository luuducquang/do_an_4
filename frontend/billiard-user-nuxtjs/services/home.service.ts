import type { Category, Product, ResponseData } from "~/constant/api";
import {
    AdvertisementUrl,
    CategoryUrl,
    ProductUrl,
} from "~/constant/endpoints";
import { apiClient } from "~/constant/request";

export const getCategory = async (): Promise<Category[]> => {
    const res = await apiClient?.get(`${CategoryUrl}/get-all-danhmuc`);
    return res?.data;
};

// export const getAds = async (data: any): Promise<any> => {
//     const res = await apiClient?.post(
//         `${AdvertisementUrl}/search-quangcao`,
//         data
//     );
//     return res?.data;
// };

export const getProductHome = async (
    data: Record<string, string | number>
): Promise<ResponseData<Product>> => {
    const res = await apiClient?.post(`${ProductUrl}/search-sanpham`, data);
    return res?.data;
};

export const getProductFavourite = async (): Promise<Product[]> => {
    const res = await apiClient?.get(`${ProductUrl}/sp-uathich`);
    return res?.data;
};
