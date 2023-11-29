import threading
import ctypes
import time



class Stop_watch():
    def __init__(self):
        self.spand_time = 0
        
        watchingThread = threading.Thread(target=self.start_watching,daemon=False)
        watchingThread.start()
        self.p_id = watchingThread.native_id
        
    def start_watching(self):
        
        while True:
            time.sleep(1)
            self.spand_time += 1
    
    def close(self):
        ctypes.pythonapi.PyThreadState_SetAsyncExc(self.p_id,
              ctypes.py_object(SystemExit))



