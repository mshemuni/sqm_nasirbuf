# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ds.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(682, 549)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)
        self.interval = QtWidgets.QDoubleSpinBox(self.tab)
        self.interval.setDecimals(5)
        self.interval.setMinimum(0.1)
        self.interval.setMaximum(60.0)
        self.interval.setSingleStep(1.0)
        self.interval.setProperty("value", 0.5)
        self.interval.setObjectName("interval")
        self.gridLayout_2.addWidget(self.interval, 0, 4, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setMinimumSize(QtCore.QSize(100, 0))
        self.label_14.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 1, 1, 5)
        self.brightness_raw = QtWidgets.QLCDNumber(self.tab)
        self.brightness_raw.setMinimumSize(QtCore.QSize(221, 111))
        self.brightness_raw.setMaximumSize(QtCore.QSize(221, 111))
        self.brightness_raw.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.brightness_raw.setDigitCount(4)
        self.brightness_raw.setProperty("value", 9999.0)
        self.brightness_raw.setProperty("intValue", 9999)
        self.brightness_raw.setObjectName("brightness_raw")
        self.gridLayout_2.addWidget(self.brightness_raw, 2, 0, 1, 4)
        self.label_10 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 2, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 5, 1, 1)
        self.brightness_new = QtWidgets.QLCDNumber(self.tab)
        self.brightness_new.setMinimumSize(QtCore.QSize(181, 81))
        self.brightness_new.setMaximumSize(QtCore.QSize(181, 81))
        self.brightness_new.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.brightness_new.setDigitCount(4)
        self.brightness_new.setProperty("value", 9999.0)
        self.brightness_new.setProperty("intValue", 9999)
        self.brightness_new.setObjectName("brightness_new")
        self.gridLayout_2.addWidget(self.brightness_new, 3, 0, 1, 3)
        self.label_11 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 3, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 5, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setMinimumSize(QtCore.QSize(100, 0))
        self.label_16.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 4, 0, 1, 2)
        self.line_3 = QtWidgets.QFrame(self.tab)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 4, 2, 1, 4)
        self.flux = QtWidgets.QLCDNumber(self.tab)
        self.flux.setMinimumSize(QtCore.QSize(191, 61))
        self.flux.setMaximumSize(QtCore.QSize(191, 61))
        self.flux.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.flux.setDigitCount(10)
        self.flux.setProperty("value", -2147483648.0)
        self.flux.setProperty("intValue", -2147483648)
        self.flux.setObjectName("flux")
        self.gridLayout_2.addWidget(self.flux, 5, 0, 1, 3)
        self.label_12 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 5, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 5, 5, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setMinimumSize(QtCore.QSize(100, 0))
        self.label_15.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 6, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 6, 2, 1, 4)
        self.temperature = QtWidgets.QLCDNumber(self.tab)
        self.temperature.setMinimumSize(QtCore.QSize(121, 61))
        self.temperature.setMaximumSize(QtCore.QSize(121, 61))
        self.temperature.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.temperature.setDigitCount(4)
        self.temperature.setProperty("value", 9999.0)
        self.temperature.setProperty("intValue", 9999)
        self.temperature.setObjectName("temperature")
        self.gridLayout_2.addWidget(self.temperature, 7, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 7, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(163, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 7, 3, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 8, 5, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 0, 0, 1, 1)
        self.sample_number = QtWidgets.QSpinBox(self.tab_2)
        self.sample_number.setMaximum(1000)
        self.sample_number.setProperty("value", 50)
        self.sample_number.setObjectName("sample_number")
        self.gridLayout_6.addWidget(self.sample_number, 0, 1, 1, 3)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 1, 0, 1, 1)
        self.comment = QtWidgets.QLineEdit(self.tab_2)
        self.comment.setObjectName("comment")
        self.gridLayout_6.addWidget(self.comment, 1, 1, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(457, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem5, 2, 0, 1, 3)
        self.read = QtWidgets.QPushButton(self.tab_2)
        self.read.setObjectName("read")
        self.gridLayout_6.addWidget(self.read, 2, 3, 1, 1)
        self.records = QtWidgets.QTableWidget(self.tab_2)
        self.records.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.records.setObjectName("records")
        self.records.setColumnCount(8)
        self.records.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.records.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.records.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.records.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.records.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.records.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.records.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.records.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.records.setHorizontalHeaderItem(7, item)
        self.gridLayout_6.addWidget(self.records, 3, 0, 1, 4)
        spacerItem6 = QtWidgets.QSpacerItem(308, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem6, 4, 0, 1, 2)
        self.remove_record = QtWidgets.QPushButton(self.tab_2)
        self.remove_record.setObjectName("remove_record")
        self.gridLayout_6.addWidget(self.remove_record, 4, 2, 1, 1)
        self.export_records = QtWidgets.QPushButton(self.tab_2)
        self.export_records.setObjectName("export_records")
        self.gridLayout_6.addWidget(self.export_records, 4, 3, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.logs = QtWidgets.QListWidget(self.tab_5)
        self.logs.setObjectName("logs")
        self.gridLayout_7.addWidget(self.logs, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.textEdit = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit.setEnabled(True)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_8.addWidget(self.textEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_4.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 682, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.port = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.port.setObjectName("port")
        self.gridLayout.addWidget(self.port, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_2.setEnabled(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_3.setEnabled(False)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.parity = QtWidgets.QComboBox(self.dockWidgetContents)
        self.parity.setEnabled(False)
        self.parity.setObjectName("parity")
        self.parity.addItem("")
        self.parity.addItem("")
        self.parity.addItem("")
        self.parity.addItem("")
        self.parity.addItem("")
        self.gridLayout.addWidget(self.parity, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_4.setEnabled(False)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.sbits = QtWidgets.QComboBox(self.dockWidgetContents)
        self.sbits.setEnabled(False)
        self.sbits.setObjectName("sbits")
        self.sbits.addItem("")
        self.sbits.addItem("")
        self.sbits.addItem("")
        self.gridLayout.addWidget(self.sbits, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_5.setEnabled(False)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.bsize = QtWidgets.QComboBox(self.dockWidgetContents)
        self.bsize.setEnabled(False)
        self.bsize.setObjectName("bsize")
        self.bsize.addItem("")
        self.bsize.addItem("")
        self.bsize.addItem("")
        self.bsize.addItem("")
        self.gridLayout.addWidget(self.bsize, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_6.setEnabled(False)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(52, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 6, 0, 1, 1)
        self.connect2dev = QtWidgets.QPushButton(self.dockWidgetContents)
        self.connect2dev.setObjectName("connect2dev")
        self.gridLayout.addWidget(self.connect2dev, 6, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 370, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 7, 0, 1, 1)
        self.boud = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.boud.setEnabled(False)
        self.boud.setMaximum(999999999)
        self.boud.setProperty("value", 115200)
        self.boud.setObjectName("boud")
        self.gridLayout.addWidget(self.boud, 1, 1, 1, 1)
        self.timeout = QtWidgets.QDoubleSpinBox(self.dockWidgetContents)
        self.timeout.setEnabled(False)
        self.timeout.setMaximum(10.0)
        self.timeout.setProperty("value", 1.0)
        self.timeout.setObjectName("timeout")
        self.gridLayout.addWidget(self.timeout, 5, 1, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.bsize.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DAG SQM Beta"))
        self.label_13.setText(_translate("MainWindow", "Interval"))
        self.label_14.setText(_translate("MainWindow", "Magnitude"))
        self.label_10.setText(_translate("MainWindow", "mag"))
        self.label_11.setText(_translate("MainWindow", "mag"))
        self.label_16.setText(_translate("MainWindow", "Flux"))
        self.label_12.setText(_translate("MainWindow", "cd/m2"))
        self.label_15.setText(_translate("MainWindow", "Temperature"))
        self.label_9.setText(_translate("MainWindow", "C"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Live"))
        self.label_7.setText(_translate("MainWindow", "Number of Samples"))
        self.label_8.setText(_translate("MainWindow", "Comments"))
        self.read.setText(_translate("MainWindow", "Read"))
        item = self.records.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "JD"))
        item = self.records.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mag(raw)"))
        item = self.records.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mag(new)"))
        item = self.records.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Temperature"))
        item = self.records.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Flux"))
        item = self.records.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "NoS"))
        item = self.records.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "VD"))
        item = self.records.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Comment"))
        self.remove_record.setText(_translate("MainWindow", "Remove"))
        self.export_records.setText(_translate("MainWindow", "Export"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Record"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Log"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This piece of software was created by <span style=\" font-weight:600; text-decoration: underline;\">Mohannad S.Niaei</span> for the DAG Project.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This software was created to drive data from an SQM-LU device.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">http://unihedron.com/projects/sqm-lu/</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Usage:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0) Connection:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">User need to connect to a SQM-LU device. User must indentify the connection port such as:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     For <span style=\" text-decoration: underline;\">Windows</span>: <span style=\" font-weight:600;\">COM[Number]</span> like: <span style=\" font-weight:600;\">COM4, COM5, etc</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     For <span style=\" text-decoration: underline;\">Linux</span>: <span style=\" font-weight:600;\">/dev/ttyUSB[number]</span> line: <span style=\" font-weight:600;\">/dev/ttyUSB0, /dev/ttyUSB1, etc </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1) Live</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">One can track the change of brightness in the environment using the <span style=\" font-weight:600;\">Live</span> tab.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Once you connected, the <span style=\" font-weight:600;\">Live</span> tab will be available. It will obtain data, only for display purpose, according to <span style=\" font-weight:600;\">Interval</span> Value</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2) Record</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">One can record <span style=\" font-weight:600;\">Bmpsa</span>, <span style=\" font-weight:600;\">NELM</span>, <span style=\" font-weight:600;\">Flux</span>, <span style=\" font-weight:600;\">Temperature</span> alongside <span style=\" font-weight:600;\">JD</span>, and <span style=\" font-weight:600;\">Data Validity</span> to a table and export it as CSV.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">http://unihedron.com/projects/darksky/cd/SQM-LU/SQM-LU_Users_manual.pdf</span> [Page 12 &amp; 13]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Once you connected, <span style=\" font-weight:600;\">Record</span> tab will be available. You can set a sample number and Comment for records.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You can delete any unwanted record line(s) and export the table to CSV.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mohammad S.Niaei: m.shemuni [at] gmail.com</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Help"))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Control Panel"))
        self.label.setText(_translate("MainWindow", "Port"))
        self.port.setText(_translate("MainWindow", "/dev/ttyUSB0"))
        self.label_2.setText(_translate("MainWindow", "Baudrate"))
        self.label_3.setText(_translate("MainWindow", "Parity"))
        self.parity.setItemText(0, _translate("MainWindow", "PARITY_NONE"))
        self.parity.setItemText(1, _translate("MainWindow", "PARITY_EVEN"))
        self.parity.setItemText(2, _translate("MainWindow", "PARITY_ODD"))
        self.parity.setItemText(3, _translate("MainWindow", "PARITY_MARK"))
        self.parity.setItemText(4, _translate("MainWindow", "PARITY_SPACE"))
        self.label_4.setText(_translate("MainWindow", "Stopbits"))
        self.sbits.setItemText(0, _translate("MainWindow", "STOPBITS_ONE"))
        self.sbits.setItemText(1, _translate("MainWindow", "STOPBITS_ONE_POINT_FIVE"))
        self.sbits.setItemText(2, _translate("MainWindow", "STOPBITS_TWO"))
        self.label_5.setText(_translate("MainWindow", "Bytesize"))
        self.bsize.setItemText(0, _translate("MainWindow", "FIVEBITS"))
        self.bsize.setItemText(1, _translate("MainWindow", "SIXBITS"))
        self.bsize.setItemText(2, _translate("MainWindow", "SEVENBITS"))
        self.bsize.setItemText(3, _translate("MainWindow", "EIGHTBITS"))
        self.label_6.setText(_translate("MainWindow", "Timeout"))
        self.connect2dev.setText(_translate("MainWindow", "Connect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

