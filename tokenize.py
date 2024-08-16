import os
import re
import json
from collections import defaultdict

# Set the input and output directories
input_dir = 'tub_text/Doc101/'
output_file = 'tub_text/tub_tokens.json'

# Initialize the index
tub_index = defaultdict(list)

try:
    # Iterate through the HTML files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.html'):
            with open(os.path.join(input_dir, filename), 'r') as file:
                html_content = file.read().lower()

            # Tokenize the text
            tokens = re.findall(r'\w+', html_content)

            # Remove stop words
            stop_words = {'the', 'a', 'and', 'in', 'to', 'is', 'it', 'for', 'on', 'with', 'at', 'this', 'from', 'that', 'by', 'as', 'be', 'have', 'not', 'but', 'or', 'an', 'were', 'will', 'are', 'can', 'if', 'they', 'their', 'which', 'one', 'you', 'your', 'some', 'all', 'when', 'what', 'out', 'so', 'up', 'do', 'him', 'her', 'has', 'had', 'were', 'was', 'been', 'would', 'there', 'these', 'those', 'then', 'than', 'now', 'only', 'other', 'more', 'most', 'into', 'over', 'after', 'before', 'between', 'under', 'during', 'because', 'while', 'through', 'against', 'above', 'below', 'off', 'again', 'further', 'also', 'such', 'no', 'own', 'both', 'how', 'why', 'where', 'who', 'whom', 'this', 'that', 'these', 'those', 'the', 'a', 'an', 'and', 'or', 'but', 'if', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'from', 'down', 'up', 'to', 'in', 'on', 'off', 'out', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very'}
            tokens = [token for token in tokens if token not in stop_words]

            # Update the index
            for i, token in enumerate(tokens):
                tub_index[token].append(i)

    # Store the index in the output file
    with open(output_file, 'w') as file:
        json.dump(tub_index, file)

    print(f"Index created and saved to {output_file}")

except Exception as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(f"An error occurred: {exc_type.__name__}: {exc_value}")
    