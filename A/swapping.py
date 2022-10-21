#swapping to reverse print element 
def rev1(arr1):
	i=0
	j=len(arr1)-1
					# t.c= o(n)
	while j>i:
		c=arr[i]
		arr[i]=arr[j]
		arr[j]=c
		i=i+j
		j=j-1


arr=[4,2,7,8,5]
print(arr)
rev1(arr)
print(arr)
