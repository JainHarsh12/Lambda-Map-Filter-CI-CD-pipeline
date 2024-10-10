# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use map() with a lambda function to square each number
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Use filter() with a lambda function to filter out even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Output the results
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
print("Even numbers:", even_numbers)
