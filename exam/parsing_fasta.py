# parsing_fasta.py
# For this exercise the pseudo-code is required (in this same file) 
# Write a script that:
# a) Reads sprot_prot.fasta line by line
# b) Copies to a new file ONLY the record(s) that are not from Homo sapiens
# b) And prints their source organism and sequence lenght 
# Use separate functions for the input and the output 


'''
Pseudo-code: -first call a function that reads the input fasta file with command open and the it saves to a variable f each line as a string, f is a list of string, al the strings in the fasta file in input.
             -then call a second function that reads in input the string created from the previous function input_handeler, this function checks for every string in the list if such string starts with '>'.
             -then if the string starts with '>' creates a new variable(find_Homo) that searches for 'Homo' in the string.
             -then with a if cycle if the find_Homo variable is equal to -1, that means that find has not find what it was searching for, it prints the name of the OS and the length of the sequence and writes to a new file called exam_test2.fasta the record that suited the search ( not human).
'''

def input_handeler(F):
    f = F.readlines()
    return f
def output_handeler(don):
    writable = open('exam_test2.fasta', 'w')
    n = 0
    for string in don:
        n += 1
        if string[0] == '>':
            find_Homo = string.find('Homo')
            if find_Homo == -1:
                s2 = don[n]
                split1_list = string.split('OS=')
                split1_string = split1_list[1]
                split2 = split1_string.split(' ')
                merged = split2[0] + ' ' + split2[1]
                record = string + '\n' + s2
                writable.write(record)
                print(len(don[n]))
                print(merged)

exp = input_handeler(open('sprot_prot.fasta', 'r'))
output_handeler(exp)
