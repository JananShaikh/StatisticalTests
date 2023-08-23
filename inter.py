def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def inter_transcriber_similarity(strings):
    num_strings = len(strings)
    similarity_matrix = [[0] * num_strings for _ in range(num_strings)]

    for i in range(num_strings):
        for j in range(i, num_strings):
            distance = levenshtein_distance(strings[i], strings[j])
            similarity = 1 - distance / max(len(strings[i]), len(strings[j]))
            similarity_matrix[i][j] = similarity
            similarity_matrix[j][i] = similarity

    return similarity_matrix

if __name__ == "__main__":
    input_strings = [
        "hello world",
        "helo wold",
        "hi there",
        "hola world"
    ]

    similarity_matrix = inter_transcriber_similarity(input_strings)

    for i, string in enumerate(input_strings):
        print(f"Similarity with '{string}':")
        for j, similarity in enumerate(similarity_matrix[i]):
            print(f"   '{input_strings[j]}': {similarity:.2f}")

