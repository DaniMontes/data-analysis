import os
import numpy as np
import json
import csv

# get the current working directory
current_working_directory = os.getcwd()

csv_file = csv.writer(open('/workspaces/data-analysis/static/csvfile.csv', 'w'))
csv_header_list = []

artist_header_list = []
artist_row_list = []
album_header_list = []

header = 0

with open('/workspaces/data-analysis/static/taylor_swift_spotify.json', "r") as json_file:
    json_data = json.load(json_file)

# Dictionary
for artist_key, artist_value in json_data.items():

    # List
    if artist_key == 'albums':    
        # print('Amount of albums: ', len(artist_value))   

        for album in artist_value:  

            album_row_list = []  
                       
            for album_key, album_value in album.items():

                if album_key == 'tracks': 
                      
                    # print('Amount of tracks: ', len(album_value))
                   

                    for track in album_value: 
                        
                        csv_row_list = []

                        for track_key, track_value in track.items():

                            if track_key == 'audio_features': 
                                
                                audio_features_header_list = []
                                audio_features_row_list = []

                                for audio_key, audio_value in track_value.items():
                                    
                                    if header == 0:
                                        audio_features_header_list.append('audio_features.'+ audio_key)  
                                        
                                    audio_features_row_list.append(audio_value)                                                      
                                    # print(track_value['energy'])

                            else:

                                if header == 0:
                                    csv_header_list.append(track_key)

                                csv_row_list.append(track_value)  

                        #csv_header_list = csv_header_list + audio_features_header_list  
                        # csv_row_list = csv_row_list + audio_features_row_list + artist_row_list + album_row_list
                        if header == 0:
                            csv_file.writerow(csv_header_list + audio_features_header_list + artist_header_list + album_header_list)

                        csv_file.writerow(csv_row_list + audio_features_row_list + artist_row_list + album_row_list)
                        header = 1 

                else: #if album_key == 'album_total_tracks':

                    if header == 0:
                        album_header_list.append(album_key) 

                    album_row_list.append(album_value) 
                    # print('album_total_tracks: ', album_value)

    else:

        if header == 0:
            artist_header_list.append(artist_key) 

        artist_row_list.append(artist_value)         
        # print(artist_value)
    

# print(artist_header_list)
# print(album_header_list)

# csv_header_list = csv_header_list + artist_header_list + album_header_list


# print(csv_header_list)

# csv_file.writerow(csv_header_list)

    
