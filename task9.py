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