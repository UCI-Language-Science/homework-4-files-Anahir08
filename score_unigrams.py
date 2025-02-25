# Write a function called score_unigrams that takes three arguments:
#   - a path to a folder of training data 
#   - a path to a test file that has a sentence on each line
#   - a path to an output CSV file
#
# Your function should do the following:
#   - train a single unigram model on the combined contents of every .txt file
#     in the training folder
#   - for each sentence (line) in the test file, calculate the log unigram 
#     probability ysing the trained model (see the lab handout for details on log 
#     probabilities)
#   - write a single CSV file to the output path. The CSV file should have two
#     columns with headers, called "sentence" and "unigram_prob" respectively.
#     "sentence" should contain the original sentence and "unigram_prob" should
#     contain its unigram probabilities.
#
# Additional details:
#   - there is training data in the training_data folder consisting of the contents 
#     of three novels by Jane Austen: Emma, Sense and Sensibility, and Pride and Prejudice
#   - there is test data you can use in the test_data folder
#   - be sure that your code works properly for words that are not in the 
#     training data. One of the test sentences contains the words 'color' (American spelling)
#     and 'television', neither of which are in the Austen novels. You should record a log
#     probability of -inf (corresponding to probability 0) for this sentence.
#   - your code should be insensitive to case, both in the training and testing data
#   - both the training and testing files have already been tokenized. This means that
#     punctuation marks have been split off of words. All you need to do to use the
#     data is to split it on spaces, and you will have your list of unigram tokens.
#   - you should treat punctuation marks as though they are words.
#   - it's fine to reuse parts of your unigram implementation from HW3.

# You will need to use log and -inf here. 
# You can add any additional import statements you need here.
from math import log, inf
from pathlib import Path
#######################
# YOUR CODE GOES HERE #
import os
import csv

def score_unigrams(training_data, output_csv_path, test_sentences_path):
    word_count = {}
    total_words = 0

    for filename in os.listdir(training_data):
        if filename.endswith(".txt"):
            with open(os.path.join(training_data, filename), 'r', encoding='utf-8') as file:
                for line in file:
                    words = line.lower().split()
                    total_words += len(words)
                    for word in words:
                        word_count[word] = word_count.get(word, 0) + 1

    output_dir = output_csv_path.parent
    if output_dir and not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)

    with open(test_sentences_path, 'r', encoding='utf-8') as test_file, \
         open(output_csv_path, 'w', newline='', encoding='utf-8') as output_csv:
        
        writer = csv.writer(output_csv)
        writer.writerow(['sentence', 'unigram_prob'])

        for line in test_file:
            sentence = line.strip()
            words = sentence.lower().split()
            log_prob = 0

            for word in words:
                if word in word_count:
                    word_prob = word_count[word] / total_words
                    log_prob += log(word_prob)
                else:
                    log_prob = -inf
                    break
            writer.writerow([sentence, log_prob])
# Do not modify the following line
if __name__ == "__main__":
    # You can write code to test your function here
    pass 
