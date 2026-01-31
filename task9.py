import random
from string import ascii_lowercase, ascii_uppercase

# Функция-генератор для создания бесконечного количества паролей
def password_generator(length=12):
    """
    Генератор случайных паролей.
    
    Args:
        length: длина пароля (по умолчанию 12)
    
    Yields:
        Случайно сгенерированный пароль заданной длины
    """
    # Формируем строку допустимых символов
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    
    print(f"Допустимые символы для пароля ({len(chars)} символов):")
    print(f"  строчные буквы: {ascii_lowercase}")
    print(f"  заглавные буквы: {ascii_uppercase}")
    print(f"  цифры: 0123456789")
    print(f"  спецсимволы: !?@#$*")
    print(f"  всего символов: {len(chars)}")
    print(f"Длина пароля: {length}")
    print("-" * 50)
    
    # Бесконечный цикл генерации паролей
    while True:
        # Создаем пароль: выбираем случайные символы из chars
        password = ''.join(random.choice(chars) for _ in range(length))
        
        # Возвращаем пароль через yield
        yield password

# Дополнительная функция для проверки качества паролей
def check_password_strength(password):
    """
    Проверяет надежность пароля.
    
    Args:
        password: пароль для проверки
    
    Returns:
        Строка с оценкой надежности
    """
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!?@#$*" for c in password)
    
    # Считаем количество выполненных критериев
    criteria_count = sum([has_lower, has_upper, has_digit, has_special])
    
    if criteria_count == 4:
        return "очень надежный"
    elif criteria_count == 3:
        return "надежный"
    elif criteria_count == 2:
        return "средней надежности"
    else:
        return "ненадежный"

# Основная часть программы
def main():
    print("Задача 3: Генератор случайных паролей")
    print("=" * 60)
    
    # Создаем генератор паролей
    N = 12  # длина пароля
    gen = password_generator(N)
    
    # Получаем и выводим первые 5 паролей
    print("\nПервые 5 сгенерированных паролей:")
    print("-" * 60)
    
    passwords = []
    for i in range(5):
        password = next(gen)
        passwords.append(password)
        
        # Проверяем надежность пароля
        strength = check_password_strength(password)
        
        # Выводим пароль с номером и оценкой надежности
        print(f"Пароль {i+1}: {password}  [надежность: {strength}]")
    
    print("-" * 60)
    
    # Демонстрация работы генератора
    print("\nДемонстрация бесконечной работы генератора:")
    print("(следующие 5 паролей из того же генератора)")
    print("-" * 60)
    
    for i in range(5, 10):
        password = next(gen)
        strength = check_password_strength(password)
        print(f"Пароль {i+1}: {password}  [надежность: {strength}]")
    
    print("-" * 60)
    
    # Покажем статистику использования символов
    print("\nСтатистика использования символов в первых 5 паролях:")
    print("-" * 60)
    
    # Объединяем все пароли для анализа
    all_passwords = ''.join(passwords)
    
    # Считаем статистику
    total_chars = len(all_passwords)
    lowercase_count = sum(1 for c in all_passwords if c.islower())
    uppercase_count = sum(1 for c in all_passwords if c.isupper())
    digit_count = sum(1 for c in all_passwords if c.isdigit())
    special_count = sum(1 for c in all_passwords if c in "!?@#$*")
    
    print(f"Всего символов: {total_chars}")
    print(f"  строчные буквы: {lowercase_count} ({lowercase_count/total_chars*100:.1f}%)")
    print(f"  заглавные буквы: {uppercase_count} ({uppercase_count/total_chars*100:.1f}%)")
    print(f"  цифры: {digit_count} ({digit_count/total_chars*100:.1f}%)")
    print(f"  спецсимволы: {special_count} ({special_count/total_chars*100:.1f}%)")
    
    print("\n" + "=" * 60)
    print("Примеры использования генератора в разных сценариях:")
    print("=" * 60)
    
    # Пример 1: Генерация пароля для пользователя
    print("\nПример 1: Генерация одного пароля для пользователя")
    user_password = next(password_generator(8))
    print(f"  Пароль для нового пользователя: {user_password}")
    print(f"  Надежность: {check_password_strength(user_password)}")
    
    # Пример 2: Создание нескольких паролей
    print("\nПример 2: Создание 3 паролей разной длины")
    for length in [6, 10, 14]:
        temp_gen = password_generator(length)
        pwd = next(temp_gen)
        print(f"  Длина {length}: {pwd}")
    
    # Пример 3: Генератор с ограничением по количеству паролей
    print("\nПример 3: Функция для генерации N паролей")
    
    def generate_n_passwords(n, length=12):
        """Генерирует указанное количество паролей."""
        gen = password_generator(length)
        return [next(gen) for _ in range(n)]
    
    # Генерируем 3 пароля
    three_passwords = generate_n_passwords(3, 10)
    print(f"  3 пароля длиной 10 символов:")
    for i, pwd in enumerate(three_passwords, 1):
        print(f"    {i}. {pwd}")