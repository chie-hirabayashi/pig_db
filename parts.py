from datetime import datetime
from db_config import Day
from db_config import Number
from dateutil import relativedelta
import statistics


def mk_all_l():
    all_list = []
    for n in Day.select():
        if n.delete_day == "3000/1/1":
            no = n.pig_no
            all_list.append(no)
    return all_list


""" リスト作成 """


def list_number(pig_no):  # numberリスト
    number = Number.get(Number.pig_no == pig_no)
    List = [
        f"{number.pig_no}",
        f"{number.born_num1}",
        f"{number.born_num2}",
        f"{number.born_num3}",
        f"{number.born_num4}",
        f"{number.born_num5}",
        f"{number.born_num6}",
        f"{number.born_num7}",
        f"{number.born_num8}",
        f"{number.born_num9}",
        f"{number.born_num10}",
        f"{number.born_num11}",
        f"{number.born_num12}",
        f"{number.pub_datetime}",
    ]

    return List


def list_day(pig_no):  # dayリスト
    day = Day.get(Day.pig_no == pig_no)
    List = [
        f"{day.pig_no}",
        f"{day.add_day}",
        f"{day.born_day1}",
        f"{day.born_day2}",
        f"{day.born_day3}",
        f"{day.born_day4}",
        f"{day.born_day5}",
        f"{day.born_day6}",
        f"{day.born_day7}",
        f"{day.born_day8}",
        f"{day.born_day9}",
        f"{day.born_day10}",
        f"{day.born_day11}",
        f"{day.born_day12}",
        f"{day.delete_day}",
        f"{day.pub_datetime}",
    ]

    return List


# リスト作成コード
# pig_no = "28-10"
# List = list_number(pig_no)  # numberのリスト作成
# List = list_day(pig_no)  # dayのリスト作成


""" Aコマンドで使用 """


def create(new_no, new_day):
    Day.create(
        pig_no=new_no,
        add_day=new_day,
        born_day1="1900/1/1",
        born_day2="1900/1/1",
        born_day3="1900/1/1",
        born_day4="1900/1/1",
        born_day5="1900/1/1",
        born_day6="1900/1/1",
        born_day7="1900/1/1",
        born_day8="1900/1/1",
        born_day9="1900/1/1",
        born_day10="1900/1/1",
        born_day11="1900/1/1",
        born_day12="1900/1/1",
        delete_day="3000/1/1",
    )
    Number.create(
        pig_no=new_no,
        born_num1=0,
        born_num2=0,
        born_num3=0,
        born_num4=0,
        born_num5=0,
        born_num6=0,
        born_num7=0,
        born_num8=0,
        born_num9=0,
        born_num10=0,
        born_num11=0,
        born_num12=0,
    )


# 新data登録コード
# new_no = "77-77"
# new_day = "2019/7/7"
# create(new_no, new_day)

""" Rコマンドで使用 """


def in_born_data1(pig_no, new_day, new_num):  # born1用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day1 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num1 = new_num
    number.save()


def in_born_data2(pig_no, new_day, new_num):  # born2用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day2 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num2 = new_num
    number.save()


def in_born_data3(pig_no, new_day, new_num):  # born3用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day3 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num3 = new_num
    number.save()


def in_born_data4(pig_no, new_day, new_num):  # born4用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day4 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num4 = new_num
    number.save()


def in_born_data5(pig_no, new_day, new_num):  # born5用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day5 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num5 = new_num
    number.save()


def in_born_data6(pig_no, new_day, new_num):  # born6用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day6 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num6 = new_num
    number.save()


def in_born_data7(pig_no, new_day, new_num):  # born7用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day7 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num7 = new_num
    number.save()


def in_born_data8(pig_no, new_day, new_num):  # born8用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day8 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num8 = new_num
    number.save()


def in_born_data9(pig_no, new_day, new_num):  # born9用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day9 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num9 = new_num
    number.save()


def in_born_data10(pig_no, new_day, new_num):  # born10用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day10 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num10 = new_num
    number.save()


def in_born_data11(pig_no, new_day, new_num):  # born11用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day11 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num11 = new_num
    number.save()


def in_born_data12(pig_no, new_day, new_num):  # born12用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day12 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num12 = new_num
    number.save()


# 出産情報登録コード
# pig_no = "28-10"
# new_day = input("出産日は？")
# new_num = 10

# in_born_data1(pig_no, new_day, new_num)  # born1入力
# in_born_data2(pig_no, new_day, new_num)  # born2入力
# in_born_data3(pig_no, new_day, new_num)  # born3入力
# in_born_data4(pig_no, new_day, new_num)  # born4入力
# in_born_data5(pig_no, new_day, new_num)  # born5入力
# in_born_data6(pig_no, new_day, new_num)  # born6入力
# in_born_data7(pig_no, new_day, new_num)  # born7入力
# in_born_data8(pig_no, new_day, new_num)  # born8入力
# in_born_data9(pig_no, new_day, new_num)  # born9入力
# in_born_data10(pig_no, new_day, new_num)  # born10入力
# in_born_data11(pig_no, new_day, new_num)  # born11入力
# in_born_data12(pig_no, new_day, new_num)  # born12入力


""" Fコマンドで使用 """


def pig_info(pig_no, number_l, day_l):
    born_span_l = []
    for n in range(2, 13):
        born_span = datetime.strptime(day_l[n + 1], "%Y/%m/%d") - datetime.strptime(
            day_l[n], "%Y/%m/%d"
        )
        born_span_l.append(born_span)

    idx = 10  # 初期値を設定 possibly unbound 回避
    for n in range(0, 10):  # 直近の出産日index取得
        if born_span_l[n].days < 0:
            idx = born_span_l.index(born_span_l[n])
            break
        else:
            idx = 10

    if born_span_l[(idx - 1)].days == 0:
        rotate = 0  # division by zero 回避
    else:
        rotate = 365 / born_span_l[(idx - 1)].days  # 回転数算出

    d = Day.get(Day.pig_no == pig_no)
    add_day = (datetime.strptime(d.add_day, "%Y/%m/%d")).strftime("%Y%m%d")
    today = (datetime.now()).strftime("%Y%m%d")
    age = int((int(today) - int(add_day) + 600) / 10000)

    print(
        f"NO.{pig_no}",
        f"年齢:{age}歳",
        f"出産日:{day_l[idx+2]}",
        f"産子数:{number_l[idx+1]}匹",
        f"回転数:{round(rotate, 2)}回",
    )


# dict形式で返す
def pig_info_dic(pig_no, number_l, day_l):
    born_span_l = []
    for n in range(2, 13):
        born_span = datetime.strptime(day_l[n + 1], "%Y/%m/%d") - datetime.strptime(
            day_l[n], "%Y/%m/%d"
        )
        born_span_l.append(born_span)

    idx = 10  # 初期値を設定 possibly unbound 回避
    for n in range(0, 10):  # 直近の出産日index取得
        if born_span_l[n].days < 0:
            idx = born_span_l.index(born_span_l[n])
            break
        else:
            idx = 10

    if born_span_l[(idx - 1)].days == 0:
        rotate = 0  # division by zero 回避
    else:
        rotate = 365 / born_span_l[(idx - 1)].days  # 回転数算出

    d = Day.get(Day.pig_no == pig_no)
    add_day = (datetime.strptime(d.add_day, "%Y/%m/%d")).strftime("%Y%m%d")
    today = (datetime.now()).strftime("%Y%m%d")
    age = int((int(today) - int(add_day) + 600) / 10000)

    # 辞書リスト作成
    rotate_ro = round(rotate, 2)
    key = ["NO", "年齢", "出産日", "産子数", "回転数"]
    value = [pig_no, age, day_l[idx + 2], number_l[idx + 1], rotate_ro]
    pic_dic = dict(zip(key, value))  # すべてのpigの辞書作成
    return pic_dic

    # 最近の出産情報表示コード


# pig_no = "28-10"
# number_l = list_number(pig_no)
# day_l = list_day(pig_no)
# pig_info_dic(pig_no, number_l, day_l)
# print(pig_dic)


""" Cコマンドで使用 """


def delete_day_delete():  # delete_dayの日付がtodayより前のデータを削除
    for p in Day.select():
        pig_no = p.pig_no
        day = Day.get(Day.pig_no == pig_no)
        # print(type(day.delete_day))
        delete_day = datetime.strptime(day.delete_day, "%Y/%m/%d").date()
        today = datetime.now().date()  # .date()でdate型に変換
        if (delete_day - today).days < 0:
            number = Number.get(Number.pig_no == pig_no)
            day = Day.get(Day.pig_no == pig_no)
            number.delete_instance()
            day.delete_instance()
        else:
            pass


# delete_day_delete()


def check(list_day):  # 2回以上出産した個体の平均算出
    all_pig_l = []  # 空リスト用意(すべてのpigの辞書が入る)
    for p in Day.select():
        pig_no = p.pig_no
        day_l = list_day(pig_no)
        born_span_l = []
        for n in range(2, 13):
            born_span = datetime.strptime(day_l[n + 1], "%Y/%m/%d") - datetime.strptime(
                day_l[n], "%Y/%m/%d"
            )
            born_span_l.append(born_span)
        idx = 10  # 初期値を設定 possibly unbound 回避
        print(born_span_l)
        for n in range(0, 10):  # 直近の出産日index取得
            if born_span_l[n].days < 0:
                idx = born_span_l.index(born_span_l[n])
                if idx == 0:  # pig_noが産子数(2)に入る防止
                    idx = 1
                else:
                    pass
                break
            else:
                idx = 10
        if born_span_l[(idx - 1)].days == 0:
            rotate = 0  # division by zero 回避
        else:
            rotate = 365 / born_span_l[(idx - 1)].days  # 回転数算出
            if rotate < 0:  # 過去1回しか出産していない場合rotateがマイナスになる防止
                rotate = 0
            else:
                pass

        # 辞書リスト作成
        key = ["pig_no", "rotate"]
        value = [pig_no, f"{round(rotate,2)}"]
        p_dic = dict(zip(key, value))  # すべてのpigの辞書作成
        all_pig_l.append(p_dic)  # すべてのpigの辞書をリスト化
    r_l = []
    for i in range(len(all_pig_l)):  # 1つずつpigの辞書を取り出す
        p_info = all_pig_l[i]
        r = float(p_info["rotate"])
        if 0 < r:
            r_l.append(r)
        else:
            pass
    print(r_l)

    mean = statistics.mean(r_l)
    print(f"平均回転数: {round(mean, 2)}回")


# 全体の平均回転数を算出
# check(list_day)

# return形式
def check_re(list_day):  # 2回以上出産した個体の平均算出
    all_pig_l = []  # 空リスト用意(すべてのpigの辞書が入る)
    for p in Day.select():
        pig_no = p.pig_no
        day_l = list_day(pig_no)
        born_span_l = []
        for n in range(2, 13):
            born_span = datetime.strptime(day_l[n + 1], "%Y/%m/%d") - datetime.strptime(
                day_l[n], "%Y/%m/%d"
            )
            born_span_l.append(born_span)
        idx = 10  # 初期値を設定 possibly unbound 回避
        print(born_span_l)
        for n in range(0, 10):  # 直近の出産日index取得
            if born_span_l[n].days < 0:
                idx = born_span_l.index(born_span_l[n])
                if idx == 0:  # pig_noが産子数(2)に入る防止
                    idx = 1
                else:
                    pass
                break
            else:
                idx = 10
        if born_span_l[(idx - 1)].days == 0:
            rotate = 0  # division by zero 回避
        else:
            rotate = 365 / born_span_l[(idx - 1)].days  # 回転数算出
            if rotate < 0:  # 過去1回しか出産していない場合rotateがマイナスになる防止
                rotate = 0
            else:
                pass

        # 辞書リスト作成
        key = ["pig_no", "rotate"]
        value = [pig_no, f"{round(rotate,2)}"]
        p_dic = dict(zip(key, value))  # すべてのpigの辞書作成
        all_pig_l.append(p_dic)  # すべてのpigの辞書をリスト化
    r_l = []
    for i in range(len(all_pig_l)):  # 1つずつpigの辞書を取り出す
        p_info = all_pig_l[i]
        r = float(p_info["rotate"])
        if 0 < r:
            r_l.append(r)
        else:
            pass
    print(r_l)

    mean = statistics.mean(r_l)
    return round(mean, 2)


# 全体の平均回転数を算出
# check_re(list_day)


""" Sコマンドで使用 """


def search(list_number, list_day):
    all_pig_l = []  # 空リスト用意(すべてのpigの辞書が入る)
    for p in Day.select():
        pig_no = p.pig_no
        d = Day.get(Day.pig_no == pig_no)

        #  age算出
        add_day = (datetime.strptime(d.add_day, "%Y/%m/%d")).strftime("%Y%m%d")
        today = (datetime.now()).strftime("%Y%m%d")
        age = int((int(today) - int(add_day) + 600) / 10000)

        # rotate算出
        number_l = list_number(pig_no)
        day_l = list_day(pig_no)
        born_span_l = []
        for n in range(2, 13):
            born_span = datetime.strptime(day_l[n + 1], "%Y/%m/%d") - datetime.strptime(
                day_l[n], "%Y/%m/%d"
            )
            born_span_l.append(born_span)
        idx = 10  # 初期値を設定 possibly unbound 回避
        print(born_span_l)
        for n in range(0, 10):  # 直近の出産日index取得
            if born_span_l[n].days < 0:
                idx = born_span_l.index(born_span_l[n])
                if idx == 0:  # pig_noが産子数(2)に入る防止
                    idx = 1
                else:
                    pass
                break
            else:
                idx = 10
        if born_span_l[(idx - 1)].days == 0:
            rotate = 0  # division by zero 回避
        else:
            rotate = 365 / born_span_l[(idx - 1)].days  # 回転数算出
            if rotate < 0:  # 過去1回しか出産していない場合rotateがマイナスになる防止
                rotate = 0
            else:
                pass

        span = (datetime.now() - datetime.strptime(day_l[idx + 2], "%Y/%m/%d")).days

        # 辞書リスト作成
        key = ["pig_no", "age", "rotate", "num1", "num2", "span"]
        value = [
            pig_no,
            age,
            f"{round(rotate,2)}",
            number_l[idx],
            number_l[idx + 1],
            span,
        ]
        p_dic = dict(zip(key, value))  # すべてのpigの辞書作成
        all_pig_l.append(p_dic)  # すべてのpigの辞書をリスト化

    for i in range(len(all_pig_l)):  # 1つずつpigの辞書を取り出す
        p_info = all_pig_l[i]
        r = float(p_info["rotate"])
        n1 = int(p_info["num1"])
        n2 = int(p_info["num2"])
        s = int(p_info["span"])
        if 0 < r < 2.2 or (0 < n1 <= 8 and 0 < n2 <= 8) or 730 > s > 165:
            print(
                f"NO.{p_info['pig_no']}",
                f"年齢:{p_info['age']}歳",
                f"回転数:{p_info['rotate']}回",
                f"産子数(1):{p_info['num1']}匹",
                f"産子数(2):{p_info['num2']}匹",
                f"予測回転数:{round(365/s,2)}回",  # 最後の出産日から165日経過した個体を抽出
            )
        else:
            pass


# list形式で返す
def search_list(list_number, list_day):
    all_pig_l = []  # 空リスト用意(すべてのpigの辞書が入る)
    for p in Day.select():
        pig_no = p.pig_no
        d = Day.get(Day.pig_no == pig_no)

        #  age算出
        add_day = (datetime.strptime(d.add_day, "%Y/%m/%d")).strftime("%Y%m%d")
        today = (datetime.now()).strftime("%Y%m%d")
        age = int((int(today) - int(add_day) + 600) / 10000)

        # rotate算出
        number_l = list_number(pig_no)
        day_l = list_day(pig_no)
        born_span_l = []
        for n in range(2, 13):
            born_span = datetime.strptime(day_l[n + 1], "%Y/%m/%d") - datetime.strptime(
                day_l[n], "%Y/%m/%d"
            )
            born_span_l.append(born_span)
        idx = 10  # 初期値を設定 possibly unbound 回避
        print(born_span_l)
        for n in range(0, 10):  # 直近の出産日index取得
            if born_span_l[n].days < 0:
                idx = born_span_l.index(born_span_l[n])
                if idx == 0:  # pig_noが産子数(2)に入る防止
                    idx = 1
                else:
                    pass
                break
            else:
                idx = 10
        if born_span_l[(idx - 1)].days == 0:
            rotate = 0  # division by zero 回避
        else:
            rotate = 365 / born_span_l[(idx - 1)].days  # 回転数算出
            if rotate < 0:  # 過去1回しか出産していない場合rotateがマイナスになる防止
                rotate = 0
            else:
                pass

        span = (datetime.now() - datetime.strptime(day_l[idx + 2], "%Y/%m/%d")).days

        # 辞書リスト作成
        key = ["pig_no", "age", "rotate", "num1", "num2", "span"]
        value = [
            pig_no,
            age,
            f"{round(rotate,2)}",
            number_l[idx],
            number_l[idx + 1],
            span,
        ]
        p_dic = dict(zip(key, value))  # すべてのpigの辞書作成
        all_pig_l.append(p_dic)  # すべてのpigの辞書をリスト化

    pig_list = []
    for i in range(len(all_pig_l)):  # 1つずつpigの辞書を取り出す
        p_info = all_pig_l[i]
        r = float(p_info["rotate"])
        n1 = int(p_info["num1"])
        n2 = int(p_info["num2"])
        s = int(p_info["span"])
        if 0 < r < 2.2 or (0 < n1 <= 8 and 0 < n2 <= 8) or 730 > s > 315:
        # if 0 < r < 2.2 or (0 < n1 <= 8 and 0 < n2 <= 8) or 730 > s > 165:
            rotate = round(365 / s, 2)
            # key = ["NO", "年齢", "回転数", "産子数(1)", "産子数(2)", "予測回転数"]
            value = [
                f"{p_info['pig_no']}",
                f"{p_info['age']}",
                f"{p_info['rotate']}",
                f"{p_info['num1']}",
                f"{p_info['num2']}",
                f"{rotate}",
            ]
            pig_list.append(value)
            # pig_dic = dict(zip(key, value))  # すべてのpigの辞書作成

            # print(
            #     f"NO.{p_info['pig_no']}",
            #     f"年齢:{p_info['age']}歳",
            #     f"回転数:{p_info['rotate']}回",
            #     f"産子数(1):{p_info['num1']}匹",
            #     f"産子数(2):{p_info['num2']}匹",
            #     f"予測回転数:{round(365/s,2)}回",  # 最後の出産日から165日経過した個体を抽出
            # )
    # search_list.append(pig_dic)
    return pig_list


# 生産性低い個体を探すキー
# search_list(list_number, list_day)


""" Dコマンドで使用 """


def delete_day_set(pig_no):  # 時限爆弾設置(str型でDBに登録)
    day = Day.get(Day.pig_no == pig_no)
    delete_day = (datetime.now() + relativedelta.relativedelta(years=1)).strftime(
        "%Y/%m/%d"
    )
    day.delete_day = delete_day
    day.save()


# pig_no = "77-77"
# delete_day_set(pig_no)


""" 全削除用 """


def delete_alldays():  # 全day削除
    for day in Day.select():
        day.delete_instance()


def delete_allnums():  # 全number削除
    for num in Number.select():
        num.delete_instance()


# delete_alldays()  # 削除キー
# delete_allnums()  # 削除キー
