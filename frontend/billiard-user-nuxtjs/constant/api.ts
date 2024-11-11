export interface ResponseData<T> {
    data: T[];
    page: number;
    pageSize: number;
    totalItems: number;
}

export interface Product {
    maSanPham: number;
    tenSanPham: string;
    anhDaiDien: string;
    giaGiam: number;
    gia: number;
    soLuong: number;
    luotBan: number;
    luotXem: number;
    danhGia: number;
    trongLuong: string;
    moTa: string;
    tendanhmucuudai?: string;
    tenDanhMuc?: string;
    xuatXu: string;
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
    maTinTuc?: number;
    tieuDe: string;
    noiDung: string;
    hinhAnh: string;
    maTaiKhoan?: number;
    luotXem?: number;
    hoTen?: string;
    trangThai: string;
}

export interface Category {
    maDanhMuc?: number;
    tenDanhMuc: string;
    dacBiet: boolean;
    noiDung: string;
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
    anhDaiDien?: string;
    diaChi?: string;
    email?: string;
    hoTen?: string;
    maChitietTaiKhoan?: Number;
    maLoaitaikhoan?: Number;
    maTaiKhoan?: Number;
    matKhau?: string;
    soDienThoai?: string;
    status?: number;
    tenLoai?: string;
    tenTaiKhoan?: string;
}

export interface Cart {
    maGioHang?: number;
    maTaiKhoan: number;
    maSanPham: number;
    anhDaiDien: string;
    tenSanPham: string;
    gia: number;
    giaGiam: number;
    trongLuong: string;
    xuatXu: string;
    soLuongMua: number;
    trangThai: boolean;
}
