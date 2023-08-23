# Sample text corpus
corpus = "This is a sample corpus with repeated words. Some words are repeated more than others."

# Tokenization
tokens = corpus.lower().split()

# Calculate the number of tokens and types
num_tokens = len(tokens)
num_types = len(set(tokens))

# Calculate the token-to-type ratio (TTR)
ttr = num_types / num_tokens

print(f"Number of Tokens: {num_tokens}")
print(f"Number of Types: {num_types}")
print(f"Token-to-Type Ratio (TTR): {ttr:.2f}")

