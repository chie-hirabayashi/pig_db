

from datetime import datetime
from db_config import Day, Number


# Cコマンド用 時限爆弾の起爆機能
# pig_no = "99-99"
for p in Day.select():
    pig_no = p.pig_no
    day = Day.get(Day.pig_no == pig_no)
    # print(type(day.delete_day))
    delete_day = day.delete_day
    today = datetime.now().date()  # .date()でdate型に変換
    if (delete_day - today).days < 0:
        number = Number.get(Number.pig_no == pig_no)
        day = Day.get(Day.pig_no == pig_no)
        number.delete_instance()
        day.delete_instance()
    else:
        pass

""" エラー内容
TypeError: unsupported operand type(s) for -: 'str' and 'datetime.date'
delete_day内にstr型とdatetime型が混在することによる
datetime型で入力が必要
上書きのエラーにも関連するかも
"""
# 99-99作ってテスト



def delete(pig_no):  # 単純削除機能
    number = Number.get(Number.pig_no == pig_no)
    day = Day.get(Day.pig_no == pig_no)
    number.delete_instance()
    day.delete_instance()


# delete(pig_no)