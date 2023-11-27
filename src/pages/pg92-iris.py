from dash import Dash, html, dcc, callback, Output, Input, register_page
import dash_bootstrap_components as dbc
import plotly.express as px


register_page(__name__,
    name='Iris Dataset'
)

df = px.data.iris()

var = [{'label':s.replace('_',' ').capitalize(),'value':s}  for s in df.columns[0:3]]

layout = dbc.Col(children=[
    html.H1(children='Dash: A web application framework for your data.'),
    
    html.H4('Horizontal scale :'),
    dcc.Dropdown(id='x', options=var, value=var[0]['value']),
    
    html.H4('Vertical scale :'),
    dcc.Dropdown(id='y', options=var, value=var[1]['value']),
    
    dcc.Graph(figure={}, id='scatter')
], width=8)


@callback(
    Output(component_id='scatter', component_property='figure'),
    Input(component_id='x', component_property='value'),
    Input(component_id='y', component_property='value'),
)
def update_graph(x, y):
    fig = px.scatter(df, x=x, y=y, color="species",
                     labels={
                         x:x.replace('_',' ').capitalize(),
                         y:y.replace('_',' ').capitalize(),
                        },
                     title="Scatter Plot of the Iris Dataset")
    return fig

