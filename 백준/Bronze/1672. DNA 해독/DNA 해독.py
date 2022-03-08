N = int(input())
dna = list(input())

dic = {
    'A': {'A': 'A', 'G': 'C', 'C': 'A', 'T': 'G'},
    'G': {'A': 'C', 'G': 'G', 'C': 'T', 'T': 'A'},
    'C': {'A': 'A', 'G': 'T', 'C': 'C', 'T': 'G'},
    'T': {'A': 'G', 'G': 'A', 'C': 'G', 'T': 'T'}
}

while len(dna) != 1:
    x = dna.pop()
    y = dna.pop()
    dna.append((dic.get(x)).get(y))

print(*dna)
