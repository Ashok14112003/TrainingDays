''' The function accepts two integers n, m as arguments Find the sum of all numbers in range from 1 to m(both inclusive) 
that are not divisible by n. Return difference between sum of integers not divisible by n with sum of numbers divisible by n.

Assumption:
n>0 and m>0
Sum lies between integral range

Example
Input
n:4
m:20
Output
90 '''
count=0
string=input()
arr=["a","e","i","o","u"]
for i in string:
    if i in arr:
        count+=1
print(count)