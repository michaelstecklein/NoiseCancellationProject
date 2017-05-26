import pyaudio
import matplotlib.pyplot as plt
import numpy as np
 
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"
 
audio = pyaudio.PyAudio()
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print "recording..."
frames = []
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print "finished recording"


# convert
numpydata = np.fromstring(data, dtype=np.int16)

# compare data types
if len(data) == 2*len(numpydata):
	for i in range(len(numpydata)):
		print "{} {}    {}".format(data[2*i],data[2*i+1],numpydata[i])
 
# plot
plt.plot(numpydata)
plt.show()
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
 
