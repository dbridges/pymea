# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pymea/ui/PyMEAMainWindow.ui'
#
# Created: Thu Jan 15 10:15:44 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1392, 685)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainLayout = QtGui.QHBoxLayout()
        self.mainLayout.setObjectName("mainLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.visualizationComboBox = QtGui.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.visualizationComboBox.setFont(font)
        self.visualizationComboBox.setObjectName("visualizationComboBox")
        self.visualizationComboBox.addItem("")
        self.visualizationComboBox.addItem("")
        self.visualizationComboBox.addItem("")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.visualizationComboBox)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.rasterRowCountSlider = QtGui.QSlider(self.centralwidget)
        self.rasterRowCountSlider.setMinimumSize(QtCore.QSize(160, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rasterRowCountSlider.setFont(font)
        self.rasterRowCountSlider.setMinimum(2)
        self.rasterRowCountSlider.setMaximum(120)
        self.rasterRowCountSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rasterRowCountSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.rasterRowCountSlider.setTickInterval(0)
        self.rasterRowCountSlider.setObjectName("rasterRowCountSlider")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.rasterRowCountSlider)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.mainLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.mainLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1392, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.actionSave_to_Spreadsheet = QtGui.QAction(MainWindow)
        self.actionSave_to_Spreadsheet.setEnabled(False)
        self.actionSave_to_Spreadsheet.setObjectName("actionSave_to_Spreadsheet")
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionDefault = QtGui.QAction(MainWindow)
        self.actionDefault.setObjectName("actionDefault")
        self.actionAnalog_Waveform = QtGui.QAction(MainWindow)
        self.actionAnalog_Waveform.setObjectName("actionAnalog_Waveform")
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MEA Data Viewer", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Visualization", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Visualization", None, QtGui.QApplication.UnicodeUTF8))
        self.visualizationComboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Raster", None, QtGui.QApplication.UnicodeUTF8))
        self.visualizationComboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Flashing Spike", None, QtGui.QApplication.UnicodeUTF8))
        self.visualizationComboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "Analog Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Raster View Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Row Count", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Flashing Spike View Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Analog Data View Options", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_to_Spreadsheet.setText(QtGui.QApplication.translate("MainWindow", "Save to Spreadsheet...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_to_Spreadsheet.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDefault.setText(QtGui.QApplication.translate("MainWindow", "Default", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAnalog_Waveform.setText(QtGui.QApplication.translate("MainWindow", "Analog Waveform", None, QtGui.QApplication.UnicodeUTF8))
