import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download the 'punkt' resource
nltk.download('punkt')
nltk.download('stopwords')

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

def combine_csv_files(file1, file2, output_file):
    # Read both CSV files into DataFrames
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    
    # Combine the DataFrames
    combined_df = pd.concat([df1, df2], ignore_index=True)
    
    # Save the combined DataFrame to a new CSV file
    combined_df.to_csv(output_file, index=False)

def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Convert to lowercase
    tokens = [token.lower() for token in tokens]
    
    # Remove punctuation and stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    
    # Apply stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]
    
    return tokens

def create_corpus(data):
    corpus = []
    for entry in data:
        transcript = entry["Answer.transcript"]
        preprocessed_transcript = preprocess_text(transcript)
        corpus.extend(preprocessed_transcript)
    return corpus

if __name__ == "__main__":
    csv_file1 = "Data/Unstructured1.csv"  
    csv_file2 = "Data/Unstructured2.csv"
    csv_file_path = "combined.csv"
    
    combine_csv_files(csv_file1, csv_file2, csv_file_path)
    
    stored_data = read_csv_and_store_lines(csv_file_path)
    
    #for entry in stored_data:
    #    print(entry)

    #for entry in stored_data:
    #    #print("HIT ID:", entry["HITId"])
    #    print("User:", entry["Turkle.Username"])
    #    print("Audio URL:", entry["Input.audio_url"])
    #    print("Transcript:", entry["Answer.transcript"])
    #    print("=" * 30)  # Separator for better readability
        
    corpus = create_corpus(stored_data)
    print("Corpus:", corpus)
    print("Corpus Size:", len(corpus))    

