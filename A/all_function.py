def factorial(n):
	result=1
	for i in range(n):
		result=result*i
	return result

n=int(input("Enter Number: "))
result=factorial(n)
print(result)

#===============================================
#combination
def factorial(n):
	result=1
	for i in range(2,n+1):
		result=result*i

	return result

def combination(n,r):
	result=factorial(n)//(factorial(r)*factorial(n-r))
	return result


n=int(input('enter first number: '))
r=int(input('enter second number: '))
result=combination(n,r)
print(result)
#===============================================
#pascal tringal 
def factorial(n):
	result=1
	for i in range(2,n+1):
		result=result*i

	return result

def combination(n,r):
	result=factorial(n)//(factorial(r)*factorial(n-r))
	return result

def pattern(n):
	for i in range(1,n+1):
		print(" "*(n-i),end=' ')
		for j in range(1,i+1):
			comb=combination(i-1,j-1)
			print(comb,end=' ')
		print()

n=int(input("enter no of rows: "))
pattern(n)
#=================================================================
#logic 1
def rev(arr1):
	# arr2=[0]*5
	arr2=[]
	for ele in arr1[::-1]:   # t.c= o(n)
		arr2.append(ele)
		# print(arr2)
	for i in range (0,len(arr1)):
		arr[i]=arr2[i]

arr=[4,2,7,8,5]
print(arr)
rev(arr)
print(arr)


#logic 2  # swapping to reverse print element 
def rev1(arr1):
	i=0
	j=len(arr1)-1

	while j>i:
		c=arr[i]			#t.c= O(n)
		arr[i]=arr[j]
		arr[j]=c
		i=i+1
		j=j-1


arr=[4,2,7,8,5]
print(arr)
rev1(arr)
print(arr)
#===========================================================================
#swapping to reverse print element 
def rev1(arr1):
	i=0
	j=len(arr1)-1

	while j>i:
		c=arr[i]           #t.c= O(n)
		arr[i]=arr[j]
		arr[j]=c
		i=i+j
		j=j-1


arr=[4,2,7,8,5]
print(arr)
rev1(arr)
print(arr)
#================================================
def power(a,b):
	result=1
	for i in range (1,b+1):
		result=result*a

	return result    				#t.c = O(n)

a=int(input('enter first number: '))
b=int(input('enter second number: '))
result=power(a,b)
print(result)

#=================================================================================
def sum_of_digit(n):
	sum=0
	while n>0:
		ld=n%10            		#t.c =O(n)
		n=n//10
		sum=sum+ld
	return sum

n=int(input('enter number: '))
result=sum_of_digit(n)
print(result)
#==========================================================================
def no_of_digits(n):
	count=0
	while n>0:
		count=count+1	# t.c= O(n)
		n=n//10

	return count

n=int(input('enter number: '))
result=no_of_digits(n)
print(result)

#===========================================================================\
# peak_element and return only one output
def peak_element(arr):
	l=len(arr)						#t.c = O(n)
	for i in range(1,l-1):
		if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
			return arr[i]

	return -1


arr=[4,7,8,9,6,14] #// 9
arr=[4,7,8,9,11,14] #// -1
result=peak_element(arr)
print(result)
#===================================================================================
# peak_element and return more than ouput  ya all return  
def peak_element(arr):
	l=len(arr)
	l1=[]						#t.c = O(n)
	for i in range(1,l-1):
		if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
			l1.append(arr[i])
			return l1

	return -1


arr=[4,7,8,9,6,8,5,14]

result=peak_element(arr)
print(result)

#===========================================================================
def extra_element(A,B):
	for i in range(0,len(A)):
		if A[i]!=B[i]:
			return i

	return -1				# t.c =O(n) where n= element prsent inside first logic arrary


# A=[2,4,6,8,9,10,12]
# B=[2,4,6,8,10,12]
# A=[3,5,7,9,11,13]
# B=[3,5,7,11,13]
A=[3,5,7,9,11,13]
B=[3,5,7,9,11,13]
result=extra_element(A,B)
print(result)




#====================================================================
def extra_element(A,B):
	for i in range(0,len(A)):
		if i>len(B)-1 or A[i]!=B[i]:
			return i

	return -1
							#t.c=O(n)

A=[3,5,7,9]
B=[3,5,7]
result=extra_element(A,B)
print(result)
#==================================================
def number_formation(arr):
	temp=1
	sum=0
	for ele in arr[: : -1]:
		sum=sum+ele*temp			#t.c=O(n)
		temp=temp*10

	return sum+1

arr=[1,2,4]
result=number_formation(arr)
print(result)
#=====================================================
#left side sum print
def left_sum_print(arr):
	sum=0
	for ele in arr:			#t.c= O(n)
		print(sum)
		sum=sum+ele

arr=[5,3,4,7,9]
left_sum_print(arr)
#=============================================================
#logic 1
def right_sum_print(arr):
	n=len(arr)					#t.c= O(n^2)
	for i in range(0,n):
		sum=0
		for j in range(i+1,n):
			sum=sum+arr[j]
		print(sum)

arr=[5,3,4,7,9]
right_sum_print(arr)


#logic 2
def right_sum_print(arr):
	sum=0
	for ele in arr:
		sum=sum+ele      #time complixity =O(n)
	for ele in arr:
		sum=sum-ele
		print(sum)

arr=[5,3,4,7,9]
right_sum_print(arr)

#========================================================
def replace_right_left(arr):
	sum=0
	n=len(arr)
	for ele in arr:  #element nekala yha se 
		sum=sum+ele
	ls=0
	for i in range(n):   #index use keya yha 
		rs=sum-arr[i]
		temp=arr[i]
		arr[i]=rs-ls
		ls=ls+temp
		sum=sum-temp


arr=[4,5,2,3,7]
print(arr)
# arr=[4,5,2,3,7]
# print(arr)
replace_right_left(arr)
print(arr)
#=================================================================
def left_sum(arr):
	n=len(arr)
	print(-1)
	min=arr[0]
	for i in range(1,n):  #index use keya # O(n)= oder of n 	
		print(min)
		if arr[i]<min:
			min=arr[i]

arr=[4,3,6,2,7,5]
left_sum(arr)

#=====================================================================
def right_min(arr):
	n=len(arr)			#doubt h 
	for i in range(n-1):
		min=arr[i+1]
		for j in range(i+1,n):
			if arr[j]<min:
				min=arr[i]
	print(min)
	print(-1)


arr=[4,3,6,2,7,5]
right_min(arr)
#=========================================================
def left_right_equal(arr):   # equal sum
	sum=0
	for ele in arr:		# O(n)=time complixity 
		sum=sum+ele
		ls=0
	for ele in arr:
		rs=sum-ele
		if ls==rs:
			return ele 

		ls=ls+ele
		sum=sum-ele

	return -1


arr=[4,5,1,7,8,2]
result=left_right_equal(arr)
print(result)

#=================================================================
# replace every element of the arrary by the product of all other elements
def replaceProduct(arr):
	product=1
	for ele in arr:
		product=product*ele
	for i in range(0,len(arr)):		# time complixity = O(n)
		arr[i]=product//arr[i]



arr=[2,3,3,5,7]
print(arr)
replaceProduct(arr)
print(arr)
#========================================================================
#find the positive sum-negative sum which element & comes right side of every indiviual element of given arrary 

#logic 1

def pos_neg(arr):
	n=len(arr)
	for i in range(0,n):
		pos_sum=0
		neg_sum=0
		for j in range(i+1,n):				#time comlixity = O(n^2)
			if arr[j]>0:
				pos_sum=pos_sum+arr[j]

			else:
				neg_sum=neg_sum+arr[j]

		print(pos_sum+neg_sum)

arr=[4,-3,-2,8,-1,6]
pos_neg(arr)
print()


#logic 2
def pos_neg(arr):
	pos_sum=0
	neg_sum=0
	for ele in arr:
		if ele >0:					#time comlixity = O(n)
			pos_sum=pos_sum+ele
		else:
			neg_sum=neg_sum+ele

	for ele in arr:
		if ele>0:
			pos_sum=pos_sum-ele

		else:
			neg_sum=neg_sum-ele

		print(pos_sum+neg_sum)



arr=[4,-3,-2,8,-1,6]
pos_neg(arr)
#====================================================================================================================
#given number is integer and find its reverse number without use any function and don't uconvert string like that 
def reverse_num(n):
	result=0
	while n>0:
		result=result*10+(n%10)			#time comlixity = O(n)
		n = n//10
	return result




n=int(input('enter number: '))
result=reverse_num(n)
print(result)
#======================================================================================
#Write a program to find area of the circle using Python

# π = 3.14  
# Radius = float (input ("Please enter the radius of the given circle: "))  
# area_of_the_circle = π * Radius * Radius  
# print (" The area of the given circle is: ", area_of_the_circle) 


#logic 2
def area_circle(r):
	return(3.14*(r*r))
r=float(input('enter radius: '))
result=area_circle(r)
print(result)
#=================================================================
#Write a program in Python to find out Simple Interest

# def simpleInterest(P, N, R):
#     SI = (P * N * R)/100
#     return SI
  
 
# P = float(input("Enter the principal amount : "))

# N = float(input("Enter the number of years : "))

# R = float(input("Enter the rate of interest : "))

# #calculate simple interest by using this formula
# SI = simpleInterest(P, N, R)

# #print
# print("Simple interest : {}".format(SI))


#logic 2
def simple_interest(p,r,t):
	return((p*r*t)//100)

p=float(input("enter principal ammount: "))
r=float(input("enter the rate of interest: "))
t=float(input("enter the time period: "))
result=simple_interest(p,r,t)
print(result)
#==========================================================================
#Write a program in Python to find the largest element in an array.
l=list(input('enter number'))
l.sort()
print(l[len(l)-1])
#==========================================================================
def left_sum_even(arr):
	n=len(arr)
	sum=0
	for i in range (0,n):
		#print(sum)
		if i%2==0:
			print(sum)
			sum=sum+arr[i]
		else:
			print(sum)
	



arr=[10,5,15,8,7,17]
print(arr)
#result=left_sum_even(arr)
#print(result)
left_sum_even(arr)
#======================================================================================
def right_sum_even(arr):
	n=len(arr)
	sum=0
	for i in range (0,n):
		if i%2==0:
			sum=sum+arr[i]
	#print(sum)
	for j in range(0,n):
		if j%2==0:
			sum=sum-arr[j]
		print(sum)




arr=[10,5,15,8,7,13]
print(arr)
#result=right_sum_even(arr)
#print(result)
right_sum_even(arr)
#======================================================================
#go fetch  left to right side and check element index if even then left that element and 
#print remaining all element print .

def lefteven_ele_allsum(arr):
	n=len(arr)
	sum=0
	temp=0
	for i in range (0,n):
		if i%2==0:
			sum=sum+arr[i]
	#print(sum)
	for j in range(0,n):
		if j%2==0:
			temp=sum-arr[j]
			print(temp)
		else:
			print(sum)



arr=[10,5,15,8,7,13]
print(arr)
# result=lefteven_ele_allsum(arr)
# print(result)
lefteven_ele_allsum(arr)



#logic 2
import math
def lefteven_ele_allsum(arr):
	n=len(arr)
	sum=0
	temp=0
	for i in range (0,n):
		if i%2==0:
			sum=sum-arr[i]
	#print(sum)
	for j in range(0,n):
		if j%2==0:
			temp=sum+arr[j]
			print(math.floor(math.fabs(temp)))
		else:
			print(math.floor(math.fabs(sum)))
	

arr=[10,5,15,8,7,13]
print(arr)
# result=lefteven_ele_allsum(arr)
# print(result)
lefteven_ele_allsum(arr)
#===========================================================================

