# Usado para executar comandos do sistema operacional
import os

# Função para limpar tela
def cleanScreem():
    os.system('cls' if os.name == 'nt' else 'clear')