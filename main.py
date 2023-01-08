import streamlit as st
from games_process import process_games, listing_games, sorting_new_games, renaming
import pandas as pd
from io import BytesIO


@st.experimental_memo
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data


# Declarando variaveis de controle
qnt_numbers = qnt_games = 0

# Processamento de dados
## Declarando tabela com todos os jogos e processando os dados
all_games = process_games(r'./assets/mega_sena.xlsx')

## Pegando todos os jogos e transforma em uma lista com todos os jogos anteriores
previous_games = listing_games(all_games)

# Função do sorteador principal
## Side Bar
st.sidebar.markdown('### Jogos Anteriores')
st.sidebar.write(all_games)

## Main Page
st.image(r'./assets/mega-sena-logo.png')
'''
# Sorteador de Jogos da Mega-Sena
### Todos os jogos sorteados pelo app, **com certeza nunca foram sorteados anteriormente** pela caixa economica
'''

### Formulario Main Page
with st.form('qnt_jogos_e_numeros'):
    qnt_games = st.number_input('Quantos Jogos Deseja Sortear?', min_value=1)
    qnt_numbers = st.number_input('Quantos Numeros Cada Jogo?', min_value=6, max_value=15)
    button = st.form_submit_button('Sortear')

### Sorteando jogos e printando na tela
if button:
    new_games_df = renaming(pd.DataFrame(sorting_new_games(qnt_games, qnt_numbers, previous_games)))
    st.dataframe(new_games_df, use_container_width=True)
    file_name = f'mega_sena_{qnt_games}_games.xlsx'
    new_games_df_xlsx = to_excel(new_games_df)
    st.download_button('Download Excel', data=new_games_df_xlsx, file_name=file_name)

