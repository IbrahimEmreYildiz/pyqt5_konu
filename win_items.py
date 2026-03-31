import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon






def window():

    def clicked(self): # Burada txt_name ve txt_surname'ye erişebilmek için window fonksiyonunun içinde tanımladık normalde class yapısı kurup erişerek daha rahat halledebiliriz
        print("Butona basildi Name:" + txt_name.text() + " - " + "Surname: "+ txt_surname.text())

    app= QApplication(sys.argv) #Komut bilgisini uygulamaya aktarır sys.argv
    win= QMainWindow() #Pencere oluşturur
    win.setWindowTitle("MetropolGYM Kayıt Formu") # Uygulamanın ismini ayarlar
    win.setGeometry(400, 400, 800, 500) # Yatayda 400 Dikeyda 400 boşluk bırakır pencere boyutu da 800'e 500 olur Önce yatay yazılır
    win.setWindowIcon(QIcon('icon.jpg')) # Uygulamanın icon'unu değiştirebiliriz.
    win.setToolTip("my tooltip")
    lbl_name= QtWidgets.QLabel(win) # Oluşturduğumuz nesneyi win'e aktarır
    lbl_name.setText("Adiniz: ") # Window'a Text ekler
    lbl_name.move(50, 30) # Ekledeğimiz nesneyi kaydırır
    
    lbl_surname= QtWidgets.QLabel(win)
    lbl_surname.setText("Soyadiniz: ")
    lbl_surname.move(50, 70)

    txt_name= QtWidgets.QLineEdit(win) #QLineEdit bir text kutucuğu oluşturur
    txt_name.move(150,30)
    
    txt_surname= QtWidgets.QLineEdit(win)
    txt_surname.move(150, 70)

    btn_save= QtWidgets.QPushButton(win) #Bu da buton oluşturur. 
    btn_save.setText("Kaydet") # Butonun üstüne yazı yazdık
    btn_save.move(250, 150)
    btn_save.clicked.connect(clicked)









    win.show() #Uygulamayı çalıştırır
    sys.exit(app.exec_()) # Çarpı butonuna tıklayınca çıkış yapmamızı sağlar
    

window()
