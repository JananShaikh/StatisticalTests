import pandas as pd

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
    csv_file_path = "Data/Structured2.csv"  # Replace with the path to your CSV file
    stored_data = read_csv_and_store_lines(csv_file_path)
    
    #for entry in stored_data:
    #    print(entry)

    for entry in stored_data:
        #print("HIT ID:", entry["HITId"])
        print("User:", entry["Turkle.Username"])
        print("Audio URL:", entry["Input.audio_url"])
        print("Transcript:", entry["Answer.transcript"])
        print("=" * 30)  # Separator for better readability

