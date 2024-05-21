class genomeToolkit:
    def __init__(self):
        print("Genome toolkit initialised")
        print("[Genome Toolkit Initiated]\n")

    def count_kmer(self, sequence, kmer):
"""
        Counts the number of times a specific k-mer appears in a given sequence,
        including overlapping k-mers.

        Parameters:
            sequence (str): The DNA sequence to search in.
            kmer (str): The specific k-mer to search for in the sequence.

        Returns:
            int: The number of times the k-mer appears in the sequence.
        """
        kmer_count = 0
        for position in range(len(sequence) - (len(kmer) - 1)):
            if sequence[position:position + len(kmer)] == kmer:
                kmer_count += 1
        return kmer_count