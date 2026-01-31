print("Введите элементы списка через пробел:")
input_str = input()
elements = input_str.split()

# Преобразуем элементы в числа, где это возможно
processed_list = []
for element in elements:
    # Пробуем преобразовать в целое число
    try:
        num = int(element)
        processed_list.append(num)
        continue
    except ValueError:
        pass
    
    # Пробуем преобразовать в дробное число
    try:
        num = float(element)
        processed_list.append(num)
        continue
    except ValueError:
        # Если не число, оставляем как строку
        processed_list.append(element)

print(f"\nПолучен список: {processed_list}")

# Реализация функции custom_any
def custom_any(lst):
    
    for item in lst:
        # Проверяем, является ли элемент числом и положительным
        if isinstance(item, (int, float)) and item > 0:
            return True
    return False

print(f"\n1. Проверка на наличие положительных чисел (custom_any):")
result = custom_any(processed_list)
print(f"   Список содержит хотя бы одно положительное число: {result}")

# Проверка с помощью встроенной функции all
print(f"\n2. Проверка, что все элементы - числа (встроенная функция all):")

# Создаем список булевых значений: True для чисел, False для других типов
are_numbers = [isinstance(item, (int, float)) for item in processed_list]
print(f"   Результат проверки каждого элемента: {are_numbers}")

# Используем встроенную функцию all
result_all = all(are_numbers)
print(f"   Все элементы списка являются числами: {result_all}")

# Сортировка с помощью встроенной функции sorted
print(f"\n3. Отсортированный список:")

# Создаем отдельные списки для чисел и не-чисел
numbers = []
non_numbers = []

# Разделяем элементы по типам
for item in processed_list:
    if isinstance(item, (int, float)):
        numbers.append(item)
    else:
        non_numbers.append(item)

# Сортируем числа
sorted_numbers = sorted(numbers)

# Сортируем не-числа (строки) лексикографически
sorted_non_numbers = sorted(non_numbers)

# Объединяем отсортированные части
sorted_list = sorted_numbers + sorted_non_numbers

print(f"   Исходный список: {processed_list}")
print(f"   Отсортированный список: {sorted_list}")

# Дополнительно: демонстрация работы функций на примерах
print("\n" + "="*50)
print("Примеры работы функций:")

# Пример для custom_any
test_list1 = [-2, -5, 0, -1]
print(f"\nТест custom_any для {test_list1}: {custom_any(test_list1)}")

test_list2 = [-2, -5, 3, -1]
print(f"Тест custom_any для {test_list2}: {custom_any(test_list2)}")

# Пример для all
test_list3 = [1, 2, 3.5, 4]
print(f"\nТест all для {test_list3}: {all(isinstance(x, (int, float)) for x in test_list3)}")

test_list4 = [1, 2, "text", 4]
print(f"Тест all для {test_list4}: {all(isinstance(x, (int, float)) for x in test_list4)}")



