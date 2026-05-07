


# operator	operation	    example	    asks
# not	    negation	    not x	    is x not True?
# and	    conjunction	    x and y	    are all of x and y True?
# or	    disjunction	    x or y	    are any of x or y True?

# The variable x contains 5 and the variable color contains "yellow".
# Which of the following expressions evaluates to True?

"""
A. x < 4 and color != "blue"            
B. x == 6 and color != "yellow"     
C. x > 3 and color == "yellow"      
D. x != 7 and color == "blue"
"""

# The variable people_seated contains 15 and the variable status contains "open".
# Which of the following expressions evaluates to False?

"""
A. people_seated < 12 or status != "open"          
B. people_seated == 15 or status == "closed"        
C. people_seated >= 16 or status != "closed"        
D. people_seated > 13 or status == "open"           
"""


genre = "lo-fi"
bpm = 136

# Match target running pace to the beats per minute.
is_running_song = bpm >= 150 and bpm <= 180 # false
print("Are the beats per minute between 150 and 180? " + str(is_running_song))

# Count alternative spellings of lo-fi as a single genre. 
is_lo_fi = genre == "lo-fi" or genre == "low-fi" or genre == "lofi" #True
print("Is the genre any of the spellings of lo-fi? " + str(is_lo_fi))

# Chill background tunes help maintain focus.
is_study_song = is_lo_fi and bpm < 100 #True and False = False
print(is_study_song)
if is_study_song:   #if False
    print("This slow, lo-fi song is perfect for studying!")

# Don't play activity-specific songs at other times of the day.
if not is_study_song and not is_running_song: #True and True    if True
    print("This is not one of my study or running songs.")
