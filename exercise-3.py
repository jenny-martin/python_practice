# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

h_age = int(input('Please enter a dog''s age in human years: '))
print(f'User entered {h_age} ')

if h_age < 0:
    print('Age must be a positive number')
    exit()
elif h_age <= 2:
    d_age = int(h_age * 10)
else: h_age >= 3
d_age = 20 + (h_age - 2)*7
print(f'The dog''s age in dog years is', d_age)

