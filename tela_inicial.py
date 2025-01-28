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
        self.button = QPushButton("Abrir Patrimonio")
        self.button2 = QPushButton("Abrir Localização")

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