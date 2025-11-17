import random
import os

caminho_arquivo = 'tamagotchi.txt'

class Tamagotchi :
    def __init__(self, nome, saude,fome):
        self.nome = nome
        self.saude = saude
        self.fome = fome
        self.morreu = False
    
    def alimentar(self) :
        limite = 100
        resto = limite - self.fome
        
        if self.fome + 20 <= limite :
            self.fome += 20    
        else :
            self.fome += resto
        print(f'{self.nome} adorou o lanche')
        return self.fome

    def brincar(self) :
        limite = 100
        resto = limite - self.saude
        
        if self.saude + 20 <= limite :
            self.saude += 20
        else :
            self.saude += resto
            
        print(f'{self.nome} adorou a brincadeira e sua vida foi recuperada')
        return self.saude
    
    def lutar(self) :
        vida_minima = 0
        fome_minima = 0
        result_luta = random.randint(1,2)
        if result_luta == 1 : #venceu
            dano_sofrido = random.randint(0,99)
            fome_atual = random.randint(0,99)
            self.saude -= dano_sofrido
            self.fome -= fome_atual
            print(f"O {self.nome} venceu\n Saúde Atual: {self.saude}\n Fome Atual: {self.fome}.")
        else : # perdeu
            dano_sofrido = random.randint(50,100)
            fome_atual = random.randint(50,100)
            
            if self.saude - dano_sofrido <= vida_minima :
                self.saude = vida_minima
            else :
                self.saude -= dano_sofrido
                
            if self.fome - dano_sofrido <= fome_minima :
                self.fome = fome_minima
            else :
                self.fome -= fome_atual
            
            print(f"O {self.nome} perdeu\n Saúde Atual: {self.saude}\n Fome Atual: {self.fome}.")
            
            if self.saude <= vida_minima or self.fome <= fome_minima :
                print(f"💀 OLHA O QUE VOCÊ FEZ!!! \n O {self.nome} MORREU")
                os.remove(caminho_arquivo)
                print(f"{tamagotchi.nome} morreu. Os céus lamentam sua morte. Eles te culpam, te chamam de monstro. O save foi deletado")
                self.morreu = True
                pass
    
    def salvar_estado(self) :
        with open (caminho_arquivo, 'w', encoding='utf-8') as arquivo :
            arquivo.write(f'{self.nome},{self.saude},{self.fome} \n')



if os.path.exists(caminho_arquivo) :
    print("Save encontrado! Carregando seu bichinho...")
    with open (caminho_arquivo, 'r', encoding='utf-8') as arquivo :
            dados = arquivo.read().split(',')
            nome = dados[0]
            saude = int(dados[1])
            fome = int(dados[2])
            tamagotchi = Tamagotchi(nome, saude, fome)
else : 
    nome = input("Digite o nome do tamagotchi: ") 
    tamagotchi = Tamagotchi(nome,100,100)
    tamagotchi.salvar_estado()
        
while True:
    
    if tamagotchi.morreu == True:
        break

    print(f"------------------- STATUS ATUAL -------------------------")
    print(f"NOME: {tamagotchi.nome}\nSAÚDE: {tamagotchi.saude}\nFOME: {tamagotchi.fome}")
    
    escolha = int(input("O QUE QUER FAZER?\n 1 - ALIMENTAR\n 2 - BRINCAR\n 3- LUTAR\n 4 - SALVAR ESTADO\n"))
    
    if escolha == 1 :
        tamagotchi.alimentar()
        continue
    elif escolha == 2 :
        tamagotchi.brincar()
        continue
    elif escolha == 3 :
        tamagotchi.lutar()
        continue
    elif escolha == 4 :
        tamagotchi.salvar_estado()
        break
    else :
        print("Escolha inválida")
        continue

if tamagotchi.morreu == False :
    print(f"VOLTE MAIS TARDE PARA CUIDAR DO {tamagotchi.nome}")
else :
    print(f"VOLTE MAIS TARDE PARA CUIDAR DO TUMULO DO {tamagotchi.nome}. SEU MONSTRO")