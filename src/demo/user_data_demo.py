import os
import sys

# base_quiz_gen_class.py 찾기
current_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, "user data manipulation"))

sys.path.insert(0, parent_dir)

from user_data import UserData

# UserData 클래스 사용 예시
def main():
    # UserData 객체 초기화
    user_data = UserData("resource/userdata.json")

    # 사용자 ID 체크
    print("Check if User1 exists:", user_data.id_check("User1"))  # True

    # 패스워드 확인
    print("Check if User1's password is '1234':", user_data.password_check("User1", 1234))  # True

    # 새 사용자 추가
    new_user_id = "User2"
    new_user_props = {"password": "abcd", "APIKEY": 5678}
    if user_data.add_user(new_user_id, new_user_props):
        print(f"New user {new_user_id} added successfully.")
    else:
        print(f"Failed to add user {new_user_id} (already exists).")

    # 사용자 속성 조회
    print("user2's email:", user_data.get_user_prop("User2", "APIKEY"))  # 5678

    # 사용자 속성 추가
    if user_data.add_prop("Manager", "APIKEY", 9090):
        print("Manager's APIKEY updated successfully.")
    else:
        print("Failed to update Manager's APIKEY")

    # 사용자 속성 수정
    if user_data.modify_prop("User1", "password", 4356):
        print("User1's password updated successfully.")
    else:
        print("Failed to update User1's password")

    # 사용자 속성 삭제제
    if user_data.delete_prop("User1", "APIKEY"):
        print("User1's APIKEY deleted successfully.")
    else:
        print("Failed to delete User1's APIKEY")

    # 사용자 삭제
    if user_data.delete_user("User2"):
        print("User2 deleted successfully.")
    else:
        print("Failed to delete User2 (user not found).")

    # 수정된 데이터를 저장
    user_data.save("resource/updated_user_data.json")
    print("Updated data saved to 'resource/updated_user_data.json'.")

if __name__ == "__main__":
    main()