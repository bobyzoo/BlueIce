#------------------------------------------------------------------------IMPOTAÇÕES E CONSTANTES
from time import sleep
import csv
import pygame
mesa = '5'
width = 1080
heigth = 720
sair= True
branco = (251,212,153)
telaAtual=1
#------------------------------------------------------------------------FUNÇÕES
def color (x):
    if str(x) == 'branco':
        return (255,255,255)
    elif str(x) == 'preto':
        return (0,0,0)
    elif str(x) == 'azul':
        return (0,178,238)
    elif str(x) == 'verde':
        return (0,238,0)
    elif str(x) == 'amarelo':
        return (238,238,0)
    elif str(x) =='vermelho':
        return (238,0,0)
    elif str(x) == 'cinzaclaro':
        return (70,70,70)
    elif str(x) == 'cinzaescuro':
        return (90,90,90)
    elif str(x) == 'cinzapadrao':
        return (55,55,55)
    elif str(x) == 'cinza':
        return (30,30,30)
    elif str(x) == 'roxo':
        return (100,0,150)
    elif str(x) == 'roxoescuro':
        return (200,75,94)
    else:
        return (0,0,0)
def txt(msg, cor, tam, x, y):
    font = pygame.font.SysFont('comicsansms', tam, True)
    txt1 = font.render(msg, True, color(cor))
    fundo.blit(txt1, [x, y])


def leCardapio():
    arq = open('_dados/tabelaProdutos.csv', 'r')
    reader = csv.reader(arq)
    tamLinha=0
    for linha in reader:
        if(linha[3]=='P' or linha[3]=='A' or linha[3]=='L'):
            txt(f"{linha[0]}-{linha[1]}", 'branco', 20, 400, 110+tamLinha)
            #print(f"{linha[0]}-{linha[1]}")
            tamLinha += 26
    arq.close()


def leLanche():
    arq = open('_dados/tabelaProdutos.csv', 'r')
    reader = csv.reader(arq)
    for linha in reader:
        if(str(linha[3])=='L'):
            print(f'{linha[0]}===={linha[1]}===={linha[2]}')
    sleep(3)
    arq.close()

def leAcai():
    arq = open('_dados/tabelaProdutos.csv', 'r')
    reader = csv.reader(arq)
    for linha in reader:
        if (str(linha[3]) == 'A'):
            print(f'{linha[0]}===={linha[1]}===={linha[2]}')
    sleep(3)
    arq.close()

def lePorcao():
    arq = open('_dados/tabelaProdutos.csv', 'r')
    reader = csv.reader(arq)
    for linha in reader:
        if (str(linha[3]) == 'P'):
            print(f'{linha[0]}===={linha[1]}===={linha[2]}')
    sleep(3)
    arq.close()

def encontraValor(nProduto):
    global conta,mesa
    arq = open('_dados/tabelaProdutos.csv', 'r')
    reader = csv.reader(arq)
    next(reader)
    for linha in reader:

        if(int(linha[0])==nProduto):
            print(f"""
            {linha[1]} R${linha[2]}
            """)
            select = int(input('Deseja confirmar?'))
            if(select==1):
                conta +=float(linha[2])
                addConta(float(linha[2]),str(linha[1]),mesa)
                print("PEDIDO EFETUADO COM SUCESSO!")
                break
            else:
                print("CANCELADO!")
                break
            break

    arq.close()

def addConta(valor,produto,mesa):

    arq = open('_dados/conta.csv', 'a')
    writer = csv.writer(arq)
    arq1 = open('_dados/pedido.csv', 'a')
    writer1 = csv.writer(arq1)
    writer.writerow([f'{produto},{valor}'])
    writer1.writerow([f'========{produto}---[{mesa}]========='])
    arq.close()
    arq1.close()

def verConta():
    arq = open('_dados/conta.csv')
    reader = csv.reader(arq)
    for linha in reader:
        print(f'{linha}')
        next(reader)
    sleep(3)
    arq.close()

def fechaConta():

    arq = open('_dados/conta.csv', 'a')
    global conta
    writer = csv.writer(arq)
    writer.writerow([f'TOTAL = R$ {conta}'])
    sleep(2)
    arq.close()
    verConta()

def pagamentoCard():
    try:
        nCard = int(input('Digite o numero do cartão(apenas numeros): '))

        nmTitular = input('Nome do titular: ')
        if nmTitular.isalpha()==False:
            raise ValueError
        cpf = int(input('Digite seu CPF/CNPJ SOMENTE NUMEROS:'))
        val = input('VALIDADE (xx/xxxx) : ')
        cds = int(input('CODIGO DE SEGURANÇA: '))
        print('PROCESSANDO...')
        sleep(1)
        global on
        on = False
    except:
        print("ERRO NO PAGAMENTO")
        sleep(1)

def addAcai():
    arq = open('_dados/tabelaProdutos.csv', 'r')
    reader = csv.reader(arq)
    print("========ADICIONAIS DE GRAÇA========")
    for linha in reader:
        if (str(linha[3]) == 'AG'):
            print(f'{linha[0]}===={linha[1]}===={linha[2]}')
    arq.close()
    arq = open('_dados/tabelaProdutos.csv', 'r')
    reader = csv.reader(arq)
    print("========ADICIONAIS PAGOS===========")
    for linha in reader:
        if (str(linha[3]) == 'AD'):
            print(f'{linha[0]}===={linha[1]}===={linha[2]}')
    arq.close()

def fazAcai():
    print("Digite '0' para terminar o pedido")
    global conta,mesa
    while 1:
        x= int(input('digite add: '))
        arq = open('_dados/tabelaProdutos.csv', 'r')
        reader = csv.reader(arq)
        next(reader)
        for linha in reader:
            if (int(linha[0]) == x):
                conta += float(linha[2])
                arq1 = open('_dados/conta.csv', 'a')
                arq2 = open('_dados/pedido.csv', 'a')
                writer2 = csv.writer(arq2)
                writer2.writerow([f'{linha[1]},{mesa}'])
                writer = csv.writer(arq1)
                writer.writerow([f'{linha[1]},{linha[2]}'])
                arq1.close()
                arq2.close()
                break
        if x==0:
            break
    arq.close()

#-----------------------------------------------------------------------MAIN
try:
    pygame.init()
except:
    print('Pygame não inicializado com sucesso!')
#-------------------------------------------------------------------ICONE
icone = pygame.image.load("_imagens/icon.bmp")
pygame.display.set_icon(icone)#--------------------------------------DEFINE ICONE DO PROGRAMA



fundo = pygame.display.set_mode((width,heigth))
pygame.display.set_caption("Blue Ice")
img =pygame.image.load("_imagens/tela01.png")
clk = pygame.time.Clock()

while sair:
    fundo.fill(color('branco'))


    for event in pygame.event.get():#--------------------------------------------INICIA EVENTOS
        pos = pygame.mouse.get_pos()
        pos_x = pos[0]
        pos_y = pos[1]
        print(f'{pos_x} {pos_y}')


        if event.type == pygame.QUIT:
            sair = False
        if event.type == pygame.MOUSEBUTTONDOWN:#-------*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*---*-*-*-*-----------------EVENTO DE CLICK-LEFT BUTTON
            pos = pygame.mouse.get_pos()
            if(telaAtual==1):
                #---------------------------------------------------------------ENTRA NO CARDAPIO
                if (pos_x>198 and pos_x<420) and (pos_y>295 and pos_y<420):
                    img = pygame.image.load("_imagens/tela03.png")
                    telaAtual=2
                # ---------------------------------------------------------------ABRE A CONTA
                if (pos_x>715 and pos_x<935) and (pos_y>290 and pos_y<420):
                    img = pygame.image.load("_imagens/tela02.png")
                    telaAtual=3
                    conta = 0.0
                    arq = open('_dados/conta.csv', 'w')
                    fieldnames = ['Produto', 'total']
                    writer = csv.DictWriter(arq, fieldnames=fieldnames)
                    writer.writeheader()
                    arq.close()

            if(telaAtual==2):
                if(pos_x > 900 and pos_x < 1050) and (pos_y > 560 and pos_y < 703):
                    img=pygame.image.load("_imagens/tela01.png")
                    telaAtual = 1

            if(telaAtual==3):
                if (pos_x > 620 and pos_x < 770) and (pos_y > 415 and pos_y < 565):
                    img = pygame.image.load("_imagens/tela01.png")
                    telaAtual = 4
                if (pos_x > 620 and pos_x < 770) and (pos_y > 220 and pos_y < 370):
                    img = pygame.image.load("_imagens/tela01.png")
                    telaAtual = 5
                if (pos_x > 281 and pos_x < 411) and (pos_y > 220 and pos_y < 370):
                    img = pygame.image.load("_imagens/tela01.png")
                    telaAtual = 6
                if (pos_x > 281 and pos_x < 411) and (pos_y > 415 and pos_y < 565):
                    img = pygame.image.load("_imagens/tela01.png")
                    telaAtual = 7
                # -----------------------------------------------------------------------FIM EVENTOS

    fundo.blit(img, (0, 0))#-----------------------------------------------------------IMAGEM DE FUNDO




    if telaAtual==1:
        if (pos_x > 198 and pos_x < 420) and (pos_y > 295 and pos_y < 420):
            pygame.draw.rect(fundo,color('roxo'),(195,295,226,125),22)

        if (pos_x>715 and pos_x<935) and (pos_y>290 and pos_y<420):
            pygame.draw.rect(fundo,color('roxo'),(715,295,220,125),22)

    if telaAtual==2:
        if(pos_x > 900 and pos_x < 1050) and (pos_y > 560 and pos_y < 703):
            pygame.draw.circle(fundo,color('roxo'),(982,632),75,10)
        leCardapio()

    if telaAtual==3:#-----------------------------------------------------------------PAGINA MENU
        if(pos_x > 620 and pos_x < 770) and (pos_y > 415 and pos_y < 565):
            pygame.draw.circle(fundo,color('roxo'),(696,486),75,10)
        if (pos_x > 620 and pos_x < 770) and (pos_y > 220 and pos_y < 370):
            pygame.draw.circle(fundo, color('roxo'), (696, 294), 75, 10)
        if (pos_x > 281 and pos_x < 411) and (pos_y > 220 and pos_y < 370):
            pygame.draw.circle(fundo, color('roxo'), (356, 294), 75, 10)
        if (pos_x > 281 and pos_x < 411) and (pos_y > 415 and pos_y < 565):
            pygame.draw.circle(fundo, color('roxo'), (356, 486), 75, 10)




    pygame.display.update()
    clk.tick(60)

pygame.quit()

while 1:
    print("""
    =====================================
            BLUE ICE SYSTEM DEMO
    =====================================
    QUAL SUA SELEÇÃO:
    [1]= CARDAPIO
    [2]= ABRIR CONTA
    """)

    select = int(input(""))
    while ((select != 1) and (select != 2)):
        print("OPÇÃO INCORRETA")
        sleep(0.5)
        print("""
    =====================================
            BLUE ICE SYSTEM DEMO
    =====================================
    QUAL SUA SELEÇÃO:
    [1]= CARDAPIO
    [2]= ABRIR CONTA
    """)
        select = int(input(""))

    if(select==1):#-----------------------------------------------------------------------------VE O CARDAPIO
        try:
            leCardapio()
        except :
            print('ERRO AO LER O CARDAPIO')
    elif(select==2):#---------------------------------------------------------------------------INICIA A COMPRA
        on=True
        conta =0.0

        arq = open('_dados/conta.csv', 'w')
        fieldnames = ['Produto','total']
        writer = csv.DictWriter(arq, fieldnames=fieldnames)
        writer.writeheader()
        arq.close()
        print('novo')

        while (on):
            print(f"""
                        ==============================
                                  MESA {mesa}
                        ==============================
                        [1]=AÇAI
                        [2]=LANCHES
                        [3]=PORÇÕES
                        [4]=PAGAR
                        ===============================
                        VALOR DA CONTA ={conta}
                        """)
            select = int(input(""))
            while ((select != 1) and (select != 2)) and (select!=3) and (select!=4):
                print("OPÇÃO INCORRETA")
                sleep(0.5)
                print("""
                            ==============================
                                      MESA 05
                            ==============================
                            [1]=AÇAI
                            [2]=LANCHES
                            [3]=PORÇÕES
                            [4]=PAGAR
                            """)
                select = int(input(""))

            if(select==1):#---------------------------------------------------------------------COMPRA AÇAI
                leAcai()
                x = int(input("QUAL NUMERO DO SEU PEDIDO:"))
                encontraValor(x)
                addAcai()
                fazAcai()

            elif (select==2):#------------------------------------------------------------------COMPRA LANCHE
                leLanche()
                x=int(input("QUAL NUMERO DO SEU PEDIDO:"))
                encontraValor(x)
            elif(select==3): #------------------------------------------------------------------PEDE PORÇÃO
                lePorcao()
                x = int(input("QUAL NUMERO DO SEU PEDIDO:"))
                encontraValor(x)
            elif(select==4):#-------------------------------------------------------------------PAGAR
                print("""1
                
                    [1]= PAGAMENTO DINHEIRO/MAQUININHA
                    [2]= PAGAMENTO ONLINE
                    
                """)
                select = int(input(""))
                if(select==1):#-----------------------------------------------------------------PAGAMENTO DINHEIRO/MAQUININHA
                    fechaConta()
                    sleep(1)
                    on=False
                elif(select==2):#---------------------------------------------------------------PAGAMENTO ONLINE
                    verConta()
                    print(f"TOTAL==R$ {conta}")
                    pagamentoCard()


