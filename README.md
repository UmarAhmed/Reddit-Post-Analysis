# Reddit-Post-Analysis
**Libraries:** pandas, numpy, sklearn, praw 

Data mined from reddit.com/r/askreddit by using praw. Obtained post titles, time post was created, and number upvotes. This data is stored in scores.txt, times.txt, and titles.txt (a better way would be a csv)

Common stop words were used to clean the data, these are found in stop_words.txt (obtained from https://github.com/Alir3z4/stop-words)

Used a chi-squared test to keep informative data and reduce dimensionality. 

Used ridge regression (from scikit-learn) to train and predict.

End-Result: On average the model was within 10 upvotes of the actual result



