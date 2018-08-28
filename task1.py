# time1=int(input("enter the value of a"))
# time2=int(input("enter the value of b"))
# if(time1>time2):
# 	print("gd morning")


# def andNums(nu1,nu2):
# 	ans=nu1 and nu2
# 	print("and of numbers is"+str(ans))
# 	return ans

# def orNums(nu1,nu2):
# 	ans=nu1 or nu2
# 	print("or of numbers is"+str(ans))
# 	return ans

# def notNums(nu1,nu2):
# 	ans=not(nu1 or nu2)
# 	print("not of numbers is"+str(ans))
# 	return ans
# num=andNums( 10,20)
# logic=orNums( 20,30)
# nor=notNums( 30,20)


# def andNums(nu1,nu2):
# 	ans=nu1 & nu2
# 	print("and of numbers is"+str(ans))
# 	return ans
# num=andNums(10,10)

# def orNums(nu1,nu2):
# 	ans=nu1 | nu2
# 	print("or of numbers is"+str(ans))
# 	return ans
# char=orNums(10,20)

# def xorNums(nu1,nu2):
# 	ans=nu1 ^ nu2
# 	print("xor of numbers is"+str(ans))
# 	return ans
# den=xorNums(30,40)










# emptyset=set()
# print(emptyset)
# print(type(emptyset))


# num1={1,2,3,4,5}
# num1.add(8)
# print(num1)


# set1={1,2,3,5,6,77,}
# set2={2,3,4,5,1,3,2}
# print(set1.symmetric_difference(set2))


# dict1={1:2,2:3}
# dict2={4:5}
# (dict1.update(dict2))
# print(dict1)

# a="10"
# b="digital"
# print(a+b)

# total=0
# a=0
# while(a<101):
# 	print(a)
# 	a+=2
# 	total=total+a
# print(total)	

# total=0
# a=1
# while(a<5):
# 	print(a)
# 	total=total+a
# 	a+=2
# print("total: %d"%(total))	


# print("*"*5+" ")
# print("*"*4+" "*1)
# print("*"*3+" "*2)
# print("*"*2+" "*3)
# print("*"*1+" "*4)

# for i in range()
# a
# print("*"*i+" "*j)


# print(" "*5+"*"*1)
# print(" "*4+"*"*2)
# print(" "*3+"*"*3)
# print(" "*2+"*"*4)
# print(" "*1+"*"*5)

# print(" "*i+"*"*j)

# def meanFunction():
# # 	print(int(input("enter your element")))
# 	print(int(input("enter your element")))



# l4=[]
# for i in range(0,76):
# 	if(i%2==0):
# 	  l4.append(i)	
# print(l4)


# tech ="python"
# tech=tech[6:0:-1]
# print(tech)


# tech="pythonbestforbeginners" 
# tech=tech[1::2]
# print(tech)


# mulNums=lambda a,b:a*b
# print(mulNums(12,3))

# a="revathi"
# a=a[::-1]
# print(a)

# a=""
# def revFun():
# 	a=input("enter the string")
# 	a=a[::-1]
# 	print(a)
# revFun()


# def funName(l4):
# 	for i in range(0,len(l4)):
# 		if(i%2==0):
# 			print(i)
# funName([1,2,3,4,5,6,7,8,9,10])

# def funName():
# 	square={i:i**2 for i in range(5)}
# 	print(square)
# funName()


# l1=[12,24,88,24,120,155,88,120,155]
# l2=[]
# for i in range(len(l1)):
# 	if(i not in l1):
# 		l2.append(l1[i])
# print(l2)	

# adding item to dict
# # dict={1:1,2:3,4:6}
# dict[7]=8
# print(dict)

# dict1={1:2}
# dict2={8:2}
# dict1.update(dict2)
# print(dict1)

# squares of values in dict
# d={i:i**2 for i in range(1,5)}
# print(d)

# remove key
# dict={1:2,3:4}
# dict.pop(3)
# print(dict)

#adding of two lists
# l3=[]
# l1=[1,2,3]
# l2=[3,7,6]
# for i in range(len(l1)):
# 	l3.append(l1[i]+l2[i])

# 	print(l3)

# sumAll=lambda l:sum(l)
# print(sumAll((1,2,3,4)))

# l1=[1,2,3,4,5]
# l1.remove(5)
# print(l1)

# l=[]
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for i in a:
# 	if(i%2==0):
# 		l.append(i)
		
# print(l)	


# l1=[1,3,4,5,7,9]
# l1.sort(reverse=True)
# print(l1[1])

# l3=[]
# l1=[1,2,3]
# l2=[2,3,4]
# for i in range(len(l1)):
# 	c=l1[i]+l2[i]
# 	l3.append(c)
# print(l3)


# l3=0
# l1=[1,2,3,4]
# for i in range(len(l1)):
# 	l3=l3+l1[i]
# print(l3)

# l1=[1,2,3]
# l2=[2,4,5]
# def resName():
# 	res=(lambda l1,l2:l1+l2)
	
# 	return(res)
# a=resName()	

# l3=[]
# a=[1,2,34]
# b=[3,2,1]
# for i in range(len(a)):
# 	c=a[i]+b[i]
# 	l3.append(c)
# print(l3)

# l1=[1,2,34]
# l2=[3,2,1]
# print(list(filter(lambda a,b:a+b,l1,l2)))


















from task2 import revathi
revathi(10,20)

