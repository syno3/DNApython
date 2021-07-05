### REVERSE ENGINNERING ANY DNA GENOME
---
**Start here**: [`genome.py`](genome.py)

## :thought_balloon: Background
This project applies techniques from [reverse engineering](https://en.wikipedia.org/wiki/Reverse_engineering) to understand any DNA genome. The goal here is simply to build an understanding of DNA protein sequesnce(genome) using first principles.

### Biology vs. software
Biological systems are fundamentally [information processing systems](https://en.wikipedia.org/wiki/Information_processor). While not a perfect analogy, software provides a useful framework for thinking about biology. The table below provides a rough outline of this analogy

:microscope: Biology | :computer: Software | Notes
------- | -------- | -----
[nucleotide](https://en.wikipedia.org/wiki/Nucleotide) | [byte](https://en.wikipedia.org/wiki/Byte) |
[genome](https://en.wikipedia.org/wiki/Genome) | [bytecode](https://en.wikipedia.org/wiki/Bytecode) |
[translation](https://en.wikipedia.org/wiki/Translation_(biology)) | [disassembly](https://en.wikipedia.org/wiki/Disassembler) | 3 byte wide instruction set with arbitrary "[reading frames](https://en.wikipedia.org/wiki/Reading_frame)"
[protein](https://en.wikipedia.org/wiki/Protein) | [function](https://en.wikipedia.org/wiki/Function_(computer_science)) | a polyprotein is a function with multiple pieces
[protein secondary structure](https://en.wikipedia.org/wiki/Protein_secondary_structure) | [basic blocks](https://en.wikipedia.org/wiki/Basic_block) | 80% accuracy in [prediction](https://en.wikipedia.org/wiki/Protein_structure_prediction#Secondary_structure)
[protein tertiary structure](https://en.wikipedia.org/wiki/Protein_tertiary_structure) | | This seems like the hard one to predict: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0205819
[quaternary structure](https://en.wikipedia.org/wiki/Protein_quaternary_structure) | [compiled function with inlining](https://en.wikipedia.org/wiki/Inline_expansion) | https://en.wikipedia.org/wiki/Protein%E2%80%93protein_interaction_prediction
[gene](https://en.wikipedia.org/wiki/Gene) | [library](https://en.wikipedia.org/wiki/Library_(computing)) | bacteria are statically linked, viruses are dynamically linked
[transcription](https://en.wikipedia.org/wiki/Transcription_(biology)) | [loading](https://en.wikipedia.org/wiki/Loader_(computing))
[protein structure prediction](https://en.wikipedia.org/wiki/Protein_structure_prediction) | [library identification](https://www.hex-rays.com/products/ida/tech/flirt/in_depth/)
[genome analysis](https://en.wikipedia.org/wiki/Genomics#Genome_analysis) | [static analysis](https://en.wikipedia.org/wiki/Static_program_analysis) |
[molecular dynamics](https://en.wikipedia.org/wiki/Molecular_dynamics) simulations of [protein folding](https://en.wikipedia.org/wiki/Protein_folding) | [dynamic analysis](https://en.wikipedia.org/wiki/Dynamic_program_analysis) | Simulation doesn't seem to work yet. Constrained by tooling and compute.
no equivalent | [execution](https://en.wikipedia.org/wiki/Execution_(computing)) | We are reverse engineering a CAD format. Runs more like FPGA code, all at once. No serial execution. (What are the FPGA reverse engineering tools?)


## :wrench: Progress
### Downloading any DNA genome
[GenBank](https://www.ncbi.nlm.nih.gov/genbank/) is the NIH genetic sequence database, an annotated collection of all publicly available DNA and RNA sequences.

### Translating RNA to proteins
[`translate.py`](translate.py) contains a function `translate` that converts an RNA sequence to a chain of [amino acids](https://en.wikipedia.org/wiki/Amino_acid). 

### Annotating functions
The `translate` function is used in [`genome.py`](genome.py) to identify and annotate functions for all proteins encoded by the genome.

### Folding proteins
The [OpenMM](http://openmm.org/) toolkit is used for molecular simulation of protein folding in [`fold.py`](fold.py).
