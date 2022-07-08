from dateutil import relativedelta
from datetime import datetime
from db_config import Day, Number


# Cコマンド用 時限爆弾の起爆機能
def delete_day_delete():
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


delete_day_delete()

""" エラー内容
TypeError: unsupported operand type(s) for -: 'str' and 'datetime.date'
delete_day内にstr型とdatetime型が混在することによる
datetime型で入力が必要
上書きのエラーにも関連するかも
"""
# 99-99作ってテスト
"""


def delete_day_set(pig_no):  # 時限爆弾設置(str型でDBに登録)
    day = Day.get(Day.pig_no == pig_no)
    delete_day = (datetime.now() + relativedelta.relativedelta(years=1)).strftime("%Y/%m/%d")
    day.delete_day = delete_day
    day.save()


def delete_day_set(pig_no):  # 時限爆弾設置
    # number = Number.get(Number.pig_no == pig_no)
    day = Day.get(Day.pig_no == pig_no)
    delete_day = datetime.now() + relativedelta.relativedelta(years=1)
    # number.delete_day = delete_day
    # number.save()
    day.delete_day = delete_day
    day.save()


pig_no = "28-10"
day = Day.get(Day.pig_no == pig_no)
delete_day = (datetime.now() + relativedelta.relativedelta(years=1)).strftime("%Y/%m/%d")
print(delete_day)
print(type(delete_day))
"""


def delete(pig_no):  # 単純削除機能
    number = Number.get(Number.pig_no == pig_no)
    day = Day.get(Day.pig_no == pig_no)
    number.delete_instance()
    day.delete_instance()


# delete(pig_no)
