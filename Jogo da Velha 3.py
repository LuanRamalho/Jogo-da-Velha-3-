import tkinter as tk
from tkinter import messagebox
import random

# Função para verificar o vencedor
def check_winner(board):
    # Verificar linhas, colunas e diagonais
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

# Função para verificar se o tabuleiro está cheio
def is_board_full(board):
    for row in board:
        if "" in row:
            return False
    return True

# Função para jogar contra a máquina
def player_vs_computer():
    global player
    player = "X"
    start_game()

def start_game():
    global board
    board = [["" for _ in range(3)] for _ in range(3)]
    global current_player
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state=tk.NORMAL)  # Corrigido

def on_button_click(i, j):
    global current_player
    if board[i][j] == "" and not game_over:
        board[i][j] = current_player
        buttons[i][j].config(text=current_player)  # Corrigido
        winner = check_winner(board)
        if winner:
            game_over_message(winner)
        elif is_board_full(board):
            game_over_message("Empate")
        else:
            current_player = "O" if current_player == "X" else "X"
            if game_mode == "vs_computer" and current_player == "O":
                computer_move()

def computer_move():
    global current_player
    # Simples lógica de movimento da máquina (joga de forma aleatória)
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = current_player
        buttons[i][j].config(text=current_player)  # Corrigido
        winner = check_winner(board)
        if winner:
            game_over_message(winner)
        elif is_board_full(board):
            game_over_message("Empate")
        else:
            current_player = "X"

def game_over_message(winner):
    global game_over
    game_over = True
    if winner == "Empate":
        messagebox.showinfo("Fim de Jogo", "O jogo terminou em empate!")
    else:
        messagebox.showinfo("Fim de Jogo", f"Jogador {winner} venceu!")
    restart_game()

def restart_game():
    global game_over
    game_over = False
    start_game()

# Função para alternar entre os modos de jogo
def choose_game_mode(mode):
    global game_mode
    game_mode = mode
    start_game()

# Criando a interface gráfica
root = tk.Tk()
root.title("Jogo da Velha")
root.geometry("400x450")
root.config(bg="#87CEFA")

# Inicializando as variáveis
game_mode = "vs_player"  # Padrão é jogar contra outro jogador
game_over = False
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]

# Criando os botões do tabuleiro
buttons = []

for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text="", font=("Arial", 30), width=5, height=2, 
                           command=lambda i=i, j=j: on_button_click(i, j))
        button.grid(row=i, column=j, padx=5, pady=5)
        row.append(button)
    buttons.append(row)

# Menu para escolher o modo de jogo
frame_menu = tk.Frame(root, bg="#87CEFA")
frame_menu.grid(row=3, column=0, columnspan=3, pady=10)

btn_vs_player = tk.Button(frame_menu, text="2 Jogadores", font=("Arial", 12), bg="#ffcc00", command=lambda: choose_game_mode("vs_player"))
btn_vs_player.grid(row=0, column=0, padx=5)

btn_vs_computer = tk.Button(frame_menu, text="VS Computador", font=("Arial", 12), bg="#ffcc00", command=lambda: choose_game_mode("vs_computer"))
btn_vs_computer.grid(row=0, column=1, padx=5)

btn_restart = tk.Button(frame_menu, text="Reiniciar", font=("Arial", 12), bg="#ffcc00", command=restart_game)
btn_restart.grid(row=0, column=2, padx=5)

root.mainloop()
