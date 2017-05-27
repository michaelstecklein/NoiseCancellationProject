import time
import FrameManager





def __output_frame(frame):
	print "Outputing frame"




def setFrameManager(fm):
	global __FM
	__FM = fm


def run_thread():
	while True:
		frame = __FM.getFrameToRead()
		while frame != None: # output all available frames
			__output_frame(frame)
			__FM.markFrameRead(frame)
			frame = __FM.getFrameToRead()
		time.sleep(0) # hand over rest of quantum

