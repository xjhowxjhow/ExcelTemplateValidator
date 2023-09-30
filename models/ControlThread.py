import typing
import PySide2.QtCore
from core import *




class ControlThread(QThreadPool):
    finished_all_thread = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # CONFIG POOL

        # timer = QTimer(self)
        # timer.timeout.connect(self.get_threadmonitor)
        # timer.start(2000)

        # self.setMaxThreadCount() #MAX THREADS IN POOL
        # self.setStackSize(100) #STACK SIZE
        # self.setMaxThreadCount(50) #MAX THREADS IN POOL
        #v 1.9
        self.setExpiryTimeout(30000)
        self.historical = []
        self.sys_thread = {"JOBS": []}
        self.allthreadisfinished = True
        self.counter_thread = 0

    def start_jobs_thread(self, QRunable):
        print('----------------SYS-CURRENT-THREADS--------------------')


        for i in QRunable:
            print(F'START THREAD: {i}')
            self.sys_thread['JOBS'].append({
                "ID_THREAD": str(i),
                "STATUS": 'RUNNING',
                "TIME": datetime.now(),
                "START_TIME": datetime.now(),
                "END_TIME": None
            })
            self.start(i, priority=QThread.NormalPriority)
        



    def finish_job_thread(self, id_thread):

        for item in self.sys_thread['JOBS']:
            if item['ID_THREAD'] == str(id_thread):
                item['STATUS'] = 'FINISHED'
                item['END_TIME'] = datetime.now()
                item['TIME'] = item['END_TIME'] - item['START_TIME']
                # historical
                self.historical.append(item)
                # remove thread
                self.sys_thread['JOBS'].remove(item)
        #         break

        self.counter_thread -= 1
        if self.counter_thread == 0:
            self.finished_all_thread.emit()


    

    def start_single_thread(self, QRunable):
        self.start(QRunable, priority=QThread.NormalPriority)


    def get_threadmonitor(self):
        print(F'Active Threads: {self.activeThreadCount()}')
        print(F'Max Thread Count: {self.maxThreadCount()}')
        print('----------------SYS-CURRENT-THREADS--------------------')
        pprint(self.sys_thread)
        print('----------------SYS-HISTORICAL-THREADS--------------------')
        pprint(self.historical)
        return

    def ActivesThreads(self):
        return self.activeThreadCount()

    def MaxThreadCount(self):
        return self.maxThreadCount()

    def RestartPool(self):
        self.clear()
        return True
