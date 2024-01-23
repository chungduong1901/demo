import csv
def nhap_ten_sinh_vien():
    ten_sinh_vien=input("nhập tên sinh viên : ")
    diem1=float(input("nhập điểm 1 : "))
    diem2=float(input('nhập điểm 2 : '))
    diem3=float(input('nhập điểm 3 : '))
    
    sinh_vien={
        'ten':ten_sinh_vien,
        'diem':[diem1,diem2,diem3]
    }
    danh_sach_sinh_vien.append(sinh_vien)
    print("Đã thêm thành công sinh viên ")
def danh_sach_sinhvien():
    for sinh_vien in danh_sach_sinh_vien:
        print(f'{sinh_vien['ten']}|{sinh_vien['diem']}')
def theo_Thu_tu_tang_dan():
    danh_sach_sinh_vien.sort(key=lambda x:x['diem'],reverse =True)
    print("Danh sách điểm theo thứ tự tăng dần \n")
    for sinh_vien in danh_sach_sinh_vien:
        print(f'{sinh_vien['ten']}|{sinh_vien['diem']}')


def bang_nhung_hoc_sinh_diem_cao():
    nguong_diem=float(input("nhập điểm cần : "))
    sinh_vien_tren_diem=[sinh_vien for sinh_vien in danh_sach_sinh_vien if max(sinh_vien['diem'])>nguong_diem]
    if not sinh_vien_tren_diem:
        print("khong co sinh vien nao")
        return
    print(f"Danh sách học sinh có điểm cao hơn {nguong_diem}")
    for sinh_vien in sinh_vien_tren_diem:
        print(f'{sinh_vien['ten']}|{sinh_vien['diem']}')
def diem_trung_binh():
    print("Điểm trung bình của học sinh \n")
    for sinh_vien in danh_sach_sinh_vien:
        dtb=sum(sinh_vien['diem'])/3
        print(f'{sinh_vien['ten']}| Điểm Trung bình {dtb} ')
def xep_loai(sinh_vien):
    dtb = sum(sinh_vien['diem']) / 3
    if dtb >= 9:
        return "Xuất sắc"
    elif dtb >= 8:
        return "Giỏi"
    elif dtb >= 7:
        return "Khá"
    elif dtb >= 5:
        return "Trung bình"
    else:
        return "Yếu"

def hien_thi_xep_loai():
    print("Xếp loại sinh viên")
    for sinh_vien in danh_sach_sinh_vien:
        loai = xep_loai(sinh_vien)
        print(f"{sinh_vien['ten']} | Xếp loại: {loai}")

def luu_danh_sach_sinh_vien_vao_csv():
    file_path = 'files/ds_sv.csv'
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Tên', 'Điểm 1', 'Điểm 2', 'Điểm 3']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for sinh_vien in danh_sach_sinh_vien:
            writer.writerow({
                'Tên': sinh_vien['ten'],
                'Điểm 1': sinh_vien['diem'][0],
                'Điểm 2': sinh_vien['diem'][1],
                'Điểm 3': sinh_vien['diem'][2]
            })

    print(f"Danh sách sinh viên đã được lưu vào tệp {file_path}")



def menu():
    while True:
        print("Bảng chọn \n")
        print("1. Thêm sinh viên ")
        print("2. Danh sách sinh viên")
        print("3. Sắp xếp theo điểm tăng dần")
        print("4. Sinh viên có điểm cao hơn mức là :")
        print("5. Danh sách điểm trung bình ")
        print("6. Xếp loại")
        print("7. lưu và thoát")



        lua_chon=input("nhập số từ 1 đến 10 ")
        if lua_chon =="1":
          nhap_ten_sinh_vien()
        elif lua_chon=="2":
          danh_sach_sinhvien()
        elif lua_chon=="3":
            theo_Thu_tu_tang_dan()
        elif lua_chon=="4":
            bang_nhung_hoc_sinh_diem_cao()
        elif lua_chon =="5":
            diem_trung_binh()
        elif lua_chon=="6":
            hien_thi_xep_loai()
        elif lua_chon=="7":
            luu_danh_sach_sinh_vien_vao_csv()
        else:
            print("số không hợp lệ")

    


















if __name__=="__main__":
    danh_sach_sinh_vien=[]
    menu()

