#Question: Let us suppose that a person is given two numbers 'A' and 'B' as two arrays of 'N' and 'M' length respectively. 
#All the array elements individually represent a digit, How will the person find the sum of two numbers and How can the sum be return in the form an array.

#solution:

a=[8,1,4,5,2]
b=[1,4,6,7,9]
n = len(a)
m = len(b)
arr = []
for i in range(n):
    arr.append(a[i]+b[i])
print(arr)
