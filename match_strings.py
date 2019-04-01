

first_string=str(input('single domain: '))
random_domain=[]

n = int(input("Enter number of words in list of domain : "))
for i in range(n):
	random_words=input()
	random_domain.append(random_words)
for j in random_domain:
	print(j.split('.')[0])

