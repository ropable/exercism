def to_rna(dna_strand):
    transcribe = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U',
    }
    return ''.join([transcribe[n] for n in dna_strand])
