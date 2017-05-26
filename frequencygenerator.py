import pyaudio
import wave
import math
import matplotlib.pyplot as plt
import numpy
 
AMP = 100
FORMAT = pyaudio.paInt16
CHANNELS = 1
F0 = 44100
FREQ = 431
WAVE_OUTPUT_FILENAME = "freq.wav"
 
audio = pyaudio.PyAudio()
 
# generate waveform
frames = []
for i in range(FREQ*1000):
	frames.append(str(int(AMP*(math.cos(2*math.pi*FREQ/F0*i)+1) + AMP/2)))
 
# save wav
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(F0)
waveFile.writeframes(b''.join(frames))
waveFile.close()


# plot
plt.plot(frames[:2000])
#plt.show()
dft = numpy.fft.fft(frames[:2000])
plt.plot(dft)
#plt.show()
