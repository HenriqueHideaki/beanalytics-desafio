import pandas as pd
import streamlit as st
import altair as alt

# Carregar dados do CSV
df = pd.read_csv("dados/extracted_game_data.csv")

# Configurar título do aplicativo
st.set_page_config(page_title='Dashboard de Dados dos Jogos Steam', layout='wide', initial_sidebar_state='expanded')
st.title('Dashboard de Dados dos Jogos Steam')

# Adicionar barra lateral para navegação
st.sidebar.title("Navegação")
page = st.sidebar.selectbox("Selecione a Página", ["Tabela de Dados", "Visualizações"])

# Função para mostrar a tabela de dados
def show_data_table():
    st.subheader('Pico de uso dos Jogos')
    st.dataframe(df.head(20), height=500)

# Função para mostrar os gráficos
def show_charts():
    st.subheader('Buscar Jogo')
    game_name = st.text_input('Nome do Jogo')

    # Filtrar dados com base na barra de pesquisa
    if game_name:
        filtered_df = df[df['Nome do Jogo'].str.contains(game_name, case=False)]
    else:
        filtered_df = df.head(20)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.dataframe(filtered_df)

    with col2:
        st.subheader('Gráficos')

        # Gráfico de Barras: Atual
        chart_atual = alt.Chart(filtered_df).mark_bar().encode(
            x=alt.X('Nome do Jogo', sort='-y', title='Nome do Jogo', axis=alt.Axis(labelAngle=-45)),
            y=alt.Y('Atual', title='Jogadores Atuais')
        ).properties(
            title='Jogadores Atuais por Jogo',
            width=600,
            height=400
        )
        st.altair_chart(chart_atual, use_container_width=True)

        # Gráfico de Barras: Pico 24hrs
        chart_24hrs = alt.Chart(filtered_df).mark_bar().encode(
            x=alt.X('Nome do Jogo', sort='-y', title='Nome do Jogo', axis=alt.Axis(labelAngle=-45)),
            y=alt.Y('Pico 24hrs', title='Pico de Jogadores nas Últimas 24hrs')
        ).properties(
            title='Pico de Jogadores nas Últimas 24hrs por Jogo',
            width=600,
            height=400
        )
        st.altair_chart(chart_24hrs, use_container_width=True)

        # Gráfico de Barras: Pico de todos os tempos
        chart_all_time = alt.Chart(filtered_df).mark_bar().encode(
            x=alt.X('Nome do Jogo', sort='-y', title='Nome do Jogo', axis=alt.Axis(labelAngle=-45)),
            y=alt.Y('Pico de todos os tempos', title='Pico de Jogadores de Todos os Tempos')
        ).properties(
            title='Pico de Jogadores de Todos os Tempos por Jogo',
            width=600,
            height=400
        )
        st.altair_chart(chart_all_time, use_container_width=True)

# Mostrar conteúdo com base na seleção do usuário
if page == "Tabela de Dados":
    show_data_table()
elif page == "Visualizações":
    show_charts()
