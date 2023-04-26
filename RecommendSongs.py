import sqlite3
from database import db_operations

db_ops = db_operations("SongData.db")


def newRecommendation():
  query_value = 0.05

#query based off of curr feature and value

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

