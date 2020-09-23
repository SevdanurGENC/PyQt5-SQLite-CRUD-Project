from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QTableWidgetItem 
from TelefonDefteriGUI import Ui_MainWindow
import sys
import sqlite3 as sql
import os 
os.system('python Connection.py')
os.system('python CreateTable.py')

global id, isim, soyisim, sehir, telefon, email

# Kullanicilar tablosunun alanlari (id INT, isim TEXT, soyisim TEXT, sehir TEXT, telefon TEXT, email TEXT)

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()  
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)     

        self.btnListeleClick()
        self.ui.btnListele.clicked.connect(self.btnListeleClick)
        self.ui.btnKaydet.clicked.connect(self.btnKaydetClick)
        self.ui.btnSil.clicked.connect(self.btnSilClick)
        self.ui.btnGuncelle.clicked.connect(self.btnGuncelleClick)
        self.ui.tblListele.clicked.connect(self.ListOnClick) 
 
    def btnTemizle(self):
        self.ui.txtID.clear()
        self.ui.txtIsim.clear()
        self.ui.txtSoyisim.clear()
        self.ui.txtSehir.clear()
        self.ui.txtTelefon.clear()
        self.ui.txtEmail.clear()

    def ListOnClick(self): 
        self.ui.txtID.setText(self.ui.tblListele.item(self.ui.tblListele.currentRow(), 0).text())
        self.ui.txtIsim.setText(self.ui.tblListele.item(self.ui.tblListele.currentRow(), 1).text())
        self.ui.txtSoyisim.setText(self.ui.tblListele.item(self.ui.tblListele.currentRow(), 2).text())
        self.ui.txtSehir.setText(self.ui.tblListele.item(self.ui.tblListele.currentRow(), 3).text())
        self.ui.txtTelefon.setText(self.ui.tblListele.item(self.ui.tblListele.currentRow(), 4).text())
        self.ui.txtEmail.setText(self.ui.tblListele.item(self.ui.tblListele.currentRow(), 5).text())
 
    def btnKaydetClick(self): 
        id = self.ui.txtID.text()
        isim = self.ui.txtIsim.text()
        soyisim = self.ui.txtSoyisim.text()
        sehir = self.ui.txtSehir.text()
        telefon = self.ui.txtTelefon.text()
        email = self.ui.txtEmail.text()

        try:
            self.conn = sql.connect("TelefonDefteri.db")
            self.c = self.conn.cursor() 
            self.c.execute("INSERT INTO Kullanicilar VALUES (?,?,?,?,?,?)",(id,isim,soyisim,sehir,telefon,email))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User is added successfully to the database.')
        except Exception:
            print('Error', 'Could not add student to the database.')
        
        self.btnTemizle()
        self.btnListeleClick()

    def btnListeleClick(self):  
        self.ui.tblListele.clear()
        self.ui.tblListele.setColumnCount(6)
        self.ui.tblListele.setHorizontalHeaderLabels(('ID','Isim','Soyisim','Sehir','Telefon','Email'))
        self.ui.tblListele.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        db = sql.connect('TelefonDefteri.db')
        cur = db.cursor()
        selectquery = "SELECT * FROM Kullanicilar"
        cur.execute(selectquery) 
        rows = cur.fetchall()
         
        self.ui.tblListele.setRowCount(len(rows))
        
        for satirIndeks, satirVeri in enumerate(rows):
            for sutunIndeks, sutunVeri in enumerate (satirVeri):
                self.ui.tblListele.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri))) 
    
    def btnGuncelleClick(self):  
        id = self.ui.txtID.text()
        isim = self.ui.txtIsim.text()
        soyisim = self.ui.txtSoyisim.text()
        sehir = self.ui.txtSehir.text()
        telefon = self.ui.txtTelefon.text()
        email = self.ui.txtEmail.text()

        try:
            self.conn = sql.connect("TelefonDefteri.db")
            self.c = self.conn.cursor()  
            self.c.execute("UPDATE Kullanicilar SET isim = ?, soyisim = ?, sehir = ?, \
                telefon = ?, email = ? WHERE id = ?",(isim,soyisim,sehir,telefon,email,id))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User is updated successfully to the database.')
        except Exception:
            print('Error', 'Could not update student to the database.')

        self.btnTemizle()
        self.btnListeleClick()

    def btnSilClick(self): 
        id = self.ui.txtID.text() 

        try:
            self.conn = sql.connect("TelefonDefteri.db")
            self.c = self.conn.cursor() 
            self.c.execute('DELETE FROM Kullanicilar WHERE id = ?  ', (id,))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User is deleted successfully from the database.')
        except Exception:
            print('Error', 'Could not delete student to the database.')
        
        self.btnTemizle()
        self.btnListeleClick()

            
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()