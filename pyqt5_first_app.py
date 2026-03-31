import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon



def window():
    app= QApplication(sys.argv) #Komut bilgisini uygulamaya aktarır sys.argv
    win= QMainWindow() #Pencere oluşturur
    win.setWindowTitle("First Application") # Uygulamanın ismini ayarlar
    win.setGeometry(400, 400, 800, 500) # Yatayda 400 Dikeyda 400 boşluk bırakır pencere boyutu da 800'e 500 olur Önce yatay yazılır
    win.setWindowIcon(QIcon('icon.jpg')) # Uygulamanın icon'unu değiştirebiliriz.
    win.setToolTip("my tooltip")
   
   
    win.show() #Uygulamayı çalıştırır
    sys.exit(app.exec_()) # Çarpı butonuna tıklayınca çıkış yapmamızı sağlar
    

window()
