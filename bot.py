
# importing the required libraries
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
import syllables
from profanity_filter import ProfanityFilter
from shareplum import Site
from shareplum import Office365

authcookie = Office365('https://ahhuatthefestivalbot.sharepoint.com', username='ahhuat@ahhuatthefestivalbot.onmicrosoft.com', password='huatah123!').GetCookies()
site = Site('https://ahhuatthefestivalbot.sharepoint.com/sites/AhHuat/', authcookie=authcookie)


# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('ah-huat-the-festival-bot-b0367fbb20e4.json', scope)

# authorize the clientsheet 
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open('Ah Huat the Festival Bot (Responses)')
# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)


# get all the records of the data




pf = ProfanityFilter()

selected_quotes=[]
final_tweet=[]


def makeQuote():
    while True:
        records_data = sheet_instance.get_all_records()
        i = 0 
        #set number of lines
        while i < 3:
            #choose a random line from the sheet
            quote_set=random.choice(records_data)
            #take the cell with the quote
            quote=quote_set["Submit your quote here:"]
            #add quote to the tweet
            selected_quotes.append(quote)
            #take the line out from the original sheet
            records_data.remove(quote_set)
            #repeat for three lines
            i+=1

        #run for each quote
        for x in selected_quotes:
            #split the quote into words
            res = x.split() 
            #create a syllable counter
            totalSyllables=0
            #create a new empty string
            quote=''
            #add words to the string one by one. For each word in the quote
            for x in res:
                #add the syllables of the current word to the counter
                syllableCount = syllables.estimate(x)
                totalSyllables += syllableCount
                #append syllable to empty string
                quote = quote + " " + x
                if totalSyllables >5:
                    break
            final_tweet.append(quote)
            ft=str(final_tweet)
        
        if pf.is_clean(ft):
            fft = str(final_tweet[0])+'\n'+str(final_tweet[1])+'\n'+str(final_tweet[2])
            return fft
    



fft = makeQuote()

new_list = site.List('Tweets for approval')
my_data = data=[{'Title': 'x', 'TweetText':fft}]
new_list.UpdateListItems(data=my_data, kind='New')