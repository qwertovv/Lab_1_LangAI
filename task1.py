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

