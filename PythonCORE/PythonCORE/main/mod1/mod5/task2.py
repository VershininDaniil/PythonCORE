class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # ссылка на предыдущий узел


class Queue:
    """
    Основной класс для очереди
    """
    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None    # ссылка на конец очереди
    
    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """
        if self.start is None:
            print("Очередь пуста!")
            return None
        
        val = self.start.data  # сохраняем значение первого элемента
        
        if self.start.nref is None:  # если в очереди только один элемент
            self.start = None
            self.end = None
        else:
            self.start = self.start.nref  # перемещаем начало на следующий элемент
            self.start.pref = None  # убираем ссылку на предыдущий элемент
        
        return val
    
    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        new_node = Node(val)  # создаем новый узел
        
        if self.end is None:  # если очередь пуста
            self.start = new_node
            self.end = new_node
        else:
            new_node.pref = self.end  # связываем новый узел с концом очереди
            self.end.nref = new_node  # связываем конец очереди с новым узлом
            self.end = new_node       # новый узел становится концом очереди
    
    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        if n < 0:
            print("Неверная позиция!")
            return
        
        new_node = Node(val)
        
        if n == 0:  # вставка в начало
            if self.start is None:  # если очередь пуста
                self.push(val)
            else:
                new_node.nref = self.start
                self.start.pref = new_node
                self.start = new_node
            return
        
        current = self.start
        count = 0
        
        # Ищем позицию для вставки
        while current is not None and count < n:
            current = current.nref
            count += 1
        
        if current is None:  # если дошли до конца
            self.push(val)   # добавляем в конец
        else:
            # Вставляем между current.pref и current
            new_node.pref = current.pref
            new_node.nref = current
            current.pref.nref = new_node
            current.pref = new_node
    
    def print(self):
        """
        вывод на печать содержимого очереди
        """
        if self.start is None:
            print("Очередь пуста")
            return
        
        print("Содержимое очереди (от начала к концу):")
        current = self.start
        while current is not None:
            print(current.data, end=' ')
            current = current.nref
        print()