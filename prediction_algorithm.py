from sklearn.linear_model import Ridge
import numpy
import random

train_rows = 7500
# Set a seed to get the same "random" shuffle every time.
random.seed(1)

# Shuffle the indices for the matrix.
indices = list(range(features.shape[0]))
random.shuffle(indices)

# Create train and test sets.
train = features[indices[:train_rows], :]
test = features[indices[train_rows:], :]
train_upvotes = submissions["upvotes"].iloc[indices[:train_rows]]
test_upvotes = submissions["upvotes"].iloc[indices[train_rows:]]
train = numpy.nan_to_num(train)

# Run the regression and generate predictions for the test set.
reg = Ridge(alpha=.1)
reg.fit(train, train_upvotes)
predictions = reg.predict(test)