from pprint import pprint


PATH = "C:/Users/Evil COre/PycharmProjects/NetologyHomeWorks/Receipts.txt"


def read_file_receipts():
    with open(PATH, 'r', encoding='UTF-8') as receipts:
        cook_book = {}
        for receipt in receipts:
            dish = receipt.strip()
            quantity = receipts.readline().strip()
            ingredients = []
            for ingredient in range(int(quantity)):
                dict_of_ingredients = {}
                data = receipts.readline().strip().split(' | ')
                dict_of_ingredients['ingredient_name'] = data[0]
                dict_of_ingredients['quantity'] = data[1]
                dict_of_ingredients['measure'] = data[2]
                ingredients.append(dict_of_ingredients)
            cook_book[dish] = ingredients
            receipts.readline()
        return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            measure = {}
            measure['measure'] = ingredient['measure']
            measure['quantity'] = int(ingredient['quantity']) * person_count
            if ingredient['ingredient_name'] in shop_list:
                shop_list[ingredient['ingredient_name']]['quantity'] = shop_list[ingredient['ingredient_name']]['quantity'] + measure['quantity']
            else:
                shop_list[ingredient['ingredient_name']] = measure
    return shop_list

pprint(read_file_receipts())
pprint(get_shop_list_by_dishes(read_file_receipts(), ['Запеченный картофель', 'Омлет', 'Шакшука'], 2))


# Задача номер 3

# Получааем словарь из файла
def text_from_file(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        list_of_lines = {}
        lines_from_file = file.readlines()
        lines_count = len(lines_from_file)
        list_of_lines[lines_count] = [file.name, lines_from_file]
        return  list_of_lines

# Создаем словарь словарей из файлов в зависимости от их количества
def dict_of_files(list_of_files):
    dict_of_files = {}
    for count in range(len(list_of_files)):
        dict_of_files.update(text_from_file(list_of_files[count]))
    return dict_of_files

# Записываем наш словарь в файл с использованием фильтра
def write_text_in_file(list_of_files):
    with open('hw_task_3.txt', 'w', encoding='UTF-8') as result_file:
        files = dict_of_files(list_of_files)
        for file in range(len(files.keys())):
            minimum = min(files.keys())
            result_file.write(files[minimum][0] + '\n')
            result_file.write(str(minimum))
            result_file.write('\n')
            for line in files[minimum][1]:
                result_file.write(line)
            files.pop(minimum)
            result_file.write('\n')

# Запускаем функцию записи в файл. можно добавлять/уменьшать количество файлов
write_text_in_file(['1.txt', '2.txt', '3.txt', '4_test.txt'])