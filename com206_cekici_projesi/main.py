import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QPushButton, QListWidget, QListWidgetItem, QDialog, QFormLayout, 
                               QLineEdit, QHBoxLayout, QStackedWidget, QLabel)

class Cekici:
    def __init__(self, plaka, surucu, tip):
        self.plaka = plaka
        self.surucu = surucu
        self.tip = tip

class GirisSayfasi(QDialog):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setWindowTitle("Sisteme Giriş")
        self.setMinimumWidth(300)
        
        layout = QFormLayout()
        self.setLayout(layout)
        
        self.user_input = QLineEdit()
        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.Password)
        self.login_btn = QPushButton("Giriş Yap")
        
        layout.addRow("Kullanıcı Adı:", self.user_input)
        layout.addRow("Şifre:", self.pass_input)
        layout.addRow(self.login_btn)
        
        self.login_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

class AracEklemeFormu(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yeni Araç Ekle")
        self.setMinimumWidth(300)
        layout = QFormLayout()
        self.setLayout(layout)
        self.plaka_input = QLineEdit()
        self.surucu_input = QLineEdit()
        self.tip_input = QLineEdit()
        layout.addRow("Plaka:", self.plaka_input)
        layout.addRow("Sürücü:", self.surucu_input)
        layout.addRow("Tip:", self.tip_input)
        buton_layout = QHBoxLayout()
        self.kaydet_btn = QPushButton("Kaydı Tamamla")
        self.iptal_btn = QPushButton("İptal")
        buton_layout.addWidget(self.kaydet_btn)
        buton_layout.addWidget(self.iptal_btn)
        layout.addRow(buton_layout)
        self.kaydet_btn.clicked.connect(self.accept)
        self.iptal_btn.clicked.connect(self.reject)

    def verileri_al(self):
        return self.plaka_input.text(), self.surucu_input.text(), self.tip_input.text()

class AnaSayfa(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Çekici Takip Sistemi")
        self.setMinimumSize(450, 600)
        merkez_widget = QWidget()
        self.setCentralWidget(merkez_widget)
        layout = QVBoxLayout()
        merkez_widget.setLayout(layout)
        self.liste = QListWidget()
        self.liste.setWordWrap(True)
        self.liste.setUniformItemSizes(False)
        layout.addWidget(self.liste)
        buton_layout = QHBoxLayout()
        self.ekle_butonu = QPushButton("Filomuza Katıl")
        self.sil_butonu = QPushButton("Seçili Aracı Sil") 
        buton_layout.addWidget(self.ekle_butonu)
        buton_layout.addWidget(self.sil_butonu)
        layout.addLayout(buton_layout)
        self.ekle_butonu.clicked.connect(self.arac_ekle)
        self.sil_butonu.clicked.connect(self.arac_sil)
        self.filo = [Cekici("34 ABC 123", "Mahmut Eren", "Kayar Kasa"), Cekici("06 DEF 456", "Ali", "Ahtapot")]
        self.listeyi_guncelle()

    def listeyi_guncelle(self):
        self.liste.clear() 
        for arac in self.filo:
            metin = f"{arac.plaka} | {arac.surucu} ({arac.tip})"
            item = QListWidgetItem(metin)
            item.setSizeHint(QSize(0, 60))
            self.liste.addItem(item)

    def arac_ekle(self):
        form = AracEklemeFormu()
        if form.exec(): 
            plaka, surucu, tip = form.verileri_al()
            self.filo.append(Cekici(plaka, surucu, tip))
            self.listeyi_guncelle()

    def arac_sil(self):
        secili_satir = self.liste.currentRow()
        if secili_satir >= 0:
            del self.filo[secili_satir]
            self.listeyi_guncelle()

tema_kodu = """
QMainWindow, QDialog { background-color: #F5F5F5; }
QListWidget { background-color: #F5F5F5; border: none; }
QListWidget::item { background-color: #FFFFFF; border-radius: 8px; margin-bottom: 10px; padding: 15px; border: 1px solid #E0E0E0; color: #333333; }
QListWidget::item:selected { background-color: #FFE0B2; border: 1px solid #FF9800; }
QPushButton { background-color: #FF9800; color: white; border-radius: 8px; padding: 12px; font-weight: bold; border: none; }
QPushButton:hover { background-color: #F57C00; }
QLineEdit { padding: 10px; border: 1px solid #CCCCCC; border-radius: 6px; background-color: #FFFFFF; }
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(tema_kodu)
    
    stacked = QStackedWidget()
    
    giris = GirisSayfasi(stacked)
    ana = AnaSayfa()
    
    stacked.addWidget(giris)
    stacked.addWidget(ana)
    
    stacked.setFixedSize(450, 600)
    stacked.show()
    sys.exit(app.exec())