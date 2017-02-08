stdout=""
for i in range(1,101):
	if i%3 == 0 and i%5 == 0:
		stdout+="FizzBuzz"
	elif i%3 == 0:
		stdout+="Fizz"
	elif i%5 == 0:
		stdout+='Buzz'
	else:
		stdout+=str(i)
	stdout+="\n"
print(stdout)