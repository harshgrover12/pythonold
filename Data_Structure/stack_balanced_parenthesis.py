from Data_Structure.stack import Stack


def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in '([{':   # only left parenthesis will be pushed in stack until present
            s.push(paren)
        else:
            if s.is_empty():  # After pushing in the stack, if no more element
                is_balanced = False
            else:
                top = s.pop()  # top element in the stack will be popped out
                if not is_match(top, paren):  # compared with right parentheis if faced.
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False


# print(is_paren_balanced('()'))  # True
# print(is_paren_balanced('(((({}))))'))  # True
# print(is_paren_balanced('(('))  # False
print(is_paren_balanced(''))  # True

