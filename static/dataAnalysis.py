import os
import numpy as np
import json

# get the current working directory
current_working_directory = os.getcwd()

with open('/workspaces/data-analysis/static/taylor_swift_spotify.json', "r") as json_file:
    json_data = json.load(json_file)

# Dictionary
for artist_key, artist_value in json_data.items():
    
    # List
    if artist_key == 'albums':    
        print('Amount of albums: ', len(artist_value))   

        for album in artist_value:                
            for album_key, album_value in album.items():

                if album_key == 'tracks':    
                    print('Amount of tracks: ', len(album_value))

                    for track in album_value:                
                        for track_key, track_value in track.items():

                            if track_key == 'audio_features': 
                                print(track_value['energy'])


                if album_key == 'album_total_tracks':
                    print('album_total_tracks: ', album_value)

    else:
        print(artist_value)
    

    
