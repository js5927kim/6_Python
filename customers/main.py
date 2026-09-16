from crm_manager import CRM

def search_customer(customers):
    if not customers:
        print("등록된 고객이 없습니다")
        
    for cus in customers:
        print(cus)

def register_customer(crm):
    cus_id = input("ID : ")
    name = input("이름 : ")
    phone = input("연락처 : ")

    customer = crm.register_customer(cus_id, name, phone)
    print("일반회원 등록 완료")

def register_VIP(crm):
    cus_id = input("ID : ")
    name = input("이름 : ")
    phone = input("연락처 : ")
    manager_name = input("전담 매니저 : ")

    customer = crm.register_VIP(cus_id, name, phone, manager_name)
    print("VIP 등록 완료")

def update_phone(crm):
    cus_id = input("수정할 고객 ID : ")
    new_phone = input("새로운 연락처 : ")

    cus = crm.update_phone(cus_id, new_phone)
    print("번호 수정 완료")

def remove(crm):
    cus_id = input("탈퇴할 고객 ID : ")

    crm.remove(cus_id)
    print(f"{cus_id}번 고객님 탈퇴 완료")



def main():
    crm = CRM()

    while True:
        print("=" * 60)
        print("1 : 일반 고객 등록")
        print("2 : VIP 고객 등록")
        print("3 : 전체 고객 조회")
        print("4 : VIP 고객 조회")
        print("5 : 고객 번호 수정")
        print("6 : 고객 삭제")
        print("0 : 종료")
        menu = int(input("메뉴 선택 : "))
        print("=" * 60)
        if menu == 1:
            register_customer(crm)
        elif menu == 2:
            register_VIP(crm)
        elif menu == 3:
            search_customer(crm.find_all_customer())
        elif menu ==4:
            search_customer(crm.find_VIP())
        elif menu == 5:
            update_phone(crm)
        elif menu == 6:
            remove(crm)
        elif menu == 0:
            print("프로그램 종료")
            break 
        else:
            print("올바른 번호를 입력해 주세요")


if __name__ == "__main__":
    main()      



