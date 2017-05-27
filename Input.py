import pyaudio
import logging
import time
import FrameManager as FM




RATE = 44100
FRAMESIZE = FM.FRAMESIZE
FORMAT = pyaudio.paInt16
CHANNELS = 1


def __collect_frame(frame):
	frame.data = stream.read(FRAMESIZE)



def setFrameManager(fm):
	global __FM
	__FM = fm


def run_thread():
	audio = pyaudio.PyAudio()
	global stream
	stream = audio.open(format=FORMAT, channels=CHANNELS,
			rate=RATE, input=True,
			frames_per_buffer=FRAMESIZE)
	while True:
		frame = __FM.getFrameToWrite()
		if frame == None:
			logging.debug('Frame manager returned None for input frame')
		else:
			__collect_frame(frame)
			__FM.markFrameWritten(frame)
		time.sleep(0) # hand over rest of quantum
	stream.close()
	audio.terminate()

