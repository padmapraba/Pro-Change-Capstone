import twint
import csv

# Basic pull tweet command on a user, outputs to terminal
# will only pull a certain amount of tweets, have yet to determine how this is based
c = twint.Config()
c.Username = "Rihanna"
# can also use ".To" and ".All" to get tweets @ someone, or both tweets from and @ someone respectively

twint.run.Search(c) # executes the search

# Pull tweets based on a keyword, stores in a txt file
j = twint.Config()
j.Search = "global warming"
j.Output = "climate.txt"

twint.run.Search(j)

# Pull tweets since 02-22-2022, about global warming, and store them in a CSV
x = twint.Config()
x.Search = "global warming"
x.Since = "2022-02-22"
x.Output = "climateChange.csv"
x.Store_csv = True

twint.run.Search(x)

# All of these and many more can be combined to make an even more powerful search
# As of right now, comments to tweets can be pulled by storing in a CSV -> find the conversation_id -> 
#	and use the conversation_id to find the replied tweets