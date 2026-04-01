# PyQt5 Temelleri

## Temel Yapı

Her PyQt5 uygulaması 3 parçadan oluşur: QApplication, ana pencere sınıfı ve event loop.

```python
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setWindowTitle("Başlık")
        self.setGeometry(x, y, width, height)
        self.initUI()

    def initUI(self):
        pass  # Widget'lar buraya tanımlanır

app = QApplication(sys.argv)
win = MainForm()
win.show()
sys.exit(app.exec_())
```

---

## Widget'lar

```python
# Metin gösterme
self.lbl = QtWidgets.QLabel(self)
self.lbl.setText("Metin")
self.lbl.move(50, 30)
self.lbl.resize(200, 32)

# Kullanıcıdan metin alma — .text() her zaman str döner
self.txt = QtWidgets.QLineEdit(self)
self.txt.move(150, 30)
self.txt.resize(200, 32)

# Buton
self.btn = QtWidgets.QPushButton(self)
self.btn.setText("Tıkla")
self.btn.move(150, 80)
```

---

## Signal & Slot

Bir olay gerçekleştiğinde (signal) ilgili method (slot) tetiklenir.

```python
# Bağlantı — parantez kullanılmaz!
self.btn.clicked.connect(self.metodum)

def metodum(self):
    pass
```

---

## Exception Handling

GUI'de hatalar kullanıcıya gösterilmelidir, terminale değil.

```python
def bolme(self):
    try:
        result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
        self.lbl_sonuc.setText(f"Sonuc: {result}")
    except ZeroDivisionError as err:
        self.lbl_sonuc.setText(f"Hata: {err}")
    except ValueError:
        self.lbl_sonuc.setText("Hata: Gecerli bir sayi girin.")
```
