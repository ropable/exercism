def proteins(strand):
    seq = []

    while strand:
        codon, strand = strand[0:3], strand[3:]
        if codon in ["AUG"]:
            seq.append("Methionine")
        elif codon in ["UUU", "UUC"]:
            seq.append("Phenylalanine")
        elif codon in ["UUA", "UUG"]:
            seq.append("Leucine")
        elif codon in ["UCU", "UCC", "UCA", "UCG"]:
            seq.append("Serine")
        elif codon in ["UAU", "UAC"]:
            seq.append("Tyrosine")
        elif codon in ["UGU", "UGC"]:
            seq.append("Cysteine")
        elif codon in ["UGG"]:
            seq.append("Tryptophan")
        elif codon in ["UAA", "UAG", "UGA"]:   # STOP
            strand = ""

    return seq
