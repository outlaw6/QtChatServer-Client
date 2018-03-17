# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\py\chat.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    from socket import AF_INET, socket, SOCK_STREAM
    from threading import Thread
    BUFSIZ = 1024

    client_socket = None
    socket = None
    receive_thread = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(461, 409)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 421, 231))
        self.textBrowser.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.textBrowser.setAutoFillBackground(True)
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 260, 421, 20))
        self.lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(350, 290, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.callback)
        
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 320, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 350, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 320, 47, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 350, 47, 13))
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(200, 320, 221, 51))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(16, 20, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 380, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.connection)
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "SEND"))
        self.label.setText(_translate("Dialog", "SERVER"))
        self.label_2.setText(_translate("Dialog", "PORT"))
        self.groupBox.setTitle(_translate("Dialog", "STATUS"))
        self.label_3.setText(_translate("Dialog", "DISCONNECTED"))
        self.pushButton_2.setText(_translate("Dialog", "CONNECT"))
    def receive(self):
        """Handles receiving of messages."""
        while True:
            try:
                msg = self.client_socket.recv(self.BUFSIZ).decode("utf8")
                self.textBrowser.append(msg)
            except OSError:  # Possibly client has left the chat.
                break
    def connection(self):

        HOST = self.lineEdit_2.text()
        print(HOST)
        PORT = int(self.lineEdit_3.text())
        ADDR = (HOST, PORT)

        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(ADDR)

        self.receive_thread = Thread(target=self.receive)
        self.receive_thread.start()
        self.label_3.setText("CONNECTED")

    def callback(self):
        msg = self.lineEdit.text()
        self.textBrowser.append(msg)
        self.client_socket.send(bytes(msg,"utf8"))
        if msg == "{quit}":
            self.client_socket.close()
            self.label_3.setText("DISCONNECTED")
        #msg.setText("")
        self.lineEdit.setText("")
                                      
        
if __name__ == "__main__":
    import sys
    from socket import AF_INET, socket, SOCK_STREAM
    from threading import Thread
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

