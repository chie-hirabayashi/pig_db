# from crypt import methods
# from flask import Flask, redirect, render_template, request, url_for
from flask import Flask, render_template, request
from parts import (
    check_re,
    create,
    delete_day_set,
    list_day,
    list_number,
    pig_info_dic,
    search_list,
)
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


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/day")
def day():
    pig_no = "28-10"
    day_l = list_day(pig_no)
    return render_template("day.html", day_l=day_l)


@app.route("/add", methods=["POST"])
def add_pig():
    """新規pigを追加する関数"""
    # フォーム入力されたpig_noとadd_dayを受け取る
    add_no = request.form["add_no"]
    add_day = request.form["add_day"]

    # 登録処理
    create(add_no, add_day)

    # index()にリダイレクトする
    return render_template("index.html", add_no=add_no)


@app.route("/delete", methods=["POST"])
def del_pig():
    """廃用pigを登録する関数"""
    # フォーム入力されたpig_noを受け取る
    del_no = request.form["del_no"]

    # 登録処理
    delete_day_set(del_no)

    # index()にリダイレクトする
    return render_template("index.html", del_no=del_no)


@app.route("/register", methods=["POST"])
def born_pig():
    """出産情報を登録する関数"""
    # フォーム入力されたpig_no、出産日、産子数を受け取る
    register_no = request.form["regi_no"]
    new_born_day = request.form["regi_day"]
    new_born_number = request.form["regi_num"]

    # 登録処理
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

    # index()にリダイレクトする
    return render_template(
        "index.html",
        register_no=register_no,
        new_born_day=new_born_day,
        new_born_number=new_born_number,
    )


@app.route("/find", methods=["POST"])
def find_pig():
    """特定の個体情報を確認する関数"""
    # フォーム入力されたpig_noを受け取る
    find_no = request.form["find_no"]

    # 処理
    number_l = list_number(find_no)
    day_l = list_day(find_no)
    pig_dic = pig_info_dic(find_no, number_l, day_l)

    # index()にリダイレクトする
    return render_template("index.html", pig_dic=pig_dic)


@app.route("/search", methods=["POST"])
def search_pig():
    """生産性の低い豚を探す関数"""

    # 処理
    pig_list = search_list(list_number, list_day)

    # index()にリダイレクトする
    return render_template("index.html", pig_list=pig_list)


@app.route("/check", methods=["POST"])
def check_pig():
    """全体の回転数を表示する関数"""

    # 処理
    check_pig = check_re(list_day)

    # index()にリダイレクトする
    return render_template("index.html", check_pig=check_pig)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
