# t=int(input())
# for _ in range(t):
#     string=input()
#     ans=""
#     for i in string:
#         ans=i+ans
#     print(int(ans))

# t=int(input())
# for _ in range(t):
#     n=int(input())
#     sm=0
#     while n>0:
#         a=n%10
#         n=n//10
#         sm=sm*+a
#     print(sm)


# t=int(input())
# for _ in range(t):
#     x,y,a,b=(input().split())
#     if a==x:
#         b==y
#         print("yes")
#     elif a==y:
#         b==x
#         print("yes")
#     elif a==b:
#         x==y
#         print("yes")
#     else:
#         print("no")


# l=int(input())
# b=int(input())
# a=l*b
# p=2*(l+b)
# if a>p:
#     print(f"Area\n{a}")
# elif a<p:
#     print(f"Peri\n{p}")
# else:
#     print(f"Eq\n{a}")

# t=int(input())
# for _ in range(t):
#     n=int(input())
#     b=n%10
#     while n>0:
#         a=n%10
#         n=n//10
#         ans=a+b
#     print(ans)

# name= input("Enter your name:")
# char= input("Enter character :")
# a = len(name)
# print(f"The length of your string of your name is : {a}")

# name= input("Enter your name :")
# date = input("Enter the date :")
# print(f"'''Dear {name}\n You are selected!\n {date}'''")


# t = int(input())
# for _ in range(t):
#     a, b = input().split()
#     if int(a) % 2 == 0 and int(b) % 2 == 0:
#         print(int((int(b)-int(a))/2))

#     elif int(a) % 2 == 0 and int(b) % 2 != 0:
#         print(int((int(b)+1-int(a))/2 + 1))

#     elif int(a) % 2 != 0 and int(b) % 2 == 0:
#         print(int((int(b)+1-int(a))/2 + 1))

#     elif int(a) % 2 != 0 and int(b) % 2 != 0:
#         print(int((int(b)-int(a))/2))

# from posixpath import split


# t = int(input())
# for _ in range(t):
#     a,b = int(input()).split
#     print(a*b)

# from turtle import *
# color("red")
# begin_fill()
# pensize(3)
# left(50)
# forward(133)
# circle(50,200)
# right(140)
# circle(50,200)
# forward(140)
# end_fill()

# import turtle 
# bob = turtle.Turtle()
# # bob.forward(100)
# # bob.left(45)
# # bob.forward(100)
# # bob.right(90)
# # bob.forward(100)
# bob.color("cyan","blue")


# bob.begin_fill()

# bob.forward(100)
# bob.left(90)
# bob.forward(100)
# bob.left(90)
# bob.forward(100)
# bob.left(90)
# bob.forward(100)

# bob.penup()
# bob.forward(150)
# bob.pendown()


# bob.forward(100)
# bob.left(90)
# bob.forward(100)
# bob.left(90)
# bob.forward(100)
# bob.left(90)
# bob.forward(100)
# bob.end_fill()






# turtle.done()

# import turtle
# bob = turtle.Turtle()
# bob.color=("red","orange")
# bob.begin_fill()
# for i in range(100):
#     bob.forward(200)
#     bob.left(170)
# bob.end_fill()

# x = int(input())
# if x>=750:
#     print("YES")
# else:
#     print("NO")

# for i in range(int(input())):
#     x,y = map(int,input().split())
#     print((x*y)//100)

# for i in range(int(input())):
#     x = int(input())
#     if x%10==0:
#         print(x//10)
#     elif x%10 != 0 and x%5==0:
#         print(1+((x-5)//10))
#     else:
#         print(-1)

# for i in range(int(input())):
#     n,x = map(int,input().split())
  
# for i in range(int(input())):
#     n,x = map(int,input().split())
#     t1 = (n//3)*2*x
#     t2 = (n%3)*x
#     print(t1+t2)






# for i in range(int(input())):
#     n = input()
#     l1 = []
#     l2=[]
#     l3=[]
#     for i in n:
#         if int(i)%2==0 and int(i)!=0:
#             l1.append(i)
#         elif int(i)%2==1:
#             l2.append(i)
#         elif int(i)==0:
#             l3.append(i)
    
#     if len(l2)==1 and len(l3)>=0 and len(l1)==0:
#         print("NO")
#     elif len(l2)==1 and len(l1)==1:
#         print("NO")
#     else:
#         print("YES")





# def digitsSum(N):
#     l=[]
#     n = str(N)
#     for i in n:
#         l.append(int(i))
#     return sum(l)

# print(digitsSum(56))

# for i in range(int(input())):
#     x,y,d = map(int,input().split())
#     if abs(x-y)<=d:
#         print("YES")
#     else:
#         print("NO")

# for i in range(int(input())):
#     n,x = map(int,input().split())
#     print(2*n+1 - x)

# for i in range(int(input())):
#     s= int(input())
#     s1 = list(map(int,input().split()))
#     d1 = list(map(int,input().split()))
#     count = 0
#     for i in range(s):
#         if s1[i]==d1[i]:
#             count = count + 1
#     print(count)

# for i in range(int(input())):
#     n = int(input())
#     s = input()
#     if abs(s.count("1")-s.count("0"))== 1 or  abs(s.count("1")-s.count("0"))== 0:
#         print(len(s))
#     elif abs(s.count("1")-s.count("0"))>1:
#         a =abs(s.count("1")-s.count("0"))
#         print(len(s)-a+1)




# for i in range(int(input())):
#     n = int(input())
#     if n%2 == 0:
#         print(n//2)
#     else :
#         print(-((n+1)//2))        

# for i in range(int(input())):
#     n = int(input())
#     c = bin(1)
#     l=[]
#     l1=[]
#     for i in range(2,n+1):
#         c = c or bin(i)
#         if i%2!=0:
#             l.append(c)
#         else:
#             l1.append(c)
#     count= 0
#     for i in range(min(len(l),len(l1))):
#         if l[i]==l1[i]:
#             count = count + 1
#     print(count)
       
# x = int(input())
# if x+7>170:
#     print("YES")
# else:
#     print("NO")

# a,b,c,x = map(int,input().split())
# if (a==x) or (b==x) or (c==x):
#     print("YES")
# else:
#     print("NO")

# for i in range(int(input())):
#     x,y,a,b = map(int,input().split())
#     if {x,y} == {a,b}:
#         print(0)
#     elif ((x==a) and (y!=b)) or ((x==b) and (y!=a)) or ((y==a) and (x!=b)) or ((y==b) and (x!=a)):
#         print(1) 
#     else:
#         print(2)




# for i in range(int(input())):
#     s = int(input())
#     y = -1
#     x = s-y
#     print(x*y)

# for i in range(int(input())):
#     n = int(input())
#     a = map(int,input().split())




# from audioop import reverse
    


# def reversestringww(str):
#    str1 = ""
#    a= str.split()
#    a.reverse()
#    for i in range(len(a)):
#       str1 = str1 + a[i]+" "
#    print(str1)

# s= input()
# reversestringww(s)
# str = "i like big butts and i cannot lie"
# a= str.split()
# a.reverse()
# for i in a:
#     print(i)

# print(str.split())
# def binary(num):
#    if(num>=1):
#       binary(num//2)
#       print(num%2, end="")

# (binary(24))

# bstring = "110001"
# x = int(bstring,2)
# print(x)




# a = list(map(int,input().split()))
# for i in range(0,len(a)):
#    print(a[i])




# import sys

# from operator import xor



# def maxScore(N,A):
#    ans= 0
#    if len(set(A))==1:
#        return (A[0])


#    for i in range(N):
#       for j in range(i+1,N):
#          x = xor(A[i],A[j])
#          if x>ans:
#             ans=x
   
#    if A[len(A)-1] >ans:
#       ans = A[len(A)-1]
   
#    return ans

# def main():

#    N = int(sys.stdin.readline().strip())

#    A=[]
#    for _ in range(N):
#       A.append(int(sys.stdin.readline().strip()))

#    result = maxScore(N,A)

#    print(result)



# if __name__ == "__main__":
#    main()




# def checkprime(n):
#    prime = True
#    for i in range(2,n//2):
#       if n%i ==0:
#          prime = False
   
#    return prime

# def calculateSumPrime(inputArray):
#    sum = 0
#    for i in range(len(inputArray)-1):
#       if checkprime(inputArray[i]) == True:
#          sum = sum + inputArray[i]
   
#    return sum



# from typing import List

# from numpy import array

# class Solution:
#     def minarray(self,arr):
#         self.arr = arr
#         min = arr[0]
#         for i in range(0,len(arr)):
#             if (arr[i]<min):
#                 min = arr[i]
    
#         return min
        
        
#     def maxarray(self,arr):
#         self.arr = arr
#         max = arr[0]  
     
    
#         for i in range(len(arr)):    
#             if(arr[i] > max):    
#                 max = arr[i]
        
#         return max
   
   
#     def maximumMultiple(self, N : int, A : List[int]) -> int:
#         B =[]
#         for i in range((N//2)):
         

#             A.remove(maxarray(A))
#             A.remove(minaray(A))
#             B.append(mulp1)
        
#         return maxarray(B)


# a =[1,2,5,0,4]
# if 


a=[0,2,3,4,5]
if len(a)==6 and  0 in a:
   print("yes")
else:
   print("no")
