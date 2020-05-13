"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
if __name__ == '__main__':
	count=0
	li= set()
	for text in texts:
		li.add(text[0])
		li.add(text[1])

	for call in calls:
		li.add(call[0])
		li.add(call[1])

	count=len(li)
	print("There are " +str(count)+" different telephone numbers in the records.")
	# print(count)
