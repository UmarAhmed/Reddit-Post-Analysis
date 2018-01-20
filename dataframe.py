import pandas
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import numpy
import re
from sklearn.linear_model import Ridge
import random

# ----------- Cleaning, and creating dataframe from text files --------------

with open('titles.txt') as f:
    titles = f.read().splitlines()

with open('scores.txt') as f:
    scores_ = f.read().splitlines()

with open('times.txt') as f:
    times = f.read().splitlines()

scores = [int(i) for i in scores_]


df = pandas.DataFrame({'titles':titles})
df['times'] = times
df['scores'] = scores


# ----------- Bag of Words Matrix -----------

vectorizer = CountVectorizer(lowercase=True, stop_words="english")
matrix = vectorizer.fit_transform(df["titles"])



# --------- Reducing Dimensionality --------------
# gotta reduce size so this doesn't take forever

col = df["scores"].copy(deep=True)
col_mean = col.mean()

col[col < col_mean] = 0
col[(col > 0) & (col > col_mean)] = 1

# Find the 1000 most informative columns, CHANGE k value depending on size of data
selector = SelectKBest(chi2, k=1000)
selector.fit(matrix, col)
top_words = selector.get_support().nonzero()

chi_matrix = matrix[:,top_words[0]]


# --------- Meta Features --------------------

meta_functions = [
    lambda x: len(x),
    lambda x: x.count(" "),
    lambda x: x.count("."),
    lambda x: x.count("!"),
    lambda x: x.count("?"),
    lambda x: len(x) / (x.count(" ") + 1),
    lambda x: x.count(" ") / (x.count(".") + 1),
    lambda x: len(re.findall("\d", x)),
    lambda x: len(re.findall("[A-Z]", x)),
]


meta_columns = []
for func in meta_functions:
    meta_columns.append(df["titles"].apply(func))

# Convert the meta features to a numpy array.
meta = numpy.asarray(meta_columns).T


# ---- Time Stuff -------------------------

time_columns = []

# conver it to the workable format, datetime
submission_dates = pandas.to_datetime(df["times"])

time_functions = [
    lambda x: x.year,
    lambda x: x.month,
    lambda x: x.day,
    lambda x: x.hour,
    lambda x: x.minute,
]

for func in time_functions:
    time_columns.append(submission_dates.apply(func))


non_nlp = numpy.asarray(time_columns).T


features = numpy.hstack([non_nlp, meta, chi_matrix.todense()])



# ------ It's prediction time friends ------------
# We gonna use ridge regression instead of linear cuz it's cool


train_rows = 8000
test_rows = 1000
# Set a seed to get the same "random" shuffle every time.
random.seed(1)

# Shuffle the indices for the matrix.
indices = list(range(features.shape[0]))
random.shuffle(indices)

# Create train and test sets.
train = features[indices[:train_rows], :]


test = features[indices[:test_rows], :]

train_upvotes = df["scores"].iloc[indices[:train_rows]]
test_upvotes = df["scores"].iloc[indices[train_rows:]]
train = numpy.nan_to_num(train)


# Run the regression and generate predictions for the test set.
reg = Ridge(alpha=1)
reg.fit(train, train_upvotes)


predictions = reg.predict(test)

