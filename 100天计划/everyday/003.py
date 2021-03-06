# -*- coding: utf-8 -*-
# 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
from pymysql import *

import random
import string


forSelect = string.ascii_letters + string.digits


def generate_code(count, length):
    for x in range(count):
        Re = ""
        for y in range(length):
            Re += random.choice(forSelect)
        yield Re


def save_code():
    conn = connect(host='localhost', port=3306, user='root', password='mysql', database='test', charset='utf8')
    csl = conn.cursor()
    codes = generate_code(200, 20)
    for code in codes:
        csl.execute("INSERT INTO youhuiquan(quanma) VALUES('%s')" % code)
    conn.commit()
    csl.close()


if __name__ == '__main__':
    save_code()
