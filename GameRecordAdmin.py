# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GameRecordAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import json
from QDialog import myDialog
from PyQt5.QtWidgets import QApplication, QAbstractItemView, QHeaderView, QListWidget, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from TcpClient import tcp_client_socket
from GameRecordUI import Ui_Dialog as getRecord


class Ui_Dialog(object):
    def setupUi(self, Dialog, administratorID):
        self.dialog = Dialog
        self.administratorID = administratorID
        Dialog.setObjectName("Dialog")
        Dialog.resize(485, 379)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 200, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 270, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.combatID = QtWidgets.QLineEdit(Dialog)
        self.combatID.setGeometry(QtCore.QRect(160, 270, 181, 51))
        self.combatID.setObjectName("combatID")
        self.playerID = QtWidgets.QLineEdit(Dialog)
        self.playerID.setGeometry(QtCore.QRect(160, 100, 181, 51))
        self.playerID.setObjectName("playerID")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 100, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.combatButton = QtWidgets.QPushButton(Dialog)
        self.combatButton.setGeometry(QtCore.QRect(370, 280, 81, 31))
        self.combatButton.setObjectName("combatButton")
        self.playerButton = QtWidgets.QPushButton(Dialog)
        self.playerButton.setGeometry(QtCore.QRect(370, 110, 81, 31))
        self.playerButton.setObjectName("playerButton")

        self.retranslateUi(Dialog)
        self.combatButton.clicked.connect(self.clickCombat)
        self.playerButton.clicked.connect(self.clickRecord)


        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "战绩管理"))
        self.label_2.setText(_translate("Dialog", "对局查询"))
        self.label_4.setText(_translate("Dialog", "对局ID："))
        self.label.setText(_translate("Dialog", "战绩查询"))
        self.label_3.setText(_translate("Dialog", "玩家ID："))
        self.combatButton.setText(_translate("Dialog", "查询"))
        self.playerButton.setText(_translate("Dialog", "查询"))

    def clickRecord(self):
        if self.playerID.text() == "" :
            QMessageBox.about(self.dialog, "提示", "请输入玩家ID！")
        else:
            tcp_client_socket.send("822 " + self.administratorID + " " + self.playerID.text())
            data_list_823 = tcp_client_socket.rec().split("@")

            if data_list_823[1] == "0":
                QMessageBox.about(self.dialog, "提示", "该玩家不存在，请重新输入！")
                self.playerID.setText("")
            elif data_list_823[1] == "1":
                recordData = json.loads(data_list_823[2])
                self.dialog.setEnabled(False)  # 设置本窗口无法选择
                form = myDialog()
                form.setWindowModality(2)  # 使本窗口无法选中
                ui = getRecord()
                ui.setupUi(form, self.administratorID, self.playerID.text(), recordData)
                form.show()
                form.exec_()
                self.dialog.setEnabled(True)
                self.playerID.setText("")

    def clickCombat(self):
        if self.combatID.text() == "" :
            QMessageBox.about(self.dialog, "提示", "请输入对局ID！")
        else:
            tcp_client_socket.send("824 " + self.administratorID + " " + self.combatID.text())
            data_list_825 = tcp_client_socket.rec().split("@")

            if data_list_825[1] == "0":
                QMessageBox.about(self.dialog, "提示", "该对局不存在，请重新输入！")
                self.combatID.setText("")
            elif data_list_825[1] == "1":
                combatData = json.loads(data_list_825[2])
                print(combatData)
                QMessageBox.about(self.dialog, "对局信息", "对局ID：" + self.combatID.text() + "\n\n玩家1ID："
                                  + str(combatData[0]) + "\n玩家2ID：" + str(combatData[1]) + "\n\n难度："
                                  + str(combatData[2]) + "\n开始时间：" + str(combatData[3])
                                  + "\n结束时间：" + str(combatData[4]) + "\n\n玩家1的积分变化："
                                  + str(combatData[5]) + "\n玩家2的积分变化：" + str(combatData[6]) + "\n")
                self.combatID.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = myDialog()
    ui = Ui_Dialog()
    ui.setupUi(form, 1111111)
    form.show()
    app.exec_()
    sys.exit()