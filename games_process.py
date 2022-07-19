import pandas as pd
from random import randint


def process_games(directory):
    '''
    by: Davi Lucciola.
    Formata o excel do site da MegaSena da Caixa Ecônomica
    '''
    mega_sena_games = pd.read_excel(directory, skiprows=6)
    mega_sena_games.drop(['Concurso', 'Data'], axis=1, inplace = True)
    mega_sena_games.columns = map(lambda c: c.capitalize(), mega_sena_games.columns)
    return mega_sena_games

def listing_games(sheet):
    '''
    by: Davi Lucciola.
    Pega a base de dados formatada (excel) e faz um jogo
    com as 6 bolas de cada linha.
    No final adiciona todos os jogos em uma lista unica.
    '''
    previous_game = list() # Variavel suporte para adicionar a lista final
    previous_games = list() # Lista final de jogos
    for rows in range(0, sheet.shape[0]):
        for columns in range(1, 7):
            previous_game.append(sheet[f'Bola {columns}'].loc[rows])
        previous_games.append(previous_game.copy())
        previous_game.clear()
    return previous_games

def sorting_new_games(qnt_games, qnt_numbers, previous_games=[]):
    '''
    by: Davi Lucciola.
    Sorteia jogos aleatorios com uma quantidade de numeros determinada pelo usuario e verifica em uma lista de jogos se tem algum jogo cujo 6 numeros são iguais.
    Caso não, esse jogo é adicionado a lista de jogos sorteados, caso sim, o jogo é descartado.
    O processo se repete até a lista ter a quantidade de jogos determinada pelo usuario.
    '''
    game_ind = list() # Cada novo Jogo Aleatorio
    games_new = list() # Lista com cada novo Jogo
    for rep in range(qnt_games):
        while len(game_ind) < qnt_numbers:
            n = randint(1, 60)
            if n not in game_ind:
                game_ind.append(n)
        game_ind.sort() 
        count_num_games = 0 # Contador para verificar se há uma sena já sorteada anteriormente no jogo
        exist_sena = False # Variavel logica para controlar se o jogo será adicionado no final das verificações
        for game in previous_games:
            if game_ind in games_new:
                break
            for num in game_ind:
                if num in game:
                    count_num_games += 1
            if count_num_games == 6:
                exist_sena = True
                break
            count_num_games = 0
        if not exist_sena:
            games_new.append(game_ind.copy())
        game_ind.clear()
    return games_new

def renaming(df):
    for c in range(len(df.columns)):
        df.rename({c: f'Bola {c+1}'}, axis=1, inplace=True)
    for c in range(len(df.index)):
        df.rename({c: f'Jogo {c+1}'}, axis=0, inplace=True)
    return df

