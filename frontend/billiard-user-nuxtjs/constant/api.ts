export interface ResponseData<T> {
    data: T[];
    page: number;
    pageSize: number;
    totalItems: number;
}

export interface Product {
    _id?: string;
    manufactor_id: string;
    category_id: string;
    item_name: string;
    image: string;
    price: number;
    price_reduction: number;
    rental_price_day: number;
    rental_price_hours: number;
    quantity_available: number;
    view?: number;
    origin: string;
    description: string;
    description_detail: string;
    categoryrentalitem?: CategoryRentalItems;
    manufactor?: Manufactors;
}

export interface CategoryRentalItems {
    _id?: string;
    category_name: string;
}

export interface Manufactors {
    _id?: string;
    name: string;
    phone: string;
    address: string;
}

export interface User {
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

export interface ImgDetail {
    id?: number;
    maSanPham?: number;
    linkAnh: string;
    status: number;
}

export interface BillSell {
    maHoaDon?: number;
    tenTaiKhoan?: string;
    trangThai: string;
    ngayTao?: Date;
    tongGia: number;
    tenKH: string;
    diaChi?: string;
    email: string;
    sdt: string;
    diaChiGiaoHang?: string;
    maSanPham?: number;
    soLuong?: number;
    donGia?: number;
    tongTien?: number;
}

export interface TableBillSell {
    maChiTietHoaDon?: number;
    maHoaDon?: number;
    stt?: number;
    maSanPham: number;
    tenSanPham?: string;
    anhDaiDien?: string;
    soLuong: number | string;
    originalSoLuong?: number;
    donGia: number;
    tongGia: number;
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

export interface Category {
    _id?: string;
    category_name: string;
}

export interface CategoryOffer {
    madanhmucuudai?: number;
    tendanhmucuudai: string;
    dacBiet: boolean;
    noiDung: string;
}

export interface Slide {
    maAnh?: number;
    linkAnh: string;
    tieuDe: string;
    moTa: string;
}

export interface Account {
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

export interface Cart {
    _id?: string;
    user_id: string;
    item_id: string;
    quantity: number;
    status: boolean;
    rentalitem?: Product;
}
