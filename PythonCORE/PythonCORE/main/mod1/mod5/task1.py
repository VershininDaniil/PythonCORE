class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел


class Stack:
    """
    Основной класс для стека
    """
    def __init__(self):
        self.end = None  # ссылка на конец стека
    
    def pop(self):
        """
        возвращение последнего элемента из списка с удалением его из списка
        """
        if self.end is None:
            print("Стек пуст!")
            return None
        
        val = self.end.data  # сохраняем значение
        self.end = self.end.pref  # перемещаем указатель на предыдущий элемент
        return val
    
    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        new_node = Node(val)  # создаем новый узел
        
        if self.end is None:
            self.end = new_node  # если стек пуст, новый узел становится концом
        else:
            new_node.pref = self.end  # связываем новый узел с предыдущим
            self.end = new_node  # новый узел становится концом стека
    
    def print(self):
        """
        вывод на печать содержимого стека
        """
        if self.end is None:
            print("Стек пуст")
            return
        
        print("Содержимое стека (сверху вниз):")
        current = self.end
        while current is not None:
            print(current.data)
            current = current.pref