import type { Bookings, ResponseData, Tables } from "~/constant/api";
import { BookingUrl, TableUrl } from "~/constant/endpoints";
import { apiClient } from "~/constant/request";

export const searchBooking = async (
    data: Record<string, string | number | Boolean>
): Promise<ResponseData<Bookings>> => {
    const res = await apiClient?.post(`${BookingUrl}/search`, data);
    return res?.data;
};

export const setFalseStatusBooking = async (id: string): Promise<Bookings> => {
    const res = await apiClient?.put(`${BookingUrl}/false-status/${id}`);
    return res?.data;
};
