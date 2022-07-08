import os
import datetime
import logging
from dotenv import load_dotenv
from playhouse.db_url import connect
from peewee import Model, IntegerField, DateField, TextField, TimestampField

print(os.environ.get("PWD"))  # 環境変数の読み込み
load_dotenv()  # .envの読み込み

# ログ出力設定
logger = logging.getLogger("peewee")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

db = connect(os.environ.get("DATABASE"))  # DB接続設定


# 接続NGメッセージ表示
if not db.connect():
    print("接続NG")
    exit()


class Day(Model):
    """Day Model"""

    id = IntegerField(primary_key=True)  # idは自動で追加
    pig_no = TextField()
    add_day = DateField()
    born_day1 = DateField()
    born_day2 = DateField()
    born_day3 = DateField()
    born_day4 = DateField()
    born_day5 = DateField()
    born_day6 = DateField()
    born_day7 = DateField()
    born_day8 = DateField()
    born_day9 = DateField()
    born_day10 = DateField()
    born_day11 = DateField()
    born_day12 = DateField()
    delete_day = DateField()
    pub_datetime = TimestampField(default=datetime.datetime.now())

    class Meta:
        database = db
        table_name = "days"


db.create_tables([Day])


class Number(Model):
    """Number Model"""

    id = IntegerField(primary_key=True)  # idは自動で追加
    pig_no = TextField()
    born_num1 = IntegerField()
    born_num2 = IntegerField()
    born_num3 = IntegerField()
    born_num4 = IntegerField()
    born_num5 = IntegerField()
    born_num6 = IntegerField()
    born_num7 = IntegerField()
    born_num8 = IntegerField()
    born_num9 = IntegerField()
    born_num10 = IntegerField()
    born_num11 = IntegerField()
    born_num12 = IntegerField()
    # delete_day = DateField()
    pub_datetime = TimestampField(default=datetime.datetime.now())

    class Meta:
        database = db
        table_name = "numbers"


db.create_tables([Number])
