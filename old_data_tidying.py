'''
def make_matrix(titles, vocab):
    matrix = []
    for i in titles:
        # Count each word in the headline, and make a dictionary.
        counter = Counter(i)
        # Turn the dictionary into a matrix row using the vocab.
        row = [counter.get(w, 0) for w in vocab]
        matrix.append(row)
    df = pandas.DataFrame(matrix)
    df.columns = unique_words
    return df

# Lowercase, then replace any non-letter, space, or digit character in the headlines.
new_titles = [re.sub(r'[^\w\s\d]','',h.lower()) for h in titles]

# Replace sequences of whitespace with a space character.
new_titles = [re.sub("\s+", " ", h) for h in new_titles]


with open("stop_words.txt", 'r') as f:
    stopwords = f.read().split("\n")

# Do the same punctuation replacement that we did for the headlines,
# so we're comparing the right things.
stopwords = [re.sub(r'[^\w\s\d]','',s.lower()) for s in stopwords]

unique_words = list(set(" ".join(new_titles).split(" ")))
# Remns, which is way betove stopwords from the vocabulary.
unique_words = [w for w in unique_words if w not in stopwords]

'''