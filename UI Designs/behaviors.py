# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'behaviors.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog():
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(581, 335)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 421, 21))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_color = QtWidgets.QLabel(Dialog)
        self.label_color.setGeometry(QtCore.QRect(360, 70, 31, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_color.setFont(font)
        self.label_color.setObjectName("label_color")
        self.label_behaviorGroup = QtWidgets.QLabel(Dialog)
        self.label_behaviorGroup.setGeometry(QtCore.QRect(200, 70, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_behaviorGroup.setFont(font)
        self.label_behaviorGroup.setAutoFillBackground(False)
        self.label_behaviorGroup.setObjectName("label_behaviorGroup")
        self.label_behavior = QtWidgets.QLabel(Dialog)
        self.label_behavior.setGeometry(QtCore.QRect(70, 70, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_behavior.setFont(font)
        self.label_behavior.setObjectName("label_behavior")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(450, 300, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 270, 121, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select behaviors to be included in the final ethogram and match them with their group:"))
        self.label_color.setText(_translate("Dialog", "Color"))
        self.label_behaviorGroup.setText(_translate("Dialog", "Behavior-Group"))
        self.label_behavior.setText(_translate("Dialog", "Behavior"))
        self.pushButton.setText(_translate("Dialog", "Plot"))
        self.pushButton_2.setText(_translate("Dialog", "Additional settings"))
