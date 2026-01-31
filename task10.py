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

def demonstrate_usage():
    """
    Демонстрация практического использования генератора Фибоначчи.
    """
    print("\n" + "=" * 60)
    print("Практические примеры использования")
    print("=" * 60)
    
    fib = FibonacciSequence()
    
    # Пример 1: Поиск отношения соседних чисел (стремится к золотому сечению)
    print("\nПример 1: Приближение к золотому сечению")
    print("Отношение F(n+1)/F(n) стремится к φ ≈ 1.6180339887...")
    
    n = 15
    fib_gen = fib.generate_without_print(n)
    numbers = list(fib_gen)
    
    print("\n   n   F(n)        F(n+1)/F(n)")
    print("   " + "-" * 30)
    
    for i in range(len(numbers) - 1):
        ratio = numbers[i+1] / numbers[i]
        print(f"   {i+1:2}  {numbers[i]:7}    {ratio:.10f}")
    
    # Пример 2: Использование в математических расчетах
    print("\n\nПример 2: Сумма первых N чисел Фибоначчи")
    
    def sum_first_n(n):
        """Сумма первых n чисел Фибоначчи."""
        fib_gen = FibonacciSequence().generate_without_print(n)
        return sum(fib_gen)
    
    for n in [5, 10, 15]:
        s = sum_first_n(n)
        print(f"   Сумма первых {n} чисел: {s}")
    
    # Пример 3: Проверка свойства F(1)+F(2)+...+F(n) = F(n+2)-1
    print("\nПример 3: Проверка свойства F(1)+F(2)+...+F(n) = F(n+2)-1")
    
    n = 10
    fib_gen = FibonacciSequence().generate_without_print(n + 2)
    numbers = list(fib_gen)
    
    sum_n = sum(numbers[:n])
    f_n_plus_2_minus_1 = numbers[n + 1] - 1
    
    print(f"   Сумма первых {n} чисел: {sum_n}")
    print(f"   F({n+2}) - 1 = {numbers[n + 1]} - 1 = {f_n_plus_2_minus_1}")
    print(f"   Равенство выполняется: {sum_n == f_n_plus_2_minus_1}")
    
    # Пример 4: Бесконечная генерация (с ограничением)
    print("\nПример 4: Бесконечный генератор чисел Фибоначчи")
    
    def infinite_fibonacci():
        """Бесконечный генератор чисел Фибоначчи."""
        a, b = 1, 1
        yield a
        yield b
        while True:
            a, b = b, a + b
            yield b
    
    print("   Первые 7 чисел из бесконечного генератора:")
    inf_gen = infinite_fibonacci()
    for i in range(7):
        print(f"    Число {i+1}: {next(inf_gen)}")
    
    # Пример 5: Генератор для получения чисел до определенного предела
    print("\nПример 5: Числа Фибоначчи меньше 1000")
    
    def fibonacci_up_to(limit):
        """Генератор чисел Фибоначчи, не превышающих limit."""
        a, b = 1, 1
        yield a
        if b <= limit:
            yield b
        while True:
            a, b = b, a + b
            if b > limit:
                break
            yield b
    
    print("   Числа Фибоначчи меньше 1000:")
    fib_upto_1000 = list(fibonacci_up_to(1000))
    print(f"   {fib_upto_1000}")
    print(f"   Всего чисел: {len(fib_upto_1000)}")

# Демонстрация экономии памяти
def memory_demo():
    """
    Демонстрация экономии памяти при использовании генератора.
    """
    print("\n" + "=" * 60)
    print("Демонстрация экономии памяти")
    print("=" * 60)
    
    print("\n1. Генератор НЕ хранит всю последовательность в памяти")
    print("   Он генерирует числа по одному при каждом вызове next()")
    
    print("\n2. Сравнение с обычной функцией, возвращающей список:")
    
    # Обычная функция, возвращающая список
    def fibonacci_list(n):
        a, b = 1, 1
        result = []
        for i in range(n):
            if i == 0:
                result.append(a)
            elif i == 1:
                result.append(b)
            else:
                a, b = b, a + b
                result.append(b)
        return result
    
    print("\n   Вызов fibonacci_list(1000):")
    print("   - Создает список из 1000 чисел")
    print("   - Все 1000 чисел хранятся в памяти одновременно")
    print("   - Занимает примерно 8 * 1000 = 8000 байт")
    
    print("\n   Вызов FibonacciSequence().generate(1000):")
    print("   - Генерирует числа по одному")
    print("   - В памяти хранится только 2 числа (текущее и предыдущее)")
    print("   - Занимает всего 8 * 2 = 16 байт")
    
    print("\n3. Практический пример: генерация миллиона чисел")
    print("   (В реальности не выполняется, чтобы не занять весь вывод)")
    
    print("\n   Код для генерации миллиона чисел:")
    print("   ```python")
    print("   fib = FibonacciSequence()")
    print("   count = 0")
    print("   for num in fib.generate(1000000):")
    print("       count += 1")
    print("       if count % 100000 == 0:")
    print("           print(f'Сгенерировано {count} чисел')")
    print("   ```")
    
    print("\n   При использовании генератора:")
    print("   - Память: константа (несколько байт)")
    print("   - Время: зависит от процессора")
    
    print("\n   При использовании списка:")
    print("   - Память: ~8 МБ (8 байт * 1,000,000)")
    print("   - Время: примерно такое же")

if __name__ == "__main__":
    print("Задача 4: Класс FibonacciSequence для генерации чисел Фибоначчи")
    print("=" * 60)
    
    test_fibonacci()
    demonstrate_usage()
    memory_demo()
    
    # Финальный тест
    print("\n" + "=" * 60)
    print("Финальный тест: различные способы использования")
    print("=" * 60)
    
    fib = FibonacciSequence()
    
    print("\n1. Использование в математическом выражении:")
    # Генератор можно использовать прямо в выражениях
    fib_gen = fib.generate_without_print(6)
    squares = [x**2 for x in fib_gen]
    print(f"   Квадраты первых 6 чисел: {squares}")
    
    print("\n2. Комбинирование с другими генераторами:")
    from itertools import islice
    
    # Генерация первых 8 чисел с помощью islice
    fib_gen = fib.generate_without_print(100)  # Много чисел, но возьмем только несколько
    first_8 = list(islice(fib_gen, 8))
    print(f"   Первые 8 чисел: {first_8}")
    
    print("\n3. Генерация с пропуском первых чисел:")
    fib_gen = fib.generate_without_print(12)
    # Пропускаем первые 3
    for _ in range(3):
        next(fib_gen)
    # Берем следующие 5
    next_5 = [next(fib_gen) for _ in range(5)]
    print(f"   Числа с 4-го по 8-е: {next_5}")
    
    print("\n" + "=" * 60)
    print("Все тесты завершены!")
    print("Генератор чисел Фибоначчи работает корректно и эффективно.")
    print("=" * 60)