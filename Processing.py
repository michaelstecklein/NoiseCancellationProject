import time
import FrameManager
import Input





def __process_frame(frame):
	print "Processing frame"




def setFrameManager(fm):
	global __FM
	__FM = fm


def run_thread():
	while True:
		frame = __FM.getFrameToProcess()
		while frame != None: # process all available frames
			__process_frame(frame)
			__FM.markFrameProcessed(frame)
			frame = __FM.getFrameToProcess()
		time.sleep(0) # hand over rest of quantum

