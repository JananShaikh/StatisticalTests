import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

# Sample text corpus
corpus = "The quick brown fox jumps over the lazy dog. The dog barks, and the fox runs away. The brown fox is fast."

# Tokenization and frequency calculation
tokens = corpus.lower().split()
word_counts = Counter(tokens)

# Sort words by frequency in descending order
sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

# Extract ranks and frequencies for plotting
ranks = np.arange(1, len(sorted_words) + 1)
frequencies = [count for word, count in sorted_words]

# Log-log plot
plt.figure(figsize=(10, 6))
plt.loglog(ranks, frequencies, marker='o', linestyle='None')
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.title("Zipf's Law")
plt.grid(True)

# Save the plot as an image file (e.g., PNG)
plt.savefig('zipfs_law_plot.png')

# Close the plot (optional)
plt.close()

