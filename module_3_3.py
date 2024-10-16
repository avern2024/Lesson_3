#1.Функция с параметрами по умолчанию:
def  print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c = [1,2,3])
print()

# 2.Распаковка параметров:
values_list = [3, 'Str', True]
values_list.remove('Str')
values_dict = {'a': 5, 'b': '23', 'c': False}
del values_dict['a']
del values_dict['b']
print_params(*values_list, **values_dict)
print()

# 3.Распаковка + отдельные параметры:
values_list_2 = [44, 'mis']
print_params(*values_list_2, 42)