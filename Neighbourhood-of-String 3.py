from itertools import product

def hamming(s1, s2):
    return sum(1 for i in range(len(s1)) if s1[i] != s2[i])

def Neighbour(kmer, d):
    with open('Output_3.txt', 'w') as file:
        for i in product('ACGT', repeat = len(kmer)):
            if hamming(kmer, ''.join(i)) <= d:
                file.write(f"{''.join(i)}\n")

filename = input('Enter filename or path: ')

with open(filename) as file:
    data = file.read().split('\n')
    Neighbour(data[0], int(data[1]))
    print('Neighbourhood of kmer generated!!!')
