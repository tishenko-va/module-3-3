def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params(1,2)
print_params(1,2,3)
print_params()
print_params(b = 25) #сработала
print_params(c = [1,2,3]) #сработала


values_list = [1, False, 'true']
values_dict = {'a': 4, 'b': 'число', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['list', True]
print_params(*values_list_2, 42) #it's warking

