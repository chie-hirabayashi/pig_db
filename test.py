from datetime import datetime
from db_config import Day
import statistics
from parts import list_day

""" Cコマンドで使用 """


def check(list_day):
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


# 回転数の平均を算出
check(list_day)
