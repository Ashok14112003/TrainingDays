def count_vowels(s):
   l=['a','e','i','o','u']
   u=[]
   for i in s:
        if (i in l):
           f=i
           break
   for i in range(len(s)):
      if(f==s[i]):
          u.append(i)
   print(u[1])
s="happy father day"
count_vowels(s)
           
           
        


