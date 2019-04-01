

first_string=str(input('single domain: '))
random_domain=[]

n = int(input("Enter number of words in list of domain : "))
for i in range(n):
	random_words=input()
	random_domain.append(random_words.split('.')[0])

sub_first=[]
first_string=first_string.split('.')[0]
for k in range(len(first_string)):
	for i in range(k):
		p=first_string[i:k+1]
		sub_first.append(p)
for ele in first_string:
    sub_first.append(ele)
#print(sub_first)


sorted = sorted(sub_first, key=len, reverse=True)

#print(sorted)

M=[]
P=0
for words in random_domain:

	for ele in sorted:
		if ele in words:
			M.append(100*len(ele)/max((len(first_string), len(words))))
	P=max(M)
	if P>=50 :
		print(words, P)
