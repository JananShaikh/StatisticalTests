import pandas as pd
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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

def calculate_similarity(transcripts):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(transcripts)
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix

if __name__ == "__main__":
    csv_file_path = "Data/Structured1.csv"  # Replace with the path to your CSV file
    stored_data = read_csv_and_store_lines(csv_file_path)
    
    audio_url_to_transcripts = {}
    
    for entry in stored_data:
        audio_url = entry["Input.audio_url"]
        transcript = entry["Answer.transcript"]
        
        if audio_url not in audio_url_to_transcripts:
            audio_url_to_transcripts[audio_url] = []
        audio_url_to_transcripts[audio_url].append(transcript)
    
    for audio_url, transcripts in audio_url_to_transcripts.items():
        similarity_matrix = calculate_similarity(transcripts)
        print(f"Audio URL: {audio_url}")
        print("Similarity Matrix:")
        print(similarity_matrix)
        print("=" * 30)

