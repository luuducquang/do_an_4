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

export interface FormProduct extends Product {
    maChiTietSanPham?: number;
    maDanhMuc: number;
    madanhmucuudai: number;
    anhChiTiet: ImgDetail[];
    gianhap: number;
    gia: number;
    trangThai: boolean;
    maNhaSanXuat: number;
    maNhaPhanPhoi: number;
    xuatXu: string;
    moTa: string;
    chiTiet: string;
}

export interface ImgDetail {
    id?: number;
    maSanPham?: number;
    linkAnh: string;
    status: number;
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

export interface Categorys {
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

export interface OptionSelect {
    value: string | number;
    label: string;
    gia?: number;
    hinhAnh?: string;
}
