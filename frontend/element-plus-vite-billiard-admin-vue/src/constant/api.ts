export interface ResponseData<T> {
    data: T[];
    page: number;
    pageSize: number;
    totalItems: number;
}

export interface Product {
    maSanPham?: number;
    tenSanPham: string;
    anhDaiDien: string;
    giaGiam: number;
    soLuong: number;
    luotBan: number;
    danhGia: number;
    trongLuong: string;
    tenDanhMuc?: string;
    tendanhmucuudai?: string;
    trangThai: boolean;
}

export interface News {
    _id?: string;
    user_id?: string;
    title: string;
    content: string;
    image: string;
    view?: number;
    status: boolean;
    fullname?: string;
}

export interface CategoryMenuItems {
    _id?: string;
    category_name: string;
}

export interface CategoryRentalItems {
    _id?: string;
    category_name: string;
}

export interface Roles {
    _id?: string;
    role_name: string;
    role_description: string;
}

export interface Users {
    _id?: string;
    username: string;
    password: string;
    fullname: string;
    email: string;
    phone: string;
    address: string;
    avatar: string;
    loyalty_points: number;
    role_name: string;
    token?: string;
}

export interface Manufactors {
    _id?: string;
    name: string;
    phone: string;
    address: string;
}

export interface Suppliers {
    _id?: string;
    name: string;
    phone: string;
    address: string;
}

export interface EmployeeTypes {
    _id?: string;
    employee_type_name: string;
}

export interface Employees {
    _id?: string;
    employee_type_id: string;
    user_id?: string;
    hourly_rate: number;
    monthly_salary: number;
    user_info?: Users;
}

export interface OptionSelect {
    value: string | number;
    label: string;
}
