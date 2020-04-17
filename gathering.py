from bs4 import BeautifulSoup
import os
import pandas as pd

# List of dictionaries to build file by file and later convert to a DataFrame
df_list = []
folder = 'rt_html'
for movie_html in os.listdir(folder):
    with open(os.path.join(folder, movie_html)) as file:
        # Your code here
        # Note: a correct implementation may take ~15 seconds to run
        soup = BeautifulSoup(file, 'lxml')
        title = soup.title.text
        title = title[: -len(' - Rotten Tomatoes')]

        # title = soup.find('title').contents[0][:-len('- Rotten Tomatoes')]

        audience_score = soup.find('div', class_='audience-score meter').span.text[:-1]

        # audience_score = soup.find('div', class_= 'audience-score meter').find('span').contents[0][:-1]

        num_audience_ratings = soup.find('div', class_='audience-info hidden-xs superPageFontColor')
        num_audience_ratings=num_audience_ratings.find_all('div')[1].contents[2].strip().replace(',', '')


        # Append to list of dictionaries
        df_list.append({'title': title,
                        'audience_score': int(audience_score),
                        'number_of_audience_ratings': int(num_audience_ratings)})
df = pd.DataFrame(df_list, columns = ['title', 'audience_score', 'number_of_audience_ratings'])
