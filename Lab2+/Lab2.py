# Найти все автоморфные числа в интервале от 1 до 1000.
# Автоморфными называются числа, которые содержатся
# в последних разрядах их квадрата, например: 5 ** 2 = 25; 25 ** 2 = 625

# def is_amfotern(x):
#     val1 = str(x)
#     val2 = str(x ** 2)
#     find = val2.rfind(val1)
#     return find + len(val1) == len(val2)
#
# for i in range(1, 1001):
#     if is_amfotern(i):
#         print(i)

m, n = (1, 1000)
for i in range(m, n + 1):
    i_str = str(i)
    i_sqr_str = str(i ** 2)
    if i_sqr_str.endswith(i_str):
        print(i)


for i in range(1, 1001):
    if str(i ** 2).rfind(str(i)) + len(str(i)) == len(str(i ** 2)):
        print(i)


