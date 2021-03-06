import numpy as np
import threading



NUMFRAMES = 3
FRAMESIZE = 1024


class Frame():

	WRITABLE = 1
	PROCESSABLE = 2
	READABLE = 3

	def __init__(self, i):
		self.id = i
		self.data = np.zeros((FRAMESIZE,), dtype=np.int)
		self.state = Frame.WRITABLE
		self.lock = threading.Lock()

	def __str__(self):
		return "<Frame  id: %i  state: %i  data len: %i>" % (self.id, self.state, len(self.data))



class FrameManager():

	def __init__(self):
		self.__frames = []
		for i in range(NUMFRAMES):
			frame = Frame(i)
			self.__frames.append(frame)

	def printFrames(self):
		for f in self.__frames:
			print f


	def getFrameToWrite(self):
		""" Returns a frame if one is available to write into, else None """
		for frame in self.__frames:
			if not frame.lock.locked() and frame.state == Frame.WRITABLE:
				frame.lock.acquire()
				return frame

	def markFrameWritten(self, frame):
		""" Marks the frame as needing to be processed """
		frame.state = Frame.PROCESSABLE
		frame.lock.release()


	def getFrameToProcess(self):
		""" Returns a frame if one is available to process, else None """
		for frame in self.__frames:
			if not frame.lock.locked() and frame.state == Frame.PROCESSABLE:
				frame.lock.acquire()
				return frame

	def markFrameProcessed(self, frame):
		""" Marks the frame as available to be read """
		frame.state = Frame.READABLE
		frame.lock.release()


	def getFrameToRead(self):
		""" Returns a frame if one is available to read from, else None """
		for frame in self.__frames:
			if not frame.lock.locked() and frame.state == Frame.READABLE:
				frame.lock.acquire()
				return frame

	def markFrameRead(self, frame):
		""" Marks the frame as available to be written """
		frame.state = Frame.WRITABLE
		frame.lock.release()


