class Stack:
    def __init__(self):
        self.list_of_elements = []

    def is_empty(self):
        if len(self.list_of_elements):
            return False
        else:
            return True

    def push(self, new_element):
        self.list_of_elements.append(new_element)

    def pop(self):
        return self.list_of_elements.pop(-1)

    def peek(self):
        return self.list_of_elements[-1]

    def size(self):
        return len(self.list_of_elements)


hooks_dict = {
    ")": "(",
    "]": "[",
    "}": "{"
}


def test_string(hooks_string):
    my_stack = Stack()

    for i in iter(hooks_string):

        if not my_stack.is_empty():
            last_element = my_stack.peek()
        elif i in hooks_dict.keys():
            return "Несбалансированно"
        else:
            my_stack.push(i)
            continue

        if i in hooks_dict.keys():
            if hooks_dict[i] != last_element:
                return "Несбалансированно"
            else:
                my_stack.pop()
                continue
        else:
            my_stack.push(i)

    if my_stack.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"


if __name__ == "__main__":
    my_strings = [
        "(((([{}]))))",
        "[([])((([[[]]])))]{()}",
        "{{[()]}}",
        "}{}",
        "{{[(])]}}",
        "[[{())}]",
        "()]",
        "((("
    ]

    for string in my_strings:
        print(test_string(string))
