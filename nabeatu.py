#nabeatu
output=''
for i in range(1,101):
	if i%3==0:
		output+="aho"
	elif (i-3)%10==0:
		output+="aho"
	elif 30<=i<=39:
		output+="aho"
	else:
		output+=str(i)
	output+="\n"
print(output)
