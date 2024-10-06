import { defineStore } from "pinia";
import { User } from "~/constant/api";

export const useUserStore = defineStore("user", {
    state: () => ({
        user: {
            anhdaidien: "/img/anh fb.png",
            email: "admin@gmail.com",
            hoten: "Lưu Đức Quangg",
            maLoaitaikhoan: 8,
            mataikhoan: 22,
            sodienthoai: "09837817823",
            taikhoan: "admin",
            token: "eyJhbGciOiJBMTI4Q0JDLUhTMjU2IiwidHlwIjoiSldUIn0.eyJ1bmlxdWVfbmFtZSI6ImFkbWluIiwiZW1haWwiOiJhZG1pbkBnbWFpbC5jb20iLCJyb2xlIjoiOCIsIm5iZiI6MTcyMTI4MTM2NCwiZXhwIjoxNzIxODg2MTY0LCJpYXQiOjE3MjEyODEzNjR9.cZIvgGriKLcRIQ2M9LtXFC7zDgA5HyfJVPwJtTjXNBc",
        },
    }),
    getters: {
        getUser: (state) => state.user,
    },
    actions: {
        setUser(user: User) {
            this.user = user;
        },
    },
});
