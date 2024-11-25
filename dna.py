#dna analiysis
sample = ['GTA','GGG','CAC']

def read_dna(dna_file):
    dna_data = ""
    with open(dna_file, "r") as f:
        for line in f:
            dna_data += line
    return dna_data

def dna_condons(dna):
    codons = []
    for i in range(0, len(dna),3):
         if (i + 3) < len(dna):
            codons.append(dna[i:i + 3])
    return codons

def match_dna(dna):
    matches = 0
    for codon in dna:
        if codon in sample:
            matches += 1
    return matches

def is_criminal(dna_sample):
    dna_data = read_dna(dna_sample)
    codons = dna_condons(dna_data)
    num_matches = match_dna(codons)
    if num_matches >= 3:
        print("the number of matches is {num_matches}, investigation should continue1".format(num_matches))
    else:
        print("Set free")

is_criminal("suspect1.txt")
is_criminal("suspect2.txt")
is_criminal("suspect3.txt")
