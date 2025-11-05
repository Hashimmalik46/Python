name = "Hashim"
age = 22
print(f"my name is {name} and my age is {age}.")

# name = input("enter your name")
# print("your name is",name)

# for i in range(5):
#   print("Hashim")

for i in range(1,5):
  print("Hashim")

count = 5
while count<=7:
  print(count)
  count+=1

def add():
  a=2
  b=1
  return a+b

print(add())

def sub(a,b):
  return a-b

print(sub(6,2))


try:
    a = int(input("Enter a number: "))
    result = 10 / a
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Enter only numbers!")
