# fobj=open("C:/Users/LENOVO/Desktop/python/files2.txt","w")
# fobj.write("helo")
# fobj.write("hai")
# fobj.write("hai")
# fobj.write("hey")
# fobj.close()

# lines=["first","second","third"]
# fobj.write("helo\n")
# fobj.write("hai\n")
# fobj.write("hai\n")
# fobj.write("hey\n")
# # fobj.writelines(lines)
# fobj.close()


# with open("C:/Users/LENOVO/Desktop/python/files2.txt","r") as fobj2:
# 	fobj2s.read("helooooohuhhu\n")
	# fobj.write("hai\n")
	# fobj.write("hai\n")
	# fobj.write("hey\n")




import random,sys
# n = 4
# for i in range(4):
# 	print(random.randint(1,9) , end ="")

def genNums(m):
	empList = []
	nums = ""
	for i in range(m):
		nums = nums + str(random.randrange(0,9))
	return nums
res = genNums(9)
# print(res)


def genChars(m):
	chars = ""
	pwd = ""
	l = []
	for i in range(m//2):
		chars=chars+chr(random.randrange(67,90))
		chars = chars + chr(random.randrange(97,122)) 
	for c in chars:
		l.append(c)
		random.shuffle(l)
		pwd = "".join(l)

	return pwd

res = genChars(4)
# print(res)


# user check
# gen pwd 

nDict = {}
def userCheck(name):
	if name in nDict.keys():
		return 0 
	else:
		return 1 

def genPwd(name):
	if userCheck(name)==0:
		print("User already exists")
	elif userCheck(name) == 1:
		password = genChars(4) + genNums(4) + genChars(4) + genNums(4) +genChars(4) + genNums(4)
		nDict[name]  = password
		print(" %s -- %s" %(name , password))
		return password
	else: 
		print("Some issue ")
# userCheck('revathi')
# genPwd(sys.argv[1])
# genPwd('pooja')
# genPwd('revathi')
# genPwd('pooja')

l=len(sys.argv)
for i in range(1,l):
	genPwd(sys.argv[i])


