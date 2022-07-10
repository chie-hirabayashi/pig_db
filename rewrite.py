from db_config import Day, Number

# すべての初期データをて入力し直す


def rewrite():
    def create(
        idx1,
        idx2,
        idx3,
        idx4,
        idx5,
        idx6,
        idx7,
        idx8,
        idx9,
        idx10,
        idx11,
        idx12,
        idx13,
        idx14,
        idx15,
        idx16,
        idx17,
        idx18,
        idx19,
        idx20,
        idx21,
        idx22,
        idx23,
        idx24,
        idx25,
        idx26,
        idx27,
    ):
        Day.create(
            pig_no=idx1,
            add_day=idx2,
            born_day1=idx3,
            born_day2=idx4,
            born_day3=idx5,
            born_day4=idx6,
            born_day5=idx7,
            born_day6=idx8,
            born_day7=idx9,
            born_day8=idx10,
            born_day9=idx11,
            born_day10=idx12,
            born_day11=idx13,
            born_day12=idx14,
            delete_day=idx15,
        )

        Number.create(
            pig_no=idx1,
            born_num1=idx16,
            born_num2=idx17,
            born_num3=idx18,
            born_num4=idx19,
            born_num5=idx20,
            born_num6=idx21,
            born_num7=idx22,
            born_num8=idx23,
            born_num9=idx24,
            born_num10=idx25,
            born_num11=idx26,
            born_num12=idx27,
        )

    pig_n_l = []
    for p in Day.select():
        pig_no = p.pig_no
        pig_n_l.append(pig_no)

    for p in pig_n_l:
        pig_no = p
        d = Day.get(Day.pig_no == pig_no)
        n = Number.get(Number.pig_no == pig_no)
        idx1 = d.pig_no
        idx2 = d.add_day
        idx3 = d.born_day1
        idx4 = d.born_day2
        idx5 = d.born_day3
        idx6 = d.born_day4
        idx7 = d.born_day5
        idx8 = d.born_day6
        idx9 = d.born_day7
        idx10 = d.born_day8
        idx11 = d.born_day9
        idx12 = d.born_day10
        idx13 = d.born_day11
        idx14 = d.born_day12
        idx15 = d.delete_day
        idx16 = n.born_num1
        idx17 = n.born_num2
        idx18 = n.born_num3
        idx19 = n.born_num4
        idx20 = n.born_num5
        idx21 = n.born_num6
        idx22 = n.born_num7
        idx23 = n.born_num8
        idx24 = n.born_num9
        idx25 = n.born_num10
        idx26 = n.born_num11
        idx27 = n.born_num12

        create(
            idx1,
            idx2,
            idx3,
            idx4,
            idx5,
            idx6,
            idx7,
            idx8,
            idx9,
            idx10,
            idx11,
            idx12,
            idx13,
            idx14,
            idx15,
            idx16,
            idx17,
            idx18,
            idx19,
            idx20,
            idx21,
            idx22,
            idx23,
            idx24,
            idx25,
            idx26,
            idx27,
        )


# 書き直し
# rewrite()


def delete_id(id_b, id_e):
    def delete(id):  # 単純削除機能
        day = Day.get(Day.id == id)
        day.delete_instance()
        number = Number.get(Number.id == id)
        number.delete_instance()

    for i in range(id_b, id_e + 1):
        id = i
        delete(id)


id_b = 131
id_e = 132
# delete_id(id_b, id_e)


# 上書き確認


def in_born_data1(pig_no, new_day, new_num):  # born1用関数
    day = Day.get(Day.pig_no == pig_no)
    day.born_day1 = new_day
    day.save()
    number = Number.get(Number.pig_no == pig_no)
    number.born_num1 = new_num
    number.save()


# 出産情報登録コード
# pig_no = "28-10"
# new_day = input("出産日は？")
# new_num = 10

# in_born_datac 1(pig_no, new_day, new_num)  # born1入力
