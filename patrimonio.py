from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,QMessageBox
import sys 

class patrimonio(QWidget):
    def __init__(self):
        super().__init__()

        # Vamos ajustar a geometria da tela
        # Setando valores da posição x e y, além da largura e altura
        self.setGeometry(500,150,500,500)

        # Texto para a barra de título
        self.setWindowTitle("Patrimonio")
        
        # Gerenciador de layout vertical
        self.layout_v = QVBoxLayout()

        # Labels para os dados do Produto
        self.label_Produto = QLabel("ID do Produto:")
        self.label_Produto.setStyleSheet("QLabel{font-size:12pt}")

        # Labels para o numero de série
        self.label_serie = QLabel("Número de Série:")
        self.label_serie.setStyleSheet("QLabel{font-size:12pt}")
        
        # Labels para o nome de Patrimonio
        self.label_patrimonio = QLabel("Nome de Património:")
        self.label_patrimonio.setStyleSheet("QLabel{font-size:12pt}")

        # Labels de tipo do produto
        self.label_tipo = QLabel("Tipo:")
        self.label_tipo.setStyleSheet("QLabel{font-size:12pt}")
        
        # Labels de descrição do produto
        self.label_descricao = QLabel("Descrição do Produto:")
        self.label_descricao.setStyleSheet("QLabel{font-size:12pt}")

        # Labels de localização do produto
        self.label_localizacao = QLabel("Localização do Produto:")
        self.label_localizacao.setStyleSheet("QLabel{font-size:12pt}")

        # Labels de Data de Fabricação
        self.label_fabricacao = QLabel("Data de Fabricação:")
        self.label_fabricacao.setStyleSheet("QLabel{font-size:12pt}")

        # Labels de Data de Aquisição
        self.label_aquisicao = QLabel("Data de Aquisição:")
        self.label_aquisicao.setStyleSheet("QLabel{font-size:12pt}")

        



        # LineEdit para Produto
        self.edit_Produto = QLineEdit()
        self.edit_Produto.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para o Numero de série
        self.edit_serie = QLineEdit()
        self.edit_serie.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para o Patrimonio
        self.edit_patrimonio = QLineEdit()
        self.edit_patrimonio.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para a Tipo
        self.edit_tipo = QLineEdit()
        self.edit_tipo.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para Descrição
        self.edit_descricao = QLineEdit()
        self.edit_descricao.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para Localização
        self.edit_localizacao = QLineEdit()
        self.edit_localizacao.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit de Data de Fabricação
        self.edit_fabricacao = QLineEdit()
        self.edit_fabricacao.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit de Data de Aquisição
        self.edit_aquisicao = QLineEdit()
        self.edit_aquisicao.setStyleSheet("QLineEdit{font-size:12pt}")
        



        self.button = QPushButton("Cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:green;color:white;font-size:12pt;font-weight:bold}")

        # Chamar a função de cadastro do cliente ao clicar no botão
        self.button.clicked.connect(self.cadastrar)

        # Adicionar a label o nome e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_Produto)
        self.layout_v.addWidget(self.edit_Produto)

        # Adicionar a label o E-mail e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_serie)
        self.layout_v.addWidget(self.edit_serie)
        
        # Adicionar a label o Telefone e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_patrimonio)
        self.layout_v.addWidget(self.edit_patrimonio)

        # Adicionar a label o Idade e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_tipo)
        self.layout_v.addWidget(self.edit_tipo)

        # Adicionar a label descrição ao layout vertical
        self.layout_v.addWidget(self.label_descricao)
        self.layout_v.addWidget(self.edit_descricao)

        # Adicionar a label Localização ao layout vertical
        self.layout_v.addWidget(self.label_localizacao)
        self.layout_v.addWidget(self.edit_localizacao)

        # Adicionar a label Fabricação ao layout vertical
        self.layout_v.addWidget(self.label_fabricacao)
        self.layout_v.addWidget(self.edit_fabricacao)

        # Adicionar a label Fabricação ao layout vertical
        self.layout_v.addWidget(self.label_aquisicao)
        self.layout_v.addWidget(self.edit_aquisicao)

        self.layout_v.addWidget(self.button)
        

        # Adicionar o layout_v a tela
        self.setLayout(self.layout_v)
    
    def cadastrar(self):
        if(self.edit_Produto.text()=="" or self.edit_serie.text or self.edit_patrimonio.text or self.edit_tipo.text or self.edit_descricao.text or self.edit_localizacao or self.edit_fabricacao.text or self.edit_aquisicao.text):
         QMessageBox.critical(self,"Erro","Você deve Preencher todos os campos")
        
        
        else:
            # Arquivo de ID do Produto
            arquivo = open("clientes.txt" ,"+a")
            arquivo.write(f"Nome: {self.label_Produto.text()}")
            arquivo.close()
            arquivo = open("clientes.txt" ,"+a")
            arquivo.write(f"Nome: {self.edit_Produto.text()}")
            arquivo.close()
            
            # Arquivo de Número de série
            arquivo = open("clientes.txt" ,"+a")
            arquivo.write(f"Nome: {self.label_serie.text()}")
            arquivo.close()
            arquivo = open("clientes.txt" ,"+a")
            arquivo.write(f"Nome: {self.edit_serie.text()}")
            arquivo.close()

            # Arquivo de Nome de Patrimonio
            arquivo = open("clientes.txt" ,"+a")
            arquivo.write(f"Nome: {self.label_patrimonio.text()}")
            arquivo.close()
            arquivo = open("clientes.txt" ,"+a")
            arquivo.write(f"Nome: {self.edit_patrimonio.text()}")
            arquivo.close()

            # Arquivo de Tipo do Produto
            arquivo = open("clientes.txt" ,"+a")
            arquivo.write(f"Nome: {self.label_tipo.text()}")
            arquivo.close()
            arquivo = open("clientes.txt" ,"+a")
            arquivo.write(f"Nome: {self.edit_tipo.text()}")
            arquivo.close()

            # Arquivo de Descrição do Produto
            arquivo = open("clientes.txt" ,"+a")
            arquivo.write(f"Nome: {self.label_descricao.text()}")
            arquivo.close()
            arquivo = open("clientes.txt" ,"+a")
            arquivo.write(f"Nome: {self.edit_descricao.text()}")
            arquivo.close()

            # Arquivo de Número de Localização
            arquivo = open("clientes.txt" ,"+a")
            arquivo.write(f"Nome: {self.label_localizacao.text()}")
            arquivo.close()
            arquivo = open("clientes.txt" ,"+a")
            arquivo.write(f"Nome: {self.edit_localizacao.text()}")
            arquivo.close()

            # Arquivo de Data de Fabricação Do Produto
            arquivo = open("clientes.txt" ,"+a")
            arquivo.write(f"Nome: {self.label_fabricacao.text()}")
            arquivo.close()
            arquivo = open("clientes.txt" ,"+a")
            arquivo.write(f"Nome: {self.edit_fabricacao.text()}")
            arquivo.close()

            # Arquivo de Data de Aquisição
            arquivo = open("clientes.txt" ,"+a")
            arquivo.write(f"Nome: {self.label_aquisicao.text()}")
            arquivo.close()
            arquivo = open("clientes.txt" ,"+a")
            arquivo.write(f"Nome: {self.edit_aquisicao.text()}")
            arquivo.close()
            QMessageBox.information(self,"Salvo","Os Dados do patrimonio foram salvos")
            



        
#app = QApplication(sys.argv)
# Em instância da classe  CadastroCliente para iniciar a janela

#tela = patrimonio()
# Exibir  a tela durante a execução 

#tela.show()
# Ao clicar no botão fechar a tela deve fechar e sair da memória

#app.exec()