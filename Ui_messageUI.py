# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\coderzgh\Documents\python-hack\第一章-Python编程基础\messageFly\messageUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_messageFly(object):
    def setupUi(self, messageFly):
        messageFly.setObjectName("messageFly")
        messageFly.resize(591, 305)
        self.label = QtWidgets.QLabel(messageFly)
        self.label.setGeometry(QtCore.QRect(70, 70, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(messageFly)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 72, 15))
        self.label_2.setObjectName("label_2")
        self.pushButtonStart = QtWidgets.QPushButton(messageFly)
        self.pushButtonStart.setGeometry(QtCore.QRect(240, 120, 92, 28))
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.lineEdit = QtWidgets.QLineEdit(messageFly)
        self.lineEdit.setGeometry(QtCore.QRect(140, 70, 301, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(messageFly)
        self.comboBox.setGeometry(QtCore.QRect(140, 120, 87, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButtonEnd = QtWidgets.QPushButton(messageFly)
        self.pushButtonEnd.setGeometry(QtCore.QRect(350, 120, 92, 28))
        self.pushButtonEnd.setObjectName("pushButtonEnd")
        self.label_3 = QtWidgets.QLabel(messageFly)
        self.label_3.setGeometry(QtCore.QRect(70, 160, 72, 15))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(messageFly)
        self.textEdit.setGeometry(QtCore.QRect(140, 160, 301, 87))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(messageFly)
        QtCore.QMetaObject.connectSlotsByName(messageFly)

    def retranslateUi(self, messageFly):
        _translate = QtCore.QCoreApplication.translate
        messageFly.setWindowTitle(_translate("messageFly", "messageFly"))
        self.label.setText(_translate("messageFly", "号码:"))
        self.label_2.setText(_translate("messageFly", "线程数:"))
        self.pushButtonStart.setText(_translate("messageFly", "开始轰炸"))
        self.comboBox.setItemText(0, _translate("messageFly", "1"))
        self.comboBox.setItemText(1, _translate("messageFly", "2"))
        self.comboBox.setItemText(2, _translate("messageFly", "3"))
        self.comboBox.setItemText(3, _translate("messageFly", "4"))
        self.comboBox.setItemText(4, _translate("messageFly", "5"))
        self.comboBox.setItemText(5, _translate("messageFly", "6"))
        self.comboBox.setItemText(6, _translate("messageFly", "7"))
        self.comboBox.setItemText(7, _translate("messageFly", "8"))
        self.comboBox.setItemText(8, _translate("messageFly", "9"))
        self.comboBox.setItemText(9, _translate("messageFly", "10"))
        self.pushButtonEnd.setText(_translate("messageFly", "结束轰炸"))
        self.label_3.setText(_translate("messageFly", "日志："))
