# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Wed Mar 21 12:57:21 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(588, 216)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setModal(True)
        self.mainW = QtGui.QWidget(Dialog)
        self.mainW.setGeometry(QtCore.QRect(9, 9, 571, 201))
        self.mainW.setObjectName("mainW")
        self.layoutWidget = QtGui.QWidget(self.mainW)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 565, 196))
        self.layoutWidget.setObjectName("layoutWidget")
        self.mainLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.mainLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.mainLayout.setObjectName("mainLayout")
        self.gridLayout2 = QtGui.QGridLayout()
        self.gridLayout2.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.gridLayout2.setObjectName("gridLayout2")
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setObjectName("label_4")
        self.gridLayout2.addWidget(self.label_4, 0, 0, 1, 1)
        self.txtInPath = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtInPath.sizePolicy().hasHeightForWidth())
        self.txtInPath.setSizePolicy(sizePolicy)
        self.txtInPath.setMinimumSize(QtCore.QSize(350, 0))
        self.txtInPath.setObjectName("txtInPath")
        self.gridLayout2.addWidget(self.txtInPath, 0, 1, 1, 1)
        self.btnInPath = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnInPath.sizePolicy().hasHeightForWidth())
        self.btnInPath.setSizePolicy(sizePolicy)
        self.btnInPath.setMaximumSize(QtCore.QSize(20, 16777215))
        self.btnInPath.setObjectName("btnInPath")
        self.gridLayout2.addWidget(self.btnInPath, 0, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setObjectName("label_5")
        self.gridLayout2.addWidget(self.label_5, 1, 0, 1, 1)
        self.txtOutPath = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtOutPath.sizePolicy().hasHeightForWidth())
        self.txtOutPath.setSizePolicy(sizePolicy)
        self.txtOutPath.setMinimumSize(QtCore.QSize(350, 0))
        self.txtOutPath.setObjectName("txtOutPath")
        self.gridLayout2.addWidget(self.txtOutPath, 1, 1, 1, 1)
        self.btnOutPath = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOutPath.sizePolicy().hasHeightForWidth())
        self.btnOutPath.setSizePolicy(sizePolicy)
        self.btnOutPath.setMaximumSize(QtCore.QSize(20, 16777215))
        self.btnOutPath.setObjectName("btnOutPath")
        self.gridLayout2.addWidget(self.btnOutPath, 1, 2, 1, 1)
        self.mainLayout.addLayout(self.gridLayout2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.btnTmpPath = QtGui.QPushButton(self.layoutWidget)
        self.btnTmpPath.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnTmpPath.sizePolicy().hasHeightForWidth())
        self.btnTmpPath.setSizePolicy(sizePolicy)
        self.btnTmpPath.setMaximumSize(QtCore.QSize(20, 16777215))
        self.btnTmpPath.setObjectName("btnTmpPath")
        self.gridLayout.addWidget(self.btnTmpPath, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.chkDefault = QtGui.QCheckBox(self.layoutWidget)
        self.chkDefault.setChecked(True)
        self.chkDefault.setObjectName("chkDefault")
        self.gridLayout.addWidget(self.chkDefault, 1, 0, 1, 1)
        self.txtTmpPath = QtGui.QLineEdit(self.layoutWidget)
        self.txtTmpPath.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtTmpPath.sizePolicy().hasHeightForWidth())
        self.txtTmpPath.setSizePolicy(sizePolicy)
        self.txtTmpPath.setMinimumSize(QtCore.QSize(350, 0))
        self.txtTmpPath.setObjectName("txtTmpPath")
        self.gridLayout.addWidget(self.txtTmpPath, 0, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnGo = QtGui.QPushButton(self.layoutWidget)
        self.btnGo.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnGo.setObjectName("btnGo")
        self.horizontalLayout.addWidget(self.btnGo)
        spacerItem = QtGui.QSpacerItem(120, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.mainLayout.addLayout(self.gridLayout)
        self.secondW = QtGui.QWidget(Dialog)
        self.secondW.setGeometry(QtCore.QRect(9, 9, 571, 201))
        self.secondW.setObjectName("secondW")
        self.verticalLayoutWidget = QtGui.QWidget(self.secondW)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 571, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblStatus = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblStatus.sizePolicy().hasHeightForWidth())
        self.lblStatus.setSizePolicy(sizePolicy)
        self.lblStatus.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lblStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStatus.setObjectName("lblStatus")
        self.verticalLayout.addWidget(self.lblStatus)
        self.progressBar = QtGui.QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Select input data (metafile):", None, QtGui.QApplication.UnicodeUTF8))
        self.btnInPath.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Select folder for mask file:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOutPath.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTmpPath.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Select folder for tmp data:", None, QtGui.QApplication.UnicodeUTF8))
        self.chkDefault.setText(QtGui.QApplication.translate("Dialog", "Use default", None, QtGui.QApplication.UnicodeUTF8))
        self.txtTmpPath.setText(QtGui.QApplication.translate("Dialog", "/tmp", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGo.setText(QtGui.QApplication.translate("Dialog", "Go!", None, QtGui.QApplication.UnicodeUTF8))
        self.lblStatus.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

