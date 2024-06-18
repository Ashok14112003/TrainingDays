'''
You are given an array A of size N. In one operation you can select any two elements
from it, add their absolute difference in your score.
Your task is to find and return an integer value, representing the maximum score.
Note:
Assume 1 based indexing
The elements on which operation has been performed cannot be selected again.
Input Specification:
Input1: An integer value N, representing the size of array A
input2: An integer array A
Output Specification:
Return an integer value, representing the maximum score
Sample Input:
4
1 2 3 4
Sample Output:
4
'''

import random
a=int(input())
arr=list(map(int,input().split()))
sum=0
dif=0
count=0
for i in range(len(arr)):
    count+=1
    ele1=random.choice(arr)
    arr.remove(ele1)
    if count==(len(arr)-3):
        ele2=0
    else:
        ele2=random.choice(arr)
        arr.remove(ele2)
    dif=abs(ele1-ele2)
    sum+=dif
print(sum)

