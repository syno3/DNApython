from __future__ import division

'''
    We analyze the corona genome

'''

try:
    import py3Dmol
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import os
    
    from Bio import SeqIO
    from Bio.SeqRecord import SeqRecord
    from matplotlib.pyplot import table
    from Bio.SeqUtils import ProtParam
    from datetime import time
except Exception as e:
    print(e)
 
 

CoronaSequence = SeqIO.read('MN908947.fna', 'fasta')
#print(CoronaSequence)
#print(len(CoronaSequence),'nucliotides')
### Transcribe DNA 'fasta' to RNA  => then RNA to amino acid sequence
for sequence in SeqIO.parse('MN908947.fna', 'fasta'):
    pass
DNA = CoronaSequence.seq
mRNA = DNA.transcribe()
## translating MRNA to amino acid
amino = mRNA.translate(table=1, cds=False)

from Bio.Data import CodonTable

print(CodonTable.unambiguous_rna_by_name['Standard'])

Proteins = amino.split('*') # split and separartes the data enclosed within the * sign
df = pd.DataFrame(Proteins) #converting the sequence to pandas dataframe
df.describe()
print('Total proteins:', len(df))

def conv(item):
    return len(item)

def to_str(item):
    return str(item)

df['sequence_str'] = df[0].apply(to_str)
df['length'] = df[0].apply(conv)
df.rename(columns={0: "sequence"}, inplace=True)
df.head()# Take only longer than 20

functional_proteins = df.loc[df['length'] >= 20]
print('Total functional proteins:', len(functional_proteins))
functional_proteins.describe()

### printing out importtant details

poi_list = []
MW_list = []

for record in Proteins[:]:
    print(record)
    try:
        print("\n")
        X = ProtParam.ProteinAnalysis(str(record))
        POI = X.count_amino_acids()
        poi_list.append(POI)
        MW = X.molecular_weight()
        MW_list.append(MW)
        print("Protein of Interest = ", POI)
        print("Amino acids percent =    ",str(X.get_amino_acids_percent()))
        print("Molecular weight = ", MW_list)
        print("Aromaticity = ", X.aromaticity())
        print("Flexibility = ", X.flexibility())
        print("Isoelectric point = ", X.isoelectric_point())
        print("Secondary structure fraction = ",   X.secondary_structure_fraction())
    except Exception as e:
        print(e)
        
        
MoW = pd.DataFrame(data = MW_list,columns = ["weighted columns"] )#plot POI
print ('\n\nConverting to csv')
time.sleep(3)
MoW.to_csv('weightedColumns.csv', index=True)