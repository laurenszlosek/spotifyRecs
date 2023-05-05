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

# Function to take a share link from the user and return a list for the system to use
def GetSongInfo():
    track_link = ReadSong()

    track_URI = track_link.split("/")[-1].split("?")[0] #Also known as the Song ID

    track_info = sp.track(track_URI) #Creates a list of All of the Song Information
    name = track_info['name'] 
    artist = track_info['album']['artists'][0]['name']

    track_audio = sp.audio_features(track_URI)[0]

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
def insertSong(song):

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
    else:
        print("song already in db")

# Function that takes a song and then recommends a list of 5 songs to the user based off of the input song's audio features
def RecommendSongs(song):
    query_value = 0.05

    #query based off of curr feature and value

    danceability = song[4]
    energy = song[5]
    speechiness = song[7]
    acousticness = song[8]
    liveness = song[9]
    valence = song[10]
    Instrumentalness = song[12]

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
        SELECT Name
        FROM Song_Data
        WHERE Energy >='''+energy_featL+" AND Energy<="+energy_featH+" AND Danceability >="+danceability_featL+" AND Danceability <="+danceability_featH+'''
        AND Speechiness >='''+speechiness_featL+" AND Speechiness <="+speechiness_featH+" AND Acousticness >="+acousticness_featL+" AND Acousticness <="+acousticness_featH+'''
        AND Valence >='''+valence_featL+" AND Valence <="+valence_featH+" AND Instrumentalness >="+Instrumentalness_featL+" AND Instrumentalness <="+Instrumentalness_featH+" LIMIT 6;"
        #set curr to query
        curr = db_ops.execute_one(query)
        print(curr)

        if len(curr) == 6:
            break
        elif len(curr) < 6:
            query_value +=0.01

    return(curr)

#Function that returns a list of 5 random songs to recommend
def RecommendRandomly()
  #Query for 5 Rand Songs
  query = '''
  SELECT Name, Artist
  FROM Song_Data
  ORDER BY random()
  limit 5; '''
  rand = db_ops.execute_one(query)
  #Return Songs

def Menu():

    if(option == "1"): #Option to Insert into DB
        song = GetSongInfo()
        insertSong(song)
        print("Song has been added to DB")
    elif(option == "2"):
        song = GetSongInfo()
        recommendation = Recommend_Song(song)
        for i in range(len(recommendation))
            print(recommendation[i])
        Rand_recommendation = RecommendRandomly()
        for i in range(len(Rand_recommendation))
            print(Rand_recommendation[i])
        insertSong(song)
        #Print out all of the artist and name of song to the interface  

def ReadSong():
    with open("frontend/user_input.txt", "r") as f:
        file_content = f.read()
        return file_content

def WriteOutput(songIds):
    SongList[]
    int i = 0

    for i in 4:
        query = '''
        SELECT Name, Artist
        FROM Song_Data
        Where SongID = \''''+songIds[0]+'''\';
        '''
        SongList[i] = db_ops.execute_one(query)

Menu()