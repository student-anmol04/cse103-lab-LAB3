# a = str(input("Enter a word:"))
# if a == a[::-1]:
#     print("The word is palindrome.")
# else:
#     print("The word is not a palindrome.")

# a = 'hello,world'
# print(a.split(","))
# print(len(a))

# a = 'hello'
# b = 'world'
# c =a+b
# print(c)

# age = 18
# name = "anmol"
# id = f"My name is {name}, My age is {age}"
# print(id)

# n = 0
# while n<=5:
#     n+=1
#     if n == 3:
#         continue
#     print(n)

# n = 1
# while n<=5:
#     if n==3:
#         break
#     n+=1
#     print(n)

# i = 1
# while i<=5:
#     print(i)
#     i+=1

# str = input("Enter the word")
# i = 0
# count = 0
# while i<len(str):
#     if str[i] in 'AEIOUaeiou':
#        count+=1
#     i+=1
# print("No. of vowels:",count)

num = int(input("Enter the value of n:"))
sum = 0
for i in range(1,num+1):
    sum+=1
    print("Sum of n digits:",sum)