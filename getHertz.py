# Import math libraries 
import math as Math

# Calculate the distance between two notes
def getDist(noteA, noteB, noteDict):

	octaveDiff = int(noteA[1]) - int(noteB[1])
	
	noteDiff = noteDict[noteA[0]+noteA[2]] - noteDict[noteB[0]+noteB[2]] 

	return octaveDiff * 12 + noteDiff	

# Return the frequency of the given note using a4 as reference
def getFreq(note, noteDict):

	# Assign a4 as reference
	A4 = "a4 "
	freqA4 = 440
	A4_to_Note = getDist(note, A4, noteDict) / 12
	return round(freqA4 * Math.pow(2, A4_to_Note), 2)

# Define listFrequencies as function
def listFreq():
	noteDict = {
		"c " : 0,
		"c+" : 1,
		"d-" : 1,
		"d " : 2,
		"d+" : 3,
		"e-" : 3,
		"e " : 4,
		"f " : 5,
		"f+" : 6,
		"g-" : 6,
		"g " : 7,
		"g+" : 8,
		"a-" : 8,
		"a " : 9,
		"a+" : 10,
		"b-" : 10,
		"b " : 11
	}

	# Store a list of frequencies from c0 to B8 
	myHertz = {}

	for octave in range(0, 9):
		for key in noteDict.keys():
			currNote = str(key[0]) + str(octave) + str(key[1])
			currFreq = getFreq(currNote, noteDict)
			myHertz[currNote] = currFreq

	return myHertz

