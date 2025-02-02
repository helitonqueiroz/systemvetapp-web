import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon  # Importe QIcon para usar o ícone


class BrowserWindow(QMainWindow):
    def __init__(self, url):
        super().__init__()

        # Configurações da janela
        self.setWindowTitle("SystemVet App Online")
        self.setGeometry(100, 100, 1280, 720)  # Tamanho inicial da janela
        self.showMaximized()  # Abre em tela cheia

        self.setWindowIcon(QIcon("static/media/logo.ico"))  # Substitua pelo caminho do seu ícone


        # Criação do navegador
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url))  # Define o endereço IP ou URL
        self.setCentralWidget(self.browser)

if __name__ == "__main__":
    # Endereço IP ou URL que deseja abrir
    ip_address = "http://34.41.179.180/"  # Substitua pelo IP desejado

    # Inicializa a aplicação
    app = QApplication(sys.argv)

    # Cria a janela do navegador
    window = BrowserWindow(ip_address)
    window.show()

    # Executa a aplicação
    sys.exit(app.exec_())