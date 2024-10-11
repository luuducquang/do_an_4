import { defineStore } from "pinia";
import { Users } from "~/constant/api";

export const useUserStore = defineStore("user", {
    state: () => ({
        user: {
            _id: "67091c27cc4dce5436908fa0",
            username: "âdas",
            password: "ád",
            fullname: "áda",
            email: "adasd",
            phone: "ádasdas",
            address: "ada",
            avatar: "adadasd",
            loyalty_points: 0,
            role_name: "stradadaing",
            token: "eyJhbGciOiJBMTI4Q0JDLUhTMjU2IiwidHlwIjoiSldUIn0.eyJ1bmlxdWVfbmFtZSI6ImFkbWluIiwiZW1haWwiOiJhZG1pbkBnbWFpbC5jb20iLCJyb2xlIjoiOCIsIm5iZiI6MTcyMTI4MTM2NCwiZXhwIjoxNzIxODg2MTY0LCJpYXQiOjE3MjEyODEzNjR9.cZIvgGriKLcRIQ2M9LtXFC7zDgA5HyfJVPwJtTjXNBc",
        },
    }),
    getters: {
        getUser: (state) => state.user,
    },
    actions: {
        setUser(user: Users) {
            this.user = user;
        },
    },
});
