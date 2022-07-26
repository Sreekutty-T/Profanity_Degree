# Profanity analysis of Twitter tweets using Python
**A. Short Description**

Given a file of tweets and a list of abuses/racial slurs, identify the degree of profanity of Twitter tweets.

**B. Long Description**

Suppose two files are provided such that one file contains Twitter tweets by various users and the other consists of a list of "profanity words" (abuses and/or racial slurs).

The file containg tweets will be called as the "tweet file".  A single column containing the tweets preceeded by the users' Twitter handle. Can be with/without a header. For example,

1. "@User1 tweet"
2. "@user2 tweet"
3. "@user3 tweet"

The other file, called "search_words" file, contains a list of abusive words and/or racial slurs such that each "profinity word" is on a new line. This file must be a text file.

Given these two files fulfilling the aforementioned requiremnets, the Python program identifies the degree of profanity per tweet. The degree of profanity is defined as the ratio of the number of abusive/racial words in a tweet to the total number of words in the times time 100.


**C. Inputs Description**


A file containing Twitter handles and their tweets such that each line contains one Twitter handle and tweets. Check any of the example files called "tweets" with extensions "txt" for the correct format.

A "txt" file with one "profanity word" per line. Check the file called "search_words.txt" for the correct format.

**D. Output Description**


A CSV file with 5 columns: "lines", "Bad_Words", "Bad_Word_Count", "Total_Word_Count", and "Degree_of_Profanity" - Check "output.csv".

**E. TO DO**


Test with a txt file which is similar to "tweets.txt". The file name should be same because "tweets.txt" is used in the code.If you are changing the input file name please rename it in the code as well.



