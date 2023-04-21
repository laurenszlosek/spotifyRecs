import sqlite3
from database import db_operations

db_ops = db_operations("SongData.db")

def recommendSong(songs): #returns a list of song ID's to be presented to User  
  #set query values
  query_value = 0.10
  song_feat = 0
  features = ["energy","danceability","valence","loudness","tempo","instrumentals","speechiness","acousticness"]
  curr_list = []
  prev_list = []

  danceability = track_audio["danceability"]
  energy = track_audio["energy"]
  #loudness = str(track_audio["loudness"])
  speechiness = track_audio["speechiness"]
  acousticness = track_audio["acousticness"]
  valence = track_audio['valence']
  #tempo = str(track_audio['tempo'])
  Instrumentalness = track_audio['instrumentalness']

  #run initial query based off Energy

  #enters while loop (list is not equal to 5)
  while(len(curr) != 5):

    #query based off of curr feature and value
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
    AND Valence >='''+valence_featL+" AND Valence <="+valence_featH+" AND Instrumentalness >="+Instrumentalness_featL+" AND Instrumentalness <="+Instrumentalness_featH+";"
    #set curr to query
    curr = db_ops.execute_one(query)

    #if length equals 5 exactly
    if(len(curr) == 5): #CASE A. List is perfectly 5, break
      #break
      break

    #if length of curr is greater than 5
    if(len(curr) > 5): #CASE B List is greater than 5, set old to current version of list and then requery with next feature
      #update old to curr
      old is curr
      #move onto next song feature
      song_feat += 1
      #resets query value to 0.15 if changed
      query_value = 0.10
      #reset loop to query
      continue

    #if length of list is less than 5 & query value < 0.25.
    if( (len(curr) < 5) and (query_value < 0.25) ): #CASE C List is less than 5, resets curr to old version and requeries with higher query value
      #update curr to old list
      curr is old
      #increase query value by 0.03
      query_value += 0.03
      #reset loop to query with new value
      continue

    #if length of list is less than 5 & feature < 8
    if( (len(curr) < 5) and (song_feat < 8)): #CASE D List is less than 5, resets curr to old version and moves onto the next feature to try process again
      #update curr to old list
      curr is old
      #reset query value to 0.1
      query_value - 0.1
      #moves onto next feature
      song_feat += 1
      #reset loop to query with next feature
      continue
    
    #if length of list is less than 5.
    if(len(curr) < 5): #CASE E (worst case), resets to older version and takes the first 5 of older version
      #clears curr list
      curr.clear()
      #update curr to old list
      #pick first 5 songs in old list
      for i in range(0, 5):
        curr[i] = old[i]
      #break
      break

  #return CURR
  return curr

def main(): #main function to run the Recommendation Algorithm
  input_song = [] #list of song's information
  recommendations = recommendSong(input_song)

  