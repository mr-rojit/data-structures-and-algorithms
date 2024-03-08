paranthesis = "(Hello) There [YOU], }{How are"

stack = []

par_map = {
    ")": "(",
    "}": "{",
    "]": "[",
}

for i in paranthesis:
    if i in "({[":
        stack.append(i)
    if i in ")}]":
        if stack:
            item = stack[-1]
            if item == par_map[i]:
                stack.pop()
        
if stack:
    print('Invalid')
else:
    print('Valid')