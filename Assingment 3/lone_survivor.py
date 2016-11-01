from imdbpie import Imdb
import string
import random

def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='utf8')

    if skip_header:
        skip_gutenberg_header(fp)


    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break
        line = line.replace('-', ' ')
        strippables = string.punctuation + string.whitespace

        for word in line.split():
            # remove punctuation and convert to lowercase
            word = word.strip(strippables)
            word = word.lower()

            #update the histrogram
            hist[word] = hist.get(word, 0) + 1


    return hist

print(process_file('lone_survivor.txt', skip_header=False))
    

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())

hist = process_file('lone_survivor.txt', skip_header=False)
# print(total_words(hist))


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)

# print(different_words(hist))




def most_common(hist):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    temp = []
    for word, frequency in hist.items():
        temp.append((frequency, word))
    
    temp.sort()
    temp.reverse()
    return temp

#for testing
common_wordlist = most_common(hist)
print(common_wordlist[100])

def print_most_common(hist, num=100):
    """Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    word_list_ordered = most_common(hist)
    top_list = word_list_ordered[0:num]
    for pair in top_list:
        print(pair[1], ":", pair[0])

print_most_common(hist)






def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.

    d1, d2: dictionaries
    """
    res = {}
    for key in d1:
        if key not in d2:
            res[key] = None
    return res



def random_word(hist):
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.
    """
    t = []
    for word, freq in hist.items():
        t.extend([word] * freq)

    return random.choice(t)


print('^^^ Top 100 Words (by frequency) used in review')

print('\n')


''' 1st: Gives the total number of words, and number of 
unique words. We can use this to determine whether it is a long 
or short review

    2nd: Ignores all of the articles and insiginificant words to display
most used words relevant to the content of the review. In addition words 
relating to emotions are displayed.'''


print('Total number of words:', total_words(hist))
print('Number of different words:', different_words(hist))
print('\n')


print('After excluding all articles and insignificant \n'
    'words (a, the, and, when, whose, yet, etc)...')
print('\n')

print('The most used "significant" words & their freq. are:')
print('film: 18, soldiers: 5, stress: 4, soldier: 4')
print('story: 3, lives: 3, weapon: 2, violent: 2, trauma: 2')
print('training: 2, killing: 2, hard: 2, fighting: 2')

print('\n')

print('Words used pertaining to the emotional aspects of the movies:')
print('violent: 2, emotions: 2, emotional: 2, angry: 2')


#NLTK

from imdbpie import Imdb

imdb = Imdb()
print(imdb.search_for_title("Lone Survivor")[0])
print(imdb._get_reviews_data("tt1091191")[0]['summary'])
print(imdb._get_reviews_data("tt1091191")[0]['user_name'])
print(imdb._get_reviews_data("tt1091191")[0]['date'])
print(imdb._get_reviews_data("tt1091191")[0]['text'])

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

sentence = open('lone_survivor.txt', 'r', encoding='utf8').read()

score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)

