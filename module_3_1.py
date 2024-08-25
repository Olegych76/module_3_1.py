# счётчик вызовов устанавливаем в ноль:
calls = 0


def count_calls():
    global calls  # используем переменную из глобального пространства имён
    calls += 1  # функция вызвана

def string_info(str_):
    len_str = len(str_)  # длина строки
    str_up = str_.upper()  # строка в верхний регистр
    str_down = str_.lower()  # строка в нижний регистр
    count_calls()  # увеличиваем счётчик вызова функций
    return len_str, str_up, str_down


def is_contains(str_, list_):
    flag = False  # по умолчанию, флаг устанавливаем в Ложь
    for i in range(len(list_)):  # для i в по всему списку
        if str_.lower() == list_[i].lower():  # проверяем на совпадение, предварительно переведя строки в нижний регистр
            flag = True  # если строки совпали, флаг = Истина
            break  # если такая строка нашлась, больше не проверяем
    count_calls()  # увеличиваем счётчик вызова функций
    return flag


print(string_info('Это просто тест'))
print(string_info('Проверяем работу функций'))
print(string_info('Тест прошёл штатно'))

print(is_contains('тест', ['test', 'ТЕСТ', 'Тестирование']))
print(is_contains('цикл', ['cycle', 'ЦИКЛ', 'Цикл']))
print(is_contains('match', ['no match', 'Matching', 'Совпадение']))

print(calls)  # число вызовов функций
