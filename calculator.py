import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon




class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm,self).__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon("calculator_icon.jpg"))
        self.initUI()


    def initUI(self):
        self.lbl_sayi1= QtWidgets.QLabel(self)
        self.lbl_sayi1.setText("Sayi 1: ")
        self.lbl_sayi1.move(50,30)
        
        self.txt_sayi1= QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150,30)
        self.txt_sayi1.resize(200,32)

        self.lbl_sayi2= QtWidgets.QLabel(self)
        self.lbl_sayi2.setText("Sayi 2: ")
        self.lbl_sayi2.move(50,80)

        self.txt_sayi2= QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150,80)
        self.txt_sayi2.resize(200,32)
        
        self.btn_topla= QtWidgets.QPushButton(self)
        self.btn_topla.setText("Topla")
        self.btn_topla.move(150,130)
        self.btn_topla.clicked.connect(self.toplama)

        self.btn_cikar= QtWidgets.QPushButton(self)
        self.btn_cikar.setText("Cikar")
        self.btn_cikar.move(150,170)
        self.btn_cikar.clicked.connect(self.cikarma)

        self.btn_carp= QtWidgets.QPushButton(self)
        self.btn_carp.setText("Carp")
        self.btn_carp.move(150,210)
        self.btn_carp.clicked.connect(self.carpma)

        self.btn_bol= QtWidgets.QPushButton(self)
        self.btn_bol.setText("Bol")
        self.btn_bol.move(150,250)
        self.btn_bol.clicked.connect(self.bolme)

        self.lbl_sonuc= QtWidgets.QLabel(self)
        self.lbl_sonuc.setText("Sonuc: ")
        self.lbl_sonuc.move(50,290)
        self.lbl_sonuc.resize(500,32)


    def toplama(self):
            result= int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
            self.lbl_sonuc.setText("Sonuc: "+ str(result))

    def cikarma(self):
        result= int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
        self.lbl_sonuc.setText("Sonuc: "+ str(result))

    def carpma(self):
        result= int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        self.lbl_sonuc.setText("Sonuc: "+ str(result))
    
    def bolme(self):
        try:
            result= int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
            self.lbl_sonuc.setText("Sonuc: "+ str(result))
        except ZeroDivisionError as err:
            print(f"{err} \nSayi 2, 0'dan farkli olmalidir.")
            self.lbl_sonuc.setText("Sonuc: " + str(f"{err} \n Uyarı: Sayi 2, 0'dan farkli olmalidir"))

        




        
def app():
    app= QApplication(sys.argv)
    win= MainForm()
    win.show()
    sys.exit(app.exec_())

app()
