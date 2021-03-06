# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pymea/ui/PyMEAMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1146, 664)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.toolbarWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolbarWidget.sizePolicy().hasHeightForWidth())
        self.toolbarWidget.setSizePolicy(sizePolicy)
        self.toolbarWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.toolbarWidget.setObjectName("toolbarWidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.toolbarWidget)
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.visualizationComboBox = QtWidgets.QComboBox(self.toolbarWidget)
        self.visualizationComboBox.setObjectName("visualizationComboBox")
        self.visualizationComboBox.addItem("")
        self.visualizationComboBox.addItem("")
        self.visualizationComboBox.addItem("")
        self.visualizationComboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.visualizationComboBox)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.stackedWidget = QtWidgets.QStackedWidget(self.toolbarWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.rasterPage = QtWidgets.QWidget()
        self.rasterPage.setObjectName("rasterPage")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.rasterPage)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.rasterPage)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.sortRasterComboBox = QtWidgets.QComboBox(self.rasterPage)
        self.sortRasterComboBox.setObjectName("sortRasterComboBox")
        self.sortRasterComboBox.addItem("")
        self.sortRasterComboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.sortRasterComboBox)
        self.dimConductanceCheckBox = QtWidgets.QCheckBox(self.rasterPage)
        self.dimConductanceCheckBox.setObjectName("dimConductanceCheckBox")
        self.horizontalLayout_5.addWidget(self.dimConductanceCheckBox)
        self.rowCountLabel = QtWidgets.QLabel(self.rasterPage)
        self.rowCountLabel.setObjectName("rowCountLabel")
        self.horizontalLayout_5.addWidget(self.rowCountLabel)
        self.rasterRowCountSlider = QtWidgets.QSlider(self.rasterPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rasterRowCountSlider.sizePolicy().hasHeightForWidth())
        self.rasterRowCountSlider.setSizePolicy(sizePolicy)
        self.rasterRowCountSlider.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rasterRowCountSlider.setFont(font)
        self.rasterRowCountSlider.setMinimum(2)
        self.rasterRowCountSlider.setMaximum(120)
        self.rasterRowCountSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rasterRowCountSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.rasterRowCountSlider.setTickInterval(0)
        self.rasterRowCountSlider.setObjectName("rasterRowCountSlider")
        self.horizontalLayout_5.addWidget(self.rasterRowCountSlider)
        self.horizontalLayout_5.setStretch(4, 1)
        self.stackedWidget.addWidget(self.rasterPage)
        self.flashingSpikePage = QtWidgets.QWidget()
        self.flashingSpikePage.setObjectName("flashingSpikePage")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.flashingSpikePage)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.speedLabel_2 = QtWidgets.QLabel(self.flashingSpikePage)
        self.speedLabel_2.setObjectName("speedLabel_2")
        self.horizontalLayout_6.addWidget(self.speedLabel_2)
        self.flashingSpikeTimescaleComboBox = QtWidgets.QComboBox(self.flashingSpikePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flashingSpikeTimescaleComboBox.sizePolicy().hasHeightForWidth())
        self.flashingSpikeTimescaleComboBox.setSizePolicy(sizePolicy)
        self.flashingSpikeTimescaleComboBox.setObjectName("flashingSpikeTimescaleComboBox")
        self.flashingSpikeTimescaleComboBox.addItem("")
        self.flashingSpikeTimescaleComboBox.addItem("")
        self.flashingSpikeTimescaleComboBox.addItem("")
        self.flashingSpikeTimescaleComboBox.addItem("")
        self.flashingSpikeTimescaleComboBox.addItem("")
        self.flashingSpikeTimescaleComboBox.addItem("")
        self.flashingSpikeTimescaleComboBox.addItem("")
        self.flashingSpikeTimescaleComboBox.addItem("")
        self.horizontalLayout_6.addWidget(self.flashingSpikeTimescaleComboBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.stackedWidget.addWidget(self.flashingSpikePage)
        self.analogPage = QtWidgets.QWidget()
        self.analogPage.setObjectName("analogPage")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.analogPage)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.scaleLabel = QtWidgets.QLabel(self.analogPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scaleLabel.sizePolicy().hasHeightForWidth())
        self.scaleLabel.setSizePolicy(sizePolicy)
        self.scaleLabel.setObjectName("scaleLabel")
        self.horizontalLayout_7.addWidget(self.scaleLabel)
        self.analogScaleSpinBox = QtWidgets.QDoubleSpinBox(self.analogPage)
        self.analogScaleSpinBox.setDecimals(0)
        self.analogScaleSpinBox.setMinimum(1.0)
        self.analogScaleSpinBox.setMaximum(20000.0)
        self.analogScaleSpinBox.setSingleStep(20.0)
        self.analogScaleSpinBox.setProperty("value", 150.0)
        self.analogScaleSpinBox.setObjectName("analogScaleSpinBox")
        self.horizontalLayout_7.addWidget(self.analogScaleSpinBox)
        self.showSpikesCheckBox = QtWidgets.QCheckBox(self.analogPage)
        self.showSpikesCheckBox.setObjectName("showSpikesCheckBox")
        self.horizontalLayout_7.addWidget(self.showSpikesCheckBox)
        self.grayConductanceCheckBox = QtWidgets.QCheckBox(self.analogPage)
        self.grayConductanceCheckBox.setChecked(False)
        self.grayConductanceCheckBox.setObjectName("grayConductanceCheckBox")
        self.horizontalLayout_7.addWidget(self.grayConductanceCheckBox)
        self.filterCheckBox = QtWidgets.QCheckBox(self.analogPage)
        self.filterCheckBox.setObjectName("filterCheckBox")
        self.horizontalLayout_7.addWidget(self.filterCheckBox)
        self.filterLowSpinBox = QtWidgets.QDoubleSpinBox(self.analogPage)
        self.filterLowSpinBox.setKeyboardTracking(False)
        self.filterLowSpinBox.setMaximum(50000.0)
        self.filterLowSpinBox.setProperty("value", 200.0)
        self.filterLowSpinBox.setObjectName("filterLowSpinBox")
        self.horizontalLayout_7.addWidget(self.filterLowSpinBox)
        self.label = QtWidgets.QLabel(self.analogPage)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.filterHighSpinBox = QtWidgets.QDoubleSpinBox(self.analogPage)
        self.filterHighSpinBox.setKeyboardTracking(False)
        self.filterHighSpinBox.setMaximum(50000.0)
        self.filterHighSpinBox.setProperty("value", 4000.0)
        self.filterHighSpinBox.setObjectName("filterHighSpinBox")
        self.horizontalLayout_7.addWidget(self.filterHighSpinBox)
        self.stackedWidget.addWidget(self.analogPage)
        self.conductionPage = QtWidgets.QWidget()
        self.conductionPage.setObjectName("conductionPage")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.conductionPage)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.stackedWidget.addWidget(self.conductionPage)
        self.horizontalLayout_8.addWidget(self.stackedWidget)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.horizontalLayout_8.setStretch(3, 1)
        self.verticalLayout_2.addWidget(self.toolbarWidget)
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setObjectName("mainLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 200))
        self.widget.setObjectName("widget")
        self.mainLayout.addWidget(self.widget)
        self.verticalLayout_2.addLayout(self.mainLayout)
        self.verticalLayout_2.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = MEAViewerStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSave_to_Spreadsheet = QtWidgets.QAction(MainWindow)
        self.actionSave_to_Spreadsheet.setEnabled(False)
        self.actionSave_to_Spreadsheet.setObjectName("actionSave_to_Spreadsheet")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionDefault = QtWidgets.QAction(MainWindow)
        self.actionDefault.setObjectName("actionDefault")
        self.actionAnalog_Waveform = QtWidgets.QAction(MainWindow)
        self.actionAnalog_Waveform.setObjectName("actionAnalog_Waveform")
        self.actionRaster = QtWidgets.QAction(MainWindow)
        self.actionRaster.setObjectName("actionRaster")
        self.actionFlashingSpikes = QtWidgets.QAction(MainWindow)
        self.actionFlashingSpikes.setObjectName("actionFlashingSpikes")
        self.actionAnalogGrid = QtWidgets.QAction(MainWindow)
        self.actionAnalogGrid.setObjectName("actionAnalogGrid")

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        self.visualizationComboBox.currentIndexChanged['int'].connect(self.stackedWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MEA Data Viewer"))
        self.visualizationComboBox.setItemText(0, _translate("MainWindow", "Raster"))
        self.visualizationComboBox.setItemText(1, _translate("MainWindow", "Flashing Spike"))
        self.visualizationComboBox.setItemText(2, _translate("MainWindow", "Analog"))
        self.visualizationComboBox.setItemText(3, _translate("MainWindow", "Conduction"))
        self.label_2.setText(_translate("MainWindow", "Sort By"))
        self.sortRasterComboBox.setItemText(0, _translate("MainWindow", "Rate"))
        self.sortRasterComboBox.setItemText(1, _translate("MainWindow", "Latency"))
        self.dimConductanceCheckBox.setText(_translate("MainWindow", "Dim Conductance"))
        self.rowCountLabel.setText(_translate("MainWindow", "Row Count"))
        self.speedLabel_2.setText(_translate("MainWindow", "Speed"))
        self.flashingSpikeTimescaleComboBox.setItemText(0, _translate("MainWindow", "1x"))
        self.flashingSpikeTimescaleComboBox.setItemText(1, _translate("MainWindow", "1/2x"))
        self.flashingSpikeTimescaleComboBox.setItemText(2, _translate("MainWindow", "1/20x"))
        self.flashingSpikeTimescaleComboBox.setItemText(3, _translate("MainWindow", "1/100x"))
        self.flashingSpikeTimescaleComboBox.setItemText(4, _translate("MainWindow", "1/200x"))
        self.flashingSpikeTimescaleComboBox.setItemText(5, _translate("MainWindow", "1/400x"))
        self.flashingSpikeTimescaleComboBox.setItemText(6, _translate("MainWindow", "1/800x"))
        self.flashingSpikeTimescaleComboBox.setItemText(7, _translate("MainWindow", "1/1600x"))
        self.scaleLabel.setText(_translate("MainWindow", "Scale"))
        self.analogScaleSpinBox.setSuffix(_translate("MainWindow", " uV"))
        self.showSpikesCheckBox.setText(_translate("MainWindow", "Spikes"))
        self.grayConductanceCheckBox.setText(_translate("MainWindow", "Grey Conductance"))
        self.filterCheckBox.setText(_translate("MainWindow", "Bandpass Filter"))
        self.filterLowSpinBox.setSuffix(_translate("MainWindow", " Hz"))
        self.label.setText(_translate("MainWindow", "to"))
        self.filterHighSpinBox.setSuffix(_translate("MainWindow", " Hz"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSave_to_Spreadsheet.setText(_translate("MainWindow", "Save to Spreadsheet..."))
        self.actionSave_to_Spreadsheet.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionDefault.setText(_translate("MainWindow", "Default"))
        self.actionAnalog_Waveform.setText(_translate("MainWindow", "Analog Waveform"))
        self.actionRaster.setText(_translate("MainWindow", "Raster"))
        self.actionRaster.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionFlashingSpikes.setText(_translate("MainWindow", "Flashing Spikes"))
        self.actionFlashingSpikes.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionAnalogGrid.setText(_translate("MainWindow", "Analog Grid"))
        self.actionAnalogGrid.setShortcut(_translate("MainWindow", "Ctrl+A"))

from pymea.ui.widgets import MEAViewerStatusBar
