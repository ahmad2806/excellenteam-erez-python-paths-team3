# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainGuiFinal.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from gui import user_input_data
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainGui(object):
    def setupUi(self, MainGui):
        MainGui.setObjectName("MainGui")
        MainGui.resize(782, 600)
        MainGui.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainGui)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(440, 140, 119, 23))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(440, 200, 119, 23))
        self.radioButton_2.setObjectName("radioButton_2")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(160, 200, 118, 25))
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_2.setGeometry(QtCore.QRect(160, 260, 118, 25))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(160, 130, 121, 25))
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 60, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 60, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 200, 68, 19))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 260, 68, 19))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 130, 68, 19))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 490, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 490, 112, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 490, 112, 34))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 350, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 420, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(480, 260, 141, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(420, 260, 68, 19))
        self.label_7.setObjectName("label_7")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(620, 260, 32, 25))
        self.toolButton.setObjectName("toolButton")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(420, 320, 51, 31))
        self.label_8.setObjectName("label_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(480, 320, 141, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(620, 320, 32, 25))
        self.toolButton_2.setObjectName("toolButton_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(430, 360, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(430, 420, 221, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        MainGui.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainGui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 31))
        self.menubar.setObjectName("menubar")
        MainGui.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainGui)
        self.statusbar.setObjectName("statusbar")
        MainGui.setStatusBar(self.statusbar)

        self.retranslateUi(MainGui)
        QtCore.QMetaObject.connectSlotsByName(MainGui)


    def on_click1(self):
        print("Button ok pressed")
        box_number = self.lineEdit.text()
        start_time = self.timeEdit.text()
        end_time = self.timeEdit_2.text()
        single_path = self.radioButton.isChecked()
        all_path = self.radioButton_2.isChecked()
        print(f'the user insert boxes #: {box_number}')
        print(f'the user insert start time : {start_time} to {end_time}')
        print(f'the user press single path : {single_path}')
        print(f'the user press all paths : {all_path}')

        user_input_data.dic_user_input["command"]=""
        user_input_data.dic_user_input["filters"]=""
        user_input_data.dic_user_input["filters_args"]=""
        user_input_data.dic_user_input["mode"]=""


    def on_click2(self):
        print("\nButton reset pressed ")
        self.lineEdit.setText("")
        self.lineEdit_4.setText("")


    def retranslateUi(self, MainGui):
        _translate = QtCore.QCoreApplication.translate
        MainGui.setWindowTitle(_translate("MainGui", "MainWindow"))
        self.radioButton.setText(_translate("MainGui", "Single Path"))
        self.radioButton_2.setText(_translate("MainGui", "All Path\'s"))
        self.label.setText(_translate("MainGui", "Choose Time and Date :"))
        self.label_2.setText(_translate("MainGui", "Display Mode :"))
        self.label_3.setText(_translate("MainGui", "from:"))
        self.label_4.setText(_translate("MainGui", "to:"))
        self.label_5.setText(_translate("MainGui", "Date:"))
        self.pushButton.setText(_translate("MainGui", "Ok"))

        self.pushButton.clicked.connect(self.on_click1)        ###########on click listener

        self.pushButton_2.setText(_translate("MainGui", "Cancel"))
        self.pushButton_3.setText(_translate("MainGui", "Reset"))

        self.pushButton_3.clicked.connect(self.on_click2)

        self.label_6.setText(_translate("MainGui", "Enter Box# To Display :"))
        self.lineEdit.setPlaceholderText(_translate("MainGui", "1,2,3,...20"))
        self.label_7.setText(_translate("MainGui", "Photo :"))
        self.toolButton.setText(_translate("MainGui", "..."))
        self.label_8.setText(_translate("MainGui", "File :"))
        self.toolButton_2.setText(_translate("MainGui", "..."))
        self.label_9.setText(_translate("MainGui", "Enter Box Coordinate :"))
        self.lineEdit_4.setPlaceholderText(_translate("MainGui", "100,100,100,100"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainGui = QtWidgets.QMainWindow()
    ui = Ui_MainGui()
    ui.setupUi(MainGui)
    MainGui.show()
    sys.exit(app.exec_())

