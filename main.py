import sys
import os
import time
from threading import Thread
from PyQt6 import QtCore,QtGui,QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QThread,pyqtSignal
from ui1 import Ui_MainWindow

try:    

    class SleepTimer(QtWidgets.QMainWindow):
        def __init__(self):
            super(SleepTimer,self).__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.initUI()
            self.show()
            self.lable = self.ui.label_3
            self.prograssbar = self.ui.progressBar

        def initUI(self):
            self.timer = Timer(mainwindow=self)
            self.progress = progressbar(mainwindow=self)
            self.ui.pushButton.clicked.connect(self.start_timer)
            self.ui.pushButton_2.clicked.connect(self.stop_timer)
        

        def start_timer(self):
            hour = self.ui.lineEdit.text()
            minut = self.ui.lineEdit_2.text()
            if hour == '':
                hour = 0
            if minut == '':
                minut = 0
            self.time1 = (int(hour)*60*60)+(int(minut)*60)
            os.system('shutdown -s -t '+ str(self.time1)) 
            os.system('exit 0') 
            self.timer.time(self.time1)
            self.progress.time(self.time1)
            self.progress.start()
            self.timer.start()
        

        def stop_timer(self):
            os.system('shutdown -a')
            os.system('exit 0')
            self.ui.label_3.setText('Таймер остановлен')
            self.timer.terminate()
            self.progress.terminate()


#______________________________________________________________________________________ 

#отдельный класс для многопоточности
    class Timer(QThread):
   

        def __init__(self,mainwindow,parent = None):
            super(Timer,self).__init__()
            self.mainwindow = mainwindow

        def time(self,time):
            self.time1 = time




        def run(self):
            while self.time1:
                    m,s = divmod(self.time1, 60)
                    h,m = divmod(m,60)
                    time1_format = '{:02d}:{:02d}:{:02d}'.format(h, m,s)
                    self.mainwindow.lable.setText('Пк выключиться через ' + time1_format) 
                    QThread.sleep(1)
                    self.time1 -=1
                
            
#______________________________________________________________________________________   

    class progressbar(QThread):
        def __init__(self,mainwindow,parent = None):
            super(progressbar,self).__init__()
            self.mainwindow = mainwindow

        def time(self,s):
            self.seconds = s
    
        def run(self):
            value = 0
            while value < 100:
                value +=1
                self.mainwindow.prograssbar.setValue(value)
                QThread.msleep(int((self.seconds/100)*1000))



    app = QtWidgets.QApplication(sys.argv)
    application = target= SleepTimer()
    sys.exit(app.exec())

except Exception as e:
    print(e)
    pass