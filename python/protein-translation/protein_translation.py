def proteins(strand):
    seq = []
    codon_map = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": False,
        "UAG": False,
        "UGA": False,
    }

    while strand:
        codon, strand = strand[0:3], strand[3:]
        if codon in codon_map:
            if codon_map[codon]:
                seq.append(codon_map[codon])
            else:
                strand = ""

    return seq
