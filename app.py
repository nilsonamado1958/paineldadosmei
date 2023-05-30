# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("BASEMEI.xlsx")

fig = px.bar(df, x="REGIAO_ATUACAO", color="SETOR_ATIVIDADE", barmode="group")
opcoes = list(df['REGIAO_ATUACAO'].unique())
opcoes.append("Todas as regiões")


app.layout = html.Div(children=[
    html.H1(children='Painel com análise de dados qualificados de MEI para MEI da cidade de São Paulo'),
    html.H2(children='No gráfico são apresentadas as quantidades de Microempreendedores Individuais distribuidos regionalmente pela cidade de Sao Paulo e por tipo de setor economico em que atua.'),
    html.Div(children='''
        Obs: Esse gráfico exibe analise quantitativa e amostral dos microempreendedores individuais que, em
dezembro de 2022, somavam mais de 1,17 milhão de MEI na cidade de São Paulo, sendo certo que a sua
proporcionalidade relativa deve ser considerada. Espera-se que as informações apresentadas ajudem os
microempreendedores no estabelecimento de estratégias em prol do desenvolvimento de seus negocios.
    '''),

    dcc.Dropdown(opcoes, value='Todas as regiões', id='lista_regioes'),

    dcc.Graph(
        id='grafico quantidade meis por regiao',
        figure=fig
    )
])

@app.callback(
    Output('grafico quantidade meis por regiao', 'figure'),
    Input('lista_regioes', 'value')
)
def update_output(value):
    if value == "Todas as regiões":
        fig = px.bar(df, x="REGIAO_ATUACAO", color="SETOR_ATIVIDADE", barmode="group")
    else:
        tabela_filtrada = df.loc[df['REGIAO_ATUACAO']==value, :]
        fig = px.bar(tabela_filtrada, x="REGIAO_ATUACAO", color="SETOR_ATIVIDADE", barmode="group")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
