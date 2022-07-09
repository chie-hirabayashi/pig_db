from parts import check, create, delete_day_delete, delete_day_set, pig_info, search
from parts import list_number, list_day
from parts import (
    in_born_data1,
    in_born_data2,
    in_born_data3,
    in_born_data4,
    in_born_data5,
    in_born_data6,
    in_born_data7,
    in_born_data8,
    in_born_data9,
    in_born_data10,
    in_born_data11,
    in_born_data12,
)

# コマンドAで実行・・・余裕があったら制限機能(重複、日付、間違い防止)追加
# コマンドDで実行・・・余裕があったら制限機能追加


# if __name__ == "__main__":
# main()

command = ""
while command != "E":
    input_command = input("新規登録: A, 廃用: D, 出産情報の登録: R, 個体情報の確認: F,"
        "生産性の低い母豚の確認: S, 全体の生産性の確認: C, 終了: E から選択してください。; "
    )
    command = input_command.upper()  # 大文字小文字区別なし
    if command in ["A", "D", "R", "F", "S", "C", "E"]:
        if command == "A":  # 新規登録
            new_no = input("登録する母豚NOを入力してください > ")
            new_day = input(f"{new_no}が入荷した日を入力してください(例:2022/7/7) ; ")
            create(new_no, new_day)
            print(f"NO.{new_no}の登録が完了しました")
        if command == "D":  # 廃用
            delete_no = input("廃用にする母豚NOを入力してください ; ")
            delete_day_set(delete_no)
            print(f"NO.{delete_no}を廃用にしました")
        if command == "R":  # 出産情報登録
            register_no = input("出産情報を登録する母豚のNOを入力してください ; ")
            new_born_day = input("出産日を入力してください(例:2022/7/7) ; ")
            new_born_number = input("産子数を入力してください ; ")
            number_l = list_number(register_no)
            if int(number_l[12]) != 0:
                print("データがいっぱいです")
            elif int(number_l[11]) != 0:
                in_born_data12(register_no, new_born_day, new_born_number)
            elif int(number_l[10]) != 0:
                in_born_data11(register_no, new_born_day, new_born_number)
            elif int(number_l[9]) != 0:
                in_born_data10(register_no, new_born_day, new_born_number)
            elif int(number_l[8]) != 0:
                in_born_data9(register_no, new_born_day, new_born_number)
            elif int(number_l[7]) != 0:
                in_born_data8(register_no, new_born_day, new_born_number)
            elif int(number_l[6]) != 0:
                in_born_data7(register_no, new_born_day, new_born_number)
            elif int(number_l[5]) != 0:
                in_born_data6(register_no, new_born_day, new_born_number)
            elif int(number_l[4]) != 0:
                in_born_data5(register_no, new_born_day, new_born_number)
            elif int(number_l[3]) != 0:
                in_born_data4(register_no, new_born_day, new_born_number)
            elif int(number_l[2]) != 0:
                in_born_data3(register_no, new_born_day, new_born_number)
            elif int(number_l[1]) != 0:
                in_born_data2(register_no, new_born_day, new_born_number)
            else:
                in_born_data1(register_no, new_born_day, new_born_number)
            print(f"登録完了...出産日:{new_born_day}, 産子数:{new_born_number}")
        if command == "F":  # 検索
            find_no = input("出産情報を確認する母豚NOを入力してください ; ")
            number_l = list_number(find_no)
            day_l = list_day(find_no)
            pig_info(find_no, number_l, day_l)
        if command == "S":  # 捜索
            search(list_number, list_day)
        if command == "C":  # 確認
            delete_day_delete()
            check(list_day)
        if command == "E":  # 終了
            print("終了します")
    else:
        print(f"{command.lower()}: keyエラー ")
