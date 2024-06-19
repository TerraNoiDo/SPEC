# [12, 3, 4, 10] => [10, 12, 3, 4]
# [1] => [1]
# [] => []
# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]

list_value_1 = [12, 3, 4, 10]
list_value_2 = [1]
list_value_3 = []
list_value_4 = [12, 3, 4, 10, 8]

list_value_1 = list_value_1[-1:] + list_value_1[:-1]
print(str(list_value_1))

list_value_2 = list_value_2[-1:] + list_value_2[:-1]
print(str(list_value_2))

list_value_3 = list_value_3[-1:] + list_value_3[:-1]
print(str(list_value_3))

list_value_4 = list_value_4[-1:] + list_value_4[:-1]
print(str(list_value_4))