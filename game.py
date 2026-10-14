import os
from pynput import keyboard
import time
import sys
import termios

tabuleiro=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
tabuleiro_focus=[[True, False, False], [False, False, False], [False, False, False]]
loc_tab_focus=[0,0]
jogador = 1
jogo_terminou=False

def game_interface(tab_user,tab_focus):#view
    
    os.system('clear')

    def pt_tb(x,y):
        barra1=" "
        barra2=" "
        
        if tab_focus[x][y]:
            barra1="["
            barra2="]"
            
        if tab_user[x][y]==1:
            return f"{barra1}x{barra2}"
        elif tab_user[x][y]==2:
            return f"{barra1}o{barra2}"
        else:
            return f"{barra1} {barra2}"
    print(
    f"""
    
    {pt_tb(0,0)}|{pt_tb(0,1)}|{pt_tb(0,2)}
    ---+---+---
    {pt_tb(1,0)}|{pt_tb(1,1)}|{pt_tb(1,2)}
    ---+---+---
    {pt_tb(2,0)}|{pt_tb(2,1)}|{pt_tb(2,2)}
    
    mover(setas) | selecionar(enter) | sair(esc)
    
    """)

def verificar_vitoria(tab_user):
    
    #linhas da matriz
    
    for i in range(3):
        if tab_user[i]==[1,1,1] or tab_user[i]==[2,2,2]:
            return tab_user[i][0]
        
    #colunas da matriz
    
    for i in range(3):
        var_de_verificacao=[tab_user[0][i],tab_user[1][i],tab_user[2][i]]
        if var_de_verificacao==[1,1,1] or var_de_verificacao ==[2,2,2]:
            return var_de_verificacao[0]
        
    #verifica diagonais

    diagonal1=[tab_user[0][0],tab_user[1][1],tab_user[2][2]]
    diagonal2=[tab_user[2][0],tab_user[1][1],tab_user[0][2]]
    if diagonal1==[2,2,2] or diagonal1==[1,1,1]:
        return diagonal1[1]
    if diagonal2==[2,2,2] or diagonal2==[1,1,1]:
        return diagonal2[1]

    #verificar impate
    
    for x in range(3):
        for y in range(3):
            if tab_user[x][y]==0:
                return 0
        if x ==2:
            return 3

def jogar(number):
    
    global jogador, jogo_terminou
    
    if not number[0]+loc_tab_focus[0]==3 and not number[1]+loc_tab_focus[1]==3 and not number[0]+loc_tab_focus[0]==-1 and not number[1]+loc_tab_focus[1]==-1 and not number==[10,10]:
        tabuleiro_focus[loc_tab_focus[0]][loc_tab_focus[1]]=False
        loc_tab_focus[0]+=number[0]
        loc_tab_focus[1]+=number[1] 
        tabuleiro_focus[loc_tab_focus[0]][loc_tab_focus[1]]=True
    
    if number ==[10,10]:
        if tabuleiro[loc_tab_focus[0]][loc_tab_focus[1]]==0:
            tabuleiro[loc_tab_focus[0]][loc_tab_focus[1]]=jogador
            
            ganhou=verificar_vitoria(tabuleiro)
            
            if ganhou == 1 or ganhou == 2:
                game_interface(tabuleiro,tabuleiro_focus)
                jogo_terminou=True
                element = "x" if ganhou==1 else "o"
                print(f"Jogador {element} ganhou!")
                return 0
            elif ganhou == 3:
                jogo_terminou=True
                print(f"O jogo empatou!")
                return 0
            
            if jogador==1:
                jogador=2
            else:
                jogador=1
    game_interface(tabuleiro,tabuleiro_focus)
    
def input_players():
    
    global jogo_terminou
    
    def on_press(key, injected):
        pass
    
    def on_release(key, injected):
            if format(key)=="Key.up":
                xy=[-1,0]
                jogar(xy)
                return not jogo_terminou
            elif format(key)=='Key.left':
                jogar([0,-1])
                return not jogo_terminou
            elif format(key)=="Key.down":
                jogar([1,0])
                return not jogo_terminou
            elif format(key)=="Key.right":
                jogar([0,1])
                return not jogo_terminou
            elif format(key)=="Key.space":
                jogar([10,10])
                return not jogo_terminou
                
            if key == keyboard.Key.esc:
                # Stop listener
                return False
    
        # Collect events until released
    with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()
    
        # ...or, in a non-blocking fashion:
continuar =True
while continuar:
    game_interface(tabuleiro,tabuleiro_focus)
    input_players()

    if jogo_terminou==True:
        while True:
            print("Quer jogar de novo?")
            termios.tcflush(sys.stdin, termios.TCIFLUSH)
            ser = input("Digite [S/n]: ")
            if ser.lower() =="n":
                continuar=False
                break
            elif ser.lower()=="s":
                print("...")
                time.sleep(1)
                tabuleiro=[[0,0,0],[0,0,0],[0,0,0]]
                jogo_terminou=False
                break  
            else:
                print(ser)
                print("Digite um valor válido")
    