# Exercise 1

for i in range(11):
    print(i**3)

# Exercise 2

for i in range(1,100,2):
    print(i)

# Exercise 3

age = int(input("How old are you? ")) 

if age > 65:
    category = "Senior"
elif age > 18:
    category = "Grown up"
elif age < 18:
    category = "Child"
    
print(f" You are a {category}")

