# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LevelDataAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAbstractItemView, QMessageBox
from TcpClient import tcp_client_socket


class Ui_Dialog(object):
    def setupUi(self, Dialog, administratorsID):

        self.path = "icon"
        self.form = Dialog
        self.administratorsID = administratorsID
        self.leveldata = []

        Dialog.setObjectName("Dialog")
        Dialog.resize(766, 664)
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(20, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(15)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(383, 10, 20, 651))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tableWidget_level = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_level.setGeometry(QtCore.QRect(20, 60, 351, 581))
        self.tableWidget_level.setObjectName("tableView_level")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(410, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_add = QtWidgets.QPushButton(Dialog)
        self.pushButton_add.setGeometry(QtCore.QRect(660, 70, 71, 21))
        self.pushButton_add.setObjectName("pushButton_add")
        self.lineEdit_add = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_add.setGeometry(QtCore.QRect(500, 70, 131, 21))
        self.lineEdit_add.setInputMask("")
        self.lineEdit_add.setFrame(True)
        self.lineEdit_add.setReadOnly(False)
        self.lineEdit_add.setObjectName("lineEdit_add")
        self.label_add = QtWidgets.QLabel(Dialog)
        self.label_add.setGeometry(QtCore.QRect(420, 70, 71, 21))
        self.label_add.setObjectName("label_add")
        self.lineEdit_delete = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_delete.setGeometry(QtCore.QRect(500, 100, 131, 21))
        self.lineEdit_delete.setReadOnly(False)
        self.lineEdit_delete.setObjectName("lineEdit_delete")
        self.pushButton_delete = QtWidgets.QPushButton(Dialog)
        self.pushButton_delete.setGeometry(QtCore.QRect(660, 100, 71, 21))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.label_delete = QtWidgets.QLabel(Dialog)
        self.label_delete.setGeometry(QtCore.QRect(420, 100, 71, 21))
        self.label_delete.setObjectName("label_delete")
        self.pushButton_areachange = QtWidgets.QPushButton(Dialog)
        self.pushButton_areachange.setGeometry(QtCore.QRect(660, 230, 71, 21))
        self.pushButton_areachange.setObjectName("pushButton_areachange")
        self.lineEdit_areachange = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_areachange.setGeometry(QtCore.QRect(420, 230, 221, 21))
        self.lineEdit_areachange.setReadOnly(False)
        self.lineEdit_areachange.setObjectName("lineEdit_areachange")
        self.label_areachange = QtWidgets.QLabel(Dialog)
        self.label_areachange.setGeometry(QtCore.QRect(420, 200, 311, 21))
        self.label_areachange.setObjectName("label_areachange")
        self.label_minechange = QtWidgets.QLabel(Dialog)
        self.label_minechange.setGeometry(QtCore.QRect(420, 310, 311, 21))
        self.label_minechange.setObjectName("label_minechange")
        self.pushButton_minechange = QtWidgets.QPushButton(Dialog)
        self.pushButton_minechange.setGeometry(QtCore.QRect(660, 340, 71, 21))
        self.pushButton_minechange.setObjectName("pushButton_minechange")
        self.lineEdit_minechange = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_minechange.setGeometry(QtCore.QRect(420, 340, 221, 21))
        self.lineEdit_minechange.setReadOnly(False)
        self.lineEdit_minechange.setObjectName("lineEdit_minechange")
        self.label_goldchange = QtWidgets.QLabel(Dialog)
        self.label_goldchange.setGeometry(QtCore.QRect(420, 420, 311, 21))
        self.label_goldchange.setObjectName("label_goldchange")
        self.pushButton_goldchange = QtWidgets.QPushButton(Dialog)
        self.pushButton_goldchange.setGeometry(QtCore.QRect(660, 450, 71, 21))
        self.pushButton_goldchange.setObjectName("pushButton_goldchange")
        self.lineEdit_goldchange = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_goldchange.setGeometry(QtCore.QRect(420, 450, 221, 21))
        self.lineEdit_goldchange.setReadOnly(False)
        self.lineEdit_goldchange.setObjectName("lineEdit_goldchange")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.update_level()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_1.setText(_translate("Dialog", "关卡数据查询"))
        self.label_2.setText(_translate("Dialog", "关卡数据修改"))
        self.pushButton_add.setText(_translate("Dialog", "确认"))
        self.lineEdit_add.setPlaceholderText(_translate("Dialog", "请输入关卡名称"))
        self.label_add.setText(_translate("Dialog", "增加关卡："))
        self.lineEdit_delete.setPlaceholderText(_translate("Dialog", "请输入关卡id"))
        self.pushButton_delete.setText(_translate("Dialog", "确认"))
        self.label_delete.setText(_translate("Dialog", "删除关卡："))
        self.pushButton_areachange.setText(_translate("Dialog", "确认"))
        self.lineEdit_areachange.setPlaceholderText(_translate("Dialog", "示例:3@20@20"))
        self.label_areachange.setText(_translate("Dialog", "关卡雷区面积修改：输入关卡id@长@宽"))
        self.label_minechange.setText(_translate("Dialog", "关卡雷数修改：输入关卡id@雷数"))
        self.pushButton_minechange.setText(_translate("Dialog", "确认"))
        self.lineEdit_minechange.setPlaceholderText(_translate("Dialog", "示例:3@30"))
        self.label_goldchange.setText(_translate("Dialog", "积分金币规则修改：输入规则序号"))
        self.pushButton_goldchange.setText(_translate("Dialog", "确认"))
        self.lineEdit_goldchange.setPlaceholderText(_translate("Dialog", "示例:1"))

        self.pushButton_add.clicked.connect(self.add_level)
        self.pushButton_delete.clicked.connect(self.delete_level)
        self.pushButton_areachange.clicked.connect(self.change_area)
        self.pushButton_minechange.clicked.connect(self.change_mine)
        self.pushButton_goldchange.clicked.connect(self.change_gold)

    def update_level(self):
        self.leveldata.clear()
        tcp_client_socket.send("804 " + self.administratorsID)
        data_list = tcp_client_socket.rec().split()
        print(data_list)
        if data_list[0] == "805":
            for i in range(int((len(data_list) - 1) / 4)):
                temp = [data_list[i * 4 + 4], data_list[i * 4 + 1], data_list[i * 4 + 2], data_list[i * 4 + 3]]
                self.leveldata.append(temp)

        level_num = len(self.leveldata)
        self.tableWidget_level.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_level.setColumnCount(4)
        self.tableWidget_level.setRowCount(level_num)

        for i in range(level_num):  # 关卡数=行数
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_level.setVerticalHeaderItem(i, item)

        for i in range(4):  # 关卡名、长、宽、雷数四列
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
            self.tableWidget_level.setHorizontalHeaderItem(i, item)

        for i in range(level_num):
            for j in range(4):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_level.setItem(i, j, item)

        self.tableWidget_level.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_level.horizontalHeader().setDefaultSectionSize(98)
        self.tableWidget_level.horizontalHeader().setMinimumSectionSize(24)
        self.tableWidget_level.setSelectionBehavior(QAbstractItemView.SelectRows)

        for i in range(level_num):
            item = self.tableWidget_level.verticalHeaderItem(i)
            item.setText(str(i + 1))

        item = self.tableWidget_level.horizontalHeaderItem(0)
        item.setText("关卡名")
        item = self.tableWidget_level.horizontalHeaderItem(1)
        item.setText("长")
        item = self.tableWidget_level.horizontalHeaderItem(2)
        item.setText("宽")
        item = self.tableWidget_level.horizontalHeaderItem(3)
        item.setText("雷数")

        __sortingEnabled = self.tableWidget_level.isSortingEnabled()
        self.tableWidget_level.setSortingEnabled(False)
        self.tableWidget_level.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(level_num):
            for j in range(4):
                item = self.tableWidget_level.item(i, j)
                item.setText(str(self.leveldata[i][j]))

        self.tableWidget_level.setSortingEnabled(__sortingEnabled)

    def add_level(self):
        if self.lineEdit_add.text() is not None:
            tcp_client_socket.send("806 " + self.administratorsID + " 1 " + self.lineEdit_add.text())
            data_list = tcp_client_socket.rec().split()
            print(data_list)
            if data_list[0] == "807":
                if data_list[1] == "1":
                    self.update_level()
                    reply = QMessageBox.about(self.form, "提示", "修改成功")
                elif data_list[1] == "0":
                    reply = QMessageBox.about(self.form, "提示", "添加关卡失败")
        else:
            reply = QMessageBox.about(self.form, "提示", "关卡名不能为空")

    def delete_level(self):
        if self.lineEdit_delete.text() is not None:
            tcp_client_socket.send("806 " + self.administratorsID + " 2 " + self.lineEdit_delete.text())
            data_list = tcp_client_socket.rec().split()
            print(data_list)
            if data_list[0] == "807":
                if data_list[1] == "1":
                    self.update_level()
                    reply = QMessageBox.about(self.form, "提示", "修改成功")
                elif data_list[1] == "0":
                    reply = QMessageBox.about(self.form, "提示", "删除关卡失败")
        else:
            reply = QMessageBox.about(self.form, "提示", "关卡名不能为空")

    def change_area(self):
        if self.lineEdit_areachange.text() is not None:
            temp = self.lineEdit_areachange.text().split("@")
            if len(temp) == 3 and temp[1] is not None and temp[2] is not None and temp[1].isdecimal() and temp[
                2].isdecimal():
                data = "806 " + self.administratorsID + " 3 " + temp[0] + " " + temp[1] + " " + temp[2]
                tcp_client_socket.send(data)
                data_list = tcp_client_socket.rec().split()
                if data_list[0] == "807":
                    if data_list[1] == "1":
                        self.update_level()
                        reply = QMessageBox.about(self.form, "提示", "修改成功")
                    elif data_list[1] == "0":
                        reply = QMessageBox.about(self.form, "提示", "修改雷区面积失败")
            else:
                reply = QMessageBox.about(self.form, "提示", "请重新输入")
        else:
            reply = QMessageBox.about(self.form, "提示", "输入不能为空")

    def change_mine(self):
        if self.lineEdit_minechange.text() is not None:
            temp = self.lineEdit_minechange.text().split("@")
            if len(temp) == 2 and temp[1] is not None and temp[1].isdecimal():
                data = "806 " + self.administratorsID + " 4 " + temp[0] + " " + temp[1]
                tcp_client_socket.send(data)
                data_list = tcp_client_socket.rec().split()
                if data_list[0] == "807":
                    if data_list[1] == "1":
                        self.update_level()
                        reply = QMessageBox.about(self.form, "提示", "修改成功")
                    elif data_list[1] == "0":
                        reply = QMessageBox.about(self.form, "提示", "修改雷数失败")
            else:
                reply = QMessageBox.about(self.form, "提示", "请重新输入")
        else:
            reply = QMessageBox.about(self.form, "提示", "输入不能为空")

    def change_gold(self):
        if self.lineEdit_goldchange.text() is not None:
            tcp_client_socket.send("806 " + self.administratorsID + " 5 " + self.lineEdit_goldchange.text())
            data_list = tcp_client_socket.rec().split()
            if data_list[0] == "807":
                if data_list[1] == "1":
                    self.update_level()
                    reply = QMessageBox.about(self.form, "提示", "修改成功")
                elif data_list[1] == "0":
                    reply = QMessageBox.about(self.form, "提示", "修改积分金币规则失败")
        else:
            reply = QMessageBox.about(self.form, "提示", "输入不能为空")


"""if __name__ == "__main__":
    import sys


    tcp_client_socket.conn()
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(widget, "12341234")
    widget.show()
    sys.exit(app.exec_())"""