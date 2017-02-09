#nabeatu
output = ''
for i in range(1,101):
    if i % 3 == 0 or "3" in str(i):
        output += "aho"
    else:
        output += str(i)
    output += "\n"
print(output)
