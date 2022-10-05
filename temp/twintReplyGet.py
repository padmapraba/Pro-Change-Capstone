import twint 
import csv
import os
import shutil

#Configure the query
c = twint.Config()
c.Search = "global warming"

c.Since = "2018-03-02"
c.Output = "step1.csv"
c.Store_csv = True

twint.run.Search(c)


# Create a copy of the initial query file, to make sure the replies are being appended after
shutil.copyfile("step1.csv", "copyOfStep1.csv")

# STEP 2, open the csv, make a new query based off the first user in the list
#	and filter by the specific conversation ID
#	repeat until EOF

replyArray = []

with open('step1.csv') as f:
	csvRead = csv.reader(f, delimiter =',')
	line_count = 0
	for row in csvRead:
		if line_count == 0:
			header = row
			line_count += 1
		elif int(row[15]) > 0:
			# get replies
			username = row[7]
			convoID = row[1]
			c = twint.Config()
			c.To = username
			c.Output = "FD.csv"
			c.Since = "2018-03-02"
			c.Store_csv = True
			twint.run.Search(c)

			# all tweets to the user in FD.csv, filter by the conversation_id
			try:
				d = open('FD.csv')
			except:
				line_count += 1
			else:
				userCSVRead = csv.reader(d, delimiter = ',')
				for row in userCSVRead:
					if row[1] == convoID:
						replyArray.append(row)
				line_count += 1
				d.close()
				os.remove('FD.csv')

			# We have the replies saved in a local array for now
		else:
			line_count += 1

# Now we can append the replies to the end of this csv
with open('step1.csv', 'a') as f:
	writer = csv.writer(f)
	writer.writerow(header)
	for row in range(len(replyArray)):
		writer.writerow(replyArray[row])
