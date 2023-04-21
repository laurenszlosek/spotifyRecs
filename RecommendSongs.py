def recommendSong(songs): #returns a list of song ID's to be presented to User  
  #set query values
  query_value = 0.10
  song_feat = 0
  features = ["energy","danceability","valence","loudness","tempo","instrumentals","speechiness","acousticness"]
  curr_list = []
  prev_list = []

  #run initial query based off Energy

  #enters while loop (list is not equal to 5)
  while(len(curr) != 5):

    #query based off of curr feature and value
    #set curr to query

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

  #Add 5 random songs onto curr
  #return CURR
  return curr

def main(): #main function to run the Recommendation Algorithm
  input_song = [] #list of song's information
  recommendations = recommendSong(input_song)

  