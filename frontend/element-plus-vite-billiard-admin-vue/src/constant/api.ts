export interface ResponseData<T> {
    data: T[];
    page: number;
    pageSize: number;
    totalItems: number;
}

export interface User {
    anhdaidien: string;
    email: string;
    hoten: string;
    maLoaitaikhoan: number;
    mataikhoan: number;
    sodienthoai: string;
    taikhoan: string;
    token: string;
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
    maTinTuc?: number;
    tieuDe: string;
    noiDung: string;
    hinhAnh: string;
    maTaiKhoan?: number;
    luotXem?: number;
    hoTen?: string;
    trangThai: string;
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
