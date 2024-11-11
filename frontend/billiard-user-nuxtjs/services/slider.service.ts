import type { Slide } from "~/constant/api";
import { SlideUrl } from "~/constant/endpoints";
import { apiClient } from "~/constant/request";

export const getAllImagesSlider = async (): Promise<Slide[]> => {
    const res = await apiClient?.get(`${SlideUrl}/get-all-slide`);
    return res?.data;
};
