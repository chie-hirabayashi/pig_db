
# 年齢
# pig_no = "28-10"
# p = Day.get(Day.pig_no == pig_no)
# print(f"{p.add_day}")
# print(type(p.add_day))
# ad = datetime.strptime(p.add_day, "%Y/%m/%d")
# print(ad)
# print(type(ad))
# str_ad = ad.strftime("%Y%m%d")
# print(str_ad)
# print(type(str_ad))

# today = datetime.now()
# print(today)
# print(type(today))
# str_td = today.strftime("%Y%m%d")
# print(str_td)
# print(type(str_td))

# old = int((int(str_td) - int(str_ad) + 600)/10000)
# print(old)


# index 3...day4-day3
# 回転数はday3-day2...[idx-1]
# 出産日はday4...List[5]...[idx+2]
# 出産頭数はnum4...List[4]...[idx+1]
# tdatetime = datetime.strptime(tstr, "%Y-%m-%d %H:%M:%S")

# 以下をインライン化して関数
# time_l = []
# for n in range(2, 13):
# t_day = datetime.strptime(List[n], "%Y-%m-%d")
# time_l.append(t_day)

# print(time_l)
# day_timne_l = []
# for n in range(10):
# day_time = time_l[n+1] - time_l[n]
# day_timne_l.append(day_time)


def delete(pig_no):  # 単純削除機能
    number = Number.get(Number.pig_no == pig_no)
    day = Day.get(Day.pig_no == pig_no)
    number.delete_instance()
    day.delete_instance()


# pig_no = "99-99"
# delete(pig_no)


"""
# age算出
pig_no = "29-37"
d = Day.get(Day.pig_no == pig_no)
add_day = (datetime.strptime(d.add_day, "%Y/%m/%d")).strftime("%Y%m%d")
today = (datetime.now()).strftime("%Y%m%d")
age = int((int(today) - int(add_day) + 600) / 10000)

# rotate算出
number_l = list_number(pig_no)
day_l = list_day(pig_no)
day_time_l = []
for n in range(2, 13):
    t_day = datetime.strptime(day_l[n + 1], "%Y/%m/%d") - datetime.strptime(
        day_l[n], "%Y/%m/%d"
    )
    day_time_l.append(t_day)
idx = 10  # 初期値を設定 possibly unbound 回避
for n in range(0, 10):  # 直近の出産日index取得
    if day_time_l[n].days < 0:
        idx = day_time_l.index(day_time_l[n])
        break
    else:
        idx = 10
if day_time_l[(idx - 1)].days == 0:
    rotate = 0  # division by zero 回避
else:
    rotate = 365 / day_time_l[(idx - 1)].days  # 回転数算出


key = ["pig_no", "age", "rotate", "num1", "num2"]
value = [pig_no, age, f"{round(rotate,2)}", number_l[idx], number_l[idx + 1]]
p_dic = dict(zip(key, value))
print(p_dic)
print(type(value[3]))
"""


