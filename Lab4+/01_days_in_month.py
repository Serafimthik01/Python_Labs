#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели месяц №', month)

# month31 = [1, 3, 5, 7, 8, 10, 12]
month30 = [4, 6, 9, 11]
if month in month30:
    print('В этом месяце', 30, 'дней')

elif month == 2:
    print('В этом месяце', 28, 'дней')

elif month > 0 and month <= 12:
    print('В этом месяце', 31, 'день')

else:
    print('Номер месяца некорректен')