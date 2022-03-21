import urllib.request
import random
import string

url = 'https://www.gutenberg.org/files/56836/56836-0.txt' #Link of the book https://www.gutenberg.org/ebooks/56836
response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
text = data.decode('utf-8')
# print(text) # for testing


def readFile(filename):
    '''takes in a file with name filename and returns list of lines read, unprocessed'''
    with open(filename, 'r') as f:
        lines = f.readlines()
        f.close()
    return lines


def process_file(filename):
    """
    Makes a histogram that contains the words from a file.

    filename: string

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='UTF8')

    strippables = string.punctuation + string.whitespace

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break

        line = line.replace('-', ' ')

        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    result = 0
    for v in hist.values():
        result += v
    return result
    #return sum(hist.values()) this can be an alternative way to calculate total words

def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)

def most_common_inc_stopwords(hist):
    """Makes a list of word-freq pairs in descending order of frequency ibcluding stopwrods

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    lst = []
    for word, freq in hist.items():
        lst.append((freq, word))
    lst.sort(reverse = True)
    return lst

def print_most_common_inc_stop_words(hist, num=20): #Got help from https://github.com/AllenDowney/ThinkPython2/blob/master/code/analyze_book1.py
    """Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common_inc_stopwords(hist)
    print('Including stopwords, the most common words are:')
    for freq, word in t[:num]:
        print(word, t, freq)


def most_common_exc_stopwords(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    stopwords = process_file("data/stopwords.txt")
    # print(stopwords.keys())
    lst = []
    for word, freq in hist.items():
        if excluding_stopwords:
            if word in stopwords:
                continue
        lst.append((freq, word))
    lst.sort(reverse = True)
    return lst


def print_most_common_exc_stopwords(hist, num=10): #Got help from https://github.com/AllenDowney/ThinkPython2/blob/master/code/analyze_book1.py
    """Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common_exc_stopwords(hist, True)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, t, freq)


def main():
    hist = process_file('data/Cleaned_56836-0.txt')
    notclean_hist = process_file('data/56836-0.txt')
    chapter1 = process_file('data/Chapter_1.txt')
    chapter2 = process_file('data/Chapter_2.txt')
    chapter3 = process_file('data/Chapter_3.txt')
    chapter4 = process_file('data/Chapter_4.txt')

    # print(hist)
    # print('Total number of words:', total_words(hist))
    # print('Number of different words:', different_words(hist))

    # t = most_common(hist, excluding_stopwords=True)
    # print('Excluding the stopwords, the amount of each word is', t)

    # t = most_common_inc_stopwords(hist) 
    # print("The most common 20 words including the stopwords and their frequncies are:")
    # print("WORD", "COUNT") #TODO: MAKE THIS A NICE LIST
    # for freq, word in t[0:20]:
    #     print(word, freq)

    # z = most_common_exc_stopwords(hist, True) 
    # print("The most common 20 words excluding the stopwords and their frequncies are:")
    # print("WORD", "COUNT") #TODO: MAKE THIS A NICE LIST
    # for freq, word in z[0:20]:
    #     print(word, freq)

    # y = most_common_exc_stopwords(notclean_hist, True) 
    # print("In the version with Biblioraphy and Index, the most common 20 words excluding the stopwords and their frequncies are:")
    # print("WORD", "COUNT") #TODO: MAKE THIS A NICE LIST
    # for freq, word in y[0:20]:
    #     print(word, freq)

    # z = most_common_exc_stopwords(chapter1, True) 
    # print("In chapter 1, The most common 20 words excluding the stopwords and their frequncies are:")
    # print("WORD", "COUNT") #TODO: MAKE THIS A NICE LIST
    # for freq, word in z[0:20]:
    #     print(word, freq)

    # z = most_common_exc_stopwords(chapter2, True) 
    # print("In chapter 2, The most common 20 words excluding the stopwords and their frequncies are:")
    # print("WORD", "COUNT") #TODO: MAKE THIS A NICE LIST
    # for freq, word in z[0:20]:
    #     print(word, freq)

    # z = most_common_exc_stopwords(chapter3, True) 
    # print("In chapter 3, The most common 20 words excluding the stopwords and their frequncies are:")
    # print("WORD", "COUNT") #TODO: MAKE THIS A NICE LIST
    # for freq, word in z[0:20]:
    #     print(word, freq)
    
    # z = most_common_exc_stopwords(chapter4, True) 
    # print("In chapter 4, The most common 20 words excluding the stopwords and their frequncies are:")
    # print("WORD", "COUNT") #TODO: MAKE THIS A NICE LIST
    # for freq, word in z[0:20]:
    #     print(word, freq)

if __name__ == '__main__':
    main()
