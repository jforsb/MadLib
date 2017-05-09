# team: Jewel Chen, Jade Forsberg
# thanks to stackoverflow for documentation on the any() function
import random

# create dictionary
madlibdict = { }

# read in grammar file
f = open("limerick.txt", "r") 

# create dictionary from the grammar file
for line in f:
	if line != "\n":
		string = line.split("|")
		for word in string:
			if "::=" not in word:
				pass
			else:
				substring = word.split("::=")
				for subword in substring:
					strippedword = subword.strip()
					substring[substring.index(subword)] = strippedword
				string.remove(word) 
				string = substring + string
			madlibdict[string[0]] = string[1:]

story = madlibdict["<limerick>"]
for word in story:
	substory = word.split()
	location = story.index(word)
	story = story[:location] + substory + story[location:]
	story.remove(word)

while any(i in madlibdict.keys() for i in story) == True:
	# go through strings in list
	for word in story:
		# if the word is a key
		if word in madlibdict.keys():
			location = story.index(word)
			newvalue = random.choice(madlibdict[word]) # randomly choose a new word from values
			newwordlist = newvalue.split() 
			for newword in newwordlist:
				if newword == "EPSILON":
					newwordlist[newwordlist.index(newword)] = " "
			story = story[:location] + newwordlist + story[location:]
			story.remove(word)
		else: 
			# do nothing
			pass

stringstory = " ".join(story)

print (" ".join(stringstory.split()))