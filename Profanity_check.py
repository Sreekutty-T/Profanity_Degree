#Importing libraries
import re, os, sys, platform
import csv
from itertools import zip_longest


#Reading bad words file
with open('search_words.txt') as f:
    list_of_abuses = [line.rstrip() for line in f]


#Searching for foul words in each sentense
def search_foul_words(x):     
            tmp_list = []
            for y in list_of_abuses: 
                if re.search(y, x, re.IGNORECASE) is not None:   
                    tmp_list.append(y) 
                else: 
                    pass 
            another_tmp_list = []
            for item in tmp_list: 
                if len(item) == 0:
                    pass 
                else:
                    another_tmp_list.append(item)
            
            foul_words = ", ".join(another_tmp_list)
            return foul_words   


#Reading input file 
with open('tweets.txt') as f:
    lines = [line.rstrip() for line in f]


#creating list for Degree of Profanity, Bad word count, Total word count
Degree_of_Profanity = []
Bad_Word_Count = []
Total_Word_Count = []


#Calculating Degree of Profanity, Bad word count, Total word count
for m in lines:
    total_words = len(m.split())
    Total_Word_Count.append(total_words)
    foul_words=search_foul_words(m)
    foul_word_count=len(foul_words.split())
    Bad_Word_Count.append(foul_word_count)
    Deg_of_Pro = foul_word_count/total_words
    Degree_of_Profanity.append(Deg_of_Pro)
    


#writing output to a csv file
d = [lines, Bad_Word_Count, Total_Word_Count, Degree_of_Profanity]
export_data = zip_longest(*d, fillvalue = '')
with open('output.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("lines", "Bad_Word_Count","Total_Word_Count","Degree_of_Profanity"))
      wr.writerows(export_data)
myfile.close()


