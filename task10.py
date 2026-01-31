class FibonacciSequence:
    """
    Класс для генерации чисел Фибоначчи.
    Последовательность начинается с 1, 1.
    """
    
    def __init__(self):
        """
        Инициализация класса.
        Здесь можно задать начальные значения.
        """
        print("FibonacciSequence инициализирован")
        print("Последовательность Фибоначчи начинается: 1, 1, 2, 3, 5, 8, 13, 21, ...")
    
    def generate(self, n):
        """
        Генератор первых n чисел Фибоначчи.
        
        Args:
            n: количество чисел для генерации
        
        Yields:
            Числа Фибоначчи по одному
        """
        if n <= 0:
            print("Ошибка: n должно быть положительным числом")
            return
        
        # Первые два числа Фибоначчи
        a, b = 1, 1
        
        print(f"\nГенерация первых {n} чисел Фибоначчи...")
        
        # Генерируем числа
        for i in range(n):
            if i == 0:
                print(f"  Выдано число {i+1}: {a}")
                yield a
            elif i == 1:
                print(f"  Выдано число {i+1}: {b}")
                yield b
            else:
                # Каждое следующее число - сумма двух предыдущих
                a, b = b, a + b
                print(f"  Выдано число {i+1}: {b}")
                yield b
        
        print(f"Генерация завершена. Сгенерировано {n} чисел.")
    
    def generate_without_print(self, n):
        """
        Упрощенная версия генератора без отладочной печати.
        
        Args:
            n: количество чисел для генерации
        
        Yields:
            Числа Фибоначчи по одному
        """
        if n <= 0:
            return
        
        a, b = 1, 1
        
        for i in range(n):
            if i == 0:
                yield a
            elif i == 1:
                yield b
            else:
                a, b = b, a + b
                yield b

def test_fibonacci():
    """
    Тестирование генератора чисел Фибоначчи.
    """
    print("=" * 60)
    print("Тест 1: Базовый тест с небольшим n")
    print("=" * 60)
    
    # Создаем объект класса
    fib = FibonacciSequence()
    
    # Генерируем первые 10 чисел
    print("\n1. Используем цикл for для генерации 10 чисел:")
    numbers = []
    for num in fib.generate(10):
        numbers.append(num)
    
    print(f"   Результат: {numbers}")
    
    print("\n" + "=" * 60)
    print("Тест 2: Проверка с помощью next()")
    print("=" * 60)
    
    # Создаем новый генератор
    print("\n2. Используем next() для пошаговой генерации:")
    fib_gen = fib.generate(5)
    
    try:
        print(f"   Шаг 1: next() -> {next(fib_gen)}")
        print(f"   Шаг 2: next() -> {next(fib_gen)}")
        print(f"   Шаг 3: next() -> {next(fib_gen)}")
        print(f"   Шаг 4: next() -> {next(fib_gen)}")
        print(f"   Шаг 5: next() -> {next(fib_gen)}")
        
        # Попытка получить еще одно число
        print("   Шаг 6: Попытка получить следующее число...")
        print(f"   Результат: {next(fib_gen)}")
    except StopIteration:
        print("   Генератор завершил работу (StopIteration)")
    
    print("\n" + "=" * 60)
    print("Тест 3: Генерация большого количества чисел")
    print("=" * 60)
    
    print("\n3. Генерация 20 чисел Фибоначчи:")
    # Используем версию без печати для чистого вывода
    fib_gen_20 = fib.generate_without_print(20)
    result = [num for num in fib_gen_20]
    
    # Выводим в красивом формате
    print("   Полученная последовательность:")
    for i, num in enumerate(result, 1):
        print(f"    {i:2}: {num:7}")
    
    print("\n" + "=" * 60)
    print("Тест 4: Проверка на больших n (демонстрация экономии памяти)")
    print("=" * 60)
    
    # Демонстрация, что мы можем генерировать очень большие последовательности
    # без хранения всех чисел в памяти
    print("\n4. Генерация первых 5, 10, 20 и 30 чисел:")
    
    for count in [5, 10, 20, 30]:
        print(f"\n   Генерация {count} чисел:")
        fib_gen = fib.generate_without_print(count)
        
        # Мы можем обрабатывать числа по одному, не храня их все в памяти
        total = 0
        for i, num in enumerate(fib_gen, 1):
            total += num
            if i <= 3 or i == count:  # Показываем первые 3 и последнее
                print(f"    Число {i}: {num}")
            elif i == count - 1:
                print(f"    ...")
        
        print(f"    Сумма всех {count} чисел: {total}")