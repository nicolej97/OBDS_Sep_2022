
# Write an algorithm to find all occurrences of a 'TATA' motif in a promoter sequence

from functools import total_ordering


sequence = 'TATAATGCTGACTTATAGCGCTATATATATATA'
motif = 'TATA'
print(sequence)
print(motif)

len(sequence)

position = 0
total = 0

for base in sequence:
    if sequence[position:position + 4] == motif:
        print(position)
        total += 1
    position += 1

print(total)
        
#Write an algorithm to compute the GC content of a DNA sequence

#Define empty variables
total_GC = 0
total = 0 

long_seq = 'GTGGCTTAAGAGGGGAGTCGTCACAGGCGTCAAGTCTTCTTTCTAAAGCCGGGGACCTGG'

#Iterate over each base and add to GC or total variables
for base in long_seq:
    if base == 'C' or base == 'G':
        total_GC += 1
        total += 1
    else:
        total += 1

#Print the variables
print(total_GC)
print(total)

#Calculate percentage GC
total_GC/total * 100




# Write an algorithm to calculate the hamming distance between two DNA sequences

#Define sequences
seq_1 = 'GAGCCTACTAACGGGAT'
seq_2 = 'CATCGTAATGACGGCCT'

#Define empty variables
hamming = 0
position = 0 

# for loop with variables seperate
for base in seq_1:
    if base != seq_2[position]:
        hamming += 1
    position += 1

print(hamming)
print(position)

# for loop with variables together
for base in seq_1, seq_2:
    if seq_1[position] != seq_2[position]:
        hamming += 1
    position += 1

print(hamming)
print(position)

# Finding a consensus sequence 
list_of_motif = ['CATATGGG', 'GATCTGGT', 'CATATGAT', 'CTTCCGGC', 'CATGAGGC', 'CATCTCGC', 'CAAATGGC', 'CATATGGC']
print(list_of_motif)
print(list_of_motif[0])


#Defining empty variables
total_A = [0, 0, 0, 0, 0, 0, 0, 0]
total_G = [0, 0, 0, 0, 0, 0, 0, 0]
total_C = [0, 0, 0, 0, 0, 0, 0, 0]
total_T = [0, 0, 0, 0, 0, 0, 0, 0]



for pos in range(len(list_of_motif[0])):

    for base in list_of_motif:

        if base[pos] == 'A':
            total_A[pos] += 1

        elif base[pos] == 'G':
            total_G[pos] += 1

        elif base[pos] == 'C':
            total_C[pos] += 1

        elif base[pos] == 'T':
            total_T[pos] += 1
        


print(total_A)
print(total_C)
print(total_T)
print(total_G)

for total in total_A:
    if total > total_G, total_T, total_C:
        
print(total_A)

profile = [total_A, total_C, total_T, total_G]

print(profile)

print(pos)



print(list_of_motif[0])







