from dash import Dash, html, dcc, callback, Input, Output, register_page, dash_table
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import plotly.express as px
import pandas as pd 
import json
import dash_daq as daq
from random import sample
import requests
import re


register_page(__name__,
    name='5. Aller plus loin'
)


#-----------------------------------------------------------------------#
# Sources                                                               #
#-----------------------------------------------------------------------#

# Importation fichier geojson
with open("assets/mdp/mdp.json") as f:
    mdp = json.load(f)

#---------------------------------------------------------#
# 5.1 Cartographie                                        #
#---------------------------------------------------------#

# Source Example
election = px.data.election() 
election_geojson = px.data.election_geojson()


# Content Example
carto_ex = html.Div([
    
    html.H3('Political candidate voting pool analysis'),
    
    html.P("Select a candidate:"),
    
    dcc.RadioItems(
        id='pg5-map-candidate', 
        options=["Joly", "Coderre", "Bergeron"],
        value="Coderre",
        inline=True
    ),
    
    dcc.Graph(id="pg5-map-graph")
    
])

# Content Code
carto_code = html.Div([
    
    dmc.Prism(
        children=
"""from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

app = Dash(__name__)

df = px.data.election() 
geojson = px.data.election_geojson()

app.layout = html.Div([
    
    html.H4('Political candidate voting pool analysis'),
    
    html.P("Select a candidate:"),
    
    dcc.RadioItems(
        id='candidate', 
        options=["Joly", "Coderre", "Bergeron"],
        value="Coderre",
        inline=True
    ),
    
    dcc.Graph(id="graph")
    
])

@callback(
    Output("graph", "figure"), 
    Input("candidate", "value"))
def display_choropleth(candidate):
    
    fig = px.choropleth(
        df, geojson=geojson, color=candidate,
        locations="district", featureidkey="properties.district",
        projection="mercator", range_color=[0, 6500])
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")

])

# Source Exercice
file1 = "assets/map/DEP_FR.geojson"
file2 = "assets/map/FD_MAR_2018.csv"

# Importation fichier geojson
with open(file1) as f:
    dep_fr_geo = json.load(f)
    

# Importation du dataframe 
mariage = pd.read_csv(file2, sep=",", low_memory=False)


# Definition du style du color-picker
picker_style = {"display":"inline-block", "margin":10}


# Content Exercice
carto_exo = html.Div([
    
    dbc.Accordion([
        dbc.AccordionItem(title="Objectif", children=[
            html.P([
                "A l’aide du package ",html.A("dash-daq", href="https://dash.plotly.com/dash-daq",target="_blank", className="l"),", utiliser deux ",html.A("color-pickers", href="https://dash.plotly.com/dash-daq/colorpicker",target="_blank", className="l")," sur la thématique du nombre de mariages en France par département en 2018 pour obtenir l’application ci-dessous."
            ]),
            html.Button("FD_MAR_2018.csv", id="btn-mariage"),
            dcc.Download(id="dnl-mariage"),
            html.Button("DEP_FR.json", id="btn-geojson"),
            dcc.Download(id="dnl-geojson")
        ])
    ]),
    
    

    dbc.Container([
    
        dbc.Row([
            html.H4('Cartographie GEOJSON'),
            html.P("Nombre de mariages en France par département en 2018")
        ]),
    
    
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='pg5-carto-graph', responsive=True)
            ], width=7),
        
            dbc.Col([
                html.H4('Interactive color picker with Dash'),
                daq.ColorPicker(id='pg5-carto-color-min',
                                label='Color Min',
                                size = 150,
                                style = picker_style,
                                value=dict(kex='#F1F1ED')),
            
                daq.ColorPicker(id='pg5-carto-color-max',
                                label='Color Max',
                                size = 150,
                                style = picker_style,
                                value=dict(kex='#1E347C'))
            
            ], width=5)
        ])
    ], fluid=True)
    
])


# Content Correction
carto_cor = html.Div([
    
    dmc.Prism(
        children=
"""from dash import Dash, dcc, html, Input, Output, callback
import plotly_express as px
import pandas as pd
import json
import dash_daq as daq
import dash_bootstrap_components as dbc

file1 = "./DEP_FR.geojson"
file2 = "./FD_MAR_2018.csv"

# Importation fichier geojson
with open(file1) as f:
    geo = json.load(f)

# Importation du dataframe 
df = pd.read_csv(file2, sep=",", low_memory=False)

# Initialisation de l'app
app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

# Definition du style du color-picker
picker_style = {"display":"inline-block", "margin":10}

app.layout = dbc.Container([
    
    dbc.Row([
        html.H4('Cartographie GEOJSON'),
        html.P('Nombre de mariages en France par département en 2018')
    ]),
      
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='graph')
        ], width=7),
        
        dbc.Col([
            html.H4('Interactive color picker with Dash'),
            daq.ColorPicker(id='color-min',
                            label='Color Min',
                            size = 150,
                            style = picker_style,
                            value=dict(kex='#F1F1ED')),
            
            daq.ColorPicker(id='color-max',
                            label='Color Max',
                            size = 150,
                            style = picker_style,
                            value=dict(kex='#1E347C'))
            
        ], width=5)
    ])
], fluid=True)

@callback(
    Output('graph', 'figure'),
    Input('color-min','value'),
    Input('color-max','value')
)
def display_choropleth(color_min, color_max):
    
    key_min = [x for x in color_min.keys()][0]
    key_max = [x for x in color_max.keys()][0]
    
    fig = px.choropleth(
        df,
        geojson=geo,
        color = 'NBMAR',
        locations='DEPMAR',
        featureidkey='properties.code',
        projection='mercator',
        range_color=[df['NBMAR'].min(), df['NBMAR'].max()],
        width=800,
        height=600,
        color_continuous_scale=[[0, color_min[key_min]],
                                [1, color_max[key_max]]]
    )
    fig.update_geos(fitbounds='locations', visible=False)
    fig.update_layout(margin={'r':0,'t':0,'l':0,'b':0})
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)""",
        language="python",
        colorScheme="dark")

])


#---------------------------------------------------------#
# 5.2 Jeu des portes                                      #
#---------------------------------------------------------#


# Source Exercice
jdp_gain = ['une voiture','une pomme','une seconde chance']

jdp_alea = sample(jdp_gain, 3)

jdp_opt = [{'label':f'Porte {i+1}','value':jdp_alea[i]} for i in range(len(jdp_alea))]

jdp_n_reset = []

# Content Exercice
jdp_exo = html.Div([
    
        dbc.Accordion([
        dbc.AccordionItem(title="Objectif", children=[
            html.P([
                "Créer une application qui permet de simuler le jeu des portes. Dans ce jeu, il existe trois portes derrières lesquelles se trouvent :", html.Br(),
                html.Li(["Une voiture"]),
                html.Li(["Une seconde chance"]),
                html.Li(["Une pomme"]),
                "L’objectif est de simuler le choix d’une de ces portes via un ",html.A("radio-item",href="https://dash.plotly.com/dash-core-components/radioitems",target="_blank", className="l")," à trois possibilités qui représenteront les trois portes. Au clique d’une des possibilités, ce qui se cache derrière la porte sera dévoilé dans un objet html au dessous.", html.Br(),
                "Tant que l’un des choix n’est pas sélectionné, la personne qui utilise l’application est invitée à jouer.",html.Br(), 
                "Après avoir joué une partie, une autre partie pourra être lancée par l’intermédiaire d’un bouton Rejouer.", html.Br(),
                "Au clique du ",html.A("bouton", href="https://dash-bootstrap-components.opensource.faculty.ai/docs/components/button/",target="_blank", className="l")," Rejouer, le choix précédemment sélectionné disparaît, ce qui se trouve derrière les portes est aléatoirement redistribué et le message d’invitation à jouer au jeu réapparaît."
            ])
        ])
    ]),
    

    html.H3("Jeu des Portes :"),
    
    dcc.RadioItems(id='pg5-jdp-radio', options=jdp_opt, value=None),
    dbc.Button(id='pg5-jdp-button', children="Rejouer", n_clicks=None),
    html.P(id='pg5-jdp-out')

])


# Content Correction
jdp_cor = html.Div([
    
    dmc.Prism(
        children=
"""from dash import Dash, dcc, html, callback, Output, Input
import dash_bootstrap_components as dbc
from random import sample

app = Dash(__name__)

gain = ['une voiture','une pomme','une seconde chance']

alea = sample(gain, 3)

opt = [{'label':f'Porte {i+1}','value':alea[i]} for i in range(len(alea))]

n_reset = []

app.layout = html.Div([
    
    html.H1("Jeu des Portes :"),
    
    dcc.RadioItems(id='radio', options=opt, value=None),
    
    dbc.Button(id='button', children="Rejouer", n_clicks=None),
    
    html.P(id='out')
    
])

@callback(
    Output('out','children'),
    Input('radio','value')
)
def update(value):
    if value is None:
        txt = "Sélectionnez une porte pour découvrir votre lot !"
    else:
        txt = f"Derrière cette porte se trouve {value}"
    return txt

@callback(
    Output('radio','options'),
    Output('radio', 'value'),
    Input('radio', 'options'),
    Input('button','n_clicks'),
    Input('radio', 'value'),
)
def update(opt, n, radio_value):
    if n is not None:
        if n > len(n_reset):
            n_reset.append(1)
            sample_opt = sample(opt, 3)
            opt = [{'label':f'Porte {i+1}','value':sample_opt[i]['value']} for i in range(len(sample_opt))]
            return opt, None
        else:
           return opt, radio_value            
    else:
        return opt, radio_value

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")

])
  

#-----------------------------------------------------------------------#
# Interface                                                             #
#-----------------------------------------------------------------------#


layout = html.Div([    
    
    html.H1("5. Aller plus loin"),
    
    html.H2("5.1 Cartographie", className="h2s"),
    
    dcc.Input(type="password", debounce=True, placeholder="Pwd to get correction", id="pg5-input-pwd-carto-cor", className="pwd"),
    
    dbc.Tabs([
            dbc.Tab(label="Exemple"   , tab_id="carto-ex"  , children=carto_ex  , className="tab"),
            dbc.Tab(label="Code"      , tab_id="carto-code", children=carto_code, className="tab"),
            dbc.Tab(label="Exercice"  , tab_id="carto-exo" , children=carto_exo , className="tab"),
            dbc.Tab(label="Correction", tab_id="carto-cor" , children=carto_cor , className="tab", id="pg5-pwd-carto-cor", disabled=True)
        ],
        id="carto",
        active_tab="carto-ex"
    ),
    
    
    html.H2("5.2 Jeu des portes", className="h2s"),
    
    dcc.Input(type="password", debounce=True, placeholder="Pwd to get correction", id="pg5-input-pwd-jdp-cor", className="pwd"),
    
    dbc.Tabs([
            dbc.Tab(label="Exercice"  , tab_id="jdp-exo" , children=jdp_exo , className="tab"),
            dbc.Tab(label="Correction", tab_id="jdp-cor" , children=jdp_cor , className="tab", id="pg5-pwd-jdp-cor", disabled=True)
        ],
        id="jdp",
        active_tab="jdp-exo"
    )
    
])

#-----------------------------------------------------------------------#
# Serveur                                                               #
#-----------------------------------------------------------------------#


#---------------------------------------------------------#
# 5.1 Cartographie                                        #
#---------------------------------------------------------#


@callback(
    Output("dnl-mariage", "data"),
    Input("btn-mariage", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(mariage.to_csv, "FD_MAR_2018.csv", index=False, sep=";")


@callback(
     Output("dnl-geojson", "data"),
     Input("btn-geojson", "n_clicks"),
    prevent_initial_call=True,
)
def download_json_file(n_clicks):
    URL = "https://github.com/LeoDtrt/univ-rennes-dash/blob/main/src/assets/map/DEP_FR.geojson"
    response = requests.get(URL)
    data = response.content.decode("utf-8")
    data = json.loads(data)
    data = data["payload"]["blob"]["rawLines"][0]
    data = json.loads(data)
    data = re.sub("\'\d{1,4}\':","", str(data))
    data = data.replace(": ",":")
    data = data.replace(", ",",")
    data = data.replace("\'FeatureCollection\', ","")
    data = data.replace("\'",'\"')
    data = data.replace('{ "FeatureCollection"}','"FeatureCollection"')  
    data = data.replace('"features":{ {','"features":[{')    
    data = data.replace('}}}}','}}]}')
    data = data.replace('-d"',"-d'")
    return dict(content=data, filename="DEP_FR.geojson")


# Example
@callback(
    Output("pg5-map-graph", "figure"), 
    Input("pg5-map-candidate", "value"))
def display_choropleth(candidate):
    
    fig = px.choropleth(election, 
                        geojson=election_geojson, 
                        color=candidate,
                        locations="district",
                        featureidkey="properties.district",
                        projection="mercator", 
                        range_color=[0, 6500])
    
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    
    return fig


# Exercice
@callback(
    Output('pg5-carto-graph', 'figure'),
    Input('pg5-carto-color-min','value'),
    Input('pg5-carto-color-max','value')
)
def display_choropleth(color_min, color_max):
    
    key_min = [x for x in color_min.keys()][0]
    key_max = [x for x in color_max.keys()][0]
    
    fig = px.choropleth(
        mariage,
        geojson=dep_fr_geo,
        color = 'NBMAR',
        locations='DEPMAR',
        featureidkey='properties.code',
        projection='mercator',
        range_color=[mariage['NBMAR'].min(), mariage['NBMAR'].max()],
        width=800,
        height=600,
        color_continuous_scale=[[0, color_min[key_min]],
                                [1, color_max[key_max]]]
    )
    fig.update_geos(fitbounds='locations', visible=False)
    fig.update_layout(margin={'r':0,'t':0,'l':0,'b':0})
    
    return fig

@callback(
    Output("pg5-pwd-carto-cor", "disabled"),
    Input("pg5-input-pwd-carto-cor","value")
)
def password(pwd):
    if pwd==mdp['exo_51']:
        return(False)
    else:
        return(True)

#---------------------------------------------------------#
# 5.2 Jeu des portes                                      #
#---------------------------------------------------------#


@callback(
    Output('pg5-jdp-out','children'),
    Input('pg5-jdp-radio','value')
)
def update(value):
    if value is None:
        txt = "Sélectionnez une porte pour découvrir votre lot !"
    else:
        txt = f"Derrière cette porte se trouve {value}"
    return txt

@callback(
    Output('pg5-jdp-radio','options'),
    Output('pg5-jdp-radio', 'value'),
    Input('pg5-jdp-radio', 'options'),
    Input('pg5-jdp-button','n_clicks'),
    Input('pg5-jdp-radio', 'value'),
)
def update(opt, n, radio_value):
    if n is not None:
        if n > len(jdp_n_reset):
            jdp_n_reset.append(1)
            sample_opt = sample(opt, 3)
            opt = [{'label':f'Porte {i+1}','value':sample_opt[i]['value']} for i in range(len(sample_opt))]
            return opt, None
        else:
           return opt, radio_value            
    else:
        return opt, radio_value

@callback(
    Output("pg5-pwd-jdp-cor", "disabled"),
    Input("pg5-input-pwd-jdp-cor","value")
)
def password(pwd):
    if pwd==mdp['exo_52']:
        return(False)
    else:
        return(True)