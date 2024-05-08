# A basic implementation of a simple search engine for retieving documents based on search keywords

import csv
import numpy as np
import nltk  
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

# Text acquisition: identifies and stores documents
def read_csv(input_file):
    documents = []
    with open(input_file, 'r', encoding='utf-8') as input_file:
        csv_reader = csv.reader(input_file)
        rows = list(csv_reader)
        for row in rows:
            documents.append(row[0]) # keywords based on the title
    return documents, rows    

# Text transformation: transforms documents into index terms or features
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    # Tokenize the text : process of splitting a text into individual words
    words = word_tokenize(text)
    # Remove stopwords and perform stemming - reduce words to their root
    filtered_words = [stemmer.stem(word.lower()) for word in words if word.lower() not in stop_words] # check word in stopwords or not
    return filtered_words

# Index creation: takes index terms created by text transformations and create data structures to support fast searching
def create_inverted_index(documents):
    inverted_index = {}
    for doc_id, document in enumerate(documents):
        # Preprocess the document text
        tokens = preprocess_text(document)
        # Update the inverted index
        for token in tokens: # add token after preprocessing into set index
            if token not in inverted_index:
                inverted_index[token] = set() # create a token with a set of id --> add doc_id
            inverted_index[token].add(doc_id)
    return inverted_index                     # return the inverted_index(data structure dict)

# search engine
def search_engine(search_key, inverted_index, rows):
    output_documents = []                          # create an empty list
    for key in inverted_index.keys():
        if key in search_key:
            output_index = inverted_index[key] # output_index is a list of doc_id
            for idx in output_index:
                output_documents.append(rows[idx])
    return output_documents

def return_new_csv(output_file, output_documents):
    with open(output_file, "w", newline='') as output_file: # write new information into new cvs file
            csv_writer = csv.writer(output_file)
            for row in output_documents:
                csv_writer.writerow(row)
def main():
    file_path = 'Data/hbr.csv' # Relative Path
    documents, rows = read_csv(file_path)
    
    inverted_index = create_inverted_index(documents)
    # for term, postings in inverted_index.items():
    #     print(f'{term}: {postings}')
    output_documents = search_engine("blockchain technology", inverted_index, rows)
    return_new_csv('search_results.csv', output_documents)

if __name__ == "__main__":
    main()
