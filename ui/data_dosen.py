from PyQt6.QtWidgets import QApplication, QWidget
import sys
from PyQt6 import uic
import os

class FORM_UI(QWidget):
    def __init__(self):
        super(FORM_UI, self).__init__()
        # Pastikan file UI ditemukan sebelum dimuat
        if os.path.exists("data_dosen.ui"):
            uic.loadUi("data_dosen.ui", self)
        else:
            print("File 'data_dosen.ui' tidak ditemukan.")

app = QApplication(sys.argv)
window = FORM_UI()
window.show()
app.exec()
