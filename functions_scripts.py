# Defining a function to return the complement of the sequence
def complement_base(base):
    output = None
    if base == 'A':
        output = 'T'
    elif base == 'T':
        output = 'A'
    elif base == 'G':
        output = 'C'
    elif base == 'C':
        output = 'G'
    else:
        print('Unknown Output')
    return output

# Defining the sequence of interest and a 'blank' variable to add to
sequence = 'AGTAGCTCGTATC'
complement = ''

# Iterate over each base, get the complement and add it to the complement variable
for base in sequence:
    complement += complement_base(base)
# Print the complement of the sequence
print(complement)

# Defining the sequence of interest and a 'blank' variable to add to
sequence = 'AGTAGCTCGTATC'
reverse = ''

# Iterate over each base, get the reverse and add it to the reverse variable
for base in sequence:
    reverse = base + reverse 
# Print the complement of the sequence
print(reverse)

# Defining the sequence of interest and a 'blank' variable to add to
sequence = 'AGTAGCTCGTATC'
reverse_complement = ''

# Iterate over each base, get the reverse and add it to the reverse variable
for base in sequence:
    reverse_complement = complement_base(base) + reverse_complement
# Print the complement of the sequence
print(reverse_complement)


# Reverse the complement sequence and print it
print(complement [::-1])

