import logging
import threading
import Input
import Output
import Processing
import FrameManager



logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )


fm = FrameManager.FrameManager()
Input.setFrameManager(fm)
Processing.setFrameManager(fm)
Output.setFrameManager(fm)


inp = threading.Thread(name='input', target=Input.run_thread)
out = threading.Thread(name='output', target=Output.run_thread)
pro = threading.Thread(name='processing', target=Processing.run_thread)


logging.debug('Starting processing thread')
pro.start()

logging.debug('Starting output thread')
out.start()

logging.debug('Starting input thread')
inp.start()

