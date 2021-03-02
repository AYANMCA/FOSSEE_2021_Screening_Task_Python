from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import *
# from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *

import sys
import sqlite3
import time
import os


class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("INSERT")

        # self.setWindowTitle("Add Student")
        # self.setFixedWidth(300)
        # self.setFixedHeight(300)

        self.setWindowTitle("INSERT ANGLE SECTION DATA")
        self.setFixedWidth(600)
        self.setFixedHeight(1000)

        self.QBtn.clicked.connect(self.add_angle_data)

        layout = QVBoxLayout()

        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("ID")
        layout.addWidget(self.id_input)

        self.designation_input = QLineEdit()
        self.designation_input.setPlaceholderText("DESIGNATION")
        layout.addWidget(self.designation_input)

        self.MASS_input = QLineEdit()
        self.MASS_input.setPlaceholderText("MASS")
        layout.addWidget(self.MASS_input)

        self.Area_input = QLineEdit()
        self.Area_input.setPlaceholderText("AREA")
        layout.addWidget(self.Area_input)

        self.AXB_input = QLineEdit()
        self.AXB_input.setPlaceholderText("AXB")
        layout.addWidget(self.AXB_input)

        self.T_input = QLineEdit()
        self.T_input.setPlaceholderText("T")
        layout.addWidget(self.T_input)

        self.R1_input = QLineEdit()
        self.R1_input.setPlaceholderText("R1")
        layout.addWidget(self.R1_input)

        self.R2_input = QLineEdit()
        self.R2_input.setPlaceholderText("R2")
        layout.addWidget(self.R2_input)

        self.CZ_input = QLineEdit()
        self.CZ_input.setPlaceholderText("Cz")
        layout.addWidget(self.CZ_input)

        self.Cy_input = QLineEdit()
        self.Cy_input.setPlaceholderText("Cy")
        layout.addWidget(self.Cy_input)

        self.TAN_input = QLineEdit()
        self.TAN_input.setPlaceholderText("TAN")
        layout.addWidget(self.TAN_input)

        self.IZ_input = QLineEdit()
        self.IZ_input.setPlaceholderText("Iz")
        layout.addWidget(self.IZ_input)

        self.IY_input = QLineEdit()
        self.IY_input.setPlaceholderText("Iy")
        layout.addWidget(self.IY_input)

        self.Iu_max_input = QLineEdit()
        self.Iu_max_input.setPlaceholderText("IU(max)")
        layout.addWidget(self.Iu_max_input)

        self.Iv_min_input = QLineEdit()
        self.Iv_min_input.setPlaceholderText("Iv(min)")
        layout.addWidget(self.Iv_min_input)

        self.rz_input = QLineEdit()
        self.rz_input.setPlaceholderText("rz")
        layout.addWidget(self.rz_input)

        self.ry_input = QLineEdit()
        self.ry_input.setPlaceholderText("ry")
        layout.addWidget(self.ry_input)

        self.ru_max_input = QLineEdit()
        self.ru_max_input.setPlaceholderText("ru(max)")
        layout.addWidget(self.ru_max_input)

        self.rv_min_input = QLineEdit()
        self.rv_min_input.setPlaceholderText("rv(min)")
        layout.addWidget(self.rv_min_input)

        self.Zz_input = QLineEdit()
        self.Zz_input.setPlaceholderText("Zz")
        layout.addWidget(self.Zz_input)

        self.Zy_input = QLineEdit()
        self.Zy_input.setPlaceholderText("Zy")
        layout.addWidget(self.Zy_input)

        self.Zpz_input = QLineEdit()
        self.Zpz_input.setPlaceholderText("Zpz")
        layout.addWidget(self.Zpz_input)

        self.Zpy_input = QLineEdit()
        self.Zpy_input.setPlaceholderText("Zpy")
        layout.addWidget(self.Zpy_input)

        self.source_input = QLineEdit()
        self.source_input.setPlaceholderText("SOURCE")
        layout.addWidget(self.source_input)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def add_angle_data(self):


        print("func call")

        Id= -1
        DESIGNATION= ""
        MASS= -1
        Area= -1
        AXB= -1
        t= -1
        R1=-1
        R2=-1
        Cz=-1
        Cy=-1
        Tan= -1
        Iz=-1
        Iy=-1
        Iu_max= -1
        Iv_min= -1
        rz=-1
        ry=-1
        ru_max=-1
        rv_min=-1
        Zz=-1
        Zy=-1
        Zpz=-1
        Zpy=-1
        SOURCE= ""

        Id=self.id_input.text()
        DESIGNATION = self.designation_input.text()
        MASS = self.MASS_input.text()
        Area =self.Area_input.text()
        AXB = self.AXB_input.text()
        t = self.T_input.text()
        R1 = self.R1_input.text()
        R2 =self.R2_input.text()
        Cz = self.CZ_input.text()
        Cy = self.Cy_input.text()
        Tan =self.TAN_input.text()
        Iz = self.IZ_input.text()
        Iy = self.IY_input.text()
        Iu_max = self.Iu_max_input.text()
        Iv_min = self.Iv_min_input.text()
        rz = self.rz_input.text()
        ry = self.ry_input.text()
        ru_max =self.ru_max_input.text()
        rv_min =self.rv_min_input.text()
        Zz = self.Zz_input.text()
        Zy = self.Zy_input.text()
        Zpz = self.Zpz_input.text()
        Zpy = self.Zpy_input.text()
        SOURCE = self.source_input.text()
        print(Id,DESIGNATION, MASS, Area,AXB, t,  R1, R2, Cz, Cy,Tan, Iz,Iy, Iu_max, Iv_min, rz, ry,  ru_max, rv_min, Zz, Zy,Zpz, Zpy,SOURCE)

        try:
            self.con= sqlite3.connect("C:\PYTHON_PROJECT\DJANGO\PYQT_APP\steel_sections.sqlite")
            print("connection test 1")
            self.cur=self.con.cursor()

            self.cur.execute("INSERT INTO Angles(Id,Designation,Mass,Area,AXB,t,R1,R2,Cz,Cy,Tan,Iz,Iy,[Iu(max)],[Iv(min)],rz,ry,[ru(max)],[rv(min)],Zz,Zy,Zpz,Zpy,Source) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(Id,DESIGNATION, MASS, Area,AXB, t,  R1, R2, Cz, Cy,Tan, Iz,Iy, Iu_max, Iv_min, rz, ry,  ru_max, rv_min, Zz, Zy,Zpz, Zpy,SOURCE))
            print("query executed 1")

            self.con.commit()
            print("query commited")
            self.cur.close()
            self.con.close()

            QMessageBox.information(QMessageBox(), 'Successful', 'ANGLE SECTION DATA SUCCESSFULLY ADDED TO THE DATABASE.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add ANGLE SECTION DATA to the database.')



class InsertDialog1(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog1, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("INSERT")

        # self.setWindowTitle("Add Student")
        # self.setFixedWidth(300)
        # self.setFixedHeight(300)

        self.setWindowTitle("INSERT BEAM SECTION DATA")
        self.setFixedWidth(600)
        self.setFixedHeight(1000)

        self.QBtn.clicked.connect(self.add_BEAMdata)

        layout = QVBoxLayout()

        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("ID")
        layout.addWidget(self.id_input)

        self.designation_input = QLineEdit()
        self.designation_input.setPlaceholderText("DESIGNATION")
        layout.addWidget(self.designation_input)

        self.MASS_input = QLineEdit()
        self.MASS_input.setPlaceholderText("MASS")
        layout.addWidget(self.MASS_input)

        self.Area_input = QLineEdit()
        self.Area_input.setPlaceholderText("AREA")
        layout.addWidget(self.Area_input)

        self.D_input = QLineEdit()
        self.D_input.setPlaceholderText("D")
        layout.addWidget(self.D_input)



        self.B_input = QLineEdit()
        self.B_input.setPlaceholderText("B")
        layout.addWidget(self.B_input)

        self.TW_input = QLineEdit()
        self.TW_input.setPlaceholderText("TW")
        layout.addWidget(self.TW_input)

        self.T_input = QLineEdit()
        self.T_input.setPlaceholderText("T")
        layout.addWidget(self.T_input)

        self.FlangeSlope = QLineEdit()
        self.FlangeSlope.setPlaceholderText("FlangeSlope")
        layout.addWidget(self.FlangeSlope)


        self.R1_input = QLineEdit()
        self.R1_input.setPlaceholderText("R1")
        layout.addWidget(self.R1_input)

        self.R2_input = QLineEdit()
        self.R2_input.setPlaceholderText("R2")
        layout.addWidget(self.R2_input)

        self.IZ_input = QLineEdit()
        self.IZ_input.setPlaceholderText("Iz")
        layout.addWidget(self.IZ_input)

        self.IY_input = QLineEdit()
        self.IY_input.setPlaceholderText("Iy")
        layout.addWidget(self.IY_input)



        self.rz_input = QLineEdit()
        self.rz_input.setPlaceholderText("rz")
        layout.addWidget(self.rz_input)

        self.ry_input = QLineEdit()
        self.ry_input.setPlaceholderText("ry")
        layout.addWidget(self.ry_input)



        self.Zz_input = QLineEdit()
        self.Zz_input.setPlaceholderText("Zz")
        layout.addWidget(self.Zz_input)

        self.Zy_input = QLineEdit()
        self.Zy_input.setPlaceholderText("Zy")
        layout.addWidget(self.Zy_input)

        self.Zpz_input = QLineEdit()
        self.Zpz_input.setPlaceholderText("Zpz")
        layout.addWidget(self.Zpz_input)

        self.Zpy_input = QLineEdit()
        self.Zpy_input.setPlaceholderText("Zpy")
        layout.addWidget(self.Zpy_input)

        self.source_input = QLineEdit()
        self.source_input.setPlaceholderText("SOURCE")
        layout.addWidget(self.source_input)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def add_BEAMdata(self):


        print("func call")

        Id= -1
        DESIGNATION= ""
        MASS= -1
        Area= -1

        D= -1
        B= -1
        TW=-1
        T=-1

        FlangeSlope=-1
        R1=-1
        R2=-1
        Iz=-1
        Iy=-1

        rz=-1
        ry=-1

        Zz=-1
        Zy=-1
        Zpz=-1
        Zpy=-1

        SOURCE= ""

        Id=self.id_input.text()
        DESIGNATION = self.designation_input.text()
        MASS = self.MASS_input.text()
        Area =self.Area_input.text()
        D= self.D_input.text()
        B = self.B_input.text()
        TW=self.TW_input.text()
        T = self.T_input.text()
        FlangeSlope=self.FlangeSlope.text()
        R1 = self.R1_input.text()
        R2 =self.R2_input.text()

        Iz = self.IZ_input.text()
        Iy = self.IY_input.text()

        rz = self.rz_input.text()
        ry = self.ry_input.text()


        Zz = self.Zz_input.text()
        Zy = self.Zy_input.text()

        Zpz = self.Zpz_input.text()
        Zpy = self.Zpy_input.text()
        SOURCE = self.source_input.text()

        try:
            self.con= sqlite3.connect("C:\PYTHON_PROJECT\DJANGO\PYQT_APP\steel_sections.sqlite")
            print("connection test 1")
            self.cur=self.con.cursor()
            print(Id, DESIGNATION, MASS, Area, D, B, TW, T, FlangeSlope, R1, R2, Iz, Iy, rz, ry, Zz, Zy, Zpz, Zpy,SOURCE)


            self.cur.execute("INSERT INTO Beams (Id, Designation, Mass, Area, D, B, tw, T, FlangeSlope, R1, R2, Iz, Iy, rz, ry, Zz, Zy, Zpz,Zpy,Source) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(Id,DESIGNATION, MASS, Area, D,B, TW, T, FlangeSlope, R1,R2, Iz, Iy, rz, ry, Zz,Zy,Zpz,Zpy,SOURCE))
            print("query executed 1")

            self.con.commit()
            print("query commited")
            self.cur.close()
            self.con.close()

            QMessageBox.information(QMessageBox(), 'Successful', 'BEAM SECTION DATA SUCCESSFULLY ADDED TO THE DATABASE.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add BEAM SECTION DATA to the database.')



class InsertDialog2(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog2, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("INSERT")

        # self.setWindowTitle("Add Student")
        # self.setFixedWidth(300)
        # self.setFixedHeight(300)

        self.setWindowTitle("INSERT CHANNEL SECTION DATA")
        self.setFixedWidth(600)
        self.setFixedHeight(1000)

        self.QBtn.clicked.connect(self.add_channel_data)

        layout = QVBoxLayout()

        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("ID")
        layout.addWidget(self.id_input)

        self.designation_input = QLineEdit()
        self.designation_input.setPlaceholderText("DESIGNATION")
        layout.addWidget(self.designation_input)

        self.MASS_input = QLineEdit()
        self.MASS_input.setPlaceholderText("MASS")
        layout.addWidget(self.MASS_input)

        self.Area_input = QLineEdit()
        self.Area_input.setPlaceholderText("AREA")
        layout.addWidget(self.Area_input)

        self.D_input = QLineEdit()
        self.D_input.setPlaceholderText("D")
        layout.addWidget(self.D_input)



        self.B_input = QLineEdit()
        self.B_input.setPlaceholderText("B")
        layout.addWidget(self.B_input)

        self.TW_input = QLineEdit()
        self.TW_input.setPlaceholderText("TW")
        layout.addWidget(self.TW_input)

        self.T_input = QLineEdit()
        self.T_input.setPlaceholderText("T")
        layout.addWidget(self.T_input)

        self.FlangeSlope = QLineEdit()
        self.FlangeSlope.setPlaceholderText("FlangeSlope")
        layout.addWidget(self.FlangeSlope)


        self.R1_input = QLineEdit()
        self.R1_input.setPlaceholderText("R1")
        layout.addWidget(self.R1_input)

        self.R2_input = QLineEdit()
        self.R2_input.setPlaceholderText("R2")
        layout.addWidget(self.R2_input)

        self.CY_input = QLineEdit()
        self.CY_input.setPlaceholderText("CY")
        layout.addWidget(self.CY_input)

        self.IZ_input = QLineEdit()
        self.IZ_input.setPlaceholderText("Iz")
        layout.addWidget(self.IZ_input)

        self.IY_input = QLineEdit()
        self.IY_input.setPlaceholderText("Iy")
        layout.addWidget(self.IY_input)



        self.rz_input = QLineEdit()
        self.rz_input.setPlaceholderText("rz")
        layout.addWidget(self.rz_input)

        self.ry_input = QLineEdit()
        self.ry_input.setPlaceholderText("ry")
        layout.addWidget(self.ry_input)



        self.Zz_input = QLineEdit()
        self.Zz_input.setPlaceholderText("Zz")
        layout.addWidget(self.Zz_input)

        self.Zy_input = QLineEdit()
        self.Zy_input.setPlaceholderText("Zy")
        layout.addWidget(self.Zy_input)

        self.Zpz_input = QLineEdit()
        self.Zpz_input.setPlaceholderText("Zpz")
        layout.addWidget(self.Zpz_input)

        self.Zpy_input = QLineEdit()
        self.Zpy_input.setPlaceholderText("Zpy")
        layout.addWidget(self.Zpy_input)

        self.source_input = QLineEdit()
        self.source_input.setPlaceholderText("SOURCE")
        layout.addWidget(self.source_input)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def add_channel_data(self):


        print("func call")

        Id= -1
        DESIGNATION= ""
        MASS= -1
        Area= -1

        D= -1
        B= -1
        TW=-1
        T=-1

        FlangeSlope=-1
        R1=-1
        R2=-1
        CY=-1

        Iz=-1
        Iy=-1

        rz=-1
        ry=-1

        Zz=-1
        Zy=-1
        Zpz=-1
        Zpy=-1

        SOURCE= ""

        Id=self.id_input.text()
        DESIGNATION = self.designation_input.text()
        MASS = self.MASS_input.text()
        Area =self.Area_input.text()
        D= self.D_input.text()
        B = self.B_input.text()
        TW=self.TW_input.text()
        T = self.T_input.text()
        FlangeSlope=self.FlangeSlope.text()
        R1 = self.R1_input.text()
        R2 =self.R2_input.text()
        CY = self.CY_input.text()

        Iz = self.IZ_input.text()
        Iy = self.IY_input.text()

        rz = self.rz_input.text()
        ry = self.ry_input.text()


        Zz = self.Zz_input.text()
        Zy = self.Zy_input.text()

        Zpz = self.Zpz_input.text()
        Zpy = self.Zpy_input.text()
        SOURCE = self.source_input.text()

        try:
            self.con= sqlite3.connect("C:\PYTHON_PROJECT\DJANGO\PYQT_APP\steel_sections.sqlite")
            print("connection test 1")
            self.cur=self.con.cursor()
            print(Id, DESIGNATION, MASS, Area, D, B, TW, T, FlangeSlope, R1, R2, CY,Iz, Iy, rz, ry, Zz, Zy, Zpz, Zpy,SOURCE)


            self.cur.execute("INSERT INTO Channels (Id, Designation, Mass, Area, D, B, tw, T, FlangeSlope, R1, R2, Cy,Iz, Iy, rz, ry, Zz, Zy, Zpz,Zpy,Source) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(Id,DESIGNATION, MASS, Area, D,B, TW, T, FlangeSlope, R1,R2,CY,Iz, Iy, rz, ry, Zz,Zy,Zpz,Zpy,SOURCE))
            print("query executed 1")

            self.con.commit()
            print("query commited")
            self.cur.close()
            self.con.close()

            QMessageBox.information(QMessageBox(), 'Successful', 'CHANNELS SECTION DATA SUCCESSFULLY ADDED TO THE DATABASE.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add CHANNELS SECTION DATA to the database.')




class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Search")

        self.setWindowTitle("Search user")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.searchstudent)
        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText("Roll No.")
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def searchstudent(self):

        searchrol = ""
        searchrol = self.searchinput.text()
        try:
            self.conn = sqlite3.connect("steel_sections.db")
            self.c = self.conn.cursor()
            result = self.c.execute("SELECT * from Angles WHERE Id=" + str(searchrol))
            row = result.fetchone()
            serachresult = "Rollno : " + str(row[0]) + '\n' + "Name : " + str(row[1]) + '\n' + "Branch : " + str(
                row[2]) + '\n' + "Sem : " + str(row[3]) + '\n' + "Address : " + str(row[4])
            QMessageBox.information(QMessageBox(), 'Successful', serachresult)
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Find student from the database.')


class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Delete")

        self.setWindowTitle("Delete Student")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.deletestudent)
        layout = QVBoxLayout()

        self.deleteinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.deleteinput.setValidator(self.onlyInt)
        self.deleteinput.setPlaceholderText("Roll No.")
        layout.addWidget(self.deleteinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def deletestudent(self):

        delrol = ""
        delrol = self.deleteinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("DELETE from students WHERE roll=" + str(delrol))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Deleted From Table Successful')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Delete student from the database.')


class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        self.setFixedWidth(500)
        self.setFixedHeight(250)

        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        self.setWindowTitle("About")
        title = QLabel("STEEL SECTION MANAGER")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        labelpic = QLabel()
        pixmap = QPixmap('icon/dexter.jpg')
        pixmap = pixmap.scaledToWidth(275)
        labelpic.setPixmap(pixmap)
        labelpic.setFixedHeight(150)

        layout.addWidget(title)

        layout.addWidget(QLabel("v2.0"))
        layout.addWidget(QLabel("Copyright Okay Dexter 2019"))
        layout.addWidget(labelpic)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # self.setWindowIcon(QIcon('icon/g2.png'))  # window icon



        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        self.show()

        self.file_menu = self.menuBar().addMenu("&File")
        self.help_menu = self.menuBar().addMenu("&About")



        self.setWindowTitle("STEEL SECTION MAINTAINER")
        self.setMinimumSize(1366, 800)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

    def handlePaintRequest(self, printer):
        document = QTextDocument()
        cursor = QTextCursor(document)
        model = self.table.model()
        table = cursor.insertTable(
            model.rowCount(), model.columnCount())
        for row in range(table.rows()):
            for column in range(table.columns()):
                cursor.insertText(model.item(row, column).text())
                cursor.movePosition(QTextCursor.NextCell)
        document.print_(printer)


    def delete(self):
        dlg = DeleteDialog()
        dlg.exec_()

    def search(self):
        dlg = SearchDialog()
        dlg.exec_()

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()



class MyTabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget,self).__init__(parent)
        self.layout = QGridLayout(self)



        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.resize(1400,800)

        # Add tabs
        self.tabs.addTab(self.tab1, "ANGLE SECTION ")
        self.tabs.addTab(self.tab2, "BEAM SECTION ")
        self.tabs.addTab(self.tab3, "CHANNEL SECTION ")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)


        self.tableWidget = QTableWidget()
        # self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(24)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
             QHeaderView.Stretch)

        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.tableWidget.setHorizontalHeaderLabels((
                                         "ID.", "DESIGNATION", "MASS", "Area", "AXB", "t", "R1", "R2", "Cz", "Cy",
                                         "Tan?", "Iz", "Iv", "Iu(max)", "Iv(min)", "rz", "ry", "ru(max)", "rv(min)",
                                         "Zz", "Zy", "Zpz", "Zpy", "SOURCE"))


        self.toolbar = QToolBar()
        self.toolbar.setMovable(False)
        self.btn_ac_add_data = QAction(QIcon("icon/add1.jpg"), "ADD ANGLE'S SECTION DATA", self)  # add student icon
        self.btn_ac_add_data.triggered.connect(self.insert)
        self.btn_ac_add_data.setStatusTip("Add ANGLE SECTION DATA")
        self.toolbar.addAction(self.btn_ac_add_data)

        self.btn_ac_refresh = QAction(QIcon("icon/r3.png"), "Refresh", self)  # refresh icon
        self.btn_ac_refresh.triggered.connect(self.loaddata)
        self.btn_ac_refresh.setStatusTip("Refresh Table")
        self.toolbar.addAction(self.btn_ac_refresh)
        #
        # btn_ac_search = QAction(QIcon("icon/s1.png"), "Search", self)  # search icon
        # btn_ac_search.triggered.connect(self.search)
        # btn_ac_search.setStatusTip("Search User")
        # toolbar.addAction(btn_ac_search)
        #
        # btn_ac_delete = QAction(QIcon("icon/d1.png"), "Delete", self)
        # btn_ac_delete.triggered.connect(self.delete)
        # btn_ac_delete.setStatusTip("Delete User")
        # toolbar.addAction(btn_ac_delete)
        #
        # add_data_action = QAction(QIcon("icon/add1.jpg"), "Insert Student", self)
        # add_data_action.triggered.connect(self.insert)
        # file_menu.addAction(add_data_action)
        #
        # searchuser_action = QAction(QIcon("icon/s1.png"), "Search Student", self)
        # searchuser_action.triggered.connect(self.search)
        # file_menu.addAction(searchuser_action)
        #
        # deluser_action = QAction(QIcon("icon/d1.png"), "Delete", self)
        # deluser_action.triggered.connect(self.delete)
        # file_menu.addAction(deluser_action)

        # about_action = QAction(QIcon("icon/i1.png"), "Developer", self)  # info icon
        # about_action.triggered.connect(self.about)
        # help_menu.addAction(about_action)

        # tab1 part
        self.tab1.layout.addWidget(self.toolbar)


        self.tab1.layout.addWidget(self.tableWidget)
        self.tab1.setLayout(self.tab1.layout)

        # tab2 part
        self.tab2.layout = QVBoxLayout(self)

        self.tableWidget1 = QTableWidget()
        # self.setCentralWidget(self.tableWidget)
        self.tableWidget1.setAlternatingRowColors(True)
        self.tableWidget1.setColumnCount(20)
        self.tableWidget1.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget1.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget1.horizontalHeader().setStretchLastSection(True)
        self.tableWidget1.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

        self.tableWidget1.verticalHeader().setVisible(False)
        self.tableWidget1.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget1.verticalHeader().setStretchLastSection(False)

        self.tableWidget1.setHorizontalHeaderLabels(("Id", "Designation", "Mass", "Area", "D", "B", "tw", "T", "FlangeSlope", "R1", "R2", "Iz", "Iy", "rz", "ry", "Zz", "Zy", "Zpz", "Zpy", "Source"))


        self.toolbar = QToolBar()
        self.toolbar.setMovable(False)
        self.btn_ac_add_data = QAction(QIcon("icon/add1.jpg"), "ADD BEAM SECTION DATA", self)  # add student icon
        self.btn_ac_add_data.triggered.connect(self.insert1)
        self.btn_ac_add_data.setStatusTip("Add ANGLE SECTION DATA")
        self.toolbar.addAction(self.btn_ac_add_data)

        self.btn_ac_refresh = QAction(QIcon("icon/r3.png"), "Refresh", self)  # refresh icon
        self.btn_ac_refresh.triggered.connect(self.loaddata1)
        self.btn_ac_refresh.setStatusTip("Refresh Table")
        self.toolbar.addAction(self.btn_ac_refresh)
        #
        # btn_ac_search = QAction(QIcon("icon/s1.png"), "Search", self)  # search icon
        # btn_ac_search.triggered.connect(self.search)
        # btn_ac_search.setStatusTip("Search User")
        # toolbar.addAction(btn_ac_search)
        #
        # btn_ac_delete = QAction(QIcon("icon/d1.png"), "Delete", self)
        # btn_ac_delete.triggered.connect(self.delete)
        # btn_ac_delete.setStatusTip("Delete User")
        # toolbar.addAction(btn_ac_delete)
        #
        # add_data_action = QAction(QIcon("icon/add1.jpg"), "Insert Student", self)
        # add_data_action.triggered.connect(self.insert)
        # file_menu.addAction(add_data_action)
        #
        # searchuser_action = QAction(QIcon("icon/s1.png"), "Search Student", self)
        # searchuser_action.triggered.connect(self.search)
        # file_menu.addAction(searchuser_action)
        #
        # deluser_action = QAction(QIcon("icon/d1.png"), "Delete", self)
        # deluser_action.triggered.connect(self.delete)
        # file_menu.addAction(deluser_action)

        # about_action = QAction(QIcon("icon/i1.png"), "Developer", self)  # info icon
        # about_action.triggered.connect(self.about)
        # help_menu.addAction(about_action)

        # Add tabs to widget
        self.layout.addWidget(self.tabs,0,0)
        self.setLayout(self.layout)

        self.tab2.layout.addWidget(self.toolbar)

        self.tab2.layout.addWidget(self.tableWidget1)
        self.tab2.setLayout(self.tab2.layout)

    # tab3 part
        self.tab3.layout = QVBoxLayout(self)

        self.tableWidget2 = QTableWidget()
    # self.setCentralWidget(self.tableWidget)
        self.tableWidget2.setAlternatingRowColors(True)
        self.tableWidget2.setColumnCount(20)
        self.tableWidget2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget2.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget2.horizontalHeader().setSectionResizeMode(
        QHeaderView.Stretch)

        self.tableWidget2.verticalHeader().setVisible(False)
        self.tableWidget2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget2.verticalHeader().setStretchLastSection(False)

        self.tableWidget2.setHorizontalHeaderLabels((
                                                "Id", "Designation", "Mass", "Area", "D", "B", "tw", "T", "FlangeSlope",
                                                "R1", "R2", "Cy","Iz", "Iy", "rz", "ry", "Zz", "Zy", "Zpz", "Zpy", "Source"))

        self.toolbar = QToolBar()
        self.toolbar.setMovable(False)
        self.btn_ac_add_data = QAction(QIcon("icon/add1.jpg"), " ADD CHANNEL SECTION DATA", self)  # add student icon
        self.btn_ac_add_data.triggered.connect(self.insert2)
        self.btn_ac_add_data.setStatusTip("ADD CHANNEL SECTION DATA")
        self.toolbar.addAction(self.btn_ac_add_data)

        self.btn_ac_refresh = QAction(QIcon("icon/r3.png"), "Refresh", self)  # refresh icon
        self.btn_ac_refresh.triggered.connect(self.loaddata2)
        self.btn_ac_refresh.setStatusTip("Refresh Table")
        self.toolbar.addAction(self.btn_ac_refresh)
    #
    # btn_ac_search = QAction(QIcon("icon/s1.png"), "Search", self)  # search icon
    # btn_ac_search.triggered.connect(self.search)
    # btn_ac_search.setStatusTip("Search User")
    # toolbar.addAction(btn_ac_search)
    #
    # btn_ac_delete = QAction(QIcon("icon/d1.png"), "Delete", self)
    # btn_ac_delete.triggered.connect(self.delete)
    # btn_ac_delete.setStatusTip("Delete User")
    # toolbar.addAction(btn_ac_delete)
    #
    # add_data_action = QAction(QIcon("icon/add1.jpg"), "Insert Student", self)
    # add_data_action.triggered.connect(self.insert)
    # file_menu.addAction(add_data_action)
    #
    # searchuser_action = QAction(QIcon("icon/s1.png"), "Search Student", self)
    # searchuser_action.triggered.connect(self.search)
    # file_menu.addAction(searchuser_action)
    #
    # deluser_action = QAction(QIcon("icon/d1.png"), "Delete", self)
    # deluser_action.triggered.connect(self.delete)
    # file_menu.addAction(deluser_action)

    # about_action = QAction(QIcon("icon/i1.png"), "Developer", self)  # info icon
    # about_action.triggered.connect(self.about)
    # help_menu.addAction(about_action)

    # Add tabs to widget
        self.layout.addWidget(self.tabs, 0, 0)
        self.setLayout(self.layout)

        self.tab3.layout.addWidget(self.toolbar)

        self.tab3.layout.addWidget(self.tableWidget2)
        self.tab3.setLayout(self.tab3.layout)

    def insert(self):
        dlg=InsertDialog()
        dlg.exec_()

    def insert1(self):
        dlg = InsertDialog1()
        dlg.exec_()
    def insert2(self):
        dlg = InsertDialog2()
        dlg.exec_()

    def loaddata(self):
        self.connection = sqlite3.connect("C:\PYTHON_PROJECT\DJANGO\PYQT_APP\steel_sections.sqlite")
        query ="SELECT * FROM Angles"
        result =self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
           self.tableWidget.insertRow(row_number)
           for column_number, data in enumerate(row_data):
             self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.connection.close()

    def loaddata1(self):
        self.connection = sqlite3.connect("C:\PYTHON_PROJECT\DJANGO\PYQT_APP\steel_sections.sqlite")
        query = "SELECT * FROM Beams"
        result = self.connection.execute(query)
        print("helo test")
        self.tableWidget1.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget1.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget1.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.connection.close()

    def loaddata2(self):
        self.connection = sqlite3.connect("C:\PYTHON_PROJECT\DJANGO\PYQT_APP\steel_sections.sqlite")
        query = "SELECT * FROM Channels"
        result = self.connection.execute(query)
        print("helo test")
        self.tableWidget2.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget2.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget2.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.connection.close()


app = QApplication(sys.argv)
if (QDialog.Accepted == True):

    window = MainWindow()
    window.show()
    # window.loaddata()
sys.exit(app.exec_())
