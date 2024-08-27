# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdateWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

class Ui_UpdateWindow(object):
    def setupUi(self, UpdateWindow):
        UpdateWindow.setObjectName("UpdateWindow")
        UpdateWindow.resize(375, 340)

        self.textEditUpdateId = QtWidgets.QTextEdit(UpdateWindow)
        self.textEditUpdateId.setGeometry(QtCore.QRect(190, 20, 151, 31))
        self.textEditUpdateId.setObjectName("textEditUpdateId")

        self.textEditUpdateNombre = QtWidgets.QTextEdit(UpdateWindow)
        self.textEditUpdateNombre.setGeometry(QtCore.QRect(190, 70, 151, 31))
        self.textEditUpdateNombre.setObjectName("textEditUpdateNombre")

        self.textEditUpdatePaginas = QtWidgets.QTextEdit(UpdateWindow)
        self.textEditUpdatePaginas.setGeometry(QtCore.QRect(190, 170, 151, 31))
        self.textEditUpdatePaginas.setObjectName("textEditUpdatePaginas")

        self.label_3 = QtWidgets.QLabel(UpdateWindow)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")

        self.label = QtWidgets.QLabel(UpdateWindow)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")

        self.label_4 = QtWidgets.QLabel(UpdateWindow)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")

        self.label_2 = QtWidgets.QLabel(UpdateWindow)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")

        self.textEditUpdatePrecio = QtWidgets.QTextEdit(UpdateWindow)
        self.textEditUpdatePrecio.setGeometry(QtCore.QRect(190, 120, 151, 31))
        self.textEditUpdatePrecio.setObjectName("textEditUpdatePrecio")

        self.textoActualizacionUpdate = QtWidgets.QLabel(UpdateWindow)
        self.textoActualizacionUpdate.setGeometry(QtCore.QRect(40, 290, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textoActualizacionUpdate.setFont(font)
        self.textoActualizacionUpdate.setText("")
        self.textoActualizacionUpdate.setAlignment(QtCore.Qt.AlignCenter)
        self.textoActualizacionUpdate.setObjectName("textoActualizacionUpdate")

        self.botonUpdateLibro = QtWidgets.QPushButton(UpdateWindow)
        self.botonUpdateLibro.setGeometry(QtCore.QRect(10, 240, 341, 28))
        self.botonUpdateLibro.setObjectName("botonUpdateLibro")
        self.botonUpdateLibro.clicked.connect(self.clickUpdate)

        self.retranslateUi(UpdateWindow)
        QtCore.QMetaObject.connectSlotsByName(UpdateWindow)

    def retranslateUi(self, UpdateWindow):
        _translate = QtCore.QCoreApplication.translate
        UpdateWindow.setWindowTitle(_translate("UpdateWindow", "Update"))
        self.botonUpdateLibro.setText(_translate("UpdateWindow", "Update"))
        self.label_3.setText(_translate("UpdateWindow", "Precio :"))
        self.label.setText(_translate("UpdateWindow", "Id :"))
        self.label_4.setText(_translate("UpdateWindow", "Paginas :"))
        self.label_2.setText(_translate("UpdateWindow", "Nombre :"))

    def clickUpdate(self):
        id = int(self.textEditUpdateId.toPlainText())
        nombre = str(self.textEditUpdateNombre.toPlainText())
        precio = int(self.textEditUpdatePrecio.toPlainText())
        paginas = int(self.textEditUpdatePaginas.toPlainText())

        query = """UPDATE libros
                SET nombre = %s,
                precio = %s,
                paginas = %s,
                WHERE idLibros = %s """
        args = (nombre, precio, paginas, id)

        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)

            cursor = conn.cursor()
            cursor.execute(query, args)
            #cursor.executemany(arreglo) #Para insertar varias cosas al mismo tiempo

            self.textoActualizacionUpdate.setText("Se actualizo el libro")

            if cursor.lastrowid:
                print('last insert id', cursor.lastrowid)
            else:
                print('last insert id not found')

            conn.commit()
        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UpdateWindow = QtWidgets.QWidget()
    ui = Ui_UpdateWindow()
    ui.setupUi(UpdateWindow)
    UpdateWindow.show()
    sys.exit(app.exec_())
