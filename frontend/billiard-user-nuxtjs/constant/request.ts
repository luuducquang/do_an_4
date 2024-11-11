import axios from "axios";
import Cookies from "js-cookie";

const customerData = Cookies.get("customer");

export const apiClient = axios.create({
    baseURL: "http://localhost:23668",
    timeout: 1000 * 60 * 30 * 3, // 90 minutes
});

export const apiImage = "http://localhost:23668";

apiClient.interceptors.request.use(
    (config) => {
        if (customerData) {
            try {
                const customer = JSON.parse(customerData);
                const token = customer.token;
                if (token) {
                    config.headers.Authorization = `Bearer ${token}`;
                }
            } catch (error) {
                console.error("Error parsing customer data:", error);
            }
        } else {
            console.warn("No customer data found in cookies");
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);