#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Составить список всех живущих на районе (пакет district) и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1.room1 import folks as f1
from district.central_street.house1.room2 import folks as f2
from district.central_street.house2.room1 import folks as f3
from district.central_street.house2.room2 import folks as f4

from district.soviet_street.house1.room1 import folks as f5
from district.soviet_street.house1.room2 import folks as f6
from district.soviet_street.house2.room1 import folks as f7
from district.soviet_street.house2.room2 import folks as f8

f_sum = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8
f1_str = ', '.join(f_sum)
print(f'В районе живут: {f1_str}')
