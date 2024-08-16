import os
import json
from collections import defaultdict

def main():
    # Load the index from the JSON file
    with open('tub_text/tub_tokens.json', 'r') as file:
        tub_index = json.load(file)

    # Prompt the user for a query
    query = input("Enter your query: ")

    # Tokenize the query and search the index
    query_tokens = query.lower().split()
    doc_ids = set()
    for token in query_tokens:
        if token in tub_index:
            doc_ids.update(tub_index[token])

    # Display the relevant document IDs
    if doc_ids:
        print(f"Relevant document IDs: {', '.join(map(str, doc_ids))}")
    else:
        print("No relevant documents found.")

if __name__ == "__main__":
    main()
    