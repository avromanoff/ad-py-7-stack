# Необходимо реализовать класс Stack со следующими методами:
# isEmpty - проверка стека на пустоту. Метод возвращает True или False.
# push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
# pop - удаляет верхний элемент стека.Стек изменяется. Метод возвращает верхний элемент стека
# peek - возвращает верхний элемент стека, но не удаляет его.Стек не меняется.
# size - возвращает количество элементов в стеке.

# balanced
s1 = '(((([{}]))))'
s2 = '[([])((([[[]]])))]{()}'
s3 = '{{[()]}}'
# unbalanced
u1 = '}{}'
u2 = '{{[(])]}}'
u3 = '[[{())}]'

opening = ['(', '[', '{']
closing = [')', ']', '}']
stack = []


class Stack:

    def __init__(self, stack):
        self.stack = stack

    def isEmpty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)
        return

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_balanced(self, text):
        self.text = text
        for character in text:
            if character in opening:
                Stack.push(self, opening.index(character))
            elif character in closing:
                if not Stack.isEmpty(self) and Stack.peek(self) == closing.index(character):
                    Stack.pop(self)
                else:
                    return 'Несбалансированная'
        return 'Сбалансированная'


mystack = Stack(stack)


if __name__ == '__main__':
    for string in (s1, s2, s3, u1, u2, u3):
        print(mystack.is_balanced(string))
