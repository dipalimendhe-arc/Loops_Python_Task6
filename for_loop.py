# 1. for loop to return only old employees from the list and break after an entry of new employees

Employees = ['Jack', 'Max', 'John', 'Tina', 'David', 'Katty', 'Megha', 'Tony']

for e in Employees:
	if e == 'Katty':
	    break
	
	print(f'Old Employee: {e}')
	
	
# 2. Loop to find a multiple of 5 with function

def multiple_of_5():
     
    for num in numbers:    
        if num % 5 == 0:        
            print(f"Multiple of 5 : {num}")       

        else:    
            print("Not a multiples of 5 : ", num)
            

numbers = [100, 121, 75, 249, 30, 64, 35, 65, 89, 105, 67, 53, 45, 64, 22, 38, 98]
multiple_of_5()

# 3. Find a table of given number

n = 2
print(f'Table of {n}')
for i in range(1, 11):
    
    product = n * i
    print(f'{n} x {i} = {product}')

# 4. Calculate the cube of all numbers in the list

def cube_function():

    for i in num:

        if i>0:
            print("Current Number is :", i, " and the cube is", (i*i*i))
        else:
            return None

num = [2,3,5,6,7,8,9]

cube_function()

# 5. Display the determined season based on the provided month and day

def get_season(month):
    if month == "December" or month == "January" or month == "February":
        return "Winter"
    elif month == "March" or month == "April" or month == "May":
        return "Spring"
    elif month == "June" or month == "July" or month == "August":
        return "Summer"
    elif month == "September" or month == "October" or month == "November":
        return "Autumn"
    else:
        return "Invalid month"

months = ["January", "April", "July", "October", "December"]

for month in months:
    season = get_season(month)
    print(f"The season in {month} is {season}.")

# 6. Doubling each value in the given dictionary

my_dict = {"a": 1, "b": 2, "c": 3}

for key in my_dict:
    my_dict[key] = my_dict[key]*2

print(my_dict)

# 7. calculate median among the three input numbers

student = {"name": "Alice", "age": 21, "sub": "Computer Science"}

for key in student:
   
   print(key)

# 8. Sum of numbers in the list

nums = (1, 2, 3, 4)
sum = 0

for num in nums:
    sum = sum + num

print(f'Sum of numbers is {sum}')

# 9. Search for a number and return true if found

nums = [1, 2, 3, 4, 5, 6]
n = 2
found = False
for num in nums:
    if n == num:
        found = True
        break

print(f'List contains {n}: {found}')

# 10 Looping through each character in a string

word = "Python"
for char in word:
    print(f"Letter: {char}")

