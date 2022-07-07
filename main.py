import streamlit as st
from games_process import process_games, listing_games, sorting_new_games
import pandas as pd

    
# Declarando variaveis de controle
qnt_numbers = qnt_games = 0

# Processamento de dados
## Declarando tabela com todos os jogos e processando os dados
all_games = process_games(r'mega_sena.xlsx')

## Pegando todos os jogos e transforma em uma lista com todos os jogos anteriores
previous_games = listing_games(all_games)

# Função do sorteador principal
## Side Bar
st.sidebar.markdown('### Jogos Anteriores')
st.sidebar.write(all_games)

## Main Page
st.image(r'imagens/mega-sena-logo-1.png')
'''
# Sorteador de Jogos da Mega-Sena
### Todos os jogos sorteados pelo app, **com certeza nunca foram sorteados anteriormente** pela caixa economica
'''

### Formulario Main Page
games_numbers = st.form('qnt_jogos_e_numeros')
qnt_games = games_numbers.number_input('Quantos Jogos Deseja Sortear?', min_value=1)
qnt_numbers = games_numbers.number_input('Quantos Numeros Cada Jogo?', min_value=6, max_value=15)
games_numbers.form_submit_button('Sortear')

### Sorteando jogos e printando na tela
if (qnt_games != 0 and qnt_numbers != 0):
    new_games_dt = pd.DataFrame(sorting_new_games(qnt_games, qnt_numbers, previous_games))
    st.table(new_games_dt.sample(5))
    qnt_numbers = qnt_games = 0