# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_form.ui'
#
# Created: Sat Mar 24 16:06:02 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(520, 187)
        self.gridLayoutWidget = QtGui.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 501, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblMetafile = QtGui.QLabel(self.gridLayoutWidget)
        self.lblMetafile.setObjectName("lblMetafile")
        self.gridLayout_2.addWidget(self.lblMetafile, 0, 0, 1, 1)
        self.lblMaskfile = QtGui.QLabel(self.gridLayoutWidget)
        self.lblMaskfile.setObjectName("lblMaskfile")
        self.gridLayout_2.addWidget(self.lblMaskfile, 1, 0, 1, 1)
        self.txtMetafile = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txtMetafile.setObjectName("txtMetafile")
        self.gridLayout_2.addWidget(self.txtMetafile, 0, 1, 1, 1)
        self.txtMaskfile = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txtMaskfile.setObjectName("txtMaskfile")
        self.gridLayout_2.addWidget(self.txtMaskfile, 1, 1, 1, 1)
        self.btnOpenMetafile = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnOpenMetafile.setObjectName("btnOpenMetafile")
        self.gridLayout_2.addWidget(self.btnOpenMetafile, 0, 2, 1, 1)
        self.btnOpenMaskfile = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnOpenMaskfile.setObjectName("btnOpenMaskfile")
        self.gridLayout_2.addWidget(self.btnOpenMaskfile, 1, 2, 1, 1)
        self.chkDefault = QtGui.QCheckBox(self.gridLayoutWidget)
        self.chkDefault.setChecked(True)
        self.chkDefault.setTristate(False)
        self.chkDefault.setObjectName("chkDefault")
        self.gridLayout_2.addWidget(self.chkDefault, 2, 0, 1, 1)
        self.lblTmpfolder = QtGui.QLabel(self.gridLayoutWidget)
        self.lblTmpfolder.setEnabled(False)
        self.lblTmpfolder.setObjectName("lblTmpfolder")
        self.gridLayout_2.addWidget(self.lblTmpfolder, 3, 0, 1, 1)
        self.txtTmpfolder = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txtTmpfolder.setEnabled(False)
        self.txtTmpfolder.setObjectName("txtTmpfolder")
        self.gridLayout_2.addWidget(self.txtTmpfolder, 3, 1, 1, 1)
        self.btnOpenTmpfolder = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnOpenTmpfolder.setEnabled(False)
        self.btnOpenTmpfolder.setObjectName("btnOpenTmpfolder")
        self.gridLayout_2.addWidget(self.btnOpenTmpfolder, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btnOk = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnOk.setObjectName("btnOk")
        self.gridLayout_4.addWidget(self.btnOk, 0, 1, 1, 1)
        self.btnCancel = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnCancel.setObjectName("btnCancel")
        self.gridLayout_4.addWidget(self.btnCancel, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.txtMetafile, self.btnOpenMetafile)
        Dialog.setTabOrder(self.btnOpenMetafile, self.txtMaskfile)
        Dialog.setTabOrder(self.txtMaskfile, self.btnOpenMaskfile)
        Dialog.setTabOrder(self.btnOpenMaskfile, self.chkDefault)
        Dialog.setTabOrder(self.chkDefault, self.txtTmpfolder)
        Dialog.setTabOrder(self.txtTmpfolder, self.btnOpenTmpfolder)
        Dialog.setTabOrder(self.btnOpenTmpfolder, self.btnOk)
        Dialog.setTabOrder(self.btnOk, self.btnCancel)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Acca Plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMetafile.setText(QtGui.QApplication.translate("Dialog", "Select metafile", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMaskfile.setText(QtGui.QApplication.translate("Dialog", "Select maskfile", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOpenMetafile.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOpenMaskfile.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.chkDefault.setText(QtGui.QApplication.translate("Dialog", "Use default", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTmpfolder.setText(QtGui.QApplication.translate("Dialog", "Select tmp folder", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOpenTmpfolder.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOk.setText(QtGui.QApplication.translate("Dialog", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
