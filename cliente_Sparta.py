import socket
import os
import sys

print("""


+--------------------------------+
| Criador      : MRX             |
| Apoiadores   : Cyber Security  |
| Versão       : 0.1 Beta        |
+--------------------------------+

""")

os.system("figlet SPARTA")
os.system("figlet CLIENTE")

print("""

+-----------------------------+
|                             |
|[01] - Abrir cliente Sparta  |
|[02] - Sair                  |
|                             |
+-----------------------------+ 

""")

aux = input("[-]   Sua escolha:_> ")

if aux == "01":

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    os.system("clear")

    cliente.connect(("199.34.228.53", 80))

    print(f"conectado ao: {cliente}")

    msg = str(input("[-]   Mensagem de envio_> "))

    cliente.send(msg.encode())

elif aux == "02":
    print("Fechando...")

else:
    print(f"[-] Parâmetro {aux} incorreto! Tente novamente!")
