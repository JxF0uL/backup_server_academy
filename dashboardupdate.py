import streamlit as st
import pandas as pd

# definição de eixos
x_values = ['1', '2', '3', '4', '5', '6']

# funções de carregamento de dados
dataframe = pd.DataFrame({
    "Entregues" : [2, 1, 1, 3, 5, 2] ,
    "Em atraso" : [0, 2, 4, 4, 0, 1] ,
    "Em desenvolvimento" : [1, 3, 2, 5, 6, 4]
}, index=x_values)
dataframe2 = pd.DataFrame({
    "Entregues" : [1, 2, 3, 4, 5, 6] ,
    "Em atraso" : [6, 5, 4, 3, 2, 1] ,
    "Em desenvolvimento" : [4, 6, 2, 1, 6, 9]
}, index=x_values)
dataframe3 = pd.DataFrame({
    "Entregues" : [8, 5, 3, 2, 6, 0] ,
    "Em atraso" : [5, 2, 7, 3, 6, 2] ,
    "Em desenvolvimento" : [1, 5, 9, 6, 2, 0]   
}, index=x_values )

# interface streamlit
st.set_page_config(page_title="Dashboard de projetos", layout="wide")
st.title("Dashboard de Projetos do Eniac Academy")
st.text("Olá, Mauro! O que quer verificar hoje?")
st.divider()

# início side bar
with st.sidebar:
    st.image("C:/Users/usrlabecon/Documents/streamlit/venv/static/logoAcademy.png")
    st.page_link("https://eniacacademy.com.br/dashboard/", label="Voltar ao dashboard de estações")
    st.page_link("https://eniacacademy.com.br/dashboard/", label="Alunos")
    st.page_link("https://eniacacademy.com.br/dashboard/", label="Perfil")      

# fim da side bar

with st.container():
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Taxa de projetos entregues dentro do prazo", "74%", "-7%", border=True)
    col2.metric("Projetos ativos", value=10, delta="+ 2", border=True)
    col3.metric("Projetos em stand-by", value=3, delta="+ 0", delta_color="off", border=True)
    col4.metric("Projetos finalizados no último mês", value=1, delta="+ 0", delta_color="off", border=True)
    st.divider()

# gráficos
st.title("Monitoramento individual de estações")
st.link_button("Dashboard de projetos", "https://eniacacademy.com.br/dashboard/")
with st.container():
    if st.checkbox("DEV, PMO, BPO e Marketing", value=True):
        with st.container():
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                with st.container(border=True):
                    st.title("DEV")
                    st.markdown("Gestor: Giovani Dantas Braconi")
                    st.divider()
                    with st.container():
                        colMetric, colButton = st.columns(2)
                        with colMetric:
                            st.metric("Projetos ativos:", value=3)
                        with colButton:
                            st.link_button("Analisar", "#")
                    st.line_chart(dataframe, x_label="Mês", y_label="Quantidade", color=["#8a2f2f", "#403778", "#2f8a30"])
                    # gráfico de linha c nivel de entrega por semestre
            
            with col2:
                with st.container(border=True):
                    st.title("PMO")
                    st.markdown("Gestor: Pedro")
                    st.divider()
                    with st.container():
                        colMetric, colButton = st.columns(2)
                        with colMetric:
                            st.metric("Projetos ativos:", value=17)
                        with colButton:
                            st.link_button("Analisar", "#")
                    st.line_chart(dataframe3, x_label="Mês", y_label="Quantidade", color=["#8a2f2f", "#403778", "#2f8a30"])

            with col3:
                with st.container(border=True):
                    st.title("BPO")
                    st.markdown("Gestor: Vanessa Reyes Manzano")
                    st.divider()
                    with st.container():
                        colMetric, colButton = st.columns(2)
                        with colMetric:
                            st.metric("Projetos ativos:", value=6)
                        with colButton:
                            st.link_button("Analisar", "#")
                    st.line_chart(dataframe2, x_label="Mês", y_label="Quantidade", color=["#8a2f2f", "#403778", "#2f8a30"])

            with col4:
                with st.container(border=True):
                    st.title("Marketing")
                    st.markdown("Gestor: Ylla")
                    st.divider()
                    with st.container():
                        colMetric, colButton = st.columns(2)
                        with colMetric:
                            st.metric("Projetos ativos:", value=4)
                        with colButton:
                            st.link_button("Analisar", "#")
                    st.line_chart(dataframe3, x_label="Mês", y_label="Quantidade", color=["#8a2f2f", "#403778", "#2f8a30"])

    # segunda linha
    if st.checkbox("RH, IA, SDR e QA"):
        with st.container():
            col5, col6, col7, col8 = st.columns(4)

            with col5:
                with st.container(border=True):
                    st.title("RH")
                    st.markdown("Gestor: Thamyres")
                    st.divider()
                    with st.container():
                        colMetric, colButton = st.columns(2)
                        with colMetric:
                            st.metric("Projetos ativos:", value=9)
                        with colButton:
                            st.link_button("Analisar", "#")
                    st.line_chart(dataframe, x_label="Mês", y_label="Quantidade", color=["#8a2f2f", "#403778", "#2f8a30"])
            
            with col6:
                with st.container(border=True):
                    st.title("IA")
                    st.markdown("Gestor: Mauro Claro")
                    st.divider()
                    with st.container():
                        colMetric, colButton = st.columns(2)
                        with colMetric:
                            st.metric("Projetos ativos:", value=1)
                        with colButton:
                            st.link_button("Analisar", "#")
                    st.line_chart(dataframe2, x_label="Mês", y_label="Quantidade", color=["#8a2f2f", "#403778", "#2f8a30"])

            with col7:
                with st.container(border=True):
                    st.title("SDR")
                    st.markdown("Gestor: Sarah Xavier")
                    st.divider()
                    with st.container():
                        colMetric, colButton = st.columns(2)
                        with colMetric:
                            st.metric("Projetos ativos:", value=4)
                        with colButton:
                            st.link_button("Analisar", "#")
                    st.line_chart(dataframe3, x_label="Mês", y_label="Quantidade", color=["#8a2f2f", "#403778", "#2f8a30"])

            with col8:
                with st.container(border=True):
                    st.title("QA")
                    st.markdown("Gestor: -")
                    st.divider()
                    with st.container():
                        colMetric, colButton = st.columns(2)
                        with colMetric:
                            st.metric("Projetos ativos:", value=6)
                        with colButton:
                            st.link_button("Analisar", "#")
                    st.line_chart(dataframe, x_label="Mês", y_label="Quantidade", color=["#8a2f2f", "#403778", "#2f8a30"])

st.divider()


# área de projetos que estao atrasados ou ha algum motivo pra precisarem de atençao extra
with st.container():
    st.title("Projetos que precisam de atenção")
    st.write("Projetos que estão sob alguma condição de irregularidade ou necessitam de um acompanhamento mais próximo; capacidade máx.: 04 projetos")
    # nível de prioridade definido na criação do projeto 
    # funções para identificar prioridade

    # fim das funções
    with st.expander("Acessar projetos"):
        with st.container(border=True):
            colunaTitulo, colunaSprint, colunaInfo, colunaBut = st.columns(4, vertical_alignment="center", gap="large")
            with colunaTitulo:
                st.write("Projeto DEV: atualização do site Eniac Academy")
            with colunaSprint:
                st.write("Sprint 01")
            with colunaInfo:
                st.write("Em desenvolvimento") 
            with colunaBut:
                st.link_button("Acessar projeto DEV", "#") # link individual para acesso àquele projeto
        with st.container(border=True):
            colunaTitulo, colunaSprint, colunaInfo, colunaBut = st.columns(4, vertical_alignment="center", gap="large")
            with colunaTitulo:
                st.write("Projeto MKT: newsletter")
            with colunaSprint:
                st.write("Sprint 03")
            with colunaInfo:
                st.write("Em desenvolvimento")
            with colunaBut:
                st.link_button("Acessar projeto MKT", "#")
        with st.container(border=True):
            colunaTitulo, colunaSprint, colunaInfo, colunaBut = st.columns(4, vertical_alignment="center", gap="large")
            with colunaTitulo:
                st.write("Projeto BPO: organização do ambiente de trabalho")
            with colunaSprint:
                st.write("Sprint 02")
            with colunaInfo:
                st.write("Em desenvolvimento")
            with colunaBut:
                st.link_button("Acessar projeto BPO", "#")
        with st.container(border=True):
            colunaTitulo, colunaSprint, colunaInfo, colunaBut = st.columns(4, vertical_alignment="center", gap="large")
            with colunaTitulo:
                st.write("Projeto SDR")
            with colunaSprint:
                st.write("Sprint 01")
            with colunaInfo:
                st.write("Em desenvolvimento")
            with colunaBut:
                st.link_button("Acessar projeto SDR", "#")
