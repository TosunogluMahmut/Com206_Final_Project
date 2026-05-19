import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QPushButton, QListWidget, QDialog, QFormLayout, 
                               QLineEdit, QHBoxLayout)

class Cekici:
    def __init__(self, plaka, surucu, tip, musait_mi=True):
        self.plaka = plaka
        self.surucu = surucu
        self.tip = tip
        self.musait_mi = musait_mi

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
        layout.addWidget(self.liste)

        buton_layout = QHBoxLayout()

        self.ekle_butonu = QPushButton("Filomuza Katıl")
        self.sil_butonu = QPushButton("Seçili Aracı Sil") 
        
        buton_layout.addWidget(self.ekle_butonu)
        buton_layout.addWidget(self.sil_butonu)

        layout.addLayout(buton_layout)

        self.ekle_butonu.clicked.connect(self.arac_ekle)
        self.sil_butonu.clicked.connect(self.arac_sil)

        self.filo = [
            Cekici("34 ABC 123", "Mahmut Eren", "Kayar Kasa"),
            Cekici("06 DEF 456", "Ali", "Ahtapot")
        ]
        self.listeyi_guncelle()

    def listeyi_guncelle(self):
        self.liste.clear() 
        for arac in self.filo:
            durum = "🟢 Müsait" if arac.musait_mi else "🔴 Meşgul"
            metin = f"{arac.plaka} | {arac.surucu} ({arac.tip}) \nDurum: {durum}"
            self.liste.addItem(metin)

    def arac_ekle(self):
        form = AracEklemeFormu()
        if form.exec(): 
            plaka, surucu, tip = form.verileri_al()
            yeni_arac = Cekici(plaka, surucu, tip)
            self.filo.append(yeni_arac)
            self.listeyi_guncelle()

    def arac_sil(self):
        secili_satir = self.liste.currentRow()
        
        if secili_satir >= 0:
            del self.filo[secili_satir]
            self.listeyi_guncelle()


tema_kodu = """
/* Ana arkaplan rengi */
QMainWindow, QDialog {
    background-color: #F5F5F5;
}

/* Flutter Card görünümlü liste elemanları */
QListWidget {
    background-color: #F5F5F5;
    border: none;
}
QListWidget::item {
    background-color: #FFFFFF;
    border-radius: 8px;
    margin-bottom: 10px;
    padding: 15px;
    border: 1px solid #E0E0E0;
    color: #333333;
    font-size: 14px;
}
QListWidget::item:selected {
    background-color: #FFE0B2;
    border: 1px solid #FF9800;
    color: #000000;
}

/* Turuncu Temalı Butonlar */
QPushButton {
    background-color: #FF9800;
    color: white;
    border-radius: 8px;
    padding: 12px;
    font-weight: bold;
    font-size: 14px;
    border: none;
}
QPushButton:hover {
    background-color: #F57C00;
}
QPushButton:pressed {
    background-color: #E65100;
}

/* Metin Giriş Kutuları (TextField karşılığı) */
QLineEdit {
    padding: 10px;
    border: 1px solid #CCCCCC;
    border-radius: 6px;
    background-color: #FFFFFF;
    font-size: 14px;
}
QLineEdit:focus {
    border: 2px solid #FF9800;
}
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Yazdığımız tasarımı sisteme entegre ediyoruz
    app.setStyleSheet(tema_kodu)
    
    pencere = AnaSayfa()
    pencere.show()
    sys.exit(app.exec())