# average_function.py
# For this exercise the pseudo-code is required (in this same file) 
# Write a function that calculates the average of the values of
# any vector of 10 numbers 
# Each single value of the vector should be read from the keyboard
# and added to a list.
# Print the input vector and its average 
# Define separate functions for the input and for calculating the average

'''
pseudo-code: -first define the input from keybord with the input command and save (as string) the input for the vector of reference.
             -then split this input into a list with the command split acted on ' ' blank spaces and sve it to a variable. The blank spaces will be requested from the input command that wil ask for numbers separeted from a space.
             -then start a for cycle that transform every element of the ref_list into numbers with the command float and saves them to a new list (operative_list), on which calculation will be carreid out later. 
             -then define a new definition that carries out the calculation on operetive list (calc). Simply making a for cycle that for each element of operative_list creates a new variable that is the element in operative_list divided by two and than this new variable is inserted in a vector called average with the command append.
             -then this last definition prints operative_list and avereage.
'''
def reference_vector(ref):
    ref_list = ref.split(' ')
    n = -1
    operative_list = []
    for i in ref_list:
        n += 1
        floats_of_i = float(ref_list[n])
        operative_list.append(floats_of_i)
    return operative_list

def average_function(calc):
    average = []
    for f in calc:
        averaged_f = f/2
        average.append(averaged_f)
    print(calc)
    print(average)
exp = reference_vector(input('please insert ten numbers spaced with a blanck space:'))
average_function(exp)

