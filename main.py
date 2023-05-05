# Python File that combines both Fetch_Song & Recommend_Song as well as logic behind system
#NOTE: Please have the following install before running! By doing !pip install (library)
#Libraries : Pandas, Spotipy, fastai

# Imports
import json
import os
import random
import string
import urllib.parse

import warnings
warnings.filterwarnings('ignore')
import requests

from fastai.collab import *
from fastai.tabular import *
import pandas as pd
import numpy as np
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.oauth2 as oauth2

import sqlite3
from database import db_operations

db_ops = db_operations("SongData.db")

class Backend:

    def __init__(self):
        CLIENT_ID = '3e1c953202b147d48f28a70a6a9b7056'
        CLIENT_SECRET = '1228a2599ef3415da3f1c0e0c6d471fc'
        username = 'k4fai1h3qbcgjz45ljtae8vmg'
        market = ['US']
        redirect_uri='http://localhost:8080/callback/'


        client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
        self.sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

    # Function to take a share link from the user and return a list for the system to use
    def GetSongInfo(self):
        track_link = self.ReadSong()

        track_URI = track_link.split("/")[-1].split("?")[0] #Also known as the Song ID

        track_info = self.sp.track(track_URI) #Creates a list of All of the Song Information
        name = track_info['name'] 
        artist = track_info['album']['artists'][0]['name']

        track_audio = self.sp.audio_features(track_URI)[0]

        song_id = track_audio["id"]
        danceability = str(track_audio["danceability"])
        energy = str(track_audio["energy"])
        key = str(track_audio["key"])
        loudness = str(track_audio["loudness"])
        mode = str(track_audio["mode"])
        speechiness = str(track_audio["speechiness"])
        acousticness = str(track_audio["acousticness"])
        liveness = str(track_audio['liveness'])
        valence = str(track_audio['valence'])
        tempo = str(track_audio['tempo'])
        Instrumentalness = str(track_audio['instrumentalness'])

        name = name.replace('\'', 'º')
        artist = artist.replace('\'', 'º')

        song_info = [track_link, name, artist, song_id, danceability, energy, loudness, speechiness, acousticness, liveness, valence, tempo, Instrumentalness, key, mode]
        return song_info

    #Function to take a Song (as a list of info) and insert into the SongData.db file
    def insertSong(self, song):

        track_link = song[0]
        name = song[1]
        artist = song[2]
        song_id = song[3]
        danceability = song[4]
        energy = song[5]
        loudness = song[6]
        speechiness = song[7]
        acousticness = song[8]
        liveness = song[9]
        valence = song[10]
        tempo = song[11]
        Instrumentalness = song[12]
        key = song[13]
        mode = song[14]

        query = '''
        SELECT *
        FROM Song_Data
        WHERE SongID = \''''+song_id+"\';"

        test = db_ops.execute_one(query)

        if not test:
            query = "INSERT INTO Song_Data VALUES(\'"+song_id+"\', \'"+name+"\', \'"+artist+"\', "+danceability+", "+energy+","+key+","+loudness+","+mode+","+speechiness+","+acousticness+","+Instrumentalness+","+liveness+","+valence+","+tempo+",\'"+track_link+"\');"
            db_ops.execute_one(query)

    # Function that takes a song and then recommends a list of 5 songs to the user based off of the input song's audio features
    def RecommendSongs(self, song):
        query_value = 0.05

        #query based off of curr feature and value

        danceability = float(song[4])
        energy = float(song[5])
        speechiness = float(song[7])
        acousticness = float(song[8])
        liveness = float(song[9])
        valence = float(song[10])
        Instrumentalness = float(song[12])

        while 1:

            energy_featL = str(energy - query_value)
            energy_featH = str(energy + query_value)

            danceability_featL = str(danceability - query_value)
            danceability_featH = str(danceability + query_value)

            speechiness_featL = str(speechiness - query_value)
            speechiness_featH = str(speechiness + query_value)

            acousticness_featL = str(acousticness - query_value)
            acousticness_featH = str(acousticness + query_value)

            valence_featL = str(valence - query_value)
            valence_featH = str(valence + query_value)

            Instrumentalness_featL = str(Instrumentalness - query_value)
            Instrumentalness_featH = str(Instrumentalness + query_value)

            query = '''
            SELECT SongID
            FROM Song_Data
            WHERE Energy >='''+energy_featL+" AND Energy<="+energy_featH+" AND Danceability >="+danceability_featL+" AND Danceability <="+danceability_featH+'''
            AND Speechiness >='''+speechiness_featL+" AND Speechiness <="+speechiness_featH+" AND Acousticness >="+acousticness_featL+" AND Acousticness <="+acousticness_featH+'''
            AND Valence >='''+valence_featL+" AND Valence <="+valence_featH+" AND Instrumentalness >="+Instrumentalness_featL+" AND Instrumentalness <="+Instrumentalness_featH+" LIMIT 6;"
            #set curr to query
            curr = db_ops.execute_one(query)

            if len(curr) == 6:
                break
            elif len(curr) < 6:
                query_value +=0.01
        
        songID = song[3]

        i = 0
        while 1:
            songstr = str(curr[i])
            songstr = songstr.replace('(', '')
            songstr = songstr.replace(')', '')
            songstr = songstr.replace(',', '')
            songstr = songstr.replace('\'', '')
            if songstr == songID:
                del curr[i]
                break
            i+=1
            if i == 6:
                del curr[5]
                break

        return(curr)

    #Function that returns a list of 5 random songs to recommend
    def RecommendRandomly(self):
    #Query for 5 Rand Songs
        query = '''
        SELECT Name, Artist
        FROM Song_Data
        ORDER BY random()
        limit 5; '''
        rand = db_ops.execute_one(query)
        return rand
        #Return Songs

    def Menu(self):

        if(option == "1"): #Option to Insert into DB
            song = GetSongInfo()
            insertSong(song)
            print("Song has been added to DB")
        elif(option == "2"):
            song = GetSongInfo()
            recommendation = Recommend_Song(song)
            for i in range(len(recommendation)):
                print(recommendation[i])
            Rand_recommendation = RecommendRandomly()
            for i in range(len(Rand_recommendation)):
                print(Rand_recommendation[i])
            insertSong(song)
            #Print out all of the artist and name of song to the interface  

    def ReadSong(self):
        with open("frontend/user_input.txt", "r") as f:
            file_content = f.read()
            return file_content

    def WriteOutput(self, songIds):

        for i in range(5):
            songstr = str(songIds[i])
            songstr = songstr.replace('(', '')
            songstr = songstr.replace(')', ' ')
            songstr = songstr.replace(',', '')

            query = '''
            SELECT Name, Artist
            FROM Song_Data
            Where SongID = '''+songstr+''';
            '''
            songIds[i] = db_ops.execute_one(query)
        
        rand = self.RecommendRandomly()
        r = 5
        i = 0
        while 1:
            songIds.append(rand[i])
            i+=1
            r+=1
            if i == 5:
                break

        for i in range(10):
            song = str(songIds[i])
            song = song.replace('[', '')
            song = song.replace(']', '')
            song = song.replace('\'', '')
            song = song.replace('º', '\'')
            song = song[1:-1]
            songIds[i] = song

        with open('frontend/output.txt', 'w') as f:
            f.write("Recommended Songs:\n")
            f.write(songIds[0])
            f.write('\n')
            f.write(songIds[1])
            f.write('\n')
            f.write(songIds[2])
            f.write('\n')
            f.write(songIds[3])
            f.write('\n')
            f.write(songIds[4])
            f.write('\n')
            f.write("Random Recomendations:\n")
            f.write(songIds[5])
            f.write('\n')
            f.write(songIds[6])
            f.write('\n')
            f.write(songIds[7])
            f.write('\n')
            f.write(songIds[8])
            f.write('\n')
            f.write(songIds[9])
            f.close()

    def main(self):
        song = self.GetSongInfo()
        self.insertSong(song)
        songList = self.RecommendSongs(song)
        self.WriteOutput(songList)