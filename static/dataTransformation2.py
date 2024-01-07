import numpy as np
#from IPython.display import display
import json
import csv

# variables
csv_file = csv.writer(open('/workspaces/data-analysis/static/csvfile.csv', 'w'))
track_header_list = []
artist_header_list = []
artist_row_list = []
album_header_list = []
header = 0  # variable to validate header concatenation

# json file reading
with open('/workspaces/data-analysis/static/taylor_swift_spotify.json', 'r') as json_file:
    json_data = json.load(json_file)

# iteration of data
# artist dictionary
for artist_key, artist_value in json_data.items():
    
    if artist_key == 'albums':    
        # print('Amount of albums: ', len(artist_value))   

        # List
        for album in artist_value:  

            album_row_list = []  

            # album dictionary           
            for album_key, album_value in album.items():

                if album_key == 'tracks':                       
                    # print('Amount of tracks: ', len(album_value))                   

                    for track in album_value: 
                        
                        track_row_list = []

                        # track dictionary 
                        for track_key, track_value in track.items():

                            if track_key == 'audio_features': 
                                
                                audio_features_header_list = []
                                audio_features_row_list = []

                                # audio features dictionary 
                                for audio_key, audio_value in track_value.items():
                                    
                                    if header == 0:
                                        audio_features_header_list.append('audio_features.'+ audio_key)  
                                        
                                    audio_features_row_list.append('' if audio_value is None else audio_value)                                                      
                                    # print(track_value['energy'])

                            else:

                                if header == 0:
                                    track_header_list.append(track_key)

                                track_row_list.append('' if track_value is None else track_value)  

                        if header == 0:
                            csv_file.writerow(track_header_list + audio_features_header_list + artist_header_list + album_header_list)

                        csv_file.writerow(track_row_list + audio_features_row_list + artist_row_list + album_row_list)
                        header = 1 

                else: 

                    if header == 0:
                        album_header_list.append(album_key) 

                    album_row_list.append('' if album_value is None else album_value) 
                    # print('album_total_tracks: ', album_value)

    else:

        if header == 0:
            artist_header_list.append(artist_key) 

        artist_row_list.append('' if artist_value is None else artist_value)         
        # print(artist_value)
