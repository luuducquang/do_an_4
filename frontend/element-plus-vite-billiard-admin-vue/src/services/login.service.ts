import { Users } from "~/constant/api";
import { UserUrl } from "~/constant/endpoints";
import { apiClient } from "~/constant/request";

export const login = async (
    data: Record<string, string | number>
): Promise<Users> => {
    const res = await apiClient?.post(`${UserUrl}/login`, data);
    return res?.data;
};
