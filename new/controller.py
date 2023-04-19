from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
from UI import Ui_MainWindow
from video_controller import video_controller
from bug import Bug
from PyQt5.QtWidgets import QHeaderView
import time
from PyQt5.QtCore import Qt
from video_processing import start


class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.file_button.clicked.connect(self.open_file) 
           
        # for i in range(self.ui.tableWidget.rowCount()):
        #     for j in range(self.ui.tableWidget.columnCount()):
        #         self.ui.tableWidget.setItem(i, j, QTableWidgetItem(' '))

        # for i in range(self.ui.tableWidget.rowCount()):
        #     for j in range(self.ui.tableWidget.columnCount()):        
        #         item = self.ui.tableWidget.item(i, j)
        #         item.setTextAlignment(Qt.AlignCenter)

        self.ui.analyze_button.clicked.connect(self.video_process)  
        self.ui.analyze_button.clicked.connect(self.show_video)  
        # self.ui.save_button.clicked.connect(self.fill)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.listWidget.itemClicked.connect(self.bug)
        self.ui.listWidget.itemClicked.connect(self.fill)
        self.ui.link_button.clicked.connect(self.link)

    def open_file(self):
        self.filename, filetype = QFileDialog.getOpenFileName(self, "Open file Window", "./", "Video Files(*.mp4 *.avi)") # start path        
        # self.video_path = self.filename
        self.video_path = "result.mp4"  
        # self.video_path = "output.mp4" ### 這行影片會濃縮
        self.ui.file_button.setText("file\nuploaded")
        print(self.filename)

    def bug(self):
        self.obj = Bug()
        self.obj.start()
        self.ui.analyze_button.setText("finish")
    
    def link(self):
        self.web = Bug()
        self.web.open_web()

    def fill(self):
        # _translate = QtCore.QCoreApplication.translate
        cnt = 0
        try:
            for info in self.obj.vehicle:
                item = QtWidgets.QTableWidgetItem(self.obj.vehicle[info])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableWidget.setItem(0, cnt, item) 
                # info.setTextAlignment(QtCore.Qt.AlignCenter)   
                cnt += 1
        except:
            pass

    def video_process(self):
        start(self.filename)
        self.ui.analyze_button.setText("Analyzed\nfinished")
        self.ui.listWidget.addItem('L2U296')

        # print(vio)

    def show_video(self):
        try:
            self.video_controller = video_controller(video_path=self.video_path,
                                                    ui=self.ui)
            time.sleep(1)
            self.ui.play_button.clicked.connect(self.video_controller.play) # connect to function()
            self.ui.stop_button.clicked.connect(self.video_controller.stop)
            self.ui.cancel_button.clicked.connect(self.video_controller.pause)
            self.ui.label_path.setText(self.filename)
        except:
            pass
##########################################################
