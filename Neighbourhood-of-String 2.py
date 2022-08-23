def ArrGen(k):
    array = ['A', 'G', 'C', 'T']

    for loop in range(k - 1):
        array = [i + j for i in array for j in 'AGCT']

    return array

def ham(str1, str2):
    dist = sum(1 for i in range(len(str1)) if str1[i] != str2[i])
    return dist

def Neighbour(kmer, d):
    file = open('Output_2.txt', 'w')
    kmer_list = ArrGen(len(kmer))

    for each in kmer_list:
        if ham(kmer, each) <= d:
            file.write(each + '\n')

    file.close()

file_name = input('Enter the filename/path: ')
reader = open(file_name)

db = reader.read().split('\n')
reader.close()

kmer = db[0]
d = int(db[1])
Neighbour(kmer, d)
print('Neighbourhood of kmer generated!!!')
