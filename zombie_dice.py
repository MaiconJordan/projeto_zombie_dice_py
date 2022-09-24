import random
"""
Aluno: Maicon Jordan de Sousa Rocha
Curso: Análise e Desenvolvimento de Sistemas - EAD
Turma 01
"""

import random
import time


class Player:
    def __init__(self, name):
        self.name = name
        self.brains = 0
        self.shots = 0

    def __repr__(self) -> str:
        return self.name


red_dice = "TPTCTP"
yellow_dice = "TPCTCP"
green_dice = "TCPCTC"

dices = []
dices += 6 * [green_dice]
dices += 4 * [yellow_dice]
dices += 3 * [red_dice]
dices = tuple(dices)
print(dices)


class Game:
    def __init__(self):
        self.all_dices = []



    def get_dices(self, passes):
        random.shuffle(self.all_dices)
        select_dices = []
        for i in range(3 - len(passes)):
            select_dices.append(self.all_dices.pop())
        #print(select_dices)
        return select_dices + passes

    def get_brains(self, dices_values):
        return dices_values.count('C')

    def get_shots(self, dices_values):
        return dices_values.count('T')

    def get_passes(self, dices_values):

        result = [i for i, v in enumerate(dices_values) if v == 'P']
        #print(result)
        return result
    def time_sleep_empty(self):
        for i in range(5):
            time.sleep(0.3)
            print('', end='')


    def time_sleep_fast(self):
        for i in range(5):
            time.sleep(0.1)
            print('', end='')

    def get_dices_values(self, select_dices):
        n1 = random.randint(0, 5)
        n2 = random.randint(0, 5)
        n3 = random.randint(0, 5)
        self.time_sleep_fast()
        print(f'dado {"vermelho" if select_dices[0] > 10 else "verde" if select_dices[0] < 7 else "amarelo"}  - {dices[select_dices[0]][n1]}')
        self.time_sleep_fast()
        print(f'dado {"vermelho" if select_dices[1] > 10 else "verde" if select_dices[1] < 7 else "amarelo"}  - {dices[select_dices[1]][n2]}')
        self.time_sleep_fast()
        print(f'dado {"vermelho" if select_dices[2] > 10 else "verde" if select_dices[2] < 7 else "amarelo"}  - {dices[select_dices[2]][n3]}')
        return dices[select_dices[0]][n1], dices[select_dices[1]][n2], dices[select_dices[2]][n3]

    def start(self):
        print("\033[1;35m************************************\033[m")
        print("\033[1;35m***********\033[m \033[1;36mZOMBIE DICE\033[m \033[1;35m************\033[m")
        print("\033[1;35m************************************\033[m")
        self.time_sleep_fast()
        print("\033[1;30;41mSeja bem-vindo ao jogo Zombie Dice!!\033[m\n");
        number_players = 0

        while True:
            try:
                self.time_sleep_fast()
                number_players = int(
                    input("\033[1;36mInforme a quantidade de jogadores: \033[m"))
                if (number_players > 1):
                    break
                else:
                    print(
                        "\033[1;33mVOCẼ PRECISA INFORMAR ACIMA DE 2 JOGADORES!\033[m")
            except ValueError:
                print('Por favor digite um número inteiro para determinar a quantidade de jogadores')



        players = []

        for i in range(number_players):
            self.time_sleep_empty()
            nome = input(
                '\033[1;36mInforme o nome do jogador {} :\033[m' .format(str(i + 1)))
            players.append(Player(name=nome))


        while (True):
            for player in players:
                self.all_dices = list(range(13))
                print(f'----------  {player.name} joga ----------' )
                passes = []
                select_dices = []
                while (True):
                    passes_id = [select_dices[i] for i in passes]
                    select_dices = self.get_dices(passes_id)
                    dices_values = self.get_dices_values(select_dices)
                    player.brains += self.get_brains(dices_values)
                    player.shots += self.get_shots(dices_values)
                    passes = self.get_passes(dices_values)

                    #print(self.all_dices)
                    self.time_sleep_fast()
                    print(f'Numero de cerébros: {player.brains} ')
                    self.time_sleep_fast()
                    print(f'Numero de tiros: {player.shots} ')

                    if player.shots >= 3:
                        player.brains = 0
                        player.shots = 0
                        break
                    self.time_sleep_fast()
                    continue_turn = input(
                        "AVISO!!! Você deseja continuar jogando dados? (s = SIM) / (n = Não):  ")
                    if continue_turn == 'n':
                        player.shots = 0
                        break

            winner = None
            winner_points = 0
            for player in players:
                if player.brains >= 13 and player.brains > winner_points:
                    winner = player
                    winner_points = player.brains

            if winner:
                print(f'O Vencedor é {winner}')
                break


if __name__ == '__main__':
    game = Game()
    game.start()
