# Reddit-Post-Analysis
**Libraries:** pandas, numpy, sklearn, praw 

Data mined from reddit.com/r/askreddit by using praw. Obtained post titles, time of creation, and upvotes. This data is stored in scores.txt, times.txt, and titles.txt 

Common stop words were used to clean the data, these are found in stop_words.txt (obtained from https://github.com/Alir3z4/stop-words)

Used pandas, sklearn, and numpy to analyze the data and add more features from the existing data:
- Used a chi-squared test to keep informative data and reduce dimensionality. 
- Created a column containing information about punctuation.
- Column containing time information was created.

The machine learning algorithm was trained on some some of our aforementioned data using ridge regression. The final result is a program that can predict the score of a post to some degree of certainty.



