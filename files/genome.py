from typing import Sequence

try:
    # IMPORTING DATA ANALYSIS LIBRARIES
    import pandas as pd
    # import numpy as np (will fix bug)
    # IMPORTING PLOTTING MODULES
    import matplotlib.pyplot as plt
    from matplotlib.pyplot import table
    # IMPORTING BIOPYTHON MODULES
    import py3Dmol
    from Bio import SeqIO
    from Bio.SeqRecord import SeqRecord
    from Bio.SeqUtils import ProtParam
    from datetime import time

    from Bio.Data import CodonTable


except Exception as e:
    print(e)


class Genome:
    def __init__(self):
        pass

    @staticmethod
    def load_data(data, Format='fasta'):
        """
        Use SeqIO.read to load the fna file

        Get dna sequence using .seq function (ie) dna = GenomeSequence.seq,

        Transcribe the dna sequence to m_rna using the .transcribe (ie.) m_rna = dna.transcribe()

        Getting the amino acids from the m_rna using .translate (ie.) amino = m_rna.translate(table=1, cds=False)

        return dna, m_rna, amino acids

        """

        genome_sequence = SeqIO.read(data, Format)

        dna = genome_sequence.seq
        m_rna = dna.transcribe()
        amino = m_rna.translate(table=1, cds=False)

        results = "DNA structure :\t{}\n M_RNA structure :\t  {}\n AMINO structure:\t {}".format(dna[:80], m_rna[:80], amino[:80])
        print(results)

        return amino

    @staticmethod
    def protein_dataframe(amino):
        """
        take the data from amino in variable load_data, use split(), and store in protein variable.
        convert the data to variable and return df

        """
        proteins = amino.split('*')
        df = pd.DataFrame(proteins)

        print(df)

        return df

if __name__ == '__main__':
    Genome = Genome()
    Genome.load_data('MN908947.fna')