def hamming_dist(s1, s2):
    ham = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            ham += 1

    return ham

def gen_kmer(k):
    arr = ['A', 'C', 'G', 'T']
    temp_arr = arr

    for update in range(k - 1):
        temp = []

        for i in arr:
            for j in temp_arr:
                temp.append(i + j)

            arr = temp

    return arr

def Neighbour(kmer, d):
    kmers = gen_kmer(len(kmer))
    neighbour = []

    for i in kmers:
        if hamming_dist(kmer, i) <= d:
               neighbour.append(i)

    return neighbour

input = input('Enter filename: ')
f1 = open(input)
read = f1.readlines()
f1.close()

f2 = open('Output_1.txt', 'w')
kmer, d = '', 0

for i in read:
    temp = i.replace('\n', '')

    if temp.isalpha():
        kmer = temp

    elif temp.isdigit():
        d = int(temp)

for i in Neighbour(kmer, d):
    f2.write(i + '\n')

f2.close()
print('Neighbourhood of kmer generated!!!')
