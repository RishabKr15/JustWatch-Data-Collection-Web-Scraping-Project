#!/usr/bin/env python
# coding: utf-8

# # **Rishabh Kumar Web Scraping Project**

# # **Web Scraping & Data Handling Challenge**

# 
# 
# ### **Website:**
# JustWatch -  https://www.justwatch.com/in/movies?release_year_from=2000
# 
# 
# ### **Description:**
# 
# JustWatch is a popular platform that allows users to search for movies and TV shows across multiple streaming services like Netflix, Amazon Prime, Hulu, etc. For this assignment, you will be required to scrape movie and TV show data from JustWatch using Selenium, Python, and BeautifulSoup. Extract data from HTML, not by directly calling their APIs. Then, perform data filtering and analysis using Pandas, and finally, save the results to a CSV file.
# 
# ### **Tasks:**
# 
# **1. Web Scraping:**
# 
# Use BeautifulSoup to scrape the following data from JustWatch:
# 
#    **a. Movie Information:**
# 
#       - Movie title
#       - Release year
#       - Genre
#       - IMDb rating
#       - Streaming services available (Netflix, Amazon Prime, Hulu, etc.)
#       - URL to the movie page on JustWatch
# 
#    **b. TV Show Information:**
# 
#       - TV show title
#       - Release year
#       - Genre
#       - IMDb rating
#       - Streaming services available (Netflix, Amazon Prime, Hulu, etc.)
#       - URL to the TV show page on JustWatch
# 
#   **c. Scope:**
# 
# ```
#  ` - Scrape data for at least 50 movies and 50 TV shows.
#    - You can choose the entry point (e.g., starting with popular movies,
#      or a specific genre, etc.) to ensure a diverse dataset.`
# 
# ```
# 
# 
# **2. Data Filtering & Analysis:**
# 
#    After scraping the data, use Pandas to perform the following tasks:
# 
#    **a. Filter movies and TV shows based on specific criteria:**
# 
#    ```
#       - Only include movies and TV shows released in the last 2 years (from the current date).
#       - Only include movies and TV shows with an IMDb rating of 7 or higher.
# ```
# 
#    **b. Data Analysis:**
# 
#    ```
#       - Calculate the average IMDb rating for the scraped movies and TV shows.
#       - Identify the top 5 genres that have the highest number of available movies and TV shows.
#       - Determine the streaming service with the most significant number of offerings.
#       
#    ```   
# 
# **3. Data Export:**
# 
# ```
#    - Dump the filtered and analysed data into a CSV file for further processing and reporting.
# 
#    - Keep the CSV file in your Drive Folder and Share the Drive link on the colab while keeping view access with anyone.
# ```
# 
# **Submission:**
# ```
# - Submit a link to your Colab made for the assignment.
# 
# - The Colab should contain your Python script (.py format only) with clear
#   comments explaining the scraping, filtering, and analysis process.
# 
# - Your Code shouldn't have any errors and should be executable at a one go.
# 
# - Before Conclusion, Keep your Dataset Drive Link in the Notebook.
# ```
# 
# 
# 
# **Note:**
# 
# 1. Properly handle errors and exceptions during web scraping to ensure a robust script.
# 
# 2. Make sure your code is well-structured, easy to understand, and follows Python best practices.
# 
# 3. The assignment will be evaluated based on the correctness of the scraped data, accuracy of data filtering and analysis, and the overall quality of the Python code.
# 
# 
# 
# 
# 
# 
# 

# # **Start The Project**

# In[ ]:


from google.colab import drive
drive.mount('/content/drive/MyDrive/AlmaBetter')


# In[ ]:


# Getting the current directory
import os
os.getcwd()


# In[ ]:


#Changing the working directory to project folder
os.chdir('/content/drive/MyDrive/AlmaBetter')
os.getcwd()


# ## **Task 1:- Web Scrapping**

# In[ ]:


#Installing all necessary labraries
get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[ ]:


#import all necessary labraries
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np


# ## **Scrapping Movies Data**

# In[ ]:


def fetch_movie_urls(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return "Failed to retrieve the page, status code:", response.status_code
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


url = 'https://www.justwatch.com/in/movies?release_year_from=2000'
soup=fetch_movie_urls(url)
print(soup.prettify())

## Hint : Use the following code to extract the film urls
# movie_links = soup.find_all('a', href=True)
# movie_urls = [link['href'] for link in movie_links if '/movie/' in link['href']]

# url_list=[]
# for x in movie_urls:
#   url_list.append('https://www.justwatch.com'+x)

#Links
list_link = []
for i in soup.find_all('a', attrs = {'class':'title-list-grid__item--link'}):
    list_link.append('https://www.justwatch.com'+i['href'])

print(list_link)


# 

# ## **Fetching Movie URL's**

# In[ ]:


#Links
list_link = []
for i in soup.find_all('a', attrs = {'class':'title-list-grid__item--link'}):
    list_link.append('https://www.justwatch.com'+i['href'])

print(list_link)


# In[ ]:


# Specifying the URL from which movies related data will be fetched
url='https://www.justwatch.com/in/movie/stree-2'
# Sending an HTTP GET request to the URL

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.google.com/',
}

page = requests.get(url, headers=headers)

# Parsing the HTML content using BeautifulSoup with the 'html.parser'
soup=BeautifulSoup(page.text,'html.parser')
# Printing the prettified HTML content
print(soup.prettify())


# ## **Scrapping Movie Title**

# In[ ]:


soup.find_all('div', attrs={'class':'title-detail-hero__details' })[0].find_all('h1',attrs={'class':'title-detail-hero__details__title'})[0].contents[0].strip()


# ## **Scrapping release Year**

# In[ ]:


# Write Your Code here
#release year
eval(soup.find_all('div', attrs={'class':'title-detail-hero__details' })[0].find_all('h1',attrs={'class':'title-detail-hero__details__title'})[0].find_all('span', attrs={'class':'release-year'})[0].text.strip())


# ## **Scrapping Genres**

# In[ ]:


# Genres
soup.find_all('div' ,attrs={'class':'detail-infos__value'})[1].find('span').text.strip()


# ## **Scrapping IMBD Rating**

# In[ ]:


# Write Your Code here
# IMDB
#eval(soup.find_all('div', attrs={'class':'jw-scoring-listing__rating--group jw-scoring-listing__rating--link'})[0].text.strip().split(' ')[0])


# In[ ]:


# IMDB
eval(soup.find_all('div' , attrs={'class':"title-detail-hero-details__item"})[2].find_all('span' , attrs={'class':"imdb-score"})[0].text.strip().split(' ')[0])


# ## **Scrapping Runtime/Duration**

# In[ ]:


#runtime/duration
soup.find_all('div',attrs={'class':'detail-infos'})[2].find_all('div', attrs={'class':'detail-infos__value'})[0].text


# ## **Scrapping Age Rating**

# In[ ]:


#AgeRating
soup.find_all('div',attrs={'class':'detail-infos'})[3].find_all('div', attrs={'class':'detail-infos__value'})[0].text


# ## **Fetching Production Countries Details**

# In[ ]:


# Write Your Code here
#Productioncountry
soup.find_all('div',attrs={'class':'detail-infos'})[4].find_all('div', attrs={'class':'detail-infos__value'})[0].text


# ## **Fetching Streaming Service Details**

# In[ ]:


soup.find_all('div',attrs={'class':'picture-wrapper'})[0].find_all('img', attrs ={'class':"offer__icon"})[0].get('alt')


# ## **Now Creating Movies DataFrame**

# In[ ]:


# importing time
import time
time.sleep(2)


# Extracting Data for the DataFrame

# In[ ]:


movie_info_full_data = []
for l in list_link:
    info_dict = {}
# Specifying the URL from which movies related data will be fetched
    url = l
# Sending an HTTP GET request to the URL
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.google.com/',
}

    page = requests.get(url, headers=headers)
# Parsing the HTML content using BeautifulSoup with the 'html.parser'
    soup=BeautifulSoup(page.text,'html.parser')
    try:
        info_dict['link'] = l
        info_dict['title'] = soup.find_all('div', attrs={'class':'title-detail-hero__details' })[0].find_all('h1',attrs={'class':'title-detail-hero__details__title'})[0].contents[0].strip()
        info_dict['release_year'] = eval(soup.find_all('div', attrs={'class':'title-detail-hero__details' })[0].find_all('h1',attrs={'class':'title-detail-hero__details__title'})[0].find_all('span', attrs={'class':'release-year'})[0].text.strip())
        info_dict['imdb'] = eval(soup.find_all('div', attrs={'class':'jw-scoring-listing__rating--group jw-scoring-listing__rating--link'})[0].text.strip().split(' ')[0])
        for i in soup.find_all('div',attrs = {'class':'detail-infos'}):
            if i.find_all('h3', attrs = {'class':'detail-infos__subheading'})[0].text =='Genres':
                info_dict['Genres'] = i.find_all('div', attrs = {'class':'detail-infos__value'})[0].text.strip()
            elif i.find_all('h3', attrs = {'class':'detail-infos__subheading'})[0].text =='Runtime':
                 info_dict['Runtime'] = i.find_all('div', attrs = {'class':'detail-infos__value'})[0].text.strip()
            elif i.find_all('h3', attrs = {'class':'detail-infos__subheading'})[0].text =='Age rating':
                 info_dict['Age_rating'] = i.find_all('div', attrs = {'class':'detail-infos__value'})[0].text.strip()
            elif i.find_all('h3', attrs = {'class':'detail-infos__subheading'})[0].text.strip() =='Production country':
                 info_dict['Production_country'] = i.find_all('div', attrs = {'class':'detail-infos__value'})[0].text.strip()

        movie_info_full_data.append(info_dict)
        print('Successful:',l)
    except:
        print('Error:',l)
        continue

    time.sleep(2)


# In[ ]:


#Creating DataFrame
movie_dataframe = pd.DataFrame(movie_info_full_data)
movie_dataframe


# ## **Scraping TV  Show Data**

# In[ ]:


import requests
from bs4 import BeautifulSoup

# Specifying the URL
tv_url = 'https://www.justwatch.com/in/tv-shows'

# Adding headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

# Sending an HTTP GET request with headers
page = requests.get(tv_url, headers=headers)

# Check the status code
if page.status_code == 200:
    # Parsing the HTML content
    soup = BeautifulSoup(page.text, 'html.parser')
    print(soup.prettify())
else:
    print(f"Failed to fetch data. Status code: {page.status_code}")


# ## **Fetching Tv shows Url details**

# In[ ]:


#Links
list_link = []
for i in soup.find_all('a', attrs = {'class':'title-list-grid__item--link'}):
    list_link.append('https://www.justwatch.com'+i['href'])

print(list_link)


# In[ ]:


# Specifying the URL from which movies related data will be fetched
url='https://www.justwatch.com/in/tv-show/from'
# Sending an HTTP GET request to the URL

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.google.com/',
}

page = requests.get(url, headers=headers)

# Parsing the HTML content using BeautifulSoup with the 'html.parser'
soup=BeautifulSoup(page.text,'html.parser')
# Printing the prettified HTML content
print(soup.prettify())


# ## **Fetching Tv Show Title details**

# In[ ]:


soup.find_all('div', attrs={'class':'title-detail-hero__details' })[0].find_all('h1',attrs={'class':'title-detail-hero__details__title'})[0].contents[0].strip()


# ## **Fetching Release Year**

# In[ ]:


eval(soup.find_all('div', attrs={'class':'title-detail-hero__details' })[0].find_all('h1',attrs={'class':'title-detail-hero__details__title'})[0].find_all('span', attrs={'class':'release-year'})[0].text.strip())


# ## **Fetching TV Show Genre Details**

# In[ ]:


# Genres
soup.find_all('div' ,attrs={'class':'detail-infos__value'})[1].find('span').text.strip()


# ## **Fetching IMDB Rating Details**

# In[ ]:


# IMDB
eval(soup.find_all('div' , attrs={'class':"title-detail-hero-details__item"})[2].find_all('span' , attrs={'class':"imdb-score"})[0].text.strip().split(' ')[0])


# ## **Fetching Age Rating Details**

# In[ ]:


#AgeRating
soup.find_all('div',attrs={'class':'detail-infos'})[3].find_all('div', attrs={'class':'detail-infos__value'})[0].text


# ## **Fetching Production Country details**

# In[ ]:


soup.find_all('div',attrs={'class':'detail-infos'})[3].find_all('div', attrs={'class':'detail-infos__value'})[0].text


# ## **Fetching Streaming Service details**

# In[ ]:


soup.find_all('picture',attrs={'class':'picture-wrapper'})[0].find_all('img', attrs ={'class':"offer__icon"})[0].get('alt')


# ## **Fetching Duration Details**

# In[ ]:


#runtime/duration
soup.find_all('div',attrs={'class':'detail-infos'})[2].find_all('div', attrs={'class':'detail-infos__value'})[0].text


# ## **Creating TV Show DataFrame**

# In[ ]:


# Write Your Code here
# importing time
import time
time.sleep(2)


# In[ ]:


tv_shows_info_full_data = []
for l in list_link:
    info_dict = {}
# Specifying the URL from which movies related data will be fetched
    url = l
# Sending an HTTP GET request to the URL
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.google.com/',
}

    page = requests.get(url, headers=headers)
# Parsing the HTML content using BeautifulSoup with the 'html.parser'
    soup=BeautifulSoup(page.text,'html.parser')
    try:
        info_dict['link'] = l
        info_dict['title'] = soup.find_all('div', attrs={'class':'title-detail-hero__details' })[0].find_all('h1',attrs={'class':'title-detail-hero__details__title'})[0].contents[0].strip()
        info_dict['release_year'] = eval(soup.find_all('div', attrs={'class':'title-detail-hero__details' })[0].find_all('h1',attrs={'class':'title-detail-hero__details__title'})[0].find_all('span', attrs={'class':'release-year'})[0].text.strip())
        info_dict['imdb'] = eval(soup.find_all('div' , attrs={'class':"title-detail-hero-details__item"})[2].find_all('span' , attrs={'class':"imdb-score"})[0].text.strip().split(' ')[0])
        info_dict['Streaming Platform']=soup.find_all('picture',attrs={'class':'picture-wrapper'})[0].find_all('img', attrs ={'class':"offer__icon"})[0].get('alt')
        for i in soup.find_all('div',attrs = {'class':'detail-infos'}):
            if i.find_all('h3', attrs = {'class':'detail-infos__subheading'})[0].text =='Genres':
                info_dict['Genres'] = i.find_all('div', attrs = {'class':'detail-infos__value'})[0].text.strip()
            elif i.find_all('h3', attrs = {'class':'detail-infos__subheading'})[0].text =='Runtime':
                 info_dict['Runtime'] = i.find_all('div', attrs = {'class':'detail-infos__value'})[0].text.strip()
            elif i.find_all('h3', attrs = {'class':'detail-infos__subheading'})[0].text =='Age rating':
                 info_dict['Age_rating'] = i.find_all('div', attrs = {'class':'detail-infos__value'})[0].text.strip()
            elif i.find_all('h3', attrs = {'class':'detail-infos__subheading'})[0].text.strip() =='Production country':
                 info_dict['Production_country'] = i.find_all('div', attrs = {'class':'detail-infos__value'})[0].text.strip()

        tv_shows_info_full_data.append(info_dict)
        print('Successful:',l)
    except:
        print('Error:',l)
        continue

    time.sleep(2)


# In[ ]:


#Creating DataFrame
tv_shows_dataframe = pd.DataFrame(tv_shows_info_full_data)
tv_shows_dataframe


# ## **Task 2 :- Data Filtering & Analysis**

# ### **Removing duplicates based on url**

# In[ ]:


#removing duplicates based on url
import pandas as pd

df = pd.DataFrame(tv_shows_info_full_data)
df = df.drop_duplicates(subset=["link"])


# ### **Handling Missing Values**

# In[ ]:


df.fillna({'Genres': 'Unknown', 'Runtime': '0 min', 'Age_rating': 'Not Rated'}, inplace=True)
df


# ### **Validating Data Formats**:
# 
# - Ensuring numerical fields (IMDb, Runtime, etc.) are in the correct format.
# 
# - Converting data types as necessary:
#   - IMDb → float
#   - Runtime → integer (in minutes)
# 

# In[ ]:


df['imdb'] = pd.to_numeric(df['imdb'], errors='coerce')  # Converting IMDb to numeric
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')  # Converting release year to numeric
# Standardizing the 'Runtime' column to replace variations of 'min'
#df['Runtime'] = df['Runtime'].str.replace(r'[^0-9]', '', regex=True)  # Keeping only digits
df['Runtime'] = pd.to_numeric(df['Runtime'], errors='coerce')  # Converting to float
df


# ###  **Normalize Text Fields:**
# - Standardize text fields like Genres or Production_country for consistency (e.g., lowercase all text).

# In[ ]:


df['Genres'] = df['Genres'].str.lower()
df['Production_country'] = df['Production_country'].str.strip()


# ## Top Rated TV Shows:
# 
# - Sort the data by IMDb scores to find the highest-rated shows.
# 

# In[ ]:


top_rated = df.sort_values(by='imdb', ascending=False).head(10)
#print(top_rated[['title', 'imdb', 'Genres']])
pd.DataFrame(top_rated)


# ## **Genre Distribution:**
# 
# Analyze the frequency of different genres.

# In[ ]:


genre_counts = df['Genres'].value_counts()
#print(genre_counts)
pd.DataFrame(genre_counts)


# ## Content by Country:
# 
# - Group data by production countries to analyze which countries produce the most content.
# 
# 

# In[ ]:


country_counts = df['Production_country'].value_counts()
pd.DataFrame(country_counts)


# ## Trends Over Time:
# 
# - Plot the number of TV shows released each year to see trends.
# 

# In[ ]:


import matplotlib.pyplot as plt

year_counts = df['release_year'].value_counts().sort_index()
year_counts.plot(kind='bar', figsize=(10, 5), title='TV Shows Released Over Time')
plt.xlabel('Year')
plt.ylabel('Number of TV Shows')
plt.show()


# ## **Calculating Mean IMDB Ratings for both Movies and Tv Shows**

# In[ ]:


# Write Your Code here


# ## **Analyzing Top Genres**

# In[ ]:


# Write Your Code here
genre_counts = df['Genres'].value_counts()
pd.DataFrame(genre_counts)


# In[ ]:


#Let's Visualize it using word cloud
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Split multiple genres into individual genres and flatten the list
genres_list = df['Genres'].str.split(',').explode().str.strip()

# Count the frequency of each genre
genre_counts = genres_list.value_counts()

# Generate Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(genre_counts)

# Display the Word Cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # No axes for the word cloud
plt.title('Genre Frequency Word Cloud')
plt.show()


# ## **Finding Predominant Streaming Service**

# In[ ]:


# Write Your Code here
Streaming_Services_counts = df['Streaming Platform'].value_counts()
pd.DataFrame(Streaming_Services_counts)


# In[ ]:


#Let's Visvalize it using word cloud
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Split multiple genres into individual genres and flatten the list
streaming_services = df['Streaming Platform'].str.split(',').explode().str.strip()

# Count the frequency of each genre
Streaming_Services_counts = df['Streaming Platform'].value_counts()

# Generate Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(Streaming_Services_counts)

# Display the Word Cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # No axes for the word cloud
plt.title('Predominant Streaming Service')
plt.show()


# ## **Task 3 :- Data Export**

# In[ ]:


#saving final dataframe as Final Data in csv format
import pandas as pd

df.to_csv("Final Data.csv", index=False)

print("Final Data has been saved as 'Final Data.csv'.")


# # **Dataset Drive Link (View Access with Anyone) -**
# **https://drive.google.com/file/d/1BRK09C6I6GX4OZXIlxeZpd3HcDHxs-vF/view?usp=sharing**

# # ***Congratulations!!! You have completed your Assignment.***
