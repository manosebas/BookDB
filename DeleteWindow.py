# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeleteWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

class Ui_DeleteWindow(object):
    def setupUi(self, DeleteWindow):
        DeleteWindow.setObjectName("DeleteWindow")
        DeleteWindow.resize(265, 166)

        self.textEditId = QtWidgets.QTextEdit(DeleteWindow)
        self.textEditId.setGeometry(QtCore.QRect(90, 20, 151, 31))
        self.textEditId.setObjectName("textEditId")

        self.label = QtWidgets.QLabel(DeleteWindow)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")

        self.botonUpdateLibro = QtWidgets.QPushButton(DeleteWindow)
        self.botonUpdateLibro.setGeometry(QtCore.QRect(20, 70, 221, 28))
        self.botonUpdateLibro.setObjectName("botonUpdateLibro")
        self.botonUpdateLibro.clicked.connect(self.clickDelete)

        self.textoActualizacionDelete = QtWidgets.QLabel(DeleteWindow)
        self.textoActualizacionDelete.setGeometry(QtCore.QRect(10, 110, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textoActualizacionDelete.setFont(font)
        self.textoActualizacionDelete.setText("")
        self.textoActualizacionDelete.setAlignment(QtCore.Qt.AlignCenter)
        self.textoActualizacionDelete.setObjectName("textoActualizacionDelete")

        self.retranslateUi(DeleteWindow)
        QtCore.QMetaObject.connectSlotsByName(DeleteWindow)

    def retranslateUi(self, DeleteWindow):
        _translate = QtCore.QCoreApplication.translate
        DeleteWindow.setWindowTitle(_translate("DeleteWindow", "Delete"))
        self.label.setText(_translate("DeleteWindow", "Id :"))
        self.botonUpdateLibro.setText(_translate("DeleteWindow", "Delete"))

    def clickDelete(self):
        id = int(self.textEditId.toPlainText())

        db_config = read_db_config()

        query = "DELETE FROM libros WHERE idLibros = %s"

        try:
            # connect to the database server
            conn = MySQLConnection(**db_config)

            # execute the query
            cursor = conn.cursor()
            cursor.execute(query, (id,))

            self.textoActualizacionDelete.setText("Se elimino el libro")
            # accept the change
            conn.commit()

        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeleteWindow = QtWidgets.QWidget()
    ui = Ui_DeleteWindow()
    ui.setupUi(DeleteWindow)
    DeleteWindow.show()
    sys.exit(app.exec_())
