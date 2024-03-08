# solving using primitive method

s = "Love is evol"

# my list to operate as a stack
stack = []
for i in s:
    stack.append(i)

rev = ""
while stack:
    item = stack.pop()
    rev = rev + item
print(rev)


