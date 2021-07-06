from typing import Sequence


try:
    # IMPORTING DATA ANALYSIS LIBRARIES
    import pandas as pd
    #import numpy as np (will fix bug)
    # IMPORTING PLOTTING MODULES
    import matplotlib.pyplot as plt
    from matplotlib.pyplot import table
    import seaborn as sns
    # IMPORTING BIOPYTHON MODULES
    import py3Dmol
    from Bio import SeqIO
    from Bio.SeqRecord import SeqRecord
    from Bio.SeqUtils import ProtParam
    from datetime import time

except Exception as e:
    print(e)

class genome:
    def __init__(self):
        pass
    def load_data(self, data, format='fasta'):
        """ 
        Use SeqIO.read to load the fna file

        Get DNA sequence using .seq function (ie) DNA = GenomeSequence.seq,

        Transcribe the DNA sequence to mRNA using the .transcribe (ie.) mRNA = DNA.transcribe()

        Getting the amino acids from the mRNA using .translate (ie.) amino = mRNA.translate(table=1, cds=False)

        return DNA, mRNA, amino acids

        """

        GenomeSequence=SeqIO.read(data, format)
        print(GenomeSequence.id)
        
        DNA = GenomeSequence.seq
        mRNA = DNA.transcribe()
        ## translating MRNA to amino acid
        amino = mRNA.translate(table=1, cds=False)


        return DNA, mRNA, amino

if __name__ == '__main__':
    Genome = genome()
    Genome.load_data('MN908947.fna')