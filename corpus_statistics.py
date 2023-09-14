# Author: Mosamat Sabiha Shaikh
# This code performs takes in transcriptions from csv files, preprocesses them, and performs statistical anaylisis on the corpus

import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, words
from nltk.stem import PorterStemmer
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import numpy as np

# Download the 'punkt','stopwords' and 'word' resource
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('words')

# This method combines 2 csv files
def combine_csv_files(file1, file2, output_file):
    # Read both CSV files into DataFrames
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    
    # Combine the DataFrames
    combined_df = pd.concat([df1, df2], ignore_index=True)
    
    # Save the combined DataFrame to a new CSV file
    combined_df.to_csv(output_file, index=False)

# This method reads in a csv file and extracts relevant information from the file
def read_csv_and_store_lines(csv_file):
    data = []
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Convert each row of the DataFrame into a dictionary and store in the 'data' list
    for index, row in df.iterrows():
        data_item = {
            "HITId": row["HITId"],
            "HITTypeId": row["HITTypeId"],
            "Title": row["Title"],
            "CreationTime": row["CreationTime"],
            "MaxAssignments": row["MaxAssignments"],
            "AssignmentDurationInSeconds": row["AssignmentDurationInSeconds"],
            "AssignmentId": row["AssignmentId"],
            "WorkerId": row["WorkerId"],
            "AcceptTime": row["AcceptTime"],
            "SubmitTime": row["SubmitTime"],
            "WorkTimeInSeconds": row["WorkTimeInSeconds"],
            "Input.audio_url": row["Input.audio_url"],
            "Answer.transcript": row["Answer.transcript"],
            "Turkle.Username": row["Turkle.Username"]
        }
        data.append(data_item)
    
    return data

# This methods performs pre-processing techniques on the corpus
def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Convert to lowercase
    tokens = [token.lower() for token in tokens]
    
    # Remove punctuation and stopwords
    stop_words = set(stopwords.words('english')) # This is a problem
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]  
    
    return tokens

# This method builds the corpus
def create_corpus(data):
    corpus = []
    english_words = set(words.words())  # Set of English words
    
    for entry in data:
        transcript = entry["Answer.transcript"]
        # Preprocess text
        preprocessed_transcript = preprocess_text(transcript)
        
        # Filter out English words
        filtered_transcript = [word for word in preprocessed_transcript if word not in english_words]
        
        corpus.extend(filtered_transcript)
    return corpus

# Calculates the token-to-type ratio for the corpus
def calculate_token_to_type_ratio(tokens):
    num_tokens = len(tokens)
    num_types = len(set(tokens))
    # Calculate the token-to-type ratio (TTR)
    ttr =  num_tokens / num_types 
    
    return ttr
 
# Calculates and plots a zipf's law graph for the corpus    
def calculate_zipfs_law(tokens):   
    # Frequency calculation
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
    plt.savefig('structured.png')  #  uncomment for structured corpus 
    #plt.savefig('unstructured.png') # uncomment for unstructured corpus
    
    # Close the plot (optional)
    plt.close()

# Finds the most appeared word in the corpus
def most_common_words(words, num_words=10):
    # Count the occurrences of each word
    word_counts = Counter(words)
    
    # Get the most common words
    most_common = word_counts.most_common(num_words)
    
    return most_common

# Finds the least appeared word in the corpus
def least_common_words(words, num_words=10):
    # Count the occurrences of each word
    word_counts = Counter(words)
    
    # Get the least common words by sorting in ascending order of frequencies
    least_common = word_counts.most_common()[:-num_words-1:-1]
    
    return least_common 

if __name__ == "__main__":
    # Comment/Uncomment depending on which corpus you want to evaluate
    csv_file1 = "Data/Structured1.csv"  
    csv_file2 = "Data/Structured2.csv"
    #csv_file1 = "Data/Unstructured1.csv"  
    #csv_file2 = "Data/Unstructured2.csv"
    csv_file_path = "combined.csv"
    
    combine_csv_files(csv_file1, csv_file2, csv_file_path)
    
    stored_data = read_csv_and_store_lines(csv_file_path)
        
    corpus = create_corpus(stored_data)
    # print the size of the corpus
    print("Corpus Size:", len(corpus))  
    
    # calculate the TTR
    token_to_type_ratio = calculate_token_to_type_ratio(corpus)    
    print(f"Token-to-Type Ratio (TTR): {token_to_type_ratio:.2f}")   
    
    # cacluclate Zipf's law 
    calculate_zipfs_law(corpus)
    
    # Find and print the top 5 common words
    result = most_common_words(corpus, num_words=5)
    
    print("Most appeared words")
    for word, count in result:
        print(f'{word}: {count}')
        
    # Find and print the bottom 5 common words
    result = least_common_words(corpus, num_words=5)
    
    print("Least appeared words")
    for word, count in result:
        print(f'{word}: {count}')    
        
    # Print the number of unique words in the corpus    
    print("Number of distinct words:")
    print(len(set(corpus)))    
    
        
    
