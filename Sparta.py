import socket
import os
import sys

print("""

+----------------------------+
|       SPARTA SERVIDOR      |
| Criador   : MRX            |
| Apoiadores: Cyber Security |
| Versão    : 0.1 - Beta     |
+----------------------------+

""")

os.system("figlet SPARTA")

print("""

+---------------------------+
|      01 - Abrir Sparta    |  
|    02 - Abrir Sparta Web  |
|    03 - O que é a Sparta  |
|      04 - Modo de usar    |
|        05 - criador       |
+---------------------------+

[-] Para informar um Bug, chame-nos pelo WhatsApp: (67) 99831-8445 e informe seu nome e o Bug encontrado! Obrigado por escolher a Sparta Servidores!

""")

escolha = input("[-]_> ")

if escolha == "01":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(("localhost", 8081))
    server.listen(5)


    os.system("clear")

    print("Aguardando conexão")

    connection, data = server.accept()

    print(f"[-] Cliente {data} conectado")

    msg = connection.recv(1024).decode()
    print(f"{data} = {msg}")

elif escolha == "02":
    os.system("node Sparta.js")

elif escolha == "03":
    print("""

 O servidor Sparta e um servidor de rede local (LocalHost) onde possui suporte para envio de mensagens (apenas uma), oservidor possui um grande diferencial que é uma ferramenta de codigo aberto, ou seja, qualquer um pode entender o seu funcionamento e entre outras coisas!

""")

elif escolha == "04":
    print("""

[-] Modo de uso da Sparta Servidor!

[-] Em primeiro lugar: Rode esse Servidor usando a opção 01 e conecte-se usando o Cliente-Sparta

[-] Segundo lugar: Aguarde o Servidor Sparta apresenta na tela o IP do Cliente, mais a porta de conexão!

[-] Porta e IP que a Sparta se localiza: A Sparta se encontra em (LocalHost) ou seja, seu proprio IP, e está configurado para rodar na porta (8081)!

""")

elif escolha == "05":
    print("""

[-] Informações do criador!

[-] O criador da Sparta Servidor, é um jovem de 17 anos, morador do Brasil em Mato Grosso do Sul, conhecido como (MRX, MWM e Coringa)!

""")

