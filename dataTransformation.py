#from IPython.display import display
import pandas as pd
import json

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def fileTransform(file_path): 

    # json file reading
    with open(file_path, encoding='utf-8') as file:
        data = json.loads(file.read())

    # converting JSON data to a dataframe
    df = pd.json_normalize(data, 
                        record_path=['albums', 'tracks'], 
                        meta=['artist_id','artist_name','artist_popularity',['albums','album_id'],['albums', 'album_name'],['albums','album_release_date'],['albums','album_total_tracks']],
                        errors='ignore')

    # renaming album columns
    df.columns = df.columns.str.replace(r'album.*\.', '', regex=True)

    # print(df.head())

    # converting dataframe to csv file
    df.to_csv('/workspaces/data-analysis/static/csv_file.csv', sep=',', index=False, encoding='utf-8')

    return 'CSV file generated successful! (' + '/workspaces/data-analysis/static/' + ')'
