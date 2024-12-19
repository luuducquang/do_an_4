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
            // {
            //     path: "",
            //     name: "Home",
            //     component: () => import("~/components/Home/ListHome.vue"),
            //     meta: {
            //         breadcrumbName: "Danh sách bàn",
            //         requiresAuth: true,
            //     },
            //     children: [
            //         {
            //             path: "/:id",
            //             name: "DetailHomeTable",
            //             component: () =>
            //                 import("~/components/Home/DetailHomeTable.vue"),
            //             meta: {
            //                 breadcrumbName: "Thônng tin bàn :id",
            //                 requiresAuth: true,
            //             },
            //         },
            //     ],
            // },
            {
                path: "",
                name: "Home",
                component: LayoutView,
                meta: {
                    breadcrumbName: "Trang chủ",
                    requiresAuth: true,
                },
                children: [
                    {
                        path: "",
                        name: "Home",
                        component: () =>
                            import("~/components/Home/ListHome.vue"),
                        meta: {
                            breadcrumbName: "Danh sách bàn",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "/:id",
                        name: "DetailHomeTable",
                        component: () =>
                            import("~/components/Home/DetailHomeTable.vue"),
                        meta: {
                            breadcrumbName: "Thông tin bàn",
                            requiresAuth: true,
                        },
                    },
                ],
            },
            {
                path: "statistic",
                name: "statistic",
                component: LayoutView,
                meta: {
                    breadcrumbName: "Thống kê",
                    requiresAuth: true,
                },
                children: [
                    {
                        path: "",
                        name: "Statistic",
                        component: () =>
                            import("~/components/Statistic/ListStatistic.vue"),
                        meta: {
                            breadcrumbName: "Danh thống kê",
                            requiresAuth: true,
                        },
                    },
                ],
            },
            {
                path: "tabletype",
                name: "TableType",
                component: LayoutView,
                meta: {
                    breadcrumbName: "Loại bàn",
                    requiresAuth: true,
                },
                children: [
                    {
                        path: "",
                        name: "ListTableType",
                        component: () =>
                            import("~/components/TableType/ListTableType.vue"),
                        meta: {
                            breadcrumbName: "Danh sách",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "add",
                        name: "AddTableType",
                        component: () =>
                            import(
                                "~/components/TableType/AddorEditTableType.vue"
                            ),
                        meta: {
                            breadcrumbName: "Thêm loại bàn",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "edit/:id",
                        name: "EditTableType",
                        component: () =>
                            import(
                                "~/components/TableType/AddorEditTableType.vue"
                            ),
                        meta: {
                            breadcrumbName: "Sửa loại bàn",
                            requiresAuth: true,
                        },
                    },
                ],
            },
            {
                path: "table",
                name: "Table",
                component: LayoutView,
                meta: {
                    breadcrumbName: "Bàn",
                    requiresAuth: true,
                },
                children: [
                    {
                        path: "",
                        name: "ListTable",
                        component: () =>
                            import("~/components/Table/ListTable.vue"),
                        meta: {
                            breadcrumbName: "Danh sách",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "add",
                        name: "AddTable",
                        component: () =>
                            import("~/components/Table/AddorEditTable.vue"),
                        meta: {
                            breadcrumbName: "Thêm bàn",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "edit/:id",
                        name: "EditTable",
                        component: () =>
                            import("~/components/Table/AddorEditTable.vue"),
                        meta: {
                            breadcrumbName: "Sửa bàn",
                            requiresAuth: true,
                        },
                    },
                ],
            },
            {
                path: "pricingrule",
                name: "PricingRule",
                component: LayoutView,
                meta: {
                    breadcrumbName: "Quy tắc giá",
                    requiresAuth: true,
                },
                children: [
                    {
                        path: "",
                        name: "ListPricingRule",
                        component: () =>
                            import(
                                "~/components/PricingRule/ListPricingRule.vue"
                            ),
                        meta: {
                            breadcrumbName: "Danh sách",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "add",
                        name: "AddPricingRule",
                        component: () =>
                            import(
                                "~/components/PricingRule/AddorEditPricingRule.vue"
                            ),
                        meta: {
                            breadcrumbName: "Thêm quy tắc giá",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "edit/:id",
                        name: "EditPricingRule",
                        component: () =>
                            import(
                                "~/components/PricingRule/AddorEditPricingRule.vue"
                            ),
                        meta: {
                            breadcrumbName: "Sửa quy tắc giá",
                            requiresAuth: true,
                        },
                    },
                ],
            },
            {
                path: "billsell",
                name: "BillSell",
                component: LayoutView,
                meta: {
                    breadcrumbName: "Hoá đơn bán",
                    requiresAuth: true,
                },
                children: [
                    {
                        path: "",
                        name: "ListBillSell",
                        component: () =>
                            import("~/components/BillSell/ListBillSell.vue"),
                        meta: {
                            breadcrumbName: "Danh sách",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "add",
                        name: "AddBillSell",
                        component: () =>
                            import(
                                "~/components/BillSell/AddorEditBillSell.vue"
                            ),
                        meta: {
                            breadcrumbName: "Thêm hoá đơn bán",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "edit/:id",
                        name: "EditBillSell",
                        component: () =>
                            import(
                                "~/components/BillSell/AddorEditBillSell.vue"
                            ),
                        meta: {
                            breadcrumbName: "Sửa hoá đơn bán",
                            requiresAuth: true,
                        },
                    },
                ],
            },
            {
                path: "importbill",
                name: "ImportBill",
                component: LayoutView,
                meta: {
                    breadcrumbName: "Hoá đơn nhập",
                    requiresAuth: true,
                },
                children: [
                    {
                        path: "",
                        name: "ListImportBill",
                        component: () =>
                            import(
                                "~/components/ImportBill/ListImportBill.vue"
                            ),
                        meta: {
                            breadcrumbName: "Danh sách",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "add",
                        name: "AddImportBill",
                        component: () =>
                            import(
                                "~/components/ImportBill/AddorEditImportBill.vue"
                            ),
                        meta: {
                            breadcrumbName: "Thêm hoá đơn nhập",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "edit/:id",
                        name: "EditImportBill",
                        component: () =>
                            import(
                                "~/components/ImportBill/AddorEditImportBill.vue"
                            ),
                        meta: {
                            breadcrumbName: "Sửa hoá đơn nhập",
                            requiresAuth: true,
                        },
                    },
                ],
            },
            {
                path: "menuitem",
                name: "MenuItem",
                component: LayoutView,
                meta: {
                    breadcrumbName: "Đồ ăn",
                    requiresAuth: true,
                },
                children: [
                    {
                        path: "",
                        name: "ListMenuItem",
                        component: () =>
                            import("~/components/MenuItem/ListMenuItem.vue"),
                        meta: {
                            breadcrumbName: "Danh sách",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "add",
                        name: "AddMenuItem",
                        component: () =>
                            import(
                                "~/components/MenuItem/AddorEditMenuItem.vue"
                            ),
                        meta: {
                            breadcrumbName: "Thêm đồ ăn",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "edit/:id",
                        name: "EditMenuItem",
                        component: () =>
                            import(
                                "~/components/MenuItem/AddorEditMenuItem.vue"
                            ),
                        meta: {
                            breadcrumbName: "Sửa đồ ăn",
                            requiresAuth: true,
                        },
                    },
                ],
            },
            {
                path: "rentalitem",
                name: "RentalItem",
                component: LayoutView,
                meta: {
                    breadcrumbName: "Đồ thuê",
                    requiresAuth: true,
                },
                children: [
                    {
                        path: "",
                        name: "ListRentalItem",
                        component: () =>
                            import(
                                "~/components/RentalItem/ListRentalItem.vue"
                            ),
                        meta: {
                            breadcrumbName: "Danh sách",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "add",
                        name: "AddRentalItem",
                        component: () =>
                            import(
                                "~/components/RentalItem/AddorEditRentalItem.vue"
                            ),
                        meta: {
                            breadcrumbName: "Thêm sản phẩm thuê",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "edit/:id",
                        name: "EditRentalItem",
                        component: () =>
                            import(
                                "~/components/RentalItem/AddorEditRentalItem.vue"
                            ),
                        meta: {
                            breadcrumbName: "Sửa sản phẩm thuê",
                            requiresAuth: true,
                        },
                    },
                ],
            },
            {
                path: "employeetype",
                name: "EmployeeType",
                component: LayoutView,
                meta: {
                    breadcrumbName: "Loại nhân viên",
                    requiresAuth: true,
                },
                children: [
                    {
                        path: "",
                        name: "ListEmployeeType",
                        component: () =>
                            import(
                                "~/components/EmployeeType/ListEmployeeType.vue"
                            ),
                        meta: {
                            breadcrumbName: "Danh sách",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "add",
                        name: "AddEmployeeType",
                        component: () =>
                            import(
                                "~/components/EmployeeType/AddorEditEmployeeType.vue"
                            ),
                        meta: {
                            breadcrumbName: "Thêm loại nhân viên",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "edit/:id",
                        name: "EditEmployeeType",
                        component: () =>
                            import(
                                "~/components/EmployeeType/AddorEditEmployeeType.vue"
                            ),
                        meta: {
                            breadcrumbName: "Sửa loại nhân viên",
                            requiresAuth: true,
                        },
                    },
                ],
            },
            {
                path: "employee",
                name: "Employee",
                component: LayoutView,
                meta: {
                    breadcrumbName: "Nhân viên",
                    requiresAuth: true,
                },
                children: [
                    {
                        path: "",
                        name: "ListEmployee",
                        component: () =>
                            import("~/components/Employee/ListEmployee.vue"),
                        meta: {
                            breadcrumbName: "Danh sách",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "add",
                        name: "AddEmployee",
                        component: () =>
                            import(
                                "~/components/Employee/AddorEditEmployee.vue"
                            ),
                        meta: {
                            breadcrumbName: "Thêm nhân viên",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "edit/:id",
                        name: "EditEmployee",
                        component: () =>
                            import(
                                "~/components/Employee/AddorEditEmployee.vue"
                            ),
                        meta: {
                            breadcrumbName: "Sửa nhân viên",
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
                path: "banner",
                name: "Banner",
                component: LayoutView,
                meta: {
                    breadcrumbName: "Banner",
                    requiresAuth: true,
                },
                children: [
                    {
                        path: "",
                        name: "ListBanner",
                        component: () =>
                            import("~/components/Banner/ListBanner.vue"),
                        meta: {
                            breadcrumbName: "Danh sách",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "add",
                        name: "AddBanner",
                        component: () =>
                            import("~/components/Banner/AddorEditBanner.vue"),
                        meta: {
                            breadcrumbName: "Thêm banner",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "edit/:id",
                        name: "EditBanner",
                        component: () =>
                            import("~/components/Banner/AddorEditBanner.vue"),
                        meta: {
                            breadcrumbName: "Sửa banner",
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
                        name: "AddCategoryMenuItem",
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
                        name: "EditCategoryMenuItem",
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
                path: "categoryrentalitem",
                name: "CategoryRentalItem",
                component: LayoutView,
                meta: {
                    breadcrumbName: "Danh mục thuê",
                    requiresAuth: true,
                },
                children: [
                    {
                        path: "",
                        name: "ListCategoryRentalItem",
                        component: () =>
                            import(
                                "~/components/CategoryRentalItem/ListCategoryRentalItem.vue"
                            ),
                        meta: {
                            breadcrumbName: "Danh sách",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "add",
                        name: "AddCategoryRentalItem",
                        component: () =>
                            import(
                                "~/components/CategoryRentalItem/AddorEditCategoryRentalItem.vue"
                            ),
                        meta: {
                            breadcrumbName: "Thêm danh mục thuê",
                            requiresAuth: true,
                        },
                    },
                    {
                        path: "edit/:id",
                        name: "EditCategoryRentalItem",
                        component: () =>
                            import(
                                "~/components/CategoryRentalItem/AddorEditCategoryRentalItem.vue"
                            ),
                        meta: {
                            breadcrumbName: "Sửa danh mục thuê",
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
