import socket
import random
from threading import *

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('0.0.0.0', 6003)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

message = "Welcome on our TicTacToe challenge (Frenchies call it 'Morpion'). You have to play 500 games with me, and you will get the flag only if you have 0 loose at the end of those games (draws are allowed). Place your coin with '13' for top right, '22' for middle center or '31' for bottom left for example. \n>>> Now Playing: "


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

            
    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        li = ""
        for row in self.board:
            for item in row:
                li += item + " "
            li += "\n"
        return li
        
    def verifcase(self, row, col):
        if self.board[int(row)][int(col)] != "-":
            return False
        elif self.board[int(row)][int(col)] == "-":
            return True  


class client(Thread):
    def __init__(self, conn, addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.ttt = TicTacToe()
        self.gameplayed = 0
        self.gameloose = 0
        self.start()

    def gamestart(self, game):
        game.create_board()

        player = 'O' if game.get_random_first_player() == 0 else 'X'
        while True:
            message = "\n>>> Player " +player + " turn \n" + game.show_board()
            self.conn.sendall(message.encode())
            game.show_board()

            if player == 'X':
                b1 = True
                while b1:
                    row, col = list(map(int, [random.randint(1,3), random.randint(1,3)]))
                    if game.verifcase(row-1, col-1):
                        b1 = False
            # taking user input
            else:
                b1 = True
                while b1:
                    respectedlength = 0
                    testchar = 0
                    while respectedlength == 0 and testchar != 3:
                        testchar = 0
                        inp = self.conn.recv(1024)
                        if len(inp) == 3:
                            respectedlength = 1
                            for i in inp.decode():
                                print(i)
                                if i in ["1", "2", "3", "\n"]:
                                    testchar += 1
                                    print("testchar " + str(testchar))
                                else:
                                    print(i)
                                    self.conn.sendall(b"not possible")
                                    respectedlength = 0
                                    break
                                   
                        else:
                            self.conn.sendall(b"Wrong input, try again")
                        
                        row = inp.decode()[0]
                        col = inp.decode()[1]
                    if game.verifcase(int(row)-1, int(col)-1):
                        b1 = False

            # fixing the spot
            game.fix_spot(int(row) - 1, int(col) - 1, player)

            # checking whether current player is won or not
            if game.is_player_win(player):
                message = f"Player {player} wins the game!"
                self.conn.sendall(message.encode())
                return player

            # checking whether the game is draw or not
            if game.is_board_filled():
                print("Match Draw!")
                return "draw"

            # swapping the turn
            player = game.swap_player_turn(player)

    def run(self):
        print('connection from', self.addr)
        self.conn.sendall(message.encode())

        while (self.gameloose == 0) and (self.gameplayed < 500):
            print("starting new game")
            self.ttt = TicTacToe()
            playing = self.gamestart(self.ttt)
            if playing != 'X':
                self.gameplayed += 1
                self.conn.sendall(b"Game played: " + str(self.gameplayed).encode())
            else:
                self.gameloose = 1
                self.conn.sendall(b"Sorry, you loose")
        
        if(self.gameplayed == 500):
            self.conn.sendall(b"Congratulation, you win the challenge, here is your flag: FMCTF{t1c-t4c-t0e_15_4w3s0m3}")
        self.conn.close()


sock.listen(20)
print('server started and listening')
while True:
    conn, addr = sock.accept()
    client(conn, addr)