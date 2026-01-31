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