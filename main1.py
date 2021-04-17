# Функция возвращающая верхнее значение стека
def top(a):
    return a[len(a) - 1]

# Приоритет действий
def priority(op: str):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2

# функция описывающая преобразования
def call(arr1, arr2):
    op = top(Stack_o)
    if op == '(':
        return 0
    elif op == ')':
        return 1
    else:
        x_input = top(Stack_n)
        x_output = Stack_n.pop()
        if op == '+':
            y_input = top(Stack_n)
            y_output = Stack_n.pop()
            z = x_input + y_input
            Stack_n.append(z)
            z_output = Stack_o.pop()
        if op == '*':
            y_input = top(Stack_n)
            y_output = Stack_n.pop()
            z = x_input * y_input
            Stack_n.append(z)
            z_output = Stack_o.pop()
        if op == '-':
            y_input = top(Stack_n)
            y_output = Stack_n.pop()
            z = y_input - x_input
            Stack_n.append(z)
            z_output = Stack_o.pop()
        if op == '/':
            y_input = top(Stack_n)
            y_output = Stack_n.pop()
            try:
                z = y_input / x_input
            except ZeroDivisionError:
                print("You can't divide by 0\n")
                raise SystemExit
            else:
                Stack_n.append(z)
                z_output = Stack_o.pop()
        return 2

# преобразование строки в массив
Stack_o = [];
Stack_n = []
input_string = input()
array = [];
glue_line = '';
i = 0
while i < len(input_string):
    if input_string[i] == ' ':
        i += 1
    elif input_string[i] in ('+', '-', '*', '/', '(', ')'):
        array.append(input_string[i])
        i += 1
    elif input_string[i] >= '0' and input_string[i] <= '9':
        while input_string[i] >= '0' and input_string[i] <= '9':
            glue_line += input_string[i]
            i += 1
            if i == len(input_string): break
        array.append(glue_line);
        glue_line = ''
    else:
        print('Error: Unacceptable symbols')
        raise SystemExit

# работа со стеками и порядком действий
for i in array:
    if i >= '0' and i <= '9':
        Stack_n.append(int(i))
        continue
    if i in ('+', '-', '*', '/'):
        if len(Stack_o) == 0:
            priority1 = priority(i)
            Stack_o.append(i)
            continue
        priority2 = priority1
        priority1 = priority(i)
        if priority1 > priority2:
            Stack_o.append(i)
            continue
        else:
            call(Stack_n, Stack_o)
            Stack_o.append(i)
    if i == "(":
        Stack_o.append(i)
        priority1 = 0
    if i == ")":
        call(Stack_n, Stack_o)
        while Stack_o != []:
            p = call(Stack_n, Stack_o)
            if p == 0:
                Stack_o.pop()
                break
        priority1 = 0

# Вывод результата
while len(Stack_n) > 1:
    call(Stack_n, Stack_o)
result = Stack_n.pop()
print(result)
