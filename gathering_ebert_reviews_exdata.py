import glob
import pandas as pd

# List of dictionaries to build file by file and later convert to a DataFrame
df_list = []
for ebert_review in glob.glob('ebert_reviews/*.txt'):
    with open(ebert_review, encoding='utf-8') as file:
        title = file.readline()[:-1]
        # Your code here
        review_url = file.readline()[:-1]
        review_text = file.read()
        # Append to list of dictionaries
        df_list.append({'title': title,
                        'review_url': review_url,
                        'review_text': review_text})
df = pd.DataFrame(df_list, columns = ['title', 'review_url', 'review_text'])
