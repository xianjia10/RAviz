# -*- coding: utf-8 -*-

import sys,random,os,subprocess,pickle,time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QTextEdit,QFileDialog,QMessageBox,QColorDialog,QTableWidgetItem,QScrollArea
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QEventLoop,QPoint,Qt
from reportlab.pdfgen import canvas
import random,time,shutil
from query_IDs import Ui_MainWindow_show_query
from reference_IDs import Ui_MainWindow_show_reference
from PyQt5.QtSvg import QSvgWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1067, 691)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setStyleSheet("background-color: #336699;")
        self.verticalLayout_2.addWidget(self.line_2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.tabWidget.setStyleSheet("font: 9pt \"Arial\";")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./source/color_picker.png"))
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setStyleSheet("font: 9pt \"Arial\";")
        self.pushButton_8.setFlat(True)#将按钮背景隐藏
        self.pushButton_8.setIconSize(QtCore.QSize(28,28))
        self.pushButton_8.clicked.connect(self.showcolorDialog)
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_3.setStyleSheet("font: 9pt \"Arial\";color:rgb(149, 149, 149)")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_4.setStyleSheet("font: 9pt \"Arial\";color:rgb(149, 149, 149)")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setStyleSheet("background-color: #336699;")
        self.verticalLayout_2.addWidget(self.line_3)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['query ID','length','start position','end position','+ or -',
        'reference ID','length','start position','end position','matching bases','mapping length','mapping quality'])
        self.horizontalLayout_12.addWidget(self.tableWidget)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        icon_instruction = QtGui.QIcon()
        icon_instruction.addPixmap(QtGui.QPixmap("./source/instruction.png"))
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setStyleSheet("font: 9pt \"Arial\";color:rgb(255, 0, 0)")
        self.verticalLayout_2.addWidget(self.label_17)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.plainTextEdit_9 = mytext()
        self.plainTextEdit_9.setParent(self.centralwidget)
        self.plainTextEdit_9.setMaximumSize(QtCore.QSize(16777215, 28))
        self.plainTextEdit_9.setStyleSheet("font: 9pt \"Arial\";color:rgb(149, 149, 149)")
        self.horizontalLayout_13.addWidget(self.plainTextEdit_9)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("color: #ffffff;\nbackground-color: #336699;\nfont: 9pt \"Arial\";\nfont: bold;")
        self.pushButton_2.clicked.connect(self.build_index)
        self.horizontalLayout_13.addWidget(self.pushButton_2)
        icon_openfile = QtGui.QIcon()
        icon_openfile.addPixmap(QtGui.QPixmap("./source/folder.png"))
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setIcon(icon_openfile)
        self.pushButton.setIconSize(QtCore.QSize(28,28))
        self.pushButton.setFlat(True)
        self.pushButton.setToolTip("open paf file")
        self.pushButton.clicked.connect(self.openfile1)
        self.horizontalLayout_13.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setIcon(icon_instruction)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setIconSize(QtCore.QSize(28,28))
        self.pushButton_4.setToolTip("about generating index file")
        self.pushButton_4.clicked.connect(self.aboutindex)
        self.horizontalLayout_13.addWidget(self.pushButton_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_20 = LoadingButton()
        self.pushButton_20.setStyleSheet("color: #ffffff;\nbackground-color: #336699;\nfont: 9pt \"Arial\";\nfont: bold;")
        self.pushButton_20.clicked.connect(self.exqueryid)
        self.horizontalLayout_9.addWidget(self.pushButton_20)
        self.pushButton_9 = LoadingButton()
        self.pushButton_9.setStyleSheet("color: #ffffff;\nbackground-color: #336699;\nfont: 9pt \"Arial\";\nfont: bold;")
        self.pushButton_9.clicked.connect(self.exreferenceid)
        self.horizontalLayout_9.addWidget(self.pushButton_9)
        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_11.setStyleSheet("font: 9pt \"Arial\";")
        self.horizontalLayout_10.addWidget(self.label_11)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit.setStyleSheet("font: 9pt \"Arial\";color:rgb(149, 149, 149)")
        self.horizontalLayout_10.addWidget(self.lineEdit)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_12.setStyleSheet("font: 9pt \"Arial\"")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_2.setStyleSheet("font: 9pt \"Arial\";color:rgb(149, 149, 149)")
        self.horizontalLayout_10.addWidget(self.lineEdit_2)
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setIcon(icon_instruction)
        self.pushButton_12.setFlat(True)
        self.pushButton_12.setIconSize(QtCore.QSize(28,28))
        self.pushButton_12.setToolTip("the mapping length and quality")
        self.pushButton_12.clicked.connect(self.mapping_quality)
        self.horizontalLayout_10.addWidget(self.pushButton_12)
        self.horizontalLayout_10.setStretch(1, 1)
        self.horizontalLayout_10.setStretch(3, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_5.setStyleSheet("font: 9pt \"Arial\";color:rgb(149, 149, 149)")
        self.horizontalLayout_8.addWidget(self.lineEdit_5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setStyleSheet("font: 9pt \"Arial\";color:rgb(255, 0, 0);\nfont: bold;")
        self.horizontalLayout_5.addWidget(self.label_19)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setStyleSheet("font: 9pt \"Arial\";")
        self.horizontalLayout_5.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setStyleSheet("font: 9pt \"Arial\";")
        self.horizontalLayout_5.addWidget(self.radioButton_2)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setStyleSheet("color: #ffe626;\nbackground-color: #336699;\nfont: 9pt \"Arial\";\nfont: bold;")
        self.pushButton_14.clicked.connect(self.drawbefore)
        self.horizontalLayout_15.addWidget(self.pushButton_14)
        self.pushButton_16 = LoadingButton()
        self.pushButton_16.setStyleSheet("color: #ffe626;\nbackground-color: #336699;\nfont: 9pt \"Arial\";\nfont: bold;")
        self.pushButton_16.clicked.connect(self.drawall)
        self.horizontalLayout_15.addWidget(self.pushButton_16)
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setStyleSheet("color: #ffe626;\nbackground-color: #336699;\nfont: 9pt \"Arial\";\nfont: bold;")
        self.pushButton_17.clicked.connect(self.detailsvg)
        self.horizontalLayout_15.addWidget(self.pushButton_17)
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setStyleSheet("color: #ffe626;\nbackground-color: #336699;\nfont: 9pt \"Arial\";\nfont: bold;")
        self.pushButton_15.clicked.connect(self.drawnext)
        self.horizontalLayout_15.addWidget(self.pushButton_15)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setStyleSheet("font: 9pt \"Arial\";color:rgb(255, 0, 0)")
        self.verticalLayout_2.addWidget(self.label_18)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.plainTextEdit_10 = mytext()
        self.plainTextEdit_10.setParent(self.centralwidget)
        self.plainTextEdit_10.setMaximumSize(QtCore.QSize(16777215, 28))
        self.plainTextEdit_10.setStyleSheet("font: 9pt \"Arial\";color:rgb(149, 149, 149)")
        self.horizontalLayout_14.addWidget(self.plainTextEdit_10)
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setStyleSheet("color: #ffffff;\nbackground-color: #336699;\nfont: 9pt \"Arial\";\nfont: bold;")
        self.pushButton_13.clicked.connect(self.build_indexuniq)
        self.horizontalLayout_14.addWidget(self.pushButton_13)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setIcon(icon_openfile)
        self.pushButton_6.setIconSize(QtCore.QSize(28,28))
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setToolTip("open kmer file")
        self.pushButton_6.clicked.connect(self.openfile2)
        self.horizontalLayout_14.addWidget(self.pushButton_6)
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setIcon(icon_instruction)
        self.pushButton_10.setFlat(True)
        self.pushButton_10.setIconSize(QtCore.QSize(28,28))
        self.pushButton_10.setToolTip("the format of kmer file")
        self.pushButton_10.clicked.connect(self.kmer_file)
        self.horizontalLayout_14.addWidget(self.pushButton_10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.pushButton_21 = LoadingButton()
        self.pushButton_21.setStyleSheet("color: #ffffff;\nbackground-color: #336699;\nfont: 9pt \"Arial\";\nfont: bold;")
        self.pushButton_21.clicked.connect(self.exqueryid2)
        self.horizontalLayout_17.addWidget(self.pushButton_21)
        self.pushButton_22 = LoadingButton()
        self.pushButton_22.setStyleSheet("color: #ffffff;\nbackground-color: #336699;\nfont: 9pt \"Arial\";\nfont: bold;")
        self.pushButton_22.clicked.connect(self.exreferenceid2)
        self.horizontalLayout_17.addWidget(self.pushButton_22)
        self.horizontalLayout_17.setStretch(0, 1)
        self.horizontalLayout_17.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_15.setStyleSheet("font: 9pt \"Arial\";")
        self.horizontalLayout_16.addWidget(self.label_15)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_7.setStyleSheet("font: 9pt \"Arial\";color:rgb(149, 149, 149)")
        self.horizontalLayout_16.addWidget(self.lineEdit_7)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_21.setStyleSheet("font: 9pt \"Arial\";")
        self.horizontalLayout_16.addWidget(self.label_21)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_9.setStyleSheet("font: 9pt \"Arial\";color:rgb(149, 149, 149)")
        self.horizontalLayout_16.addWidget(self.lineEdit_9)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_16.setStyleSheet("font: 9pt \"Arial\";")
        self.horizontalLayout_16.addWidget(self.label_16)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_8.setStyleSheet("font: 9pt \"Arial\";color:rgb(149, 149, 149)")
        self.horizontalLayout_16.addWidget(self.lineEdit_8)
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setIcon(icon_instruction)
        self.pushButton_11.setFlat(True)
        self.pushButton_11.setIconSize(QtCore.QSize(28,28))
        self.pushButton_11.setToolTip("the mean of alignment length")
        self.horizontalLayout_16.addWidget(self.pushButton_11)
        self.horizontalLayout_16.setStretch(1, 1)
        self.horizontalLayout_16.setStretch(3, 1)
        self.horizontalLayout_16.setStretch(5, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_6.setStyleSheet("font: 9pt \"Arial\";color:rgb(149, 149, 149)")
        self.horizontalLayout_11.addWidget(self.lineEdit_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setStyleSheet("font: 9pt \"Arial\";color:rgb(255, 0, 0);\nfont: bold;")
        self.horizontalLayout_7.addWidget(self.label_20)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setStyleSheet("font: 9pt \"Arial\";")
        self.horizontalLayout_7.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setStyleSheet("font: 9pt \"Arial\";")
        self.horizontalLayout_7.addWidget(self.radioButton_4)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_18 = LoadingButton()
        self.pushButton_18.setStyleSheet("color: #ffe626;\nbackground-color: #336699;\nfont: 9pt \"Arial\";\nfont: bold;")
        self.pushButton_18.clicked.connect(self.draw_before)
        self.horizontalLayout.addWidget(self.pushButton_18)
        self.pushButton_5 = LoadingButton()
        self.pushButton_5.setStyleSheet("color: #ffe626;\nbackground-color: #336699;\nfont: 9pt \"Arial\";\nfont: bold;")
        self.pushButton_5.clicked.connect(self.draw_part)
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_7 = LoadingButton()
        self.pushButton_7.setStyleSheet("color: #ffe626;\nbackground-color: #336699;\nfont: 9pt \"Arial\";\nfont: bold;")
        self.pushButton_7.clicked.connect(self.draw_all_alignment)
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.pushButton_19 = LoadingButton()
        self.pushButton_19.setStyleSheet("color: #ffe626;\nbackground-color: #336699;\nfont: 9pt \"Arial\";\nfont: bold;")
        self.pushButton_19.clicked.connect(self.draw_after)
        self.horizontalLayout.addWidget(self.pushButton_19)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1067, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RAviz"))
        icon=QIcon('./source/RAviz.ico')
        MainWindow.setWindowIcon(icon)
        self.label_21.setText(_translate("MainWindow", "KMAPQ>="))
        self.lineEdit_9.setPlaceholderText(_translate("MainWindow", "optional,default value is 50"))
        self.pushButton_8.setText(_translate("MainWindow", "color picker"))
        self.label_13.setText(_translate("MainWindow", "the alignment color:"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "e.g., #ff0000"))
        self.label_14.setText(_translate("MainWindow", "the unqkmer color:"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "e.g., #ff0000"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "line"))
        self.label_17.setText(_translate("MainWindow", "for paf file"))
        self.plainTextEdit_9.setPlaceholderText(_translate("MainWindow", "input the paf file"))
        self.pushButton_2.setText(_translate("MainWindow", "t->q"))
        self.label_11.setText(_translate("MainWindow", "alignment_length>="))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "optional, default value is 10000"))
        self.label_12.setText(_translate("MainWindow", "mapping_ quality>="))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "optional, default value is 60"))
        self.pushButton_14.setText(_translate("MainWindow", "before"))
        self.pushButton_16.setText(_translate("MainWindow", "draw"))
        self.pushButton_17.setText(_translate("MainWindow", "draw details based on the input ID"))
        self.pushButton_15.setText(_translate("MainWindow", "next"))
        self.label_18.setText(_translate("MainWindow", "for uniqkmer file"))
        self.plainTextEdit_10.setPlaceholderText(_translate("MainWindow", "uniqkmer file"))
        self.pushButton_5.setText(_translate("MainWindow", "show alignment-related part"))
        self.pushButton_7.setText(_translate("MainWindow", "show all alignments"))
        self.pushButton_18.setText(_translate("MainWindow", "before"))
        self.pushButton_19.setText(_translate("MainWindow", "next"))
        self.pushButton_13.setText(_translate("MainWindow", "t->q"))
        self.pushButton_20.setText(_translate("MainWindow", "show query ID"))
        self.pushButton_9.setText(_translate("MainWindow", "show reference ID"))
        self.pushButton_21.setText(_translate("MainWindow", "show query ID"))
        self.pushButton_22.setText(_translate("MainWindow", "show reference ID"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "input the interested ID"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "input the interested ID"))
        self.label_20.setText(_translate("MainWindow", "this is:"))
        self.radioButton_3.setText(_translate("MainWindow", "query ID"))
        self.radioButton_4.setText(_translate("MainWindow", "referencce ID"))
        self.label_19.setText(_translate("MainWindow", "this is:"))
        self.radioButton.setText(_translate("MainWindow", "query ID"))
        self.radioButton_2.setText(_translate("MainWindow", "referencce ID"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "optional, default value is 1000"))
        self.label_15.setText(_translate("MainWindow", "alignment_length>="))
        self.label_16.setText(_translate("MainWindow", "uniqkmer_number<="))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "optional,default value is 20"))


    global contentdir
    contentdir={}
    global number_index
    number_index=0
    global uniqker_dir
    uniqker_dir={}
    global current_number
    current_number=0
    global countmax
    countmax=0
    def openfile1(self):
        f, s = QFileDialog.getOpenFileName(self.centralwidget, "choose your file", "", "paf file(*.paf);;txt file(*.txt);;All Files (*)")
        if f!='':
            self.plainTextEdit_9.setPlainText(f)

    def openfile2(self):
        f, s = QFileDialog.getOpenFileName(self.centralwidget, "choose your file", "", "paf file(*.paf);;txt file(*.txt);;All Files (*)")
        if f!='':
            self.plainTextEdit_10.setPlainText(f)

    def kmer_file(self):
        QMessageBox.about(self.pushButton_10, 'the kmer-file format', 'The column ID and content:\n 1:query ID;\n2:query length;\n3:query start;\n4:query end;\n5:positive or negative strand;\n6:reference ID;\n7:reference length;\n8:reference start;\n9:reference end\n10:kmer position in query,kmer position in reference\nthe next was same to the ten column')

    def mapping_quality(self):
        QMessageBox.about(self.pushButton_12, 'help message', 'The format of input file should be the paf format.\n\nThe "mapping quality" means mapping quality, and it should be located in column 12 of paf file\
            \n\n"The default value is 60" means the mapping quality should  be greater than or equal to 60.\n\nThe "alignment length" means the number of matching bases, and it should be located in column 10 of paf file\
            \n\n"The default value is 0" means do not filter the alignment length.\n\nIf the input value is default value, you can choose to input the value or not')

    def segment_id(self):
        QMessageBox.about(self.pushButton_9, 'help message', 'Two classes of IDs are contained in the paf file: the first column is query ID, and the sixth column is target ID. Here, ID means query ID.\
            \n If you want to observe the related results of a interested target ID, the above function "t->q" can be used for autoswitching the positions between query and target ID.')

    def aboutindex(self):
        QMessageBox.about(self.pushButton_4, 'help message', 'if the size of the input file is more than 100 M, please press the button of "generate index" to generate the index file for drawing efficiently')

    def showcolorDialog(self):
        colors=QColorDialog()
        colors.setWindowIcon(QIcon('./source/RAviz.ico'))
        colors.getColor()

    def showwindow(self):
        newWindow = loginviewer()
        qe = QEventLoop()
        qe.exec_()

    def showallid_query(self,lists):
        newWindow = showids_query(lists)
        newWindow.show()
        qe = QEventLoop()
        qe.exec_()

    def showallid_reference(self,lists):
        newWindow = showids_reference(lists)
        newWindow.show()
        qe = QEventLoop()
        qe.exec_()

    def index_file(self,file):
        with open(file,"rb") as f:
            indexs={}
            index=f.tell()
            line=f.readline()
            count=0
            while line:
                if count%8000==0:
                    indexs[count]=index
                    index=f.tell()
                count+=1
                line=f.readline()
        with open(file+"_number.index","wb") as f:
            pickle.dump(indexs,f)

    def insertcontent(self,lists):
        self.tableWidget.clearContents()
        row_number=len(lists)
        column_number=max([len(line.split()) for line in lists])
        self.tableWidget.setRowCount(row_number)
        self.tableWidget.setColumnCount(column_number)
        for i,content in enumerate(lists):
            for j,infor in enumerate(content.split()):
                self.tableWidget.setItem(i,j, QTableWidgetItem(infor))

    def changeformat(self):
        try:
            file=self.plainTextEdit_9.toPlainText()
            lines=""
            with open(file) as f,open("./changeformat.paf","w") as f1:
                for line in f:
                    linelist=line.split()
                    if len(linelist)>=12:
                        list1=linelist[:4];list2=linelist[5:9]
                        linelist[:4]=list2;linelist[5:9]=list1
                        lines+="\t".join(linelist)+"\n"
                f1.write(lines)
            self.pushButton_2.setText("target <-> query")
        except Exception as e:
            QMessageBox.warning(self.pushButton_2, "Warning", str(e))

    def draw_pdf(self,file,index_path,number,alignment_quality,alignment_seqs,alignment_color):
        global contentdir
        if alignment_color=="":alignment_color="#dcdcdc"
        if index_path!="":
            with open(index_path,"rb") as f:
                indexs=pickle.load(f)
            with open(file) as f:
                start=int(number)*8000
                if start not in indexs:QMessageBox.about(self.pushButton_15, 'help message', 'you have drawn all results')
                f.seek(indexs[start])
                targetlist_index=[line for index,line in enumerate(f) if index<=8000]
        else:
            with open(file) as f:
                targetlist_index=f.readlines()
        r = lambda: random.randint(0,255)
        f=targetlist_index
        query_id_length={line.split()[0]:int(line.split()[1])*10**-6 for line in f if len(line.split())>=12 and int(line.split()[11])>=alignment_quality and int(line.split()[9])>alignment_seqs}
        query_color={i:"#%02X%02X%02X" % (r(),r(),r()) for i in query_id_length}#随机生成颜色
        target_id_length={line.split()[5]:int(line.split()[6])*10**-6 for line in f if len(line.split())>=12 and int(line.split()[11])>=alignment_quality and int(line.split()[9])>alignment_seqs}
        target_color={i:"#%02X%02X%02X" % (r(),r(),r()) for i in target_id_length}
        query_id={}
        for line in f:
            linelist=line.split()
            if len(linelist)>=12 and int(linelist[11])>=alignment_quality and int(linelist[9])>alignment_seqs:
                if linelist[0] not in query_id:
                    query_id[linelist[0]]=set()
                query_id[linelist[0]].add(linelist[5])
        n=0
        largelist=[]
        allinfor={}
        queryx=5
        ymax=0
        x_large=[]
        for query,qs in query_id.items():
            if n%10==0:queryx=5
            if len(qs)<=10:
                for index,i in enumerate(qs):
                    x1=queryx;x2=queryx+target_id_length[i];y1=y2=5+20*int(n/10)
                    allinfor[query+" "+i]=(x1,y1,x2,y2)#query id+target id后面的位置为target的位置
                    if index==0:
                        x3=x1;x4=queryx+query_id_length[query];y3=y4=ymax=y1+10
                        allinfor[query]=(x3,y3,x4,y4)#query id后面的位置为query的位置
                    queryx=x2+5
                    x_large.append(queryx)
            else:
                largelist.append(query)
            n+=1
        if largelist!=[]:
            for index,query in enumerate(largelist):
                n=index+1
                y1=y2=ymax+20*n
                queryx=5
                for index,target in enumerate(query_id[query]):
                    x1=queryx;x2=queryx+target_id_length[target]
                    allinfor[query+" "+target]=(x1,y1,x2,y2)
                    if index==0:
                        x3=x1;x4=queryx+query_id_length[query];y3=y4=y2+10
                        allinfor[query]=(x3,y3,x4,y4)
                    queryx=x2+5
                    x_large.append(queryx)
            x1,y1,x2,ymax=allinfor[largelist[-1]]
        xmax=max(x_large)
        name=time.strftime('%H%M%S',time.localtime(time.time()))
        filename="./pdfresult/myImagePDF"+name+".pdf"
        c = canvas.Canvas(filename,pagesize=(xmax,ymax+10))
        for line in f:
            if len(line.split())>=12:
                id1,length1,std1,ed1,dir,id2,length2,std2,ed2=line.split()[:9]
                name1=id1;name2=id1+" "+id2
                if name1 in allinfor and name2 in allinfor:
                    x1q,y1q,x2q,y2q=allinfor[name1];x1t,y1t,x2t,y2t=allinfor[name2]
                    x1=x1q+int(std1)*10**-6;y1=y1q;x2=x1t+int(std2)*10**-6;y2=y1t;x3=x1q+int(ed1)*10**-6;x4=x1t+int(ed2)*10**-6
                    c.setStrokeColor(alignment_color)
                    c.setLineWidth(0.01)
                    if dir=="+":
                        c.bezier(x1,y1,x1,(y1+y2)*0.5,x2,(y1+y2)*0.5,x2,y2)
                        c.bezier(x3,y1,x3,(y1+y2)*0.5,x4,(y1+y2)*0.5,x4,y2)
                    else:
                        c.bezier(x1,y1,x1,(y1+y2)*0.5,x4,(y1+y2)*0.5,x4,y2)
                        c.bezier(x3,y1,x3,(y1+y2)*0.5,x2,(y1+y2)*0.5,x2,y2)
        for ID,positions in allinfor.items():
            x1,y1,x2,y2=positions
            c.setLineWidth(0.5)
            if " " not in ID:
                c.setStrokeColor(query_color[ID])
                c.line(x1,y1,x2,y2)
                c.setFont("Times-Roman",1.5)#控制query id的大小
                # c.drawString((x1+x2)*0.5,y1+1,ID)
                c.drawCentredString((x1+x2)*0.5,y1+1,ID)
            else:
                targid=ID.split(" ")[1]
                c.setStrokeColor(target_color[targid])
                c.line(x1,y1,x2,y2)
                c.setFont("Times-Roman",1)#控制target id的大小
                c.drawCentredString((x1+x2)*0.5,y1-1.5,targid)
        c.setLineWidth(0.5)#标注比例尺
        c.setStrokeColor("#ff0000")
        x1=xmax-15;y1=y2=ymax;x2=x1+10
        c.line(x1,y1,x2,y2)
        c.setFont("Times-Roman",4)
        c.drawCentredString((x1+x2)*0.5,y1+3,"10 Mb")
        c.showPage()
        c.save()
        subprocess.Popen(['start',filename],shell=True)
            
    def drawall(self):
        global number_index
        file=self.plainTextEdit_9.toPlainText()
        file_size=os.path.getsize(file)
        if self.lineEdit.text()!="":alignment_seqs=int(self.lineEdit.text())
        else:alignment_seqs=0
        if self.lineEdit_2.text()!="":alignment_quality=int(self.lineEdit_2.text())
        else:alignment_quality=60
        alignment_color=self.lineEdit_3.text()
        if self.pushButton_16.isChecked:
            self.pushButton_16.setGif("./source/loading.gif")
            QtCore.QTimer.singleShot(10, self.pushButton_16.start)
            try:
                if file_size>10000000:
                    index_path=file+"_number.index"
                    number_index=0
                    if not os.path.exists(index_path):
                        self.pushButton_16.setText('generating the index file, just a moment...')
                        self.pushButton_16.repaint()
                        with open(file,"rb") as f:
                            indexs={}
                            index=f.tell()
                            line=f.readline()
                            count=0
                            while line:
                                QApplication.processEvents()
                                if count%8000==0:
                                    indexs[count]=index
                                    index=f.tell()
                                count+=1
                                line=f.readline()
                        with open(file+"_number.index","wb") as f:
                            pickle.dump(indexs,f)
                    self.pushButton_16.setText('drawing...')
                    self.pushButton_16.repaint()
                    self.draw_pdf(file,index_path,number_index,alignment_quality,alignment_seqs,alignment_color)
                else:
                    index_path=""
                    self.draw_pdf(file,index_path,number_index,alignment_quality,alignment_seqs,alignment_color)
                self.pushButton_16.setText("ok, finished")
                self.pushButton_16.repaint()
                time.sleep(1)
                self.pushButton_16.setText('draw')
                self.pushButton_16.repaint()
                QtCore.QTimer.singleShot(10, self.pushButton_16.stop)
            except Exception as e:
                QMessageBox.warning(self.pushButton_16, "Warning", str(e))

    def drawnext(self):
        global number_index
        file=self.plainTextEdit_9.toPlainText()
        if os.path.getsize(file)<=10000000:
            QMessageBox.about(self.pushButton_15, 'help message', 'the size of the input file is no more than 10 M, therefore, the "draw" button will draw all results')
        else:
            if self.lineEdit.text()!="":alignment_seqs=int(self.lineEdit.text())
            else:alignment_seqs=0
            if self.lineEdit_2.text()!="":alignment_quality=int(self.lineEdit_2.text())
            else:alignment_quality=60
            alignment_color=self.lineEdit_3.text()
            if self.pushButton_15.isChecked:
                try:
                    index_path=file+"_number.index"
                    number_index=number_index+1
                    if not os.path.exists(index_path):
                        self.pushButton_15.setText('generating the index file, just a moment...')
                        self.pushButton_15.repaint()
                        self.index_file(file)
                    self.pushButton_15.setText('drawing...')
                    self.pushButton_15.repaint()
                    self.draw_pdf(file,index_path,number_index,alignment_quality,alignment_seqs,alignment_color)
                    self.pushButton_15.setText("ok, finished")
                    self.pushButton_15.repaint()
                    time.sleep(1)
                    self.pushButton_15.setText('next')
                    self.pushButton_15.repaint()
                except Exception as e:
                    QMessageBox.warning(self.pushButton_15, "Warning", str(e))

    def drawbefore(self):
        global number_index
        file=self.plainTextEdit_9.toPlainText()
        if os.path.getsize(file)<=10000000:
            QMessageBox.about(self.pushButton_14, 'help message', 'the size of the input file is no more than 10 M, therefore, the "draw" button will draw all results')
        else:
            if self.lineEdit.text()!="":alignment_seqs=int(self.lineEdit.text())
            else:alignment_seqs=0
            if self.lineEdit_2.text()!="":alignment_quality=int(self.lineEdit_2.text())
            else:alignment_quality=60
            alignment_color=self.lineEdit_3.text()
            if self.pushButton_14.isChecked:
                try:
                    index_path=file+"_number.index"
                    number_index=abs(number_index-1)
                    if not os.path.exists(index_path):
                        self.pushButton_14.setText('generating the index file, just a moment...')
                        self.pushButton_14.repaint()
                        self.index_file(file)
                    self.pushButton_14.setText('drawing...')
                    self.pushButton_14.repaint()
                    self.draw_pdf(file,index_path,number_index,alignment_quality,alignment_seqs,alignment_color)
                    self.pushButton_14.setText("ok, finished")
                    self.pushButton_14.repaint()
                    time.sleep(1)
                    self.pushButton_14.setText('before')
                    self.pushButton_14.repaint()
                except Exception as e:
                    QMessageBox.warning(self.pushButton_14, "Warning", str(e))

    def drawdetail_list(self,idlist,alignment_color,hide_mark=0,chr_color=0):
        linelist=idlist
        if alignment_color=="":alignment_color="#e5e5e5"
        colorlista=["#8ecfc9","#ffbe7a","#fa7f6f","#82b0d2","#beb8dc","#2878b5","#9ac9db","#f8ac8c","#c82423","#ff8884","#14517c","#2f7fc1","#96c37d",
            "#f3d266","#d8383a","#a9b8c6","#c497b2","#8e8bfe","#fe99a2","#934b43","#d76364","#ef7a6d","#63e398","#b1ce46","#f1d77e","#9394e7","#5f97d2","#9dc3e7","#a1a9d0","#f0988c","#b883d3","#c4a5de",
            "#f6cae5","#96cccb"]
        xmax=query_length=int(linelist[0].split()[1])*10**-6
        query_ID=linelist[0].split()[0]
        query_color=random.choice(colorlista)
        id_length={}
        id_position={}
        mark_list=[]
        mark_listq=[]
        mark_line=[]
        mark_text=[]
        query_chr='    <path d="M {},{} h {}" stroke="{}"/>'
        target_chr='    <path d="M 5,{} h {}" stroke="segment-color"/>'
        text_chr='    <text x="{}" y="{}">{}</text>'
        line_mark='    <path d="M {},{} v {}"/>'
        bezier_line='    <path d="M {},{} C {},{} {},{} {},{} H {} C {},{} {},{} {},{}Z" />'
        bezier_line2='    <path d="M {},{} C {},{} {},{} {},{}" />'
        bezier_list=[]
        bezier_lists=[]
        chr_list=[]
        chr_text=[]
        startpo={}
        query_start={}
        for line in linelist:
            lineinfor=line.split()
            ID=lineinfor[5];length=int(lineinfor[6])*10**-6;stp=5+int(lineinfor[7])*10**-6
            id_length[ID]=length
            if ID not in startpo:
                startpo[ID]=[]
            startpo[ID].append(stp)
            if length>xmax:xmax=length
        ymax=len(id_length)*8+5
        for i,ID in enumerate(id_length):
            length=id_length[ID]
            tp=target_chr.format(10+8*i,length)#target的坐标,坐标跟在列表中的顺序是相关的
            id_position[ID]=10+8*i
            mark_list.append((11+8*i,5+length))
            chr_list.append(tp)
            if length<0.2:tt=text_chr.format((10+length)*0.5,11.7+8*i,ID)
            else:tt=text_chr.format((10+length)*0.5,12.3+8*i,ID)
            chr_text.append(tt)
        #标注marker
        for i in mark_list:
            y1,x2=i
            y2=y1;x1=5
            y1=y1-0.8
            if x2>15:
                for k in range(int((x2-x1)/0.2)):
                    x3=x1+k*0.2
                    if k%10==0:
                        lm=line_mark.format(x3,y1,0.8)
                        mark_line.append(lm)
                        markt=text_chr.format(x3,y1+1.2,str(int(k/5)))
                        mark_text.append(markt)
                    else:
                        lm=line_mark.format(x3,y1,0.5)
                        mark_line.append(lm)
            else:
                for k in range(int((x2-x1)/0.2)):
                    x3=x1+k*0.2
                    if k%5==0:
                        lm=line_mark.format(x3,y1,0.8)
                        mark_line.append(lm)
                        markt=text_chr.format(x3,y1+1.2,str(int(k/5)))
                        mark_text.append(markt)
                    else:
                        lm=line_mark.format(x3,y1,0.5)
                        mark_line.append(lm)
        for ID,content in startpo.items():
            x=sum(content)/len(content);y=id_position[ID]-4
            qp=query_chr.format(x,y,query_length,query_color)
            query_start[y]=x
            chr_list.append(qp)
            mark_listq.append((y-0.5,x+query_length,x))
            if query_length<0.2:qt=text_chr.format((2*x+query_length)*0.5,y-0.8,query_ID)
            else:qt=text_chr.format((2*x+query_length)*0.5,y-1.6,query_ID)
            chr_text.append(qt)
        for j in mark_listq:
            y1,x2,x1=j
            y2=y1
            y1=y1+0.5
            if x2-x1>10:
                for k in range(int((x2-x1)/0.2)):
                    x3=x1+k*0.2
                    if k%10==0:
                        lm=line_mark.format(x3,y1-0.9,1)
                        mark_line.append(lm)
                        markt=text_chr.format(x3,y1-1,str(int(k/5)))
                        mark_text.append(markt)
                    else:
                        lm=line_mark.format(x3,y1-0.7,0.5)
                        mark_line.append(lm)
            else:
                for k in range(int((x2-x1)/0.2)):
                    x3=x4=x1+k*0.2
                    if k%5==0:
                        lm=line_mark.format(x3,y1-0.9,1)
                        mark_line.append(lm)
                        markt=text_chr.format(x3,y1-1,str(int(k/5)))
                        mark_text.append(markt)
                    else:
                        lm=line_mark.format(x3,y1-0.7,0.5)
                        mark_line.append(lm)
        for line in linelist:
            id1,length1,std1,ed1,dir,id2,length2,std2,ed2=line.split()[:9]
            y1=y3=id_position[id2]-0.4;y2=y4=id_position[id2]-3.6#query的y值
            xq=query_start[id_position[id2]-4]#query的起始
            x1=5+int(std2)*10**-6;x2=xq+int(std1)*10**-6;x3=5+int(ed2)*10**-6;x4=xq+int(ed1)*10**-6
            if dir=="+":
                if x3-x1<1 and x4-x2<1:
                    bl1=bezier_line2.format(x1,y1,x1,(y1+y2)*0.5,x2,(y1+y2)*0.5,x2,y2);bl2=bezier_line2.format(x3,y3,x3,(y3+y4)*0.5,x4,(y3+y4)*0.5,x4,y4)
                    bezier_lists.append(bl1);bezier_lists.append(bl2)
                else:
                    bl1=bezier_line.format(x1,y1,x1,(y1+y2)*0.5,x2,(y1+y2)*0.5,x2,y2,x4,x4,(y3+y4)*0.5,x3,(y3+y4)*0.5,x3,y3)
                    bezier_list.append(bl1)
            else:
                if x3-x1<1 and x4-x2<1:
                    bl1=bezier_line2.format(x1,y1,x1,(y1+y4)*0.5,x4,(y1+y4)*0.5,x4,y4);bl2=bezier_line2.format(x3,y3,x3,(y3+y2)*0.5,x2,(y3+y2)*0.5,x2,y2)
                    bezier_lists.append(bl1);bezier_lists.append(bl2)
                else:
                    bl1=bezier_line.format(x1,y1,x1,(y1+y4)*0.5,x4,(y1+y4)*0.5,x4,y4,x2,x2,(y3+y2)*0.5,x3,(y3+y2)*0.5,x3,y3)
                    bezier_list.append(bl1)
        with open("./draw_detail.svg","w") as f:
            title='<svg width="{}px" height="{}px" xmlns="http://www.w3.org/2000/svg" version="1.1">\n'
            line_title=title.format(xmax+8,ymax)
            chr_line='  <g id="chrs" stroke-width="0.8">\n'+"\n".join(chr_list)+"\n  </g>\n"
            r = lambda: random.randint(0,255)
            number=chr_line.count("segment-color")
            colorlist=["#%02X%02X%02X" % (r(),r(),r()) for i in range(number)]
            if chr_color==1:chr_line=chr_line.replace("segment-color",random.choice(colorlista))
            else:
                for color in colorlist:
                    chr_line=chr_line.replace("segment-color",color,1)
            chrid_text='  <g id="query_text" fill="#ff0000" font-size="0.7" text-anchor="middle" font-family="Times New Roman">\n'+"\n".join(chr_text)+"\n  </g>\n"
            align_connect='  <g id="connection" fill="{}" stroke="{}" stroke-width="0.01">\n'.format(alignment_color,alignment_color)+"\n".join(bezier_list)+"\n  </g>\n"
            align_connects='  <g id="connections" fill="none" stroke="{}" stroke-width="0.01">\n'.format(alignment_color)+"\n".join(bezier_lists)+"\n  </g>\n"
            mark='  <g id="mark" stroke="#8e8d8d" stroke-width="0.02">\n'+"\n".join(mark_line)+"\n  </g>\n"
            markfont='  <g id="text" fill="black" font-size="0.3" text-anchor="middle" font-family="Times New Roman">\n'+"\n".join(mark_text)+"\n  </g>\n"
            if hide_mark==1:mark="";markfont=""
            end='  </svg>'
            f.write(line_title+mark+markfont+align_connect+align_connects+chr_line+chrid_text+end)

    def detailsvg(self):
        if self.pushButton_17.isChecked:
            self.pushButton_17.setText('drawing...')
            self.pushButton_17.repaint()
            try:
                if os.path.exists("./draw_detail.svg"):
                    os.remove("./draw_detail.svg")
                file=self.plainTextEdit_9.toPlainText()
                if self.radioButton_2.isChecked():
                    file_index=file+"_reference.index"#需要添加以reference为主的index
                    if not os.path.exists(file_index):self.build_reference_index(file)
                else:
                    file_index=file+".index"
                    if not os.path.exists(file_index):self.build_uniq_index(file)
                if self.lineEdit.text()!="":alignment_quality=int(self.lineEdit.text())
                else:alignment_quality=60
                if self.lineEdit_2.text()!="":alignment_seqs=int(self.lineEdit_2.text())
                else:alignment_seqs=10000
                chrid1=self.lineEdit_5.text()#这与下面的参数与ID选择相关，后来废除掉了，与这两个相关的函数都需要修正
                chrid1=chrid1.encode("utf-8")
                hide_mark=0;chr_color=0
                alignment_color=self.lineEdit_3.text()
                uniqkmercolor=""
                if "_reference.index" not in file_index:
                    with open(file_index,"rb") as f:
                        indexs=pickle.load(f)
                    with open(file,"rb") as file:
                        targetlist=[]
                        if chrid1 not in indexs:QMessageBox.warning(self.pushButton_17, "Warning","the input ID was not detected, please check")
                        else:
                            file.seek(indexs[chrid1])
                            for line in file:
                                if line.split()[0]!=chrid1:
                                    break
                                targetlist.append(line.decode())
                    idlist={line for line in targetlist if len(line.split())>=12 and int(line.split()[11])>=alignment_quality and int(line.split()[9])>alignment_seqs}
                    if idlist!=set():
                        self.insertcontent(idlist)#这个函数用来以表的方式展示原始数据
                    idlist=list(idlist)
                    if 0<len(idlist)<=200:self.drawdetail_list(idlist,alignment_color,hide_mark,chr_color)
                    elif len(idlist)>200:self.showpartialpdf_query(idlist,alignment_color,uniqkmercolor)
                    elif len(idlist)==0:QMessageBox.about(self.pushButton_17, "Help", "the content of this ID did not satisfy the setting value")
                else:
                    with open(file_index,"rb") as f:
                        indexs=pickle.load(f)
                    with open(file,"rb") as file:
                        targetlist=[]
                        if chrid1 not in indexs:QMessageBox.warning(self.pushButton_17, "Warning","the input ID was not detected, please check")
                        else:
                            for position in indexs[chrid1]:
                                file.seek(position)
                                for line in file:
                                    targetlist.append(line.decode('utf-8'))
                                    break
                    idlist={line for line in targetlist if len(line.split())>=12 and int(line.split()[11])>=alignment_quality and int(line.split()[9])>alignment_seqs}
                    if idlist!=set():self.insertcontent(idlist)
                    idlist=list(idlist)
                    if 0<len(idlist)<=200:
                        self.reference_ID(idlist,alignment_color,uniqkmercolor)
                    elif len(idlist)>200:
                        self.showpartialpdf(idlist,alignment_color,uniqkmercolor)
                    elif len(idlist)==0:
                        QMessageBox.about(self.pushButton_17, "Help", "the content of this ID did not satisfy the setting value")
            except Exception as e:
                    QMessageBox.warning(self.pushButton_17, "Warning", str(e))
            self.pushButton_17.setText("ok, finished")
            self.pushButton_17.repaint()
            time.sleep(1)
            self.pushButton_17.setText('draw details based on the input ID')
            self.pushButton_17.repaint()
            if 0<len(idlist)<=200:
                self.showwindow()
        
    def build_uniq_index(self,file):
        global countmax
        file_index=file+".index"
        with open(file,"rb") as f:
            indexs={}
            index=f.tell()
            line=f.readline()
            count=1
            while line:
                ID=line.split()[0]
                if ID not in indexs:
                    indexs[ID]=index
                uniqker_dir[count]=ID#试试看这样行不行，有因为在使用ID的时候要用二进制形式，那么当将ID直接存成二进制是不是就可以直接使用
                index=f.tell()
                line=f.readline()
                count+=1
        countmax=count
        with open(file_index,"wb") as f:
            pickle.dump(indexs,f)

    def build_uniq_index2(self,file):
        global countmax
        file_index=file+".index"
        with open(file,"rb") as f:
            indexs={}
            index=f.tell()
            line=f.readline()
            count=0
            while line:
                ID=line.split()[5]
                if ID not in indexs:
                    indexs[ID]=index
                    uniqker_dir[count]=ID#试试看这样行不行，有因为在使用ID的时候要用二进制形式，那么当将ID直接存成二进制是不是就可以直接使用
                    count+=1
                index=f.tell()
                line=f.readline()
        countmax=count
        with open(file_index,"wb") as f:
            pickle.dump(indexs,f)

    def build_uniq_index3(self,file):
        file_index=file+".index"
        file=file+".reference.index"
        indexs={}
        with open(file,"rb") as f:
            for count,line in enumerate(f):
                ID=line.split()[0];index=int(line.split()[1])
                indexs[ID]=index
        with open(file_index,"wb") as f:
            pickle.dump(indexs,f)

    def build_reference_index(self,file):
        file_index=file+"_reference.index"
        with open(file,"rb") as f:
            indexs={}
            index=f.tell()
            line=f.readline()
            while line:
                ID=line.split()[5]
                if ID not in indexs:
                    indexs[ID]=[]
                indexs[ID].append(index)
                index=f.tell()
                line=f.readline()
        with open(file_index,"wb") as f:
            pickle.dump(indexs,f)

    def build_query_index(self,file):
        file_index=file+"_query.index"
        with open(file,"rb") as f:
            indexs={}
            index=f.tell()
            line=f.readline()
            while line:
                ID=line.split()[0]
                if ID not in indexs:
                    indexs[ID]=[]
                indexs[ID].append(index)
                index=f.tell()
                line=f.readline()
        with open(file_index,"wb") as f:
            pickle.dump(indexs,f)

    def build_query_index2(self,file):
        file_index=file+"_query.index"
        file=file+".query.index"
        indexs={}
        with open(file,"rb") as f:
            for line in f:
                ID=line.split()[0];index=int(line.split()[1])
                if ID not in indexs:
                    indexs[ID]=[]
                indexs[ID].append(index)
        with open(file_index,"wb") as f:
            pickle.dump(indexs,f)

    def build_index(self):
        if self.pushButton_2.isChecked:
            self.pushButton_2.setText('generating...')
            self.pushButton_2.repaint()
            file=self.plainTextEdit_9.toPlainText()
            file_index=file+"_reference.index"
            if os.path.exists(file_index)==False:
                self.build_reference_index(file)
        self.pushButton_2.setText("ok, finished")
        self.pushButton_2.repaint()
        time.sleep(1)
        self.pushButton_2.setText('t<->q')
        self.pushButton_2.repaint()

    def build_indexuniq(self):
        if self.pushButton_13.isChecked:
            self.pushButton_13.setText('generating...')
            self.pushButton_13.repaint()
            file=self.plainTextEdit_10.toPlainText()
            file_index=file+"_reference.index"
            file_index2=file+".query.index"
            if os.path.exists(file_index2)==True and os.path.exists(file_index)==False:
                self.build_query_index2(file)
            if os.path.exists(file_index2)==False and os.path.exists(file_index)==False:
                self.build_query_index(file)
        self.pushButton_13.setText("ok, finished")
        self.pushButton_13.repaint()
        time.sleep(1)
        self.pushButton_13.setText('t<->q')
        self.pushButton_13.repaint()

    def partial_result_reference(self,lists,alignment_color,uniqkmercolor):#对reference作图
        linelist=lists
        if alignment_color=="":alignment_color="#E6E6E6"
        if uniqkmercolor=="":uniqkmercolor="#ff0000"
        ql=int(linelist[0].split()[6])
        if 100<ql*10**-6<1000:unit=10**-6;unit_text="(Mb)"
        elif 100<ql*10**-5<1000:unit=10**-5;unit_text="(100 Kb)"
        elif 100<ql*10**-4<1000:unit=10**-4;unit_text="(10 Kb)"
        elif 100<ql*10**-3<1000:unit=10**-3;unit_text="(Kb)"
        elif 100<ql*10**-2<1000:unit=10**-2;unit_text="(100 bp)"
        elif 100<ql*10**-1<1000:unit=10**-1;unit_text="(10 bp)"
        elif 100<ql<1000:unit=1;unit_text="(bp)"
        query_length=ql*unit;query_id=linelist[0].split()[5]
        chr_line='    <path d="M {},{} h {}"/>'
        chr_text='    <text x="{}" y="{}">{}</text>'
        align_line='    <path d="M {},{} V {} H {} V {} Z" />'
        align_line_='    <path d="M {},{} L {},{} H {} L {},{} Z" />'
        kmer_connect='    <path d="M {},{} L {},{}"/>'
        kmer_mark='    <path d="M {},{} v {}"/>'
        chr_listt=[]
        chr_IDsr=[]
        align_list=[]
        kmer_connection=[]#存储的是kmer连线
        kmer_po=[]#存储的是kmer本身
        mark_line=[]
        mark_text=[]
        xq=5;yq=5
        query_chr=chr_line.format(xq,yq,query_length)
        query_text=chr_text.format((2*xq+query_length)*0.5,3,query_id)
        for index,line in enumerate(linelist):
            infor=line.split()
            ID=infor[0];position=infor[2]+"-"+infor[3];dir=infor[4]
            ref_length=(int(infor[8])-int(infor[7]))*unit
            xr=x1=int(infor[7])*unit+5;yr=5*(index+2);x2=int(infor[8])*unit+5
            ref_chr=chr_line.format(xr,yr,ref_length)
            chr_listt.append(ref_chr)
            xrt=(int(infor[8])+int(infor[7]))*unit*0.5+5;yrt=yr+1;text=ID+": "+position
            ref_text=chr_text.format(xrt,yrt,text)#有可能ID会很长
            chr_IDsr.append(ref_text)
            if dir=="+":
                alignarea=align_line.format(xr,5.5,yr-0.5,x2,5.5)
                align_list.append(alignarea)
            else:
                alignarea=align_line_.format(xr,5.5,x2,yr-0.5,xr,x2,5.5)
                align_list.append(alignarea)
            if len(infor)>=10 and "," in infor[9]:
                uniqkmers=infor[9:]
                for u in uniqkmers:
                    if "," in u:
                        p1=u.split(",")[0];p2=u.split(",")[1]
                        x1=5+int(p2)*unit;y1=5;x2=(int(p1)-int(infor[2])+int(infor[7]))*unit+5;y2=5*(index+2)
                        if int(p1)*int(p2)==0:kmerc=""
                        else:kmerc=kmer_connect.format(x1,y1+0.5,x2,y2-0.5)#kmer连线
                        kmer_connection.append(kmerc)
                        if int(p2)==0:kmers_q=""
                        else:kmers_q=kmer_mark.format(x1,y1-0.5,1)
                        kmer_po.append(kmers_q)
                        if int(p1)==0:kmers_r=""
                        else:kmers_r=kmer_mark.format(x2,y2-0.5,1)
                        kmer_po.append(kmers_r)
            x1,y1,length=5,5,query_length
            for k in range(int((length)/0.2)):
                x3=x1+k*0.2
                if k%10==0:
                    lm=kmer_mark.format(x3,y1-1,0.5)#大刻度
                    mark_line.append(lm)
                    markt=chr_text.format(x3,y1-1.1,str(int(k/5)))#只有在大刻度上才有数字数字
                    mark_text.append(markt)
                else:
                    lm=kmer_mark.format(x3,y1-0.75,0.25)#小刻度
                    mark_line.append(lm)
        unit_mark=chr_text.format(query_length+6,y1-1.1,unit_text)
        mark_text.append(unit_mark)
        with open("./draw_detail.svg","w") as f:
            x=query_length+10;y=len(linelist)*5+10
            file_title='<svg width="{}px" height="{}px" xmlns="http://www.w3.org/2000/svg" version="1.1">\n'.format(x,y)
            mark_l='  <g id="mark" stroke="#8e8d8d" stroke-width="0.02">\n'+"\n".join(mark_line)+"\n  </g>\n"
            markfont='  <g id="mark_text" fill="black" font-size="0.5" text-anchor="middle" font-family="Times New Roman">\n'+"\n".join(mark_text)+"\n  </g>\n"
            colorlista=["#8ecfc9","#ffbe7a","#fa7f6f","#82b0d2","#beb8dc","#2878b5","#9ac9db","#f8ac8c","#c82423","#ff8884","#14517c","#2f7fc1","#96c37d",
                        "#f3d266","#d8383a","#a9b8c6","#c497b2","#8e8bfe","#fe99a2","#934b43","#d76364","#ef7a6d","#63e398","#b1ce46","#f1d77e","#9394e7","#5f97d2","#9dc3e7","#a1a9d0","#f0988c","#b883d3","#c4a5de",
                        "#f6cae5","#96cccb"]
            query_color=random.choice(colorlista)
            query_segment='  <g id="chrs" stroke="{}" stroke-width="1">\n'.format(query_color)+query_chr+"\n  </g>\n"
            r = lambda: random.randint(0,255)
            t_color="#%02X%02X%02X" % (r(),r(),r())
            target_segments='  <g id="chrs" stroke="{}" stroke-width="1">\n'.format(t_color)+"\n".join(chr_listt)+"\n  </g>\n"
            chrid_text_query='  <g id="query_text" fill="#ff0000" font-size="1" text-anchor="middle" font-family="Times New Roman">\n'+query_text+"\n  </g>\n"
            chrid_text_target='  <g id="target_text" fill="black" font-size="0.5" text-anchor="middle" font-family="Times New Roman">\n'+"\n".join(chr_IDsr)+"\n  </g>\n"
            align_connects='  <g id="connections" fill="{}" stroke="{}" stroke-width="0.01" stroke-opacity="0.3">\n'.format(alignment_color,alignment_color)+"\n".join(align_list)+"\n  </g>\n"
            allkmers='  <g id="kmer" stroke="{}" stroke-width="0.01">\n'.format(uniqkmercolor)+"\n".join(kmer_po)+"\n  </g>\n"
            kmers_connect='  <g id="kmer" stroke="{}" stroke-width="0.01">\n'.format(uniqkmercolor)+"\n".join(kmer_connection)+"\n  </g>\n"
            end='  </svg>'
            f.write(file_title+mark_l+markfont+align_connects+query_segment+target_segments+chrid_text_query+chrid_text_target+allkmers+kmers_connect+end)

    def partial_result_reference2(self,lists,alignment_color,uniqkmercolor):
        linelist=lists
        if alignment_color=="":alignment_color="#E6E6E6"
        if uniqkmercolor=="":uniqkmercolor="#ff0000"
        ql=int(linelist[0].split()[1])
        if 100<ql*10**-6<1000:unit=10**-6;unit_text="(Mb)"
        elif 100<ql*10**-5<1000:unit=10**-5;unit_text="(100 Kb)"
        elif 100<ql*10**-4<1000:unit=10**-4;unit_text="(10 Kb)"
        elif 100<ql*10**-3<1000:unit=10**-3;unit_text="(Kb)"
        elif 100<ql*10**-2<1000:unit=10**-2;unit_text="(100 bp)"
        elif 100<ql*10**-1<1000:unit=10**-1;unit_text="(10 bp)"
        elif 100<ql<1000:unit=1;unit_text="(bp)"
        query_length=ql*unit;query_id=linelist[0].split()[0]
        chr_line='    <path d="M {},{} h {}"/>'
        chr_text='    <text x="{}" y="{}">{}</text>'
        align_line='    <path d="M {},{} V {} H {} V {} Z" />'
        align_line_='    <path d="M {},{} L {},{} H {} L {},{} Z" />'
        kmer_connect='    <path d="M {},{} L {},{}"/>'
        kmer_mark='    <path d="M {},{} v {}"/>'
        chr_listt=[]
        chr_IDsr=[]
        align_list=[]
        kmer_connection=[]#存储的是kmer连线
        kmer_po=[]#存储的是kmer本身
        mark_line=[]
        mark_text=[]
        xq=5;yq=5
        query_chr=chr_line.format(xq,yq,query_length)
        query_text=chr_text.format((2*xq+query_length)*0.5,3,query_id)
        for index,line in enumerate(linelist):
            infor=line.split()
            ID=infor[5];position=infor[7]+"-"+infor[8];dir=infor[4]
            ref_length=(int(infor[3])-int(infor[2]))*unit
            xr=x1=int(infor[2])*unit+5;yr=5*(index+2);x2=int(infor[3])*unit+5
            ref_chr=chr_line.format(xr,yr,ref_length)
            chr_listt.append(ref_chr)
            xrt=(int(infor[2])+int(infor[3]))*unit*0.5+5;yrt=yr+1;text=ID+": "+position
            ref_text=chr_text.format(xrt,yrt,text)#有可能ID会很长
            chr_IDsr.append(ref_text)
            if dir=="+":
                alignarea=align_line.format(xr,5.5,yr-0.5,x2,5.5)
                align_list.append(alignarea)
            else:
                alignarea=align_line_.format(xr,5.5,x2,yr-0.5,xr,x2,5.5)
                align_list.append(alignarea)
            if len(infor)>=10 and "," in infor[9]:#画uniqkmer
                uniqkmers=infor[9:]
                for u in uniqkmers:
                    if "," in u:
                        p2=u.split(",")[0];p1=u.split(",")[1]
                        x1=5+int(p2)*unit;y1=5;x2=(int(p1)-int(infor[7])+int(infor[2]))*unit+5;y2=5*(index+2)
                        if int(p1)*int(p2)==0:kmerc=""
                        else:kmerc=kmer_connect.format(x1,y1+0.5,x2,y2-0.5)#kmer连线
                        kmer_connection.append(kmerc)
                        if int(p2)==0:kmers_q=""
                        else:kmers_q=kmer_mark.format(x1,y1-0.5,1)
                        kmer_po.append(kmers_q)
                        if int(p1)==0:kmers_r=""
                        else:kmers_r=kmer_mark.format(x2,y2-0.5,1)
                        kmer_po.append(kmers_r)
            x1,y1,length=5,5,query_length
            for k in range(int((length)/0.2)):
                x3=x1+k*0.2
                if k%10==0:
                    lm=kmer_mark.format(x3,y1-1,0.5)#大刻度
                    mark_line.append(lm)
                    markt=chr_text.format(x3,y1-1.1,str(int(k/5)))#只有在大刻度上才有数字数字
                    mark_text.append(markt)
                else:
                    lm=kmer_mark.format(x3,y1-0.75,0.25)#小刻度
                    mark_line.append(lm)
        unit_mark=chr_text.format(query_length+6,y1-1.1,unit_text)
        mark_text.append(unit_mark)
        with open("./draw_detail.svg","w") as f:
            x=query_length+10;y=len(linelist)*5+10
            file_title='<svg width="{}px" height="{}px" xmlns="http://www.w3.org/2000/svg" version="1.1">\n'.format(x,y)
            mark_l='  <g id="mark" stroke="#8e8d8d" stroke-width="0.02">\n'+"\n".join(mark_line)+"\n  </g>\n"
            markfont='  <g id="mark_text" fill="black" font-size="0.5" text-anchor="middle" font-family="Times New Roman">\n'+"\n".join(mark_text)+"\n  </g>\n"
            colorlista=["#8ecfc9","#ffbe7a","#fa7f6f","#82b0d2","#beb8dc","#2878b5","#9ac9db","#f8ac8c","#c82423","#ff8884","#14517c","#2f7fc1","#96c37d",
                        "#f3d266","#d8383a","#a9b8c6","#c497b2","#8e8bfe","#fe99a2","#934b43","#d76364","#ef7a6d","#63e398","#b1ce46","#f1d77e","#9394e7","#5f97d2","#9dc3e7","#a1a9d0","#f0988c","#b883d3","#c4a5de",
                        "#f6cae5","#96cccb"]
            query_color=random.choice(colorlista)
            query_segment='  <g id="chrs" stroke="{}" stroke-width="1">\n'.format(query_color)+query_chr+"\n  </g>\n"
            r = lambda: random.randint(0,255)
            t_color="#%02X%02X%02X" % (r(),r(),r())
            target_segments='  <g id="chrs" stroke="{}" stroke-width="1">\n'.format(t_color)+"\n".join(chr_listt)+"\n  </g>\n"
            chrid_text_query='  <g id="query_text" fill="#ff0000" font-size="1" text-anchor="middle" font-family="Times New Roman">\n'+query_text+"\n  </g>\n"
            chrid_text_target='  <g id="target_text" fill="black" font-size="0.5" text-anchor="middle" font-family="Times New Roman">\n'+"\n".join(chr_IDsr)+"\n  </g>\n"
            align_connects='  <g id="connections" fill="{}" stroke="{}" stroke-width="0.01" stroke-opacity="0.3">\n'.format(alignment_color,alignment_color)+"\n".join(align_list)+"\n  </g>\n"
            allkmers='  <g id="kmer" stroke="{}" stroke-width="0.01">\n'.format(uniqkmercolor)+"\n".join(kmer_po)+"\n  </g>\n"
            kmers_connect='  <g id="kmer" stroke="{}" stroke-width="0.01">\n'.format(uniqkmercolor)+"\n".join(kmer_connection)+"\n  </g>\n"
            end='  </svg>'
            f.write(file_title+mark_l+markfont+align_connects+query_segment+target_segments+chrid_text_query+chrid_text_target+allkmers+kmers_connect+end)
            
    def showpartialpdf(self,lists,alignment_color,uniqkmercolor):
        linelist=lists
        if alignment_color=="":alignment_color="#D3D3D3"
        if uniqkmercolor=="":uniqkmercolor="#ff0000"
        colorlista=["#8ecfc9","#ffbe7a","#fa7f6f","#82b0d2","#beb8dc","#2878b5","#9ac9db","#f8ac8c","#c82423","#ff8884","#14517c","#2f7fc1","#96c37d",
                    "#f3d266","#d8383a","#a9b8c6","#c497b2","#8e8bfe","#fe99a2","#934b43","#d76364","#ef7a6d","#63e398","#b1ce46","#f1d77e","#9394e7","#5f97d2","#9dc3e7","#a1a9d0","#f0988c","#b883d3","#c4a5de",
                    "#f6cae5","#96cccb"]
        ql=int(linelist[0].split()[6])
        if 100<ql*10**-6<1000:unit=10**-6;unit_text="(Mb)"
        elif 100<ql*10**-5<1000:unit=10**-5;unit_text="(100 Kb)"
        elif 100<ql*10**-4<1000:unit=10**-4;unit_text="(10 Kb)"
        elif 100<ql*10**-3<1000:unit=10**-3;unit_text="(Kb)"
        elif 100<ql*10**-2<1000:unit=10**-2;unit_text="(100 bp)"
        elif 100<ql*10**-1<1000:unit=10**-1;unit_text="(10 bp)"
        elif 100<ql<1000:unit=1;unit_text="(bp)"
        query_length=ql*unit;query_id=linelist[0].split()[5]
        xmax=10+query_length;ymax=(len(linelist)+1)*6+5;reference_y=ymax-5
        name=time.strftime('%H%M%S',time.localtime(time.time()))
        filename="./pdfresult/myImagePDF"+name+".pdf"
        c = canvas.Canvas(filename,pagesize=(xmax,ymax+10))
        targetlist=[]
        kmer={}
        for index,line in enumerate(linelist):
            lineinfor=line.split()
            x1=5+int(lineinfor[7])*unit;y1=y2=reference_y-(index+1)*5;x2=5+int(lineinfor[8])*unit
            targetinfor=lineinfor[0]+": "+lineinfor[2]+"-"+lineinfor[3];length=x2-x1;dir=lineinfor[4]
            targetlist.append((x1,y1,x2,y2,targetinfor))
            kmer[targetinfor]=(x1,y1)
            c.setFillColor(alignment_color,alpha=0.8)
            if dir=="+":c.rect(x1,y1+0.5,length,(index+1)*5,stroke=0,fill=1)
            else:
                p=c.beginPath()
                p.moveTo(x1,reference_y)
                p.lineTo(x2,y2)
                p.lineTo(x1,y1)
                p.lineTo(x2,reference_y)
                p.close()
                c.drawPath(p,stroke=0,fill=1)
        c.setFillColor("#000000")
        query_color=random.choice(colorlista)
        c.setStrokeColor(query_color)
        c.setDash(1,0)
        c.setLineWidth(1)
        c.line(5,reference_y,5+query_length,reference_y)
        x1,y1,x2,y2=(5,reference_y,5+query_length,reference_y)
        y1=y1-0.5
        if x2-x1>10:
            for k in range(int((x2-x1)/0.2)):
                x3=x4=x1+k*0.2
                if k%10==0:y3=y1-1;c.setFont("Times-Roman",0.5);c.drawCentredString(x3,y3-0.5,str(int(k/5)))
                else:y3=y1-0.5
                c.setLineWidth(0.002)
                c.setStrokeColor("#8e8d8d")
                c.line(x3,y1,x4,y3)
        else:
            for k in range(int((x2-x1)/0.2)):
                x3=x4=x1+k*0.2
                if k%5==0:y3=y1-1;c.setFont("Times-Roman",0.5);c.drawCentredString(x3,y3-0.5,str(int(k/5)))
                else:y3=y1-0.5
                c.setLineWidth(0.002)
                c.setStrokeColor("#8e8d8d")
                c.line(x3,y1,x4,y3)
        c.drawCentredString(x3+1,y3-1,unit_text)
        c.setFont("Times-Roman",1.5)
        c.setFillColor("#ff0000")#改变字体颜色的方法
        c.drawCentredString((10+query_length)*0.5,reference_y+1,query_id)
        target_color=random.choice(colorlista)
        c.setDash(1,0)
        c.setStrokeColor(target_color)
        c.setLineWidth(1)
        for infor in targetlist:
            x1,y1,x2,y2,targetinfor=infor
            c.line(x1,y1,x2,y2)
            c.setFont("Times-Roman",0.5)
            c.drawCentredString((x1+x2)*0.5,y2-1.8,targetinfor)
        c.setStrokeColor(uniqkmercolor,alpha=0.05)#调节线的颜色；字体颜色用full来填
        c.setLineWidth(0.002)
        for line in linelist:
            if "," in line:
                lineinfor=line.split()
                targetinfor=lineinfor[0]+": "+lineinfor[2]+"-"+lineinfor[3]
                x0,y0=kmer[targetinfor];y1=reference_y-0.5;xlength=int(lineinfor[2])*unit
                y0=y0+0.5;x0=x0-xlength
                ks=lineinfor[9:]
                for i in ks:
                    if "," in i:
                        k1=int(i.split(",")[0])*unit;k2=int(i.split(",")[1])*unit
                        if k1*k2!=0:
                            x1=5+k2;x2=x0+k1
                            c.line(x1,y1,x2,y0)
        c.save()
        subprocess.Popen(['start',filename],shell=True)

    def showpartialpdf_query(self,lists,alignment_color,uniqkmercolor):
        linelist=lists
        if alignment_color=="":alignment_color="#D3D3D3"
        if uniqkmercolor=="":uniqkmercolor="#ff0000"
        colorlista=["#8ecfc9","#ffbe7a","#fa7f6f","#82b0d2","#beb8dc","#2878b5","#9ac9db","#f8ac8c","#c82423","#ff8884","#14517c","#2f7fc1","#96c37d",
                    "#f3d266","#d8383a","#a9b8c6","#c497b2","#8e8bfe","#fe99a2","#934b43","#d76364","#ef7a6d","#63e398","#b1ce46","#f1d77e","#9394e7","#5f97d2","#9dc3e7","#a1a9d0","#f0988c","#b883d3","#c4a5de",
                    "#f6cae5","#96cccb"]
        ql=int(linelist[0].split()[1])
        if 100<ql*10**-6<1000:unit=10**-6;unit_text="(Mb)"
        elif 100<ql*10**-5<1000:unit=10**-5;unit_text="(100 Kb)"
        elif 100<ql*10**-4<1000:unit=10**-4;unit_text="(10 Kb)"
        elif 100<ql*10**-3<1000:unit=10**-3;unit_text="(Kb)"
        elif 100<ql*10**-2<1000:unit=10**-2;unit_text="(100 bp)"
        elif 100<ql*10**-1<1000:unit=10**-1;unit_text="(10 bp)"
        elif 100<ql<1000:unit=1;unit_text="(bp)"
        query_length=ql*unit;query_id=linelist[0].split()[0]
        xmax=10+query_length;ymax=(len(linelist)+1)*6+5;reference_y=ymax-5
        name=time.strftime('%H%M%S',time.localtime(time.time()))
        filename="./pdfresult/myImagePDF"+name+".pdf"
        c = canvas.Canvas(filename,pagesize=(xmax,ymax+10))
        targetlist=[]
        kmer={}
        for index,line in enumerate(linelist):
            lineinfor=line.split()
            x1=5+int(lineinfor[2])*unit;y1=y2=reference_y-(index+1)*5;x2=5+int(lineinfor[3])*unit
            targetinfor=lineinfor[5]+": "+lineinfor[7]+"-"+lineinfor[8];length=x2-x1;dir=lineinfor[4]
            targetlist.append((x1,y1,x2,y2,targetinfor))
            kmer[targetinfor]=(x1,y1)
            c.setFillColor(alignment_color,alpha=0.8)
            if dir=="+":c.rect(x1,y1+0.5,length,(index+1)*5,stroke=0,fill=1)
            else:
                p=c.beginPath()
                p.moveTo(x1,reference_y)
                p.lineTo(x2,y2)
                p.lineTo(x1,y1)
                p.lineTo(x2,reference_y)
                p.close()
                c.drawPath(p,stroke=0,fill=1)
        c.setFillColor("#000000")
        query_color=random.choice(colorlista)
        c.setStrokeColor(query_color)
        c.setDash(1,0)
        c.setLineWidth(1)
        c.line(5,reference_y,5+query_length,reference_y)
        x1,y1,x2,y2=(5,reference_y,5+query_length,reference_y)
        y1=y1-0.5
        if x2-x1>10:
            for k in range(int((x2-x1)/0.2)):
                x3=x4=x1+k*0.2
                if k%10==0:y3=y1-1;c.setFont("Times-Roman",0.5);c.drawCentredString(x3,y3-0.5,str(int(k/5)))
                else:y3=y1-0.5
                c.setLineWidth(0.002)
                c.setStrokeColor("#8e8d8d")
                c.line(x3,y1,x4,y3)
        else:
            for k in range(int((x2-x1)/0.2)):
                x3=x4=x1+k*0.2
                if k%5==0:y3=y1-1;c.setFont("Times-Roman",0.5);c.drawCentredString(x3,y3-0.5,str(int(k/5)))
                else:y3=y1-0.5
                c.setLineWidth(0.002)
                c.setStrokeColor("#8e8d8d")
                c.line(x3,y1,x4,y3)
        c.drawCentredString(x3+1,y3-1,unit_text)
        c.setFont("Times-Roman",1.5)
        c.setFillColor("#ff0000")#改变字体颜色的方法
        c.drawCentredString((10+query_length)*0.5,reference_y+1,query_id)
        target_color=random.choice(colorlista)
        c.setDash(1,0)
        c.setStrokeColor(target_color)
        c.setLineWidth(1)
        for infor in targetlist:
            x1,y1,x2,y2,targetinfor=infor
            c.line(x1,y1,x2,y2)
            c.setFont("Times-Roman",0.5)
            c.drawCentredString((x1+x2)*0.5,y2-1.8,targetinfor)
        c.setStrokeColor(uniqkmercolor,alpha=0.05)
        c.setLineWidth(0.002)
        for line in linelist:
            if "," in line:
                lineinfor=line.split()
                targetinfor=lineinfor[0]+": "+lineinfor[2]+"-"+lineinfor[3]
                x0,y0=kmer[targetinfor];y1=reference_y-0.5;xlength=int(lineinfor[2])*unit
                y0=y0+0.5;x0=x0-xlength
                ks=lineinfor[9:]
                for i in ks:
                    if "," in i:
                        k1=int(i.split(",")[0])*unit;k2=int(i.split(",")[1])*unit
                        if k1*k2!=0:
                            x1=5+k2;x2=x0+k1
                            c.line(x1,y1,x2,y0)
        c.save()
        subprocess.Popen(['start',filename],shell=True)
    
    def draw_part(self):
        global current_number#注意global定义的时候要与一开始呼应
        global uniqker_dir
        global targetlist
        if self.pushButton_5.isChecked:
            self.pushButton_5.setGif("./source/loading.gif")
            QtCore.QTimer.singleShot(10, self.pushButton_5.start)
            try:
                file=self.plainTextEdit_10.toPlainText()
                if self.lineEdit_7.text()=="":alignment_length=1000
                else:alignment_length=int(self.lineEdit_7.text())
                if self.lineEdit_8.text()=="":uniqkmer_number=20
                else:uniqkmer_number=int(self.lineEdit_8.text())
                self.pushButton_5.setText('drawing...')
                self.pushButton_5.repaint()
                interested_ID=self.lineEdit_6.text()
                alignment_color=self.lineEdit_3.text()
                uniqkmercolor=self.lineEdit_4.text()
                kmapq=self.lineEdit_9.text()
                if kmapq=="":kmapq=50
                else:kmapq=float(kmapq)
                targetset=set()
                targetlist=[]
                if interested_ID=="":
                    file_index=file+".index"
                    file_index2=file+".reference.index"
                    if os.path.exists(file_index2)==True and os.path.exists(file_index)==False:
                        self.pushButton_5.setText('generating the index file, just a moment...')
                        self.pushButton_5.repaint()
                        self.build_uniq_index3(file)
                    if os.path.exists(file_index2)==False and os.path.exists(file_index)==False:
                        self.pushButton_5.setText('generating the index file, just a moment...')
                        self.pushButton_5.repaint()
                        self.build_uniq_index2(file)
                    with open(file_index,"rb") as f:
                        indexs=pickle.load(f)
                    if uniqker_dir=={}:uniqker_dir={number:content for number,content in enumerate(indexs)}
                    ID=uniqker_dir[current_number]
                    file_save_uniq=file+"_"+ID.decode("utf-8")+"_all_uniqkmer.txt"
                    with open(file,"rb") as file,open(file_save_uniq,"a") as f:
                        file.seek(indexs[ID])
                        for line in file:
                            QApplication.processEvents()
                            line=line.decode('utf-8')
                            linelist=line.split()
                            if linelist[5].encode("utf-8")!=ID:
                                break
                            if int(linelist[3])-int(linelist[2])>=alignment_length and int(linelist[-1])>=kmapq:
                                cut=uniqkmer_number+9
                                if len(linelist)>=cut:
                                    f.write(line)
                                    target="\t".join(linelist[:9])
                                    line="\t".join(linelist[:cut])
                                    if target not in targetset:
                                        targetset.add(target)
                                        targetlist.append(line)
                                else:
                                    targetlist.append(line)
                    if 0<len(targetlist)<=200:
                        self.partial_result_reference(targetlist,alignment_color,uniqkmercolor)#;self.showwindow()
                    elif len(targetlist)>200:
                        self.showpartialpdf(targetlist,alignment_color,uniqkmercolor)
                    elif len(targetlist)==0:
                        QMessageBox.about(self.pushButton_5, "Help", "the alignment length of this ID did not satisfy the setting value")
                    if len(targetlist)!=0:
                        targetlist=["\t".join(i.split()[:9])+"\t"+str(i.count(",")) for i in targetlist]
                        self.tableWidget.setHorizontalHeaderLabels(['query ID','length','start position','end position','+ or -',
                'reference ID','length','start position','end position','uniqkmer number'])
                        self.insertcontent(targetlist)
                else:
                    file_save_uniq=file+"_"+interested_ID+"_"+"_all_uniqkmer.txt"
                    if "," not in interested_ID:
                        ID=interested_ID;ID2=""
                    else:ID=interested_ID.split(",")[0];ID2=interested_ID.split(",")[1]
                    if self.radioButton_3.isChecked()==False and self.radioButton_4.isChecked()==True:
                        if "," in interested_ID:ID,ID2=ID2,ID
                        ID=ID.encode("utf-8")
                        file_index=file+".index"
                        file_index2=file+".reference.index"
                        if os.path.exists(file_index2)==True and os.path.exists(file_index)==False:
                            self.pushButton_5.setText('generating the index file, just a moment...')
                            self.pushButton_5.repaint()
                            self.build_uniq_index3(file)
                        if os.path.exists(file_index)==False and os.path.exists(file_index)==False:
                            self.pushButton_5.setText('generating the index file, just a moment...')
                            self.pushButton_5.repaint()
                            self.build_uniq_index2(file)
                        with open(file_index,"rb") as f:
                            indexs=pickle.load(f)
                        with open(file,"rb") as file,open(file_save_uniq,"a") as f:
                            file.seek(indexs[ID])
                            for line in file:
                                QApplication.processEvents()
                                line=line.decode('utf-8')
                                linelist=line.split()
                                if linelist[5].encode("utf-8")!=ID:
                                    break
                                if int(linelist[3])-int(linelist[2])>=alignment_length and int(linelist[-1])>=kmapq:
                                    cut=uniqkmer_number+9
                                    if len(linelist)>=cut:
                                        f.write(line)
                                        target="\t".join(linelist[:9])
                                        line="\t".join(linelist[:cut])
                                        if target not in targetset:
                                            targetset.add(target)
                                            targetlist.append(line)
                                    else:
                                        targetlist.append(line)
                        if ID2!="":targetlist=[line for line in targetlist if ID2 +"\t" in line]
                        if 0<len(targetlist)<=200:
                            self.partial_result_reference(targetlist,alignment_color,uniqkmercolor)#;self.showwindow()
                        elif len(targetlist)>200:
                            self.showpartialpdf(targetlist,alignment_color,uniqkmercolor)
                        elif len(targetlist)==0:
                            QMessageBox.about(self.pushButton_5, "Help", "the alignment length of this ID did not satisfy the setting value")
                        if len(targetlist)!=0:
                            targetlist=["\t".join(i.split()[:9])+"\t"+str(i.count(",")) for i in targetlist]
                            self.tableWidget.setHorizontalHeaderLabels(['query ID','length','start position','end position','+ or -',
                            'reference ID','length','start position','end position','uniqkmer number'])
                            self.insertcontent(targetlist)
                    elif self.radioButton_4.isChecked()==False and self.radioButton_3.isChecked()==True:
                        file_index=file+"_query.index"
                        file_index2=file+".query.index"
                        if os.path.exists(file_index2)==True and os.path.exists(file_index)==False:
                            self.pushButton_5.setText('generating the index file, just a moment...')
                            self.pushButton_5.repaint()
                            self.build_query_index2(file)
                        if os.path.exists(file_index2)==False and os.path.exists(file_index)==False:
                            self.pushButton_5.setText('generating the index file, just a moment...')
                            self.pushButton_5.repaint()
                            self.build_query_index(file)
                        self.pushButton_5.setText('drawing...')
                        self.pushButton_5.repaint()
                        with open(file_index,"rb") as f:
                            indexs=pickle.load(f)
                        with open(file,"rb") as file,open(file_save_uniq,"a") as f:
                            for position in indexs[ID.encode("utf-8")]:
                                QApplication.processEvents()
                                file.seek(position)
                                for line in file:
                                    line=line.decode("utf-8")
                                    linelist=line.split()
                                    if int(linelist[3])-int(linelist[2])>=alignment_length and int(linelist[-1])>=kmapq:
                                        cut=uniqkmer_number+9
                                        if len(linelist)>=cut:
                                            f.write(line)
                                            target="\t".join(linelist[:9])
                                            line="\t".join(linelist[:cut])
                                            if target not in targetset:
                                                targetset.add(target)
                                                targetlist.append(line)
                                        else:targetlist.append(line)
                                    break
                        if ID2!="":targetlist=[line for line in targetlist if ID2 +"\t" in line]
                        if len(targetlist)<=200:self.partial_result_reference2(targetlist,alignment_color,uniqkmercolor)
                        elif len(targetlist)>200:self.showpartialpdf_query(targetlist,alignment_color,uniqkmercolor)
                        elif len(targetlist)==0:
                            QMessageBox.about(self.pushButton_5, "Help", "the information of this ID(s) did not satisfy the setting value")
                        if len(targetlist)!=0:
                            targetlist=["\t".join(i.split()[:9])+"\t"+str(i.count(",")) for i in targetlist]
                            self.tableWidget.setHorizontalHeaderLabels(['query ID','length','start position','end position','+ or -',
                            'reference ID','length','start position','end position','uniqkmer number'])
                            self.insertcontent(targetlist)
                    else:QMessageBox.about(self.pushButton_5, "Help", "the input ID is query ID or reference ID? please select one of them")
                self.pushButton_5.setText("ok, finished")
                self.pushButton_5.repaint()
                time.sleep(1)
                self.pushButton_5.setText('show alignment-related part')
                self.pushButton_5.repaint()
                QtCore.QTimer.singleShot(10, self.pushButton_5.stop)
                if 0<len(targetlist)<=200:
                    self.showwindow()
            except Exception as e:
                QMessageBox.warning(self.pushButton_5, "Warning", str(e)) 

    def total_result(self,linelist,alignment_color,uniqkmercolor):
        colorlista=["#8ecfc9","#ffbe7a","#fa7f6f","#82b0d2","#beb8dc","#2878b5","#9ac9db","#f8ac8c","#c82423","#ff8884","#14517c","#2f7fc1","#96c37d",
            "#f3d266","#d8383a","#a9b8c6","#c497b2","#8e8bfe","#fe99a2","#934b43","#d76364","#ef7a6d","#63e398","#b1ce46","#f1d77e","#9394e7","#5f97d2","#9dc3e7","#a1a9d0","#f0988c","#b883d3","#c4a5de",
            "#f6cae5","#96cccb"]
        if alignment_color=="":alignment_color="#f2f2f2"
        if uniqkmercolor=="":uniqkmercolor="#ff0000"
        xmax=query_length=int(linelist[0].split()[1])*10**-6
        query_ID=linelist[0].split()[0]
        query_color=random.choice(colorlista)
        id_length={}
        id_position={}
        mark_list=[]
        mark_listq=[]
        mark_line=[]
        mark_text=[]
        query_chr='    <path d="M {},{} h {}" stroke="{}"/>'
        target_chr='    <path d="M 5,{} h {}" stroke="segment-color"/>'
        text_chr='    <text x="{}" y="{}">{}</text>'
        line_mark='    <path d="M {},{} v {}"/>'
        bezier_line='    <path d="M {},{} C {},{} {},{} {},{} H {} C {},{} {},{} {},{}Z" />'
        bezier_line2='    <path d="M {},{} C {},{} {},{} {},{}" />'
        bezier_list=[]
        bezier_lists=[]
        kmer_bezier=[]
        chr_list=[]
        chr_text=[]
        kmer_line=[]
        startpo={}
        query_start={}
        for line in linelist:
            lineinfor=line.split()
            ID=lineinfor[5];length=int(lineinfor[6])*10**-6;stp=5+int(lineinfor[7])*10**-6
            id_length[ID]=length
            if ID not in startpo:
                startpo[ID]=[]
            startpo[ID].append(stp)
            if length>xmax:xmax=length
        ymax=len(id_length)*8+5
        for i,ID in enumerate(id_length):
            length=id_length[ID]
            tp=target_chr.format(10+8*i,length)#target的坐标,坐标跟在列表中的顺序是相关的
            id_position[ID]=10+8*i
            mark_list.append((11+8*i,5+length))
            chr_list.append(tp)
            if length<0.2:tt=text_chr.format((10+length)*0.5,11.7+8*i,ID)
            else:tt=text_chr.format((10+length)*0.5,12.3+8*i,ID)
            chr_text.append(tt)
        #标注marker
        for i in mark_list:
            y1,x2=i
            y2=y1;x1=5
            y1=y1-0.8
            if x2>15:
                for k in range(int((x2-x1)/0.2)):
                    x3=x1+k*0.2
                    if k%10==0:
                        lm=line_mark.format(x3,y1,0.8)
                        mark_line.append(lm)
                        markt=text_chr.format(x3,y1+1.2,str(int(k/5)))
                        mark_text.append(markt)
                    else:
                        lm=line_mark.format(x3,y1,0.5)
                        mark_line.append(lm)
            else:
                for k in range(int((x2-x1)/0.2)):
                    x3=x1+k*0.2
                    if k%5==0:
                        lm=line_mark.format(x3,y1,0.8)
                        mark_line.append(lm)
                        markt=text_chr.format(x3,y1+1.2,str(int(k/5)))
                        mark_text.append(markt)
                    else:
                        lm=line_mark.format(x3,y1,0.5)
                        mark_line.append(lm)
        for ID,content in startpo.items():
            x=sum(content)/len(content);y=id_position[ID]-4
            qp=query_chr.format(x,y,query_length,query_color)
            query_start[y]=x
            chr_list.append(qp)
            mark_listq.append((y-0.5,x+query_length,x))
            if query_length<0.2:qt=text_chr.format((2*x+query_length)*0.5,y-0.8,query_ID)
            else:qt=text_chr.format((2*x+query_length)*0.5,y-1.6,query_ID)
            chr_text.append(qt)
        for j in mark_listq:
            y1,x2,x1=j
            y2=y1
            y1=y1+0.5
            if x2-x1>10:
                for k in range(int((x2-x1)/0.2)):
                    x3=x1+k*0.2
                    if k%10==0:
                        lm=line_mark.format(x3,y1-0.9,1)
                        mark_line.append(lm)
                        markt=text_chr.format(x3,y1-1,str(int(k/5)))
                        mark_text.append(markt)
                    else:
                        lm=line_mark.format(x3,y1-0.7,0.5)
                        mark_line.append(lm)
            else:
                for k in range(int((x2-x1)/0.2)):
                    x3=x4=x1+k*0.2
                    if k%5==0:
                        lm=line_mark.format(x3,y1-0.9,1)
                        mark_line.append(lm)
                        markt=text_chr.format(x3,y1-1,str(int(k/5)))
                        mark_text.append(markt)
                    else:
                        lm=line_mark.format(x3,y1-0.7,0.5)
                        mark_line.append(lm)
        for line in linelist:
            id1,length1,std1,ed1,dir,id2,length2,std2,ed2=line.split()[:9]
            y1=y3=id_position[id2]-0.4;y2=y4=id_position[id2]-3.6#query的y值
            xq=query_start[id_position[id2]-4]#query的起始
            x1=5+int(std2)*10**-6;x2=xq+int(std1)*10**-6;x3=5+int(ed2)*10**-6;x4=xq+int(ed1)*10**-6
            if dir=="+":
                if x3-x1<1 and x4-x2<1:
                    bl1=bezier_line2.format(x1,y1,x1,(y1+y2)*0.5,x2,(y1+y2)*0.5,x2,y2);bl2=bezier_line2.format(x3,y3,x3,(y3+y4)*0.5,x4,(y3+y4)*0.5,x4,y4)
                    bezier_lists.append(bl1);bezier_lists.append(bl2)
                else:
                    bl1=bezier_line.format(x1,y1,x1,(y1+y2)*0.5,x2,(y1+y2)*0.5,x2,y2,x4,x4,(y3+y4)*0.5,x3,(y3+y4)*0.5,x3,y3)
                    bezier_list.append(bl1)
            else:
                if x3-x1<1 and x4-x2<1:
                    bl1=bezier_line2.format(x1,y1,x1,(y1+y4)*0.5,x4,(y1+y4)*0.5,x4,y4);bl2=bezier_line2.format(x3,y3,x3,(y3+y2)*0.5,x2,(y3+y2)*0.5,x2,y2)
                    bezier_lists.append(bl1);bezier_lists.append(bl2)
                else:
                    bl1=bezier_line.format(x1,y1,x1,(y1+y4)*0.5,x4,(y1+y4)*0.5,x4,y4,x2,x2,(y3+y2)*0.5,x3,(y3+y2)*0.5,x3,y3)
                    bezier_list.append(bl1)
            y1=id_position[id2];y4=id_position[id2]-4
            if len(line.split())>=10 and "," in line.split()[9]:
                for i in line.split()[9:]:
                    if "," in i:
                        q=int(i.split(",")[0])*10**-6;t=int(i.split(",")[1])*10**-6
                        x1q=xq+q;y1q=y4;x2t=5+t;y2t=y1;y3q=y1q-0.4;y6t=y2t-0.4
                        if q*t==0:bezier_kmer=""
                        else:bezier_kmer=bezier_line2.format(x1q,y1q+0.4,x1q,(y1q+y2t)*0.5,x2t,(y1q+y2t)*0.5,x2t,y6t)
                        kmer_bezier.append(bezier_kmer)
                        if q==0:line_kmerq=""
                        else:line_kmerq=line_mark.format(x1q,y3q,0.8)
                        kmer_line.append(line_kmerq)
                        if t==0:line_kmer=""
                        else:line_kmer=line_mark.format(x2t,y6t,0.8)
                        kmer_line.append(line_kmer)
        with open("./draw_detail.svg","w") as f:
            title='<svg width="{}px" height="{}px" xmlns="http://www.w3.org/2000/svg" version="1.1">\n'
            line_title=title.format(xmax+8,ymax)
            chr_line='  <g id="chrs" stroke-width="0.8">\n'+"\n".join(chr_list)+"\n  </g>\n"
            r = lambda: random.randint(0,255)
            number=chr_line.count("segment-color")
            colorlist=["#%02X%02X%02X" % (r(),r(),r()) for i in range(number)]
            for color in colorlist:
                chr_line=chr_line.replace("segment-color",color,1)
            chrid_text='  <g id="query_text" fill="#ff0000" font-size="0.7" text-anchor="middle" font-family="Times New Roman">\n'+"\n".join(chr_text)+"\n  </g>\n"
            align_connect='  <g id="connection" fill="{}" stroke="{}" stroke-width="0.01">\n'.format(alignment_color,alignment_color)+"\n".join(bezier_list)+"\n  </g>\n"
            align_connects='  <g id="connections" fill="none" stroke="{}" stroke-width="0.01">\n'.format(alignment_color)+"\n".join(bezier_lists)+"\n  </g>\n"
            mark='  <g id="mark" stroke="#8e8d8d" stroke-width="0.02">\n'+"\n".join(mark_line)+"\n  </g>\n"
            markfont='  <g id="text" fill="black" font-size="0.3" text-anchor="middle" font-family="Times New Roman">\n'+"\n".join(mark_text)+"\n  </g>\n"
            kmerb='  <g id="kmer_connection" fill="none" stroke="{}" stroke-width="0.01">\n'.format(uniqkmercolor)+"\n".join(kmer_bezier)+"\n  </g>\n"
            kmer='  <g id="kmer" stroke="{}" stroke-width="0.01">\n'.format(uniqkmercolor)+"\n".join(kmer_line)+"\n  </g>\n"
            end='  </svg>'
            f.write(line_title+mark+markfont+align_connect+align_connects+kmerb+chr_line+kmer+chrid_text+end)

    def total_result_pdf(self,linelist,alignment_color,uniqkmercolor):
        if alignment_color=="":alignment_color="#D3D3D3"
        if uniqkmercolor=="":uniqkmercolor="#ff0000"
        colorlista=["#8ecfc9","#ffbe7a","#fa7f6f","#82b0d2","#beb8dc","#2878b5","#9ac9db","#f8ac8c","#c82423","#ff8884","#14517c","#2f7fc1","#96c37d",
                    "#f3d266","#d8383a","#a9b8c6","#c497b2","#8e8bfe","#fe99a2","#934b43","#d76364","#ef7a6d","#63e398","#b1ce46","#f1d77e","#9394e7","#5f97d2","#9dc3e7","#a1a9d0","#f0988c","#b883d3","#c4a5de",
                    "#f6cae5","#96cccb"]
        ql=int(linelist[0].split()[1])
        if 100<ql*10**-6<1000:unit=10**-6;unit_text="(Mb)"
        elif 100<ql*10**-5<1000:unit=10**-5;unit_text="(100 Kb)"
        elif 100<ql*10**-4<1000:unit=10**-4;unit_text="(10 Kb)"
        elif 100<ql*10**-3<1000:unit=10**-3;unit_text="(Kb)"
        elif 100<ql*10**-2<1000:unit=10**-2;unit_text="(100 bp)"
        elif 100<ql*10**-1<1000:unit=10**-1;unit_text="(10 bp)"
        elif 100<ql<1000:unit=1;unit_text="(bp)"
        query_length=ql*unit;query_id=linelist[0].split()[0]
        xmax=10+query_length;ymax=(len(linelist)+1)*6+5;reference_y=ymax-5
        name=time.strftime('%H%M%S',time.localtime(time.time()))
        filename="./pdfresult/myImagePDF"+name+".pdf"
        c = canvas.Canvas(filename,pagesize=(xmax,ymax+10))
        targetlist=[]
        kmer={}
        for index,line in enumerate(linelist):
            lineinfor=line.split()
            x1=5+int(lineinfor[2])*unit;y1=y2=reference_y-(index+1)*5;x2=5+int(lineinfor[3])*unit;qx1=int(lineinfor[7])*unit;qx2=(int(lineinfor[6])-int(lineinfor[8]))*unit
            targetinfor=lineinfor[5]+": "+lineinfor[7]+"-"+lineinfor[8];length=x2-x1;dir=lineinfor[4]
            targetlist.append((x1-qx1,y1,x2+qx2,y2,targetinfor))
            kmer[targetinfor]=(x1-qx1,y1)
            c.setFillColor(alignment_color,alpha=0.8)#画比对部分
            if dir=="+":c.rect(x1,y1+0.5,length,(index+1)*5,stroke=0,fill=1)
            else:
                p=c.beginPath()
                p.moveTo(x1,reference_y)
                p.lineTo(x2,y2)
                p.lineTo(x1,y1)
                p.lineTo(x2,reference_y)
                p.close()
                c.drawPath(p,stroke=0,fill=1)
        c.setFillColor("#000000")
        query_color=random.choice(colorlista)
        c.setStrokeColor(query_color)
        c.setDash(1,0)
        c.setLineWidth(1)
        c.line(5,reference_y,5+query_length,reference_y)
        x1,y1,x2,y2=(5,reference_y,5+query_length,reference_y)
        x_position_min=5;x_position_max=5+query_length
        y1=y1-0.5
        if x2-x1>10:
            for k in range(int((x2-x1)/0.2)):
                x3=x4=x1+k*0.2
                if k%10==0:y3=y1-1;c.setFont("Times-Roman",0.5);c.drawCentredString(x3,y3-0.5,str(int(k/5)))
                else:y3=y1-0.5
                c.setLineWidth(0.002)
                c.setStrokeColor("#8e8d8d")
                c.line(x3,y1,x4,y3)
        else:
            for k in range(int((x2-x1)/0.2)):
                x3=x4=x1+k*0.2
                if k%5==0:y3=y1-1;c.setFont("Times-Roman",0.5);c.drawCentredString(x3,y3-0.5,str(int(k/5)))
                else:y3=y1-0.5
                c.setLineWidth(0.002)
                c.setStrokeColor("#8e8d8d")
                c.line(x3,y1,x4,y3)
        c.drawCentredString(x3+1,y3-1,unit_text)
        c.setFont("Times-Roman",1.5)
        c.setFillColor("#ff0000")#改变字体颜色的方法
        c.drawCentredString((10+query_length)*0.5,reference_y+1,query_id)
        target_color=random.choice(colorlista)
        c.setDash(1,0)
        c.setStrokeColor(target_color)
        c.setLineWidth(1)
        for infor in targetlist:
            x1,y1,x2,y2,targetinfor=infor
            c.line(x1,y1,x2,y2)
            c.setFont("Times-Roman",0.5)
            if x_position_min<=(x1+x2)*0.5<=x_position_max:
                c.drawCentredString((x1+x2)*0.5,y2-1.8,targetinfor)
            elif (x1+x2)*0.5<x_position_min:c.drawCentredString(x_position_min,y2-1.8,targetinfor)
            elif (x1+x2)*0.5>x_position_max:c.drawCentredString(x_position_max,y2-1.8,targetinfor)
        c.setStrokeColor(uniqkmercolor,alpha=0.05)#调节线的颜色；字体颜色用full来填
        c.setLineWidth(0.002)
        for line in linelist:
            if "," in line:
                lineinfor=line.split()
                targetinfor=lineinfor[5]+": "+lineinfor[7]+"-"+lineinfor[8]
                x0,y0=kmer[targetinfor];y1=reference_y-0.5
                y0=y0+0.5
                ks=lineinfor[9:]
                for i in ks:
                    if "," in i:
                        k1=int(i.split(",")[1])*unit;k2=int(i.split(",")[0])*unit
                        if k1*k2!=0:
                            x1=5+k2;x2=x0+k1
                            c.line(x1,y1,x2,y0)
        c.save()
        subprocess.Popen(['start',filename],shell=True)
    
    def reference_ID(self,lists,alignment_color,uniqkmercolor):
        linelist=lists
        if alignment_color=="":alignment_color="#f2f2f2"
        if uniqkmercolor=="":uniqkmercolor="#ff0000"
        colorlista=["#8ecfc9","#ffbe7a","#fa7f6f","#82b0d2","#beb8dc","#2878b5","#9ac9db","#f8ac8c","#c82423","#ff8884","#14517c","#2f7fc1","#96c37d",
            "#f3d266","#d8383a","#a9b8c6","#c497b2","#8e8bfe","#fe99a2","#934b43","#d76364","#ef7a6d","#63e398","#b1ce46","#f1d77e","#9394e7","#5f97d2","#9dc3e7","#a1a9d0","#f0988c","#b883d3","#c4a5de",
            "#f6cae5","#96cccb"]
        queryline=linelist[0].split()#这里的query与reference是针对实际作图命名的，不是按照文件来的
        querylength=int(queryline[6])*10**-6
        query_color=random.choice(colorlista)
        xmax=5+querylength
        queryID=queryline[5]
        referencestdp={}#存储的是每个ref的比对的起始位置
        referencelength={}#存的是ref的全长
        referencestd={}#存储的是refe的x起始位置
        chr_list=[]
        chr_text=[]
        mark_listq=[]
        mark_list=[]
        mark_line=[]
        mark_text=[]
        x_length=[]
        x_length.append(xmax)
        reference_xyposition={}
        bezier_lists=[]
        bezier_list=[]
        kmer_bezier=[]
        kmer_line=[]
        for line in linelist:
            lineinfor=line.split()
            ID=lineinfor[0];length=int(lineinfor[1])*10**-6;std=int(lineinfor[2])*10**-6;refstd=5+int(lineinfor[7])*10**-6
            if refstd+length>xmax:refstd=5
            x_length.append(5+length)
            referencelength[ID]=length
            referencestd[ID]=refstd
            if ID not in referencestdp:
                referencestdp[ID]=[]
            referencestdp[ID].append(std)
        ymax=len(referencestd)*8+5
        xmax=max(x_length)
        query_chr='    <path d="M 5,{} h {}" stroke="{}"/>'
        target_chr='    <path d="M {},{} h {}" stroke="segment-color"/>'
        text_chr='    <text x="{}" y="{}">{}</text>'
        line_mark='    <path d="M {},{} v {}"/>'
        bezier_line='    <path d="M {},{} C {},{} {},{} {},{} H {} C {},{} {},{} {},{}Z" />'
        bezier_line2='    <path d="M {},{} C {},{} {},{} {},{}" />'
        for index,ID in enumerate(referencestd):
            qp=query_chr.format(6+8*index,querylength,query_color)
            chr_list.append(qp)
            mark_listq.append((5.5+8*index,5+querylength))
            tp=target_chr.format(referencestd[ID],10+8*index,referencelength[ID])
            chr_list.append(tp)
            reference_xyposition[ID]=(referencestd[ID],10+8*index)
            mark_list.append((11+8*index,referencestd[ID],referencestd[ID]+referencelength[ID]))
            qtext=text_chr.format((10+querylength)*0.5,4.4+8*index,queryID)
            chr_text.append(qtext)
            ttext=text_chr.format((2*(referencestd[ID])+referencelength[ID])*0.5,12.1+8*index,ID)
            chr_text.append(ttext)
        for j in mark_listq:
            y1,x2=j
            y2=y1;x1=5
            y1=y1+0.5
            if x2-x1>10:
                for k in range(int((x2-x1)/0.2)):
                    x3=x1+k*0.2
                    if k%10==0:
                        lm=line_mark.format(x3,y1-0.9,0.5)
                        mark_line.append(lm)
                        markt=text_chr.format(x3,y1-1,str(int(k/5)))
                        mark_text.append(markt)
                    else:
                        lm=line_mark.format(x3,y1-0.65,0.25)
                        mark_line.append(lm)
            else:
                for k in range(int((x2-x1)/0.2)):
                    x3=x4=x1+k*0.2
                    if k%5==0:
                        lm=line_mark.format(x3,y1-0.9,0.5)
                        mark_line.append(lm)
                        markt=text_chr.format(x3,y1-1,str(int(k/5)))
                        mark_text.append(markt)
                    else:
                        lm=line_mark.format(x3,y1-0.65,0.25)
                        mark_line.append(lm)
        for i in mark_list:
            y1,x1,x2=i
            y2=y1
            y1=y1-0.6
            if x2>15:
                for k in range(int((x2-x1)/0.2)):
                    x3=x1+k*0.2
                    if k%10==0:
                        lm=line_mark.format(x3,y1,0.5)
                        mark_line.append(lm)
                        markt=text_chr.format(x3,y1+0.9,str(int(k/5)))
                        mark_text.append(markt)
                    else:
                        lm=line_mark.format(x3,y1,0.25)
                        mark_line.append(lm)
            else:
                for k in range(int((x2-x1)/0.2)):
                    x3=x1+k*0.2
                    if k%5==0:
                        lm=line_mark.format(x3,y1,0.5)
                        mark_line.append(lm)
                        markt=text_chr.format(x3,y1+0.9,str(int(k/5)))
                        mark_text.append(markt)
                    else:
                        lm=line_mark.format(x3,y1,0.25)
                        mark_line.append(lm)
        for line in linelist:
            infor=line.split()
            id1,length1,std1,ed1,dir,id2,length2,std2,ed2=infor[:9]
            xr,yr=reference_xyposition[id1]
            y1=y3=yr-0.4;y2=y4=yr-3.6
            x1=xr+int(std1)*10**-6;x3=xr+int(ed1)*10**-6;x2=5+int(std2)*10**-6;x4=5+int(ed2)*10**-6
            if dir=="+":
                if x3-x1<1 and x4-x2<1:
                    bl1=bezier_line2.format(x1,y1,x1,(y1+y2)*0.5,x2,(y1+y2)*0.5,x2,y2);bl2=bezier_line2.format(x3,y3,x3,(y3+y4)*0.5,x4,(y3+y4)*0.5,x4,y4)
                    bezier_lists.append(bl1);bezier_lists.append(bl2)
                else:
                    bl1=bezier_line.format(x1,y1,x1,(y1+y2)*0.5,x2,(y1+y2)*0.5,x2,y2,x4,x4,(y3+y4)*0.5,x3,(y3+y4)*0.5,x3,y3)
                    bezier_list.append(bl1)
            else:
                if x3-x1<1 and x4-x2<1:
                    bl1=bezier_line2.format(x1,y1,x1,(y1+y4)*0.5,x4,(y1+y4)*0.5,x4,y4);bl2=bezier_line2.format(x3,y3,x3,(y3+y2)*0.5,x2,(y3+y2)*0.5,x2,y2)
                    bezier_lists.append(bl1);bezier_lists.append(bl2)
                else:
                    bl1=bezier_line.format(x1,y1,x1,(y1+y4)*0.5,x4,(y1+y4)*0.5,x4,y4,x2,x2,(y3+y2)*0.5,x3,(y3+y2)*0.5,x3,y3)
                    bezier_list.append(bl1)
            y1=y3=yr;y2=y4=yr-4
            if len(infor)>=10 and "," in infor[9]:
                for i in infor[9:]:
                    if "," in i:
                        q=int(i.split(",")[0])*10**-6;t=int(i.split(",")[1])*10**-6
                        x1q=5+t;y1q=y4;x2t=xr+q;y2t=y1;y3q=y1q-0.4;y6t=y2t-0.4
                        if q*t==0:bezier_kmer=""
                        else:bezier_kmer=bezier_line2.format(x1q,y1q+0.4,x1q,(y1q+y2t)*0.5,x2t,(y1q+y2t)*0.5,x2t,y6t)
                        kmer_bezier.append(bezier_kmer)
                        if t==0:line_kmerq=""
                        else:line_kmerq=line_mark.format(x1q,y3q,0.8)
                        kmer_line.append(line_kmerq)
                        if q==0:line_kmer=0
                        else:line_kmer=line_mark.format(x2t,y6t,0.8)
                        kmer_line.append(line_kmer)
        with open("./draw_detail.svg","w") as f:
            title='<svg width="{}px" height="{}px" xmlns="http://www.w3.org/2000/svg" version="1.1">\n'
            line_title=title.format(xmax+5,ymax)
            chr_line='  <g id="chrs" stroke-width="0.8">\n'+"\n".join(chr_list)+"\n  </g>\n"
            r = lambda: random.randint(0,255)
            number=chr_line.count("segment-color")
            colorlist=["#%02X%02X%02X" % (r(),r(),r()) for i in range(number)]
            for color in colorlist:
                chr_line=chr_line.replace("segment-color",color,1)
            chrid_text='  <g id="query_text" fill="#ff0000" font-size="0.7" text-anchor="middle" font-family="Times New Roman">\n'+"\n".join(chr_text)+"\n  </g>\n"
            align_connect='  <g id="connection" fill="{}" stroke="{}" stroke-width="0.01">\n'.format(alignment_color,alignment_color)+"\n".join(bezier_list)+"\n  </g>\n"
            align_connects='  <g id="connections" fill="none" stroke="{}" stroke-width="0.01">\n'.format(alignment_color)+"\n".join(bezier_lists)+"\n  </g>\n"
            mark='  <g id="mark" stroke="#8e8d8d" stroke-width="0.02">\n'+"\n".join(mark_line)+"\n  </g>\n"
            markfont='  <g id="text" fill="black" font-size="0.3" text-anchor="middle" font-family="Times New Roman">\n'+"\n".join(mark_text)+"\n  </g>\n"
            kmerb='  <g id="kmer_connection" fill="none" stroke="{}" stroke-width="0.01">\n'.format(uniqkmercolor)+"\n".join(kmer_bezier)+"\n  </g>\n"
            kmer='  <g id="kmer" stroke="{}" stroke-width="0.01">\n'.format(uniqkmercolor)+"\n".join(kmer_line)+"\n  </g>\n"
            end='  </svg>'
            f.write(line_title+mark+markfont+align_connect+align_connects+kmerb+chr_line+kmer+chrid_text+end)
    
    def reference_ID_pdf(self,lists,alignment_color,uniqkmercolor):
        linelist=lists
        if alignment_color=="":alignment_color="#D3D3D3"
        if uniqkmercolor=="":uniqkmercolor="#ff0000"
        colorlista=["#8ecfc9","#ffbe7a","#fa7f6f","#82b0d2","#beb8dc","#2878b5","#9ac9db","#f8ac8c","#c82423","#ff8884","#14517c","#2f7fc1","#96c37d",
                    "#f3d266","#d8383a","#a9b8c6","#c497b2","#8e8bfe","#fe99a2","#934b43","#d76364","#ef7a6d","#63e398","#b1ce46","#f1d77e","#9394e7","#5f97d2","#9dc3e7","#a1a9d0","#f0988c","#b883d3","#c4a5de",
                    "#f6cae5","#96cccb"]
        ql=int(linelist[0].split()[6])
        if 100<ql*10**-6<1000:unit=10**-6;unit_text="(Mb)"
        elif 100<ql*10**-5<1000:unit=10**-5;unit_text="(100 Kb)"
        elif 100<ql*10**-4<1000:unit=10**-4;unit_text="(10 Kb)"
        elif 100<ql*10**-3<1000:unit=10**-3;unit_text="(Kb)"
        elif 100<ql*10**-2<1000:unit=10**-2;unit_text="(100 bp)"
        elif 100<ql*10**-1<1000:unit=10**-1;unit_text="(10 bp)"
        elif 100<ql<1000:unit=1;unit_text="(bp)"
        query_length=ql*unit;query_id=linelist[0].split()[5]
        xmax=10+query_length;ymax=(len(linelist)+1)*6+5;reference_y=ymax-5
        name=time.strftime('%H%M%S',time.localtime(time.time()))
        filename="./pdfresult/myImagePDF"+name+".pdf"
        c = canvas.Canvas(filename,pagesize=(xmax,ymax+10))
        targetlist=[]
        kmer={}
        for index,line in enumerate(linelist):
            lineinfor=line.split()
            x1=5+int(lineinfor[7])*unit;y1=y2=reference_y-(index+1)*5;x2=5+int(lineinfor[8])*unit;qx1=int(lineinfor[2])*unit;qx2=(int(lineinfor[1])-int(lineinfor[3]))*unit
            targetinfor=lineinfor[0]+": "+lineinfor[2]+"-"+lineinfor[3];length=x2-x1;dir=lineinfor[4]
            targetlist.append((x1-qx1,y1,x2+qx2,y2,targetinfor))
            kmer[targetinfor]=(x1-qx1,y1)
            c.setFillColor(alignment_color,alpha=0.8)#画比对部分
            if dir=="+":c.rect(x1,y1+0.5,length,(index+1)*5,stroke=0,fill=1)
            else:
                p=c.beginPath()
                p.moveTo(x1,reference_y)
                p.lineTo(x2,y2)
                p.lineTo(x1,y1)
                p.lineTo(x2,reference_y)
                p.close()
                c.drawPath(p,stroke=0,fill=1)
        c.setFillColor("#000000")
        query_color=random.choice(colorlista)
        c.setStrokeColor(query_color)
        c.setDash(1,0)
        c.setLineWidth(1)
        c.line(5,reference_y,5+query_length,reference_y)
        x_position_min=5;x_position_max=5+query_length
        x1,y1,x2,y2=(5,reference_y,5+query_length,reference_y)
        y1=y1-0.5
        if x2-x1>10:
            for k in range(int((x2-x1)/0.2)):
                x3=x4=x1+k*0.2
                if k%10==0:y3=y1-1;c.setFont("Times-Roman",0.5);c.drawCentredString(x3,y3-0.5,str(int(k/5)))
                else:y3=y1-0.5
                c.setLineWidth(0.002)
                c.setStrokeColor("#8e8d8d")
                c.line(x3,y1,x4,y3)
        else:
            for k in range(int((x2-x1)/0.2)):
                x3=x4=x1+k*0.2
                if k%5==0:y3=y1-1;c.setFont("Times-Roman",0.5);c.drawCentredString(x3,y3-0.5,str(int(k/5)))
                else:y3=y1-0.5
                c.setLineWidth(0.002)
                c.setStrokeColor("#8e8d8d")
                c.line(x3,y1,x4,y3)
        c.drawCentredString(x3+1,y3-1,unit_text)
        c.setFont("Times-Roman",1.5)
        c.setFillColor("#ff0000")#改变字体颜色的方法
        c.drawCentredString((10+query_length)*0.5,reference_y+1,query_id)
        target_color=random.choice(colorlista)
        c.setDash(1,0)
        c.setStrokeColor(target_color)
        c.setLineWidth(1)
        for infor in targetlist:
            x1,y1,x2,y2,targetinfor=infor
            c.line(x1,y1,x2,y2)
            c.setFont("Times-Roman",0.5)
            if x_position_min<=(x1+x2)*0.5<=x_position_max:c.drawCentredString((x1+x2)*0.5,y2-1.8,targetinfor)
            elif (x1+x2)*0.5<x_position_min:c.drawCentredString(x_position_min,y2-1.8,targetinfor)
            elif (x1+x2)*0.5>x_position_max:c.drawCentredString(x_position_max,y2-1.8,targetinfor)
        c.setStrokeColor(uniqkmercolor,alpha=0.05)#调节线的颜色；字体颜色用full来填
        c.setLineWidth(0.002)
        for line in linelist:
            if "," in line:
                lineinfor=line.split()
                targetinfor=lineinfor[0]+": "+lineinfor[2]+"-"+lineinfor[3]
                x0,y0=kmer[targetinfor];y1=reference_y-0.5
                y0=y0+0.5
                ks=lineinfor[9:]
                for i in ks:
                    if "," in i:
                        k1=int(i.split(",")[0])*unit;k2=int(i.split(",")[1])*unit
                        if k1*k2!=0:
                            x1=5+k2;x2=x0+k1
                            c.line(x1,y1,x2,y0) 
        c.save()
        subprocess.Popen(['start',filename],shell=True)

    def draw_all_alignment(self):#需要考虑更多的匹配的情况
        global current_number#注意global定义的时候要与一开始呼应
        global uniqker_dir
        if self.pushButton_7.isChecked:
            self.pushButton_7.setGif("./source/loading.gif")
            QtCore.QTimer.singleShot(10, self.pushButton_7.start)
            try:
                file=self.plainTextEdit_10.toPlainText()
                file_index=file+".index"
                if self.lineEdit_7.text()=="":alignment_length=1000
                else:alignment_length=int(self.lineEdit_7.text())
                if self.lineEdit_8.text()=="":uniqkmer_number=20
                else:uniqkmer_number=int(self.lineEdit_8.text())
                self.pushButton_7.setText('drawing...')
                self.pushButton_7.repaint()
                interested_ID=self.lineEdit_6.text()
                alignment_color=self.lineEdit_3.text()
                uniqkmercolor=self.lineEdit_4.text()
                kmapq=self.lineEdit_9.text()
                if kmapq=="":kmapq=50
                else:kmapq=float(kmapq)
                targetset=set()
                targetlist=[]
                if interested_ID=="":
                    file_index=file+".index"
                    file_index2=file+".reference.index"
                    if os.path.exists(file_index2)==True and os.path.exists(file_index)==False:
                        self.pushButton_7.setText('generating the index file, just a moment...')
                        self.pushButton_7.repaint()
                        self.build_uniq_index3(file)
                    if os.path.exists(file_index2)==False and os.path.exists(file_index)==False:
                        self.pushButton_7.setText('generating the index file, just a moment...')
                        self.pushButton_7.repaint()
                        self.build_uniq_index2(file)
                    with open(file_index,"rb") as f:
                        indexs=pickle.load(f)
                    if uniqker_dir=={}:uniqker_dir={number:content for number,content in enumerate(indexs)}
                    ID=uniqker_dir[current_number]
                    file_save_uniq=file+"_"+ID.decode("utf-8")+"_all_uniqkmer.txt"
                    with open(file,"rb") as file,open(file_save_uniq,"a") as f:
                        file.seek(indexs[ID])
                        for line in file:
                            QApplication.processEvents()
                            line=line.decode('utf-8')
                            linelist=line.split()
                            if line.split()[5].encode("utf-8")!=ID:
                                break
                            if int(linelist[3])-int(linelist[2])>=alignment_length and int(linelist[-1])>= kmapq:
                                cut=uniqkmer_number+9
                                if len(linelist)>=cut:
                                    f.write(line)
                                    target="\t".join(linelist[:9])
                                    line="\t".join(linelist[:cut])
                                    if target not in targetset:
                                        targetset.add(target)
                                        targetlist.append(line)
                                else:
                                    targetlist.append(line)
                    if 0<len(targetlist)<=200:
                        self.reference_ID(targetlist,alignment_color,uniqkmercolor)#;self.showwindow()
                    elif len(targetlist)>200:
                        self.reference_ID_pdf(targetlist,alignment_color,uniqkmercolor)
                    elif len(targetlist)==0:
                        QMessageBox.about(self.pushButton_7, "Help", "the alignment length of this ID did not satisfy the setting value")
                    if len(targetlist)!=0:
                        targetlist=["\t".join(i.split()[:9])+"\t"+str(i.count(",")) for i in targetlist]
                        self.tableWidget.setHorizontalHeaderLabels(['query ID','length','start position','end position','+ or -',
                'reference ID','length','start position','end position','uniqkmer number'])
                        self.insertcontent(targetlist)
                else:
                    file_save_uniq=file+"_"+interested_ID+"_"+"_all_uniqkmer.txt"
                    if "," not in interested_ID:
                        ID=interested_ID;ID2=""
                    else:ID=interested_ID.split(",")[0];ID2=interested_ID.split(",")[1]
                    if self.radioButton_3.isChecked()==False and self.radioButton_4.isChecked()==True:
                        if "," in interested_ID:ID,ID2=ID2,ID
                        ID=ID.encode("utf-8")
                        file_index=file+".index"
                        file_index2=file+".reference.index"
                        if os.path.exists(file_index2)==True and os.path.exists(file_index)==False:
                            self.pushButton_7.setText('generating the index file, just a moment...')
                            self.pushButton_7.repaint()
                            self.build_uniq_index3(file)
                        if os.path.exists(file_index)==False and os.path.exists(file_index)==False:
                            self.pushButton_7.setText('generating the index file, just a moment...')
                            self.pushButton_7.repaint()
                            self.build_uniq_index2(file)
                        with open(file_index,"rb") as f:
                            indexs=pickle.load(f)
                        with open(file,"rb") as file,open(file_save_uniq,"a") as f:
                            file.seek(indexs[ID])
                            for line in file:
                                QApplication.processEvents()
                                line=line.decode('utf-8')
                                linelist=line.split()
                                if line.split()[5].encode("utf-8")!=ID:
                                    break
                                if int(linelist[3])-int(linelist[2])>=alignment_length and int(linelist[-1])>= kmapq:
                                    cut=uniqkmer_number+9
                                    if len(linelist)>=cut:
                                        f.write(line)
                                        target="\t".join(linelist[:9])
                                        line="\t".join(linelist[:cut])
                                        if target not in targetset:
                                            targetset.add(target)
                                            targetlist.append(line)
                                    else:
                                        targetlist.append(line.strip())
                        if ID2!="":targetlist=[line for line in targetlist if ID2+"\t" in line]
                        if 0<len(targetlist)<=200:
                            self.reference_ID(targetlist,alignment_color,uniqkmercolor)#;self.showwindow()
                        elif len(targetlist)>200:
                            self.reference_ID_pdf(targetlist,alignment_color,uniqkmercolor)
                        elif len(targetlist)==0:
                            QMessageBox.about(self.pushButton_7, "Help", "the information of this ID(s) did not satisfy the setting value")
                        if len(targetlist)!=0:
                            targetlist=["\t".join(i.split()[:9])+"\t"+str(i.count(",")) for i in targetlist]
                            self.tableWidget.setHorizontalHeaderLabels(['query ID','length','start position','end position','+ or -',
                            'reference ID','length','start position','end position','uniqkmer number'])
                            self.insertcontent(targetlist)
                    elif self.radioButton_4.isChecked()==False and self.radioButton_3.isChecked()==True:
                        file_index=file+"_query.index"
                        file_index2=file+".query.index"
                        if os.path.exists(file_index2)==True and os.path.exists(file_index)==False:
                            self.pushButton_7.setText('generating the index file, just a moment...')
                            self.pushButton_7.repaint()
                            self.build_query_index2(file)
                        if os.path.exists(file_index2)==False and os.path.exists(file_index)==False:
                            self.pushButton_7.setText('generating the index file, just a moment...')
                            self.pushButton_7.repaint()
                            self.build_query_index(file)
                        self.pushButton_7.setText('drawing...')
                        self.pushButton_7.repaint()
                        with open(file_index,"rb") as f:
                            indexs=pickle.load(f)
                        with open(file,"rb") as file,open(file_save_uniq,"a") as f:
                            for position in indexs[ID.encode("utf-8")]:
                                QApplication.processEvents()
                                file.seek(position)
                                for line in file:
                                    line=line.decode("utf-8")
                                    linelist=line.split()
                                    if int(linelist[3])-int(linelist[2])>=alignment_length and int(linelist[-1])>= kmapq:
                                        cut=uniqkmer_number+9
                                        if len(linelist)>=cut:
                                            f.write(line)
                                            target="\t".join(linelist[:9])
                                            line="\t".join(linelist[:cut])
                                            if target not in targetset:
                                                targetset.add(target)
                                                targetlist.append(line)
                                        else:targetlist.append(line)
                                    break
                        if ID2!="":targetlist=[line for line in targetlist if ID2+"\t" in line]
                        if 0<len(targetlist)<=200:self.total_result(targetlist,alignment_color,uniqkmercolor)
                        elif len(targetlist)>200:self.total_result_pdf(targetlist,alignment_color,uniqkmercolor)
                        elif len(targetlist)==0:
                            QMessageBox.about(self.pushButton_7, "Help", "the information of this ID(s) did not satisfy the setting value")
                        if len(targetlist)!=0:
                            targetlist=["\t".join(i.split()[:9])+"\t"+str(i.count(",")) for i in targetlist]
                            self.tableWidget.setHorizontalHeaderLabels(['query ID','length','start position','end position','+ or -',
                            'reference ID','length','start position','end position','uniqkmer number'])
                            self.insertcontent(targetlist)
                    else:QMessageBox.about(self.pushButton_7, "Help", "the input ID is query ID or reference ID? please select one of them")
                self.pushButton_7.setText("ok, finished")
                self.pushButton_7.repaint()
                time.sleep(1)
                self.pushButton_7.setText('show all alignments')
                self.pushButton_7.repaint()
                QtCore.QTimer.singleShot(10, self.pushButton_7.stop)
                if 0<len(targetlist)<=200:
                    self.showwindow()
            except Exception as e:
                QMessageBox.warning(self.pushButton_7, "Warning", str(e))
        
    def draw_before(self):
        global current_number
        global uniqker_dir
        if self.pushButton_18.isChecked:
            self.pushButton_18.setGif("./source/loading.gif")
            QtCore.QTimer.singleShot(10, self.pushButton_18.start)
            try:
                file=self.plainTextEdit_10.toPlainText()
                alignment_color=self.lineEdit_3.text()
                uniqkmercolor=self.lineEdit_4.text()
                kmapq=self.lineEdit_9.text()
                if kmapq=="":kmapq=50
                else:kampq=float(kmapq)
                file_index=file+".index"
                file_index2=file+".reference.index"
                targetlist=[]
                targetset=set()
                if self.lineEdit_7.text()=="":alignment_length=1000
                else:alignment_length=int(self.lineEdit_7.text())
                if self.lineEdit_8.text()=="":uniqkmer_number=20
                else:uniqkmer_number=int(self.lineEdit_8.text())
                if os.path.exists(file_index2)==True and os.path.exists(file_index)==False:
                        self.pushButton_18.setText('generating the index file, just a moment...')
                        self.pushButton_18.repaint()
                        self.build_uniq_index3(file)
                if os.path.exists(file_index2)==False and os.path.exists(file_index)==False:
                    self.pushButton_18.setText('generating the index file, just a moment...')
                    self.pushButton_18.repaint()
                    self.build_uniq_index2(file)
                self.pushButton_18.setText('drawing...')
                self.pushButton_18.repaint()
                with open(file_index,"rb") as f:
                    indexs=pickle.load(f)
                current_number=current_number-1
                if current_number<0:
                    current_number=0
                    QMessageBox.about(self.pushButton_18, 'help message', 'this is the first ID, press the "next" button for showing other IDs')
                if uniqker_dir=={}:uniqker_dir={number:content for number,content in enumerate(indexs)}
                ID=uniqker_dir[current_number]
                file_save_uniq=file+"_"+ID.decode("utf-8")+"_all_uniqkmer.txt"
                with open(file,"rb") as file,open(file_save_uniq,"a") as f:
                    file.seek(indexs[ID])
                    for line in file:
                        QApplication.processEvents()
                        line=line.decode('utf-8')
                        linelist=line.split()
                        if line.split()[5]!=ID:
                            break
                        if int(linelist[3])-int(linelist[2])>=alignment_length and int(linelist[2])>=kampq:
                            cut=uniqkmer_number+9
                            if len(linelist)>cut:
                                f.write(line)
                                target="\t".join(linelist[:9])
                                line="\t".join(linelist[:cut])
                                if target not in targetset:
                                    targetset.add(target)
                                    targetlist.append(line)
                            else:
                                targetlist.append(line)
                if 0<len(targetlist)<=200:
                        self.partial_result_reference(targetlist,alignment_color,uniqkmercolor)
                elif len(targetlist)>200:
                    self.showpartialpdf(targetlist,alignment_color,uniqkmercolor)
                elif len(targetlist)==0:
                    QMessageBox.about(self.pushButton_18, "Help", "the alignment length of this ID did not satisfy the setting value")
                if len(targetlist)!=0:
                    targetlist=["\t".join(i.split()[:9])+"\t"+str(i.count(",")) for i in targetlist]
                    self.tableWidget.setHorizontalHeaderLabels(['query ID','length','start position','end position','+ or -','reference ID','length','start position','end position','uniqkmer number'])
                    self.insertcontent(targetlist)
                self.pushButton_18.setText("ok, finished")
                self.pushButton_18.repaint()
                time.sleep(1)
                self.pushButton_18.setText('before')
                self.pushButton_18.repaint()
                QtCore.QTimer.singleShot(10, self.pushButton_18.stop)
                if 0<len(targetlist)<=200:self.showwindow()
            except Exception as e:
                QMessageBox.warning(self.pushButton_18, "Warning", str(e))

    def draw_after(self):
        global current_number
        global uniqker_dir
        if self.pushButton_19.isChecked:
            self.pushButton_19.setGif("./source/loading.gif")
            QtCore.QTimer.singleShot(10, self.pushButton_19.start)
            try:
                file=self.plainTextEdit_10.toPlainText()
                alignment_color=self.lineEdit_3.text()
                uniqkmercolor=self.lineEdit_4.text()
                kmapq=self.lineEdit_9.text()
                if kmapq=="":kmapq=50
                else:kmapq=float(kmapq)
                file_index=file+".index"
                file_index2=file+".reference.index"
                targetset=set()
                targetlist=[]
                if self.lineEdit_7.text()=="":alignment_length=1000
                else:alignment_length=int(self.lineEdit_7.text())
                if self.lineEdit_8.text()=="":uniqkmer_number=20
                else:uniqkmer_number=int(self.lineEdit_8.text())
                if os.path.exists(file_index2)==True and os.path.exists(file_index)==False:
                        self.pushButton_19.setText('generating the index file, just a moment...')
                        self.pushButton_19.repaint()
                        self.build_uniq_index3(file)
                if os.path.exists(file_index2)==False and os.path.exists(file_index)==False:
                    self.pushButton_19.setText('generating the index file, just a moment...')
                    self.pushButton_19.repaint()
                    self.build_uniq_index2(file)
                self.pushButton_19.setText('drawing...')
                self.pushButton_19.repaint()
                with open(file_index,"rb") as f:
                    indexs=pickle.load(f)
                current_number=current_number+1
                if uniqker_dir=={}:uniqker_dir={number:content for number,content in enumerate(indexs)}
                if current_number>len(uniqker_dir):current_number=0
                ID=uniqker_dir[current_number]
                file_save_uniq=file+"_"+ID.decode("utf-8")+"_all_uniqkmer.txt"
                with open(file,"rb") as file,open(file_save_uniq,"a") as f:
                    file.seek(indexs[ID])
                    for line in file:
                        QApplication.processEvents()
                        line=line.decode('utf-8')
                        linelist=line.split()
                        if linelist[5].encode("utf-8")!=ID:
                            break
                        if int(linelist[3])-int(linelist[2])>=alignment_length and int(linelist[-1])>= kmapq:
                            cut=uniqkmer_number+9
                            if len(linelist)>=cut:
                                f.write(line)
                                target="\t".join(linelist[:9])
                                line="\t".join(linelist[:cut])
                                if target not in targetset:
                                    targetset.add(target)
                                    targetlist.append(line)
                            else:
                                targetlist.append(line)
                if 0<len(targetlist)<=200:
                        self.partial_result_reference(targetlist,alignment_color,uniqkmercolor)
                elif len(targetlist)>200:
                    self.showpartialpdf(targetlist,alignment_color,uniqkmercolor)
                elif len(targetlist)==0:
                    QMessageBox.about(self.pushButton_19, "Help", "the alignment length of this ID did not satisfy the setting value")
                if len(targetlist)!=0:
                    targetlist=["\t".join(i.split()[:9])+"\t"+str(i.count(",")) for i in targetlist]
                    self.tableWidget.setHorizontalHeaderLabels(['query ID','length','start position','end position','+ or -','reference ID','length','start position','end position','uniqkmer number'])
                    self.insertcontent(targetlist)
                self.pushButton_19.setText("ok, finished")
                self.pushButton_19.repaint()
                time.sleep(1)
                self.pushButton_19.setText('next')
                self.pushButton_19.repaint()
                QtCore.QTimer.singleShot(10, self.pushButton_19.stop)
                if 0<len(targetlist)<=200:self.showwindow()
            except Exception as e:
                QMessageBox.warning(self.pushButton_19, "Warning", str(e))

    def exqueryid(self):
        self.pushButton_20.setGif("./source/loading.gif")
        QtCore.QTimer.singleShot(10, self.pushButton_20.start)
        try:
            file1=self.plainTextEdit_9.toPlainText()
            if file1!="":
                with open(file1) as f:
                    ids=set()
                    for line in f:
                        linelist=line.split()
                        if len(linelist)>=9:
                            ids.add(linelist[0])
                            QApplication.processEvents()
                    content="\n".join(ids)
            else:
                content=""
                QMessageBox.warning(self.pushButton_20, "Warning", "please input the paf file for visualizing")
            QtCore.QTimer.singleShot(100, self.pushButton_20.stop)
        except Exception as e:
            QMessageBox.warning(self.pushButton_20, "Warning", str(e))
        if content!="":self.showallid_query(content)

    def exqueryid2(self):
        try:
            file2=self.plainTextEdit_10.toPlainText()
            if os.path.exists(file2+".query.index")==True:
                with open(file2+".query.index") as f:
                    ids={line.split()[0] for line in f}
                    content="\n".join(ids)
            else:
                content=""
                QMessageBox.warning(self.pushButton_21, "Warning", "the query.index was not be detected, please check! detailed descriptions can be found in RAviz manual")
        except Exception as e:
            QMessageBox.warning(self.pushButton_21, "Warning", str(e))
        if content!="":self.showallid_query(content)
        
    def exreferenceid(self):
        self.pushButton_9.setGif("./source/loading.gif")
        QtCore.QTimer.singleShot(10, self.pushButton_9.start)
        try:
            file1=self.plainTextEdit_9.toPlainText()
            if file1!="":
                with open(file1) as f:
                    ids=set()
                    for line in f:
                        linelist=line.split()
                        if len(linelist)>=9:
                            ids.add(linelist[5])
                            QApplication.processEvents()
                    content="\n".join(ids)
            else:
                content=""
                QMessageBox.warning(self.pushButton_9, "Warning", "please input the paf file for visualizing")
            QtCore.QTimer.singleShot(100, self.pushButton_9.stop)
        except Exception as e:
            QMessageBox.warning(self.pushButton_9, "Warning", str(e))
        if content!="":self.showallid_reference(content)

    def exreferenceid2(self):
        try:
            file2=self.plainTextEdit_10.toPlainText()
            if os.path.exists(file2+".reference.index")==True:
                with open(file2+".reference.index") as f:
                    ids={line.split()[0] for line in f}
                    content="\n".join(ids)
                self.showallid_reference(content)
            else:QMessageBox.warning(self.pushButton_22, "Warning", "the reference.index was not be detected, please check! detailed descriptions can be found in RAviz manual")
        except Exception as e:
            QMessageBox.warning(self.pushButton_22, "Warning", str(e))
        
class mytext(QTextEdit):
    def __int__(self):
        super(mytext, self).__init__()

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        self.setText(os.path.abspath((e.mimeData().urls())[0].toLocalFile()))

class loginform(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

class loginviewer(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent)
        self.ui=MainWindow()
        self.ui.show()

class showids_query(QMainWindow):
    def __init__(self,IDtext,parent=None):
        QMainWindow.__init__(self,parent)
        self.ui=Ui_MainWindow_show_query()
        self.ui.information = IDtext#传递text
        self.ui.setupUi(self)

class showids_reference(QMainWindow):
    def __init__(self,IDtext,parent=None):
        QMainWindow.__init__(self,parent)
        self.ui=Ui_MainWindow_show_reference()
        self.ui.information = IDtext#传递text
        self.ui.setupUi(self)

class SvgWidget(QSvgWidget):
    def __init__(self):
        super(SvgWidget, self).__init__()
        self.status = 0
        self.newPos = QPoint()

    def wheelEvent(self, e):
        if self.status == 1:
            e = e.angleDelta() / 8
            self.diff = 0.3
            if e.y() > 0:
                self.mywidth = self.width() + self.width() * self.diff
                self.myheight = self.height() + self.height() * self.diff
            else:
                self.mywidth = self.width() - self.width() * self.diff
                self.myheight = self.height() - self.height() * self.diff
            self.resize(int(self.mywidth),int(self.myheight))

class SvgWindow(QScrollArea):
    def __init__(self):
        super(SvgWindow, self).__init__()
        self.svgwidget = SvgWidget()
        self.setWidget(self.svgwidget)
        self.svgwidget.setStyleSheet('''QWidget{background-color:#FFFFFF;}''')
        self.OK = False

    def setFileSize(self,filename):
        self.svgwidget.load(filename)
        myrender = self.svgwidget.renderer()
        self.svgwidget.resize(myrender.defaultSize())
        self.OK = True
        return myrender.defaultSize()

    def keyPressEvent(self, e) -> None:
        if e.modifiers() == Qt.ControlModifier:
            self.svgwidget.status = 1

    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None:
        self.svgwidget.status = 0

    def mousePressEvent(self,e) -> None:
        if self.OK:
            self.mousePressPos = e.pos()
            self.svgwidget.newPos.setX(self.horizontalScrollBar().value())
            self.svgwidget.newPos.setY(self.verticalScrollBar().value())
            e.accept()
        else:
            return
    
    def mouseMoveEvent(self,e) -> None:
        if self.OK:
            self.horizontalScrollBar().setValue(self.svgwidget.newPos.x() + (self.mousePressPos.x() - e.pos().x()))
            self.verticalScrollBar().setValue(self.svgwidget.newPos.y() + (self.mousePressPos.y() - e.pos().y()))
            self.horizontalScrollBar().update()
            self.verticalScrollBar().update()
            e.accept()
        else:
            return

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("svg viewer ('ctrl+the mouse wheel' will change the picture size)")
        self.svgwindow = SvgWindow()
        self.opensvgfile()
        self.setCentralWidget(self.svgwindow)

    def opensvgfile(self):
        size = self.svgwindow.setFileSize("./draw_detail.svg")#这里需要传递一个文件名
        self.resize(size) 

class LoadingButton(QtWidgets.QPushButton):
    @QtCore.pyqtSlot()
    def start(self):
        if hasattr(self, "_movie"):
            self._movie.start()

    @QtCore.pyqtSlot()
    def stop(self):
        if hasattr(self, "_movie"):
            self._movie.stop()
            self.setIcon(QtGui.QIcon())

    def setGif(self, filename):
        if not hasattr(self, "_movie"):
            self._movie = QtGui.QMovie(self)
            self._movie.setFileName(filename)
            self._movie.frameChanged.connect(self.on_frameChanged)
            if self._movie.loopCount() != -1:
                self._movie.finished.connect(self.start)
        self.stop()

    @QtCore.pyqtSlot(int)
    def on_frameChanged(self, frameNumber):
        self.setIcon(QtGui.QIcon(self._movie.currentPixmap()))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    comboxDemo=loginform()
    comboxDemo.show()
    try:
        if len(os.listdir("./pdfresult/"))!=0:
            shutil.rmtree("./pdfresult/")
            os.mkdir("./pdfresult/")
    except Exception as e:
        pass
    sys.exit(app.exec_())