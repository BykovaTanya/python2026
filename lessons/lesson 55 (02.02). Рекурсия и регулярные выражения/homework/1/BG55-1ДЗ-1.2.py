def is_balanced(string):
    bracket_pairs = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for symbol1 in string:
        if symbol1 == "(" or symbol1 == "{" or symbol1 == "[":
            stack.append(symbol1) 
        elif len(stack) <= 0:
            return False
        elif symbol1 == ")" and stack.pop() != "(":
            return False
        elif symbol1 == "]" and stack.pop() != "[":
            return False
        elif symbol1 == "}" and stack.pop() != "{":
            return False
    if len(stack) == 0:
        return True
    return False
print(is_balanced("(hgjhg}"))
