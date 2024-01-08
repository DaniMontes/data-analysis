#from IPython.display import display
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# exploring data

# csv file reading
df = pd.read_csv('/workspaces/data-analysis/static/csv_file.csv')

# identifying columns
print(df.head())

# columns description
print(df.info())

# summary statistics
print(df.describe())

# checking artist 
print(df['artist_name'].value_counts())

# checking album names
print(df['album_name'].value_counts())

# identifying album without name
df_album_name = df[df['album_name']==""]
print(df_album_name)

# identifying album name with null value
df_album_name = df[df['album_name'].isnull()]
print(df_album_name)

# checking the number of tracks per album
df_group = df.groupby(['album_name','album_total_tracks'])['track_name'].count()
print(df_group)

drop_duplicate = df.drop_duplicates()
print(drop_duplicate.shape)
print(drop_duplicate.count())
print('--------------------')
print(df.shape)
print(df.count())

"""
dict_tables = {"tables": [table1],
                "titles": ['', 'CSV content'],
                }
"""

