import csv

def read_csv_and_store(filename):
    data_list = []

    with open(filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data_list.append(row)

    return data_list

def main():
    csv_filename = 'Data/Unstructured1.csv'  # Replace with the actual filename

    try:
        stored_data = read_csv_and_store(csv_filename)
        for entry in stored_data:
            print(entry)  # You can modify this to store the data in any desired format
    except FileNotFoundError:
        print(f"File '{csv_filename}' not found.")

if __name__ == "__main__":
    main()
