# Generating-the-Neighbourhood-of-String

The d-neighborhood Neighbors(Pattern, d) is the set of all k-mers whose Hamming distance from Pattern does not exceed d.

We are given with a k-mer and a d value. So, we define
functions to compute the hamming distance of 2 k-mers,
generating all possible k-mers for a given value of k &
computing the neighbourhood of the provided string.
Our aim is to thus generate all possible k-mers and
compute the hamming distance of each k-mer produced with
the given k-mer. If the hamming distance doesn’t exceed the
d value that is given as the input, then those k-mers are
returned as the neighbourhood of the string.

Three versions of the same algorithm with decreasing time complexity are provided.
