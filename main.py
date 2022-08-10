import streamlit as st
import pickle
import pandas as pd


def top_games(game):
    count = 1
    print('similar game to {} include \n'.format(game))
    for item in df_item.sort_values(ascending=False, by=game).index[1:6]:
        print('NO.{} = {}'.format(count,item))
        count += 1


game_dict = pickle.load(open('game_dict.pkl', 'rb'))
top_games = pickle.load(open('top_games.pkl', 'rb'))
piovt_dic = pickle.load(open('pivot_dict.pkl', 'rb'))
df_item = pickle.load(open('df_item.pkl', 'rb'))
df = pd.DataFrame(game_dict)
pv = pd.DataFrame(piovt_dic)
df_item = pd.DataFrame(df_item)

st.title("Game Recommendation System")
select_game_name = st.selectbox('Enter Your Game Name',
                                df['game_name'].values)

if st.button('Recommend Games'):
    name = top_games(select_game_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(name[0])

    with col2:
        st.text(name[1])

    with col3:
        st.text(name[2])

    with col4:
        st.text(name[3])

    with col5:
        st.text(name[4])
