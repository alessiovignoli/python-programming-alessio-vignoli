# miscellaneous.py
# For the following exercises, pseudo-code is not required

# Exercise 1
# Create a list L of numbers from 21 to 39
# print the numbers of the list that are even
# print the numbers of the list that are multiples of 3

l = []
for i in range(21, 40):
    l.append(i)

print(l[1::2])

print(l[0::3])

# Exercise 2
# Print the last two elements of L 

print(l[len(l)-2:len(l)])

# Exercise 3
# What's wrong with the following piece of code? Fix it and 
# modify the code in order to have it work AND to have "<i> is in the list" 
# printed at least once

L = ['1', '2', '3']
for i in range(1, 10):
    s = '%d' %(i)
    if s == L[0]:
        print('i is in the list')
    else:
        print('i not found')    


# Exercise 4
# Read the first line from the sprot_prot.fasta file
# Split the line using 'OS=' as delimiter and print the second element
# of the resulting list 

exercise_file = open('sprot_prot.fasta', 'r')
List_of_all_lines = exercise_file.readlines()
first_line = List_of_all_lines[0]
exercise4_list = first_line.split('OS=')
print(exercise4_list[1])

# Exercise 5
# Split the second element of the list of Exercise 4 using blanks
# as separators, concatenate the first and the second elements and print
# the resulting string

exercise5_line = exercise4_list[1]
exercise5_list = exercise5_line.split(' ')
merged = exercise5_list[0] + exercise5_list[1]
print(merged)

# Exercise 6
# reverse the string 'asor rosa'

s = 'asor rosa'
print(s[::-1])

# Exercise 7
# Sort the following list: L = [1, 7, 3, 9]

to_be_sorted = [1, 7, 3, 9]
to_be_sorted.sort()
print(to_be_sorted)

# Exercise 8
# Create a new sorted list from L = [1, 7, 3, 9] without modifying L

exercise_8 = [1, 7, 3, 9]
m = sorted(exercise_8)
print(m)

# Exercise 9
# Write to a file the following 2 x 2 table:
# 2 4
# 3 6

output_file = open('exam_test1.txt', 'w')
refer_list = [2, 3]
for i in refer_list:
    column2 = i*2
    row = '%d %d\n' %(i, column2)
    output_file.write(row)
