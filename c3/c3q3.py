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

inp = input("Enter Infix : ")

precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}

associativity = {
    '+': 'L',
    '-': 'L',
    '*': 'L',
    '/': 'L',
    '^': 'R'
}

output = []
ops = stack()
valid = True

for token in inp:
    if token.isalpha():
        output.append(token)
    elif token in precedence:
        while not ops.is_empty():
            top = ops.get_stack()[-1]
            if top in precedence:
                top_prec = precedence[top]
                curr_prec = precedence[token]
                if top_prec > curr_prec or (top_prec == curr_prec and associativity[token] == 'L'):
                    output.append(ops.pop())
                else:
                    break
            else:
                break
        ops.push(token)
    elif token == '(':
        ops.push(token)
    elif token == ')':
        found_open = False
        while not ops.is_empty():
            top = ops.pop()
            if top == '(':
                found_open = True
                break
            elif top in precedence:
                output.append(top)
            else:
                print(f"{inp} Unmatch open-close")
                valid = False
                break
        if not found_open and valid:
            print(f"{inp} close paren excess")
            valid = False
            break

if valid:
    unmatched_opens = 0
    leftover_opens = ''
    while not ops.is_empty():
        top = ops.pop()
        if top == '(':
            unmatched_opens += 1
            leftover_opens += '('
        else:
            output.append(top)

    if unmatched_opens > 0:
        print(f"{inp} open paren excess   {unmatched_opens} : {leftover_opens}")
    elif valid:
        print("Postfix :", ''.join(output))