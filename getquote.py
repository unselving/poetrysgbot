import random
import time
import sys
import tweepy
import csv

def get_quote():
    with open('quotes.csv', mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        chosen_row = random.choice(list(reader))
        print(f'{chosen_row["quote"]}\n— {chosen_row["poem title"]}, {chosen_row["poet name"]}\n{chosen_row["published in"]}')
        

get_quote()
   

