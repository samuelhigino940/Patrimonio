import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout
from patrimonio import patrimonio
from Localizacoes import localizacao

class TelaInicial(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciar")
        self.setGeometry(300,200,200,150)
        self.layout_v = QVBoxLayout()

        self.label_titulo = QLabel("Clique para abrir a janela")
        self.label_titulo.setStyleSheet("color: white; background-color: red; font-size: 14px; font-weight:bold")
        self.button = QPushButton("Abrir Patrimonio")
        self.button.setStyleSheet("QPushButton{background-color:green;color:white;font-size:8pt;font-weight:bold}")
        self.button2 = QPushButton("Abrir Localização")
        self.button2.setStyleSheet("QPushButton{background-color:green;color:white;font-size:8pt;font-weight:bold}")

        self.layout_v.addWidget(self.label_titulo)
        self.layout_v.addWidget(self.button)
        self.layout_v.addWidget(self.button2)

        self.button.clicked.connect(self.abrir_cadastro)
        self.button2.clicked.connect(self.abrir_localizacao)

        self.setLayout(self.layout_v)
    
    def abrir_cadastro(self):
        self.pat = patrimonio()
        self.pat.show()
    
    def abrir_localizacao(self):
        self.pat = localizacao()
        self.pat.show()

app = QApplication(sys.argv)
tela = TelaInicial()
tela.show()
app.exec()