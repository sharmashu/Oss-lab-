from collections import defaultdict

#python week 2
#question 1
# Initialize a list with 10 names of friends
friends = ["Krishna", "shaurya", "devansh", "vansh", "himanshu", "harsh", "kartikeya", "aditya", "aashu", "aryan"]

# a. Print the first name
print("First name:", friends[0])

# b. Print the last name
print("Last name:", friends[-1])

# c. Use slicing to print the names from the third to the fifth index
print("Names from third to fifth index:", friends[2:5])

# d. Use slicing to print the names in reverse order
print("Names in reverse order:", friends[::-1])

# e. Use slicing to print the names from eighth to third
print("Names from eighth to third:", friends[7:2:-1])


# question 2

# Create a tuple of 5 students
students = ("Krishna", "harsh", "shaurya", "devansh", "vansh")

# a. Display all the students
print("All students:", students)

# b. Add new student (Tuples are immutable, so we create a new tuple)
students = students + ("David",)
print("After adding a new student:", students)

# c. Delete a student (Tuples are immutable, so we create a new tuple without the student)
students = tuple(student for student in students if student != "Bob")
print("After deleting a student:", students)

# d. Use slicing to print students from the first index to third index
print("Students from first to third index:", students[1:4])

# e. Modify the second index value (Tuples are immutable, so direct modification is not possible)
# To modify, we need to convert the tuple to a list, make changes, and convert it back to a tuple
students_list = list(students)
students_list[1] = "Grace"
students = tuple(students_list)
print("After modifying the second index value:", students)

#question 3

# Create a dictionary with key as name and value as age
students_age = {
    "Krishna": 19,
    "Shaurya": 21,
    "Devansh": 22,
    "Vansh": 18,
    "Himanshu": 23
}

# a. Display those students whose age is greater than 20
print("Students with age greater than 20:")
for name, age in students_age.items():
    if age > 20:
        print(name, "-", age)

# b. Add one more student with age 30
students_age["David"] = 30
print("After adding a new student:", students_age)

# c. Display all the students using .items()
print("All students:")
for name, age in students_age.items():
    print(name, "-", age)

# d. Delete a student
del students_age["Vansh"]
print("After deleting a student:", students_age)

# e. Display the average age of all the students
average_age = sum(students_age.values()) / len(students_age)
print("Average age of all students:", average_age)



#question 4
# Function to print all even numbers from a list
def print_even_numbers(numbers):
    print("Even numbers in the list:")
    for num in numbers:
        if num % 2 == 0:
            print(num)

# Example usage
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_even_numbers(numbers_list)


#question 5
# Function to print all duplicate elements in a list
def print_duplicates(numbers):
    print("Duplicate elements in the list:")
    seen = set()
    duplicates = set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    for duplicate in duplicates:
        print(duplicate)

# Example usage
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8]
print_duplicates(numbers_list)


#question 6

# Function to reverse a string
def reverse_string(s):
    return s[::-1]

# Example usage
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print("Original string:", input_string)
print("Reversed string:", reversed_string)



#question 7


# Question 7
# Function to print Fibonacci series till 5th term
def fibonacci_series(n):
    a, b = 0, 1
    print("Fibonacci series till 5th term:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

fibonacci_series(5)

# Question 8
# Replace contents of a file
def replace_file_contents(file_path, new_content):
    with open(file_path, 'w') as file:
        file.write(new_content)

replace_file_contents('example.txt', "Hi, I am currently pursuing my BTech from Jaypee.")

# Question 9
# Print lines of a file in reverse order
def print_file_reverse(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    print("Lines in reverse order:")
    for line in reversed(lines):
        print(line.strip())

print_file_reverse('example.txt')

# Question 10
# Print odd elements from a list using list comprehension
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_elements = [num for num in numbers_list if num % 2 != 0]
print("Odd elements in the list:", odd_elements)

# Question 11
# Count the number of characters in a file
def count_characters_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return len(content)

character_count = count_characters_in_file('example.txt')
print("Number of characters in the file:", character_count)

# Question 12
# Find anagrams in a given list of words
def find_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    return [group for group in anagrams.values() if len(group) > 1]

words_list = ['eat', 'ate', 'tea', 'bat', 'tab', 'cat']
anagram_groups = find_anagrams(words_list)
print("Anagram groups:", anagram_groups)