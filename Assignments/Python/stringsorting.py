count=dict()
line=raw_input(" ")
words = line.split()
print(words,"\n")
for word in words:
	count[word]=count.get(word,0)+1
print(count,"\n")
lis=list()
strlis=list()
for k,v in count.items():
	x=(v,k)
	lis.append(x)
lis=sorted(lis,reverse=True)
for v ,k in lis:
	x=(k,v)
	strlis.append(x)
print(strlis[:10])


