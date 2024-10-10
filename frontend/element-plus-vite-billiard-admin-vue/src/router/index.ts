import { createRouter, createWebHistory } from "vue-router";
import { useUserStore } from "~/store";

import DefaultLayout from "~/layouts/DefaultLayout.vue";
import OnlyChildren from "~/layouts/OnlyChildren.vue";

import LayoutView from "~/views/LayoutView.vue";

import Login from "~/views/Login.vue";

const routes = [
    {
        path: "/",
        component: DefaultLayout,
        children: [
            {
                path: "",
                name: "Home",
                component: () => import("~/views/Home.vue"),
                meta: {
                    breadcrumbName: "Tổng quan",
                    requiresAuth: true,
                },
            },
            {
                path: "product",
                name: "Product",
                component: LayoutView,
                meta: {
                    breadcrumbName: "Thông tin sản phẩm",
                    requiresAuth: true,
                },
                children: [
                    {
                        path: "",
                        name: "ListProduct",
                        component: () =>
                            import("~/components/Product/ListProduct.vue"),
                        meta: {
                            breadcrumbName: "Danh sách",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "add",
                        name: "AddProduct",
                        component: () =>
                            import("~/components/Product/AddorEditProduct.vue"),
                        meta: {
                            breadcrumbName: "Thêm sản phẩm",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "edit/:id",
                        name: "EditProduct",
                        component: () =>
                            import("~/components/Product/AddorEditProduct.vue"),
                        meta: {
                            breadcrumbName: "Sửa sản phẩm",
                            requiresAuth: true,
                        },
                    },
                ],
            },
            {
                path: "news",
                name: "News",
                component: LayoutView,
                meta: {
                    breadcrumbName: "Tin tức",
                    requiresAuth: true,
                },
                children: [
                    {
                        path: "",
                        name: "ListNews",
                        component: () =>
                            import("~/components/News/ListNews.vue"),
                        meta: {
                            breadcrumbName: "Danh sách",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "add",
                        name: "AddNews",
                        component: () =>
                            import("~/components/News/AddorEditNews.vue"),
                        meta: {
                            breadcrumbName: "Thêm tin tức",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "edit/:id",
                        name: "EditNews",
                        component: () =>
                            import("~/components/News/AddorEditNews.vue"),
                        meta: {
                            breadcrumbName: "Sửa tin tức",
                            requiresAuth: true,
                        },
                    },
                ],
            },
            {
                path: "categorymenuitem",
                name: "CategoryMenuItem",
                component: LayoutView,
                meta: {
                    breadcrumbName: "Danh mục đồ ăn",
                    requiresAuth: true,
                },
                children: [
                    {
                        path: "",
                        name: "ListCategoryMenuItem",
                        component: () =>
                            import(
                                "~/components/CategoryMenuItem/ListCategoryMenuItem.vue"
                            ),
                        meta: {
                            breadcrumbName: "Danh sách",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "add",
                        name: "AddCategory",
                        component: () =>
                            import(
                                "~/components/CategoryMenuItem/AddorEditCategoryMenuItem.vue"
                            ),
                        meta: {
                            breadcrumbName: "Thêm danh mục đồ ăn",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "edit/:id",
                        name: "EditCategory",
                        component: () =>
                            import(
                                "~/components/CategoryMenuItem/AddorEditCategoryMenuItem.vue"
                            ),
                        meta: {
                            breadcrumbName: "Sửa danh mục đồ ăn",
                            requiresAuth: true,
                        },
                    },
                ],
            },
            {
                path: "manufactor",
                name: "Manufactor",
                component: LayoutView,
                meta: {
                    breadcrumbName: "Hãng sản xuất",
                    requiresAuth: true,
                },
                children: [
                    {
                        path: "",
                        name: "ListManufactor",
                        component: () =>
                            import(
                                "~/components/Manufactor/ListManufactor.vue"
                            ),
                        meta: {
                            breadcrumbName: "Danh sách",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "add",
                        name: "AddManufactor",
                        component: () =>
                            import(
                                "~/components/Manufactor/AddorEditManufactor.vue"
                            ),
                        meta: {
                            breadcrumbName: "Thêm hãng sản xuất",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "edit/:id",
                        name: "EditManufactor",
                        component: () =>
                            import(
                                "~/components/Manufactor/AddorEditManufactor.vue"
                            ),
                        meta: {
                            breadcrumbName: "Sửa hãng sản xuất",
                            requiresAuth: true,
                        },
                    },
                ],
            },
            {
                path: "supplier",
                name: "Supplier",
                component: LayoutView,
                meta: {
                    breadcrumbName: "Nhà phân phối",
                    requiresAuth: true,
                },
                children: [
                    {
                        path: "",
                        name: "ListSupplier",
                        component: () =>
                            import("~/components/Supplier/ListSupplier.vue"),
                        meta: {
                            breadcrumbName: "Danh sách",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "add",
                        name: "AddSupplier",
                        component: () =>
                            import(
                                "~/components/Supplier/AddorEditSupplier.vue"
                            ),
                        meta: {
                            breadcrumbName: "Thêm nhà phân phối",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "edit/:id",
                        name: "EditSupplier",
                        component: () =>
                            import(
                                "~/components/Supplier/AddorEditSupplier.vue"
                            ),
                        meta: {
                            breadcrumbName: "Sửa nhà phân phối",
                            requiresAuth: true,
                        },
                    },
                ],
            },
            {
                path: "typeaccount",
                name: "TypeAccount",
                component: LayoutView,
                meta: {
                    breadcrumbName: "Loại tài khoản",
                    requiresAuth: true,
                },
                children: [
                    {
                        path: "",
                        name: "ListTypeAccount",
                        component: () =>
                            import(
                                "~/components/TypeAccount/ListTypeAccount.vue"
                            ),
                        meta: {
                            breadcrumbName: "Danh sách",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "add",
                        name: "AddTypeAccount",
                        component: () =>
                            import(
                                "~/components/TypeAccount/AddorEditTypeAccount.vue"
                            ),
                        meta: {
                            breadcrumbName: "Thêm loại tài khoản",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "edit/:id",
                        name: "EditTypeAccount",
                        component: () =>
                            import(
                                "~/components/TypeAccount/AddorEditTypeAccount.vue"
                            ),
                        meta: {
                            breadcrumbName: "Sửa loại tài khoản",
                            requiresAuth: true,
                        },
                    },
                ],
            },
            {
                path: "account",
                name: "Account",
                component: LayoutView,
                meta: {
                    breadcrumbName: "Tài khoản",
                    requiresAuth: true,
                },
                children: [
                    {
                        path: "",
                        name: "ListAccount",
                        component: () =>
                            import("~/components/Account/ListAccount.vue"),
                        meta: {
                            breadcrumbName: "Danh sách",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "add",
                        name: "AddAccount",
                        component: () =>
                            import("~/components/Account/AddorEditAccount.vue"),
                        meta: {
                            breadcrumbName: "Thêm tài khoản",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "edit/:id",
                        name: "EditAccount",
                        component: () =>
                            import("~/components/Account/AddorEditAccount.vue"),
                        meta: {
                            breadcrumbName: "Sửa tài khoản",
                            requiresAuth: true,
                        },
                    },
                ],
            },
        ],
    },
    {
        path: "/",
        component: OnlyChildren,
        children: [
            {
                path: "login",
                name: "Login",
                component: Login,
            },
        ],
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

router.beforeEach((to, from, next) => {
    const store = useUserStore();
    const requiresAuth = to.matched.some((record) => record.meta.requiresAuth);
    const user = store.getUser;

    if (requiresAuth && (!user || Object.keys(user).length === 0)) {
        next({ name: "Login" });
    } else {
        next();
    }
});

export default router;
