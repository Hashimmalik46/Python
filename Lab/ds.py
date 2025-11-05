# Lists
my_list = [1,2,3,4]

print(my_list)

print(my_list[2])

print(my_list[1:3])

my_list[3]=6
print(my_list)

my_list.append(2)
print(my_list)

my_list.remove(2)
print(my_list)

my_list.insert(3,5)
print(my_list)

my_list.pop()
print(my_list)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

print(len(my_list))

#Tuples
numbers =(1,2,3,4)

numbers
print(numbers.count(2))
print(numbers.index(2))


#Dictionary
student={
  "name":"Hashim",
  "age":22,
  "course":"CSE"
}
print(student)
print(student.keys())
print(student.values())
print(student.items())

student.pop("age")
print(student)


#Sets
nums = {1,2,3}
print(nums)

nums.add(4)
print(nums)

nums.remove(4)
print(nums)

nums2={1,2,3,4,5}
print(nums.difference(nums2))
print(nums.union(nums2))

print(nums.intersection(nums2))


#Strings
a="Hello"
print(len(a))

b="World!"

print(a+ " " +b)

print(a[0])

print(a[1:3])

print("P" in a)

print(a.upper())
print(a.lower())
