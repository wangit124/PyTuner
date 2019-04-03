from scipy.io.wavfile import read
from scipy.fftpack import fft,fftfreq
import speech_recognition as sr
import getHertz as hz
import pyaudio
import time
from os import path

outFile = path.join(path.dirname(path.realpath(__file__)), "wavData/note.wav")

# this is called from the background thread
def callback(recognizer, audio):
	with open(outFile, "wb") as f:
		f.write(audio.get_wav_data())
	
	# Read data from wav file using scipy
	fs, data = read(outFile)

	# Get frequency values
	samples = data.shape[0]
	datafft = fft(data)
	fftabs = abs(datafft)
	freqs = fftfreq(samples, 1/fs)

	maxData = -1
	freqFlag = 0

	# Get dictionary of frequencies and find min, max
	freqDict = hz.listFreq()
	maxFreq = int(freqDict["e5 "] + 3)
	minFreq = int(freqDict["e2 "] - 3)
	subData = fftabs[minFreq:(maxFreq+1)]
	maxData = max(subData)

	# Get the frequency of the maximum data value
	for i in range(0, len(subData)):
		if subData[i] == maxData:
			freqFlag = i
			break

	# Define notes to search
	noteList = list(freqDict.keys())

	# Filter out duplicates
	for note in reversed(noteList):
		if "+" in note:
			noteList.remove(note)

	# Search keys determine match
	for index in range(0, len(noteList)-1):
		# Get low and high indexs/pitches
		lowNote = index
		highNote = index + 1
		lowPitch = int(freqDict[noteList[lowNote]])
		highPitch = int(freqDict[noteList[highNote]])

		# Find range of notes for this frequency
		if freqFlag == lowPitch:
			print(f'({noteList[lowNote]})={freqFlag}')
			break
		elif freqFlag == highPitch:
			print(f'({noteList[highNote]})={freqFlag}')
			break
		elif lowPitch < freqFlag < highPitch:
			halfWay = int((highPitch - lowPitch) * 0.5 + lowPitch)
			if freqFlag == halfWay:
				print(f'({noteList[lowNote]})={lowPitch} <- [to] -> ({noteList[highNote]})={highPitch}')
			elif freqFlag > halfWay:
				print(f'({noteList[lowNote]})={lowPitch} <- to [->] ({noteList[highNote]})={highPitch}')
			else:
				print(f'({noteList[lowNote]})={lowPitch} [<-] to -> ({noteList[highNote]})={highPitch}')
			break
		else:
			continue

# Calibrate once before recording
r = sr.Recognizer()
m = sr.Microphone()
with m as source:
	r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(m, callback)

#tune for 1000 seconds
for _ in range(100000000):
	time.sleep(0.00001)

stop_listening(wait_for_stop=False)
