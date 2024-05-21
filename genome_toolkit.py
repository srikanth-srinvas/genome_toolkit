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

    def find_most_frequent_kmers(self, sequence, k_len):
        """
        Finds the most frequent k-mers of a given length in a DNA string.

        Parameters:
            sequence (str): The DNA string to search.
            k_len (int): The length of the k-mers to search for.

        Returns:
            list: A list of the most frequent k-mers in the DNA string.
                  Each k-mer is returned once, even if it appears multiple times
                  with the same highest frequency.
        """
        kmer_frequencies = {}  # Dictionary to store k-mer frequencies

        # Iterate over the DNA sequence to extract k-mers of length k_len
        for i in range(len(sequence) - k_len + 1):
            kmer = sequence[i:i+k_len]  # Extract the k-mer
            if kmer in kmer_frequencies:
                kmer_frequencies[kmer] += 1  # Increment count if k-mer already seen
            else:
                kmer_frequencies[kmer] = 1  # Initialize count if k-mer is seen for the first time

        # Determine the highest frequency of any k-mer
        highest_frequency = max(kmer_frequencies.values())

        # Return all k-mers that have the highest frequency
        return [
            kmer for kmer, frequency in kmer_frequencies.items()
            if frequency == highest_frequency
        ]