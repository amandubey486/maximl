def substring(s):
	list1=[]
	count=0
	for i in s:
		if i not in list1:  #for removing repeated letters
			list1.append(i)
		else:
			count=max(count,len(list1)) #counting the substring
			list1.clear()
			list1.append(i)
	count=max(count,len(list1))
	return count


inp=input("Enter a string:")

print(substring(inp))
