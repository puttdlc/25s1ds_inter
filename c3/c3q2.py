class stack:
    def __init__(self, values=[]):
        self.stack = values
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None
    def is_empty(self):
        return len(self.stack) == 0
    def get_stack(self):
        return self.stack

opens = "({["
closes = ")}]"
pairs = {')': '(', '}': '{', ']': '['}

def check_expression(expression):
    vars = stack()
    for ch in expression:
        if ch in opens:
            vars.push(ch)
        elif ch in closes:
            if vars.is_empty():
                print(f"{expression} close paren excess")
                return
            top = vars.pop()
            if pairs[ch] != top:
                print(f"{expression} Unmatch open-close")
                return

    if not vars.is_empty():
        leftover = ''.join(vars.get_stack()) # for all remaining in stack
        print(f"{expression} open paren excess   {len(leftover)} : {leftover}")
    else:
        print(f"{expression} MATCH")

expression = input("Enter expresion : ")
check_expression(expression)