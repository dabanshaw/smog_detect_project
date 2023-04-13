from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
from UI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtWidgets import QLabel

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        self.O_icon = QLabel("")
        self.O_icon.setPixmap(QPixmap("O.jpg"))
        self.X_icon = QLabel("")
        self.X_icon.setPixmap(QPixmap("X.jpg"))
        self.cnt = 0
        # self.table = [[0]*3 for i in range(3)]
        self.start = False
        self.row_dic = {1:0, 2:0}
        self.col_dic = {1:0, 2:0}
        self.tilt_dic = {1:0, 2:0}
        self.result = []

    def setup_control(self):
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.ui.tableWidget.cellClicked().connect(self.handleCellClicked) #記得這個
        self.ui.tableWidget.cellClicked.connect(self.handleCellClicked)    
        self.ui.start_button.clicked.connect(self.start_fun)
        self.ui.restart_button.setText("Restart")
        self.ui.restart_button.clicked.connect(self.restart)
        
            # self.ui.tableWidget.setHorizontalHeaderLabels()
    def start_fun(self):
        self.start = True
        self.table = [[0 for _ in range(3)] for _ in range(3)]
        self.row_dic = [{1:0, 2:0} for _ in range(3)]
        self.col_dic = [{1:0, 2:0} for _ in range(3)]
        self.til1_dic = {1:0, 2:0}
        self.til2_dic = {1:0, 2:0}
        self.ui.start_button.setText("game\nstart")

    def handleCellClicked(self, row, col):
        if self.start:
            self.check = self.ui.tableWidget.cellWidget(row, col)
            if not self.check:
                self.cnt += 1
                self.draw(row, col, self.cnt)
                self.fill(row, col, self.cnt)
                # print(row, col)
            else:
                print(row, col, "checked")
        

    def draw(self, row, col, cnt):
        # self.ui.tableWidget.setCellWidget(row, col, self.O_icon)
        self.icon_label = QLabel("")
        # self.check = self.ui.tableWidget.cellWidget(row, col)
        # if not self.check:
        if cnt % 2 == 1:
            self.icon_label.setPixmap(QPixmap("O.jpg"))
        else:
            self.icon_label.setPixmap(QPixmap("X.jpg"))
        self.ui.tableWidget.setCellWidget(row, col, self.icon_label)

    
    def fill(self, row, col, cnt):
        if cnt % 2 == 1:
            self.table[row][col] = 1
            self.row_dic[row][1] += 1
            self.col_dic[col][1] += 1
            if row == col: self.til1_dic[1] += 1
            if row == 2-col: self.til2_dic[1] += 1

            if self.row_dic[row][1] == 3: self.start = False; print("gameover")
            if self.col_dic[col][1] == 3: self.start = False; print("gameover")
            if self.til1_dic[1] == 3: self.start = False; print("gameover")
            if self.til2_dic[1] == 3: self.start = False; print("gameover")
        else:
            self.table[row][col] = 2 
            self.row_dic[row][2] += 1
            self.col_dic[col][2] += 1
            if row == col: self.til1_dic[2] += 1
            if row == 2-col: self.til2_dic[2] += 1

            if self.row_dic[row][2] == 3: self.start = False; print("gameover")
            if self.col_dic[col][2] == 3: self.start = False; print("gameover")
            if self.til1_dic[2] == 3: self.start = False; print("gameover")
            if self.til2_dic[2] == 3: self.start = False; print("gameover")
        
        print(self.til1_dic[1], self.til1_dic[2])



