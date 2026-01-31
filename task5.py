class CyclicListIterator:
    """
    Итератор для циклического обхода списка.
    При достижении конца начинает сначала.
    """
    
    def __init__(self, data):
        """
        Инициализация итератора.
        
        Args:
            data: список для циклического обхода
        """
        if not isinstance(data, list):
            raise TypeError("CyclicListIterator ожидает список в качестве аргумента")
        
        self.data = data  # Сохраняем исходный список
        self.index = 0    # Текущий индекс в списке
        self.length = len(data)  # Длина списка
        
        # Проверяем, не пустой ли список
        if self.length == 0:
            print("Внимание: передан пустой список")
    
    def __iter__(self):
        """
        Возвращает сам объект как итератор.
        """
        return self
    
    def __next__(self):
        """
        Возвращает следующий элемент списка.
        При достижении конца начинает сначала.
        
        Returns:
            Следующий элемент списка
            
        Raises:
            StopIteration: если список пустой
        """
        # Если список пустой, сразу вызываем исключение
        if self.length == 0:
            raise StopIteration("Список пустой, невозможно выполнить итерацию")
        
        # Получаем текущий элемент
        current_element = self.data[self.index]
        
        # Увеличиваем индекс для следующего вызова
        self.index += 1
        
        # Если достигли конца списка, начинаем с начала
        if self.index >= self.length:
            self.index = 0
        
        return current_element
    
    def reset(self):
        """
        Сбрасывает итератор к началу списка.
        """
        self.index = 0
        print("Итератор сброшен к началу")

def test_iterator():
    """
    Тестирование итератора CyclicListIterator.
    """
    print("=" * 50)
    print("Тест 1: Базовый тест с числами")
    print("=" * 50)
    
    # Создаем список чисел
    numbers = [1, 2, 3, 4, 5]
    print(f"Исходный список: {numbers}")
    
    # Создаем итератор
    cyclic_iterator = CyclicListIterator(numbers)
    
    # Проходим 10 элементов (2 полных цикла)
    print("\nПервые 10 элементов (2 цикла по 5 элементов):")
    result = []
    for i, item in enumerate(cyclic_iterator):
        result.append(item)
        if i >= 9:  # Ограничиваем количество итераций
            break
    print(f"Результат: {result}")
    
    print("\n" + "=" * 50)
    print("Тест 2: Работа со строками")
    print("=" * 50)
    
    # Создаем список строк
    words = ["яблоко", "банан", "вишня"]
    print(f"Исходный список: {words}")
    
    # Создаем итератор
    word_iterator = CyclicListIterator(words)
    
    # Проходим 7 элементов
    print("\nПервые 7 элементов (2 полных цикла + 1 элемент):")
    result = []
    for i, item in enumerate(word_iterator):
        result.append(item)
        if i >= 6:
            break
    print(f"Результат: {result}")
    
    print("\n" + "=" * 50)
    print("Тест 3: Тест с reset()")
    print("=" * 50)
    
    # Создаем новый итератор
    colors = ["красный", "зеленый", "синий"]
    color_iterator = CyclicListIterator(colors)
    
    # Получаем первые 2 элемента
    print(f"Исходный список: {colors}")
    print("\nПервые 2 элемента:")
    for i in range(2):
        print(f"  Элемент {i+1}: {next(color_iterator)}")
    
    # Сбрасываем итератор
    color_iterator.reset()
    
    # Снова получаем первые 2 элемента
    print("\nПосле reset(), снова первые 2 элемента:")
    for i in range(2):
        print(f"  Элемент {i+1}: {next(color_iterator)}")
    
    print("\n" + "=" * 50)
    print("Тест 4: Граничные случаи")
    print("=" * 50)
    
    # Тест с пустым списком
    print("\nТест с пустым списком:")
    try:
        empty_iterator = CyclicListIterator([])
        next(empty_iterator)
    except StopIteration as e:
        print(f"  Ошибка (ожидаемо): {e}")
    
    # Тест со списком из одного элемента
    print("\nТест со списком из одного элемента:")
    single_item = ["единственный"]
    single_iterator = CyclicListIterator(single_item)
    print(f"  Исходный список: {single_item}")
    
    # Получаем 3 элемента
    print("  Первые 3 элемента:")
    for i in range(3):
        print(f"    Элемент {i+1}: {next(single_iterator)}")