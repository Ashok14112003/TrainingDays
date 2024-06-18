'''
 Smallest Number
Prince participated in three Olympiads at school and received marks for all of them. 
He is interested in finding out the lowest mark he obtained among the three 
Olympiads. Write a program to find the minimum mark.
Example:
Input: 50 66 23
Output: Smallest number is 23'''

arr=list(map(int,input().split()))
smallest=arr[0]
for i in arr:
    if i < smallest:
        smallest=i
print(smallest)