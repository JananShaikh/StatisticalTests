import pandas as pd
import textdistance

def combine_csv_files(file1, file2, output_file):
    # Read both CSV files into DataFrames
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    
    # Combine the DataFrames
    combined_df = pd.concat([df1, df2], ignore_index=True)
    
    # Save the combined DataFrame to a new CSV file
    combined_df.to_csv(output_file, index=False)

def extract_audio_name(url):
    # Extract the part after the last '/' and before '.mp3'
    audio_name = url.split("/")[-1].split(".mp3")[0]
    return audio_name

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

if __name__ == "__main__":
    csv_file1 = "Data/Structured1.csv"  
    csv_file2 = "Data/Structured2.csv"
    csv_file_path = "combined.csv"
    
    combine_csv_files(csv_file1, csv_file2, csv_file_path)
    
    stored_data = read_csv_and_store_lines(csv_file_path)
    
    audio_url_to_transcripts = {}
    
    for entry in stored_data:
        audio_url = entry["Input.audio_url"]
        transcript = entry["Answer.transcript"]
        
        if audio_url not in audio_url_to_transcripts:
            audio_url_to_transcripts[audio_url] = []
        audio_url_to_transcripts[audio_url].append(transcript)
    
    output_filename = "similarity_results.txt"
    
    with open(output_filename, "w") as output_file:
        for audio_url, transcripts in audio_url_to_transcripts.items():
            audio_name = extract_audio_name(audio_url)
            print(f"Audio URL: {audio_name}")
        
            output_file.write(f"Audio URL: {audio_name}")   
            output_file.write("\n")
            
            for i in range(len(transcripts)):
                for j in range(i + 1, len(transcripts)):
                    transcript_1 = transcripts[i]
                    transcript_2 = transcripts[j]
                
                    levenshtein_distance = textdistance.levenshtein(transcript_1, transcript_2)
                    similarity = 1 - (levenshtein_distance / max(len(transcript_1), len(transcript_2)))
                
                    print(f"Similarity between Transcript {i+1} and Transcript {j+1}: {similarity:.4f}")
                    output_file.write(f"Similarity between Transcript {i+1} and Transcript {j+1}: {similarity:.4f}\n")
            output_file.write("\n")        
                    
                    

