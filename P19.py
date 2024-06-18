'''Angela has decided to throw a pizza party. she has ordered N number of pizzas to be
served to her N number of friends. In this way, she will be serving only one pizza to
each friend.
She now wants to invite fewer people to her party in order to provide more pizzas per
person. But at the same time, she wants to ensure that there are at least Y friends at
her party.
Your task is to help Angela find and return an integer value, representing the sum of
digits of the minimum number of friends that she can invite to the party, ensuring
that each person gets an equal number of pizzas
Sample Input:
100 17
Sample Output:2'''

def pizza(n,mini):
    eqi=0
    s=0
    for i in range(mini,n+1):
        if n%i==0:
            eqi=i
            break
    for i in str(eqi):
        s+=int(i)
    return s
    
n=int(input())
mini=int(input())
print(pizza(n,mini))
