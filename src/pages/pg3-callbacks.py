from dash import Dash, html, dcc, callback, Input, Output, register_page, dash_table, State
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import plotly.express as px
import base64
import datetime
import io
import json
import pandas as pd

register_page(__name__,
    name='3. Callbacks'
)


#-----------------------------------------------------------------------#
# Sources                                                               #
#-----------------------------------------------------------------------#

# Importation fichier geojson
with open("assets/mdp/mdp.json") as f:
    mdp = json.load(f)

#---------------------------------------------------------#
# 3.1 Dropdown                                            #
#---------------------------------------------------------#


# Source Example
opt = ['Choix 1', 'Choix 2', 'Choix 3']

# Content Example
dropdown_ex = html.Div([

    html.H3("Simple dropdown choice :"),
    dcc.Dropdown(id="pg3-dropdown", options=opt, value=opt[0]),
    
    html.H3("Multi dropdown choice :"),
    dcc.Dropdown(id="pg3-dropdown-multi", options=opt, value=opt[0], multi=True)

    
])

# Content code
dropdown_code = html.Div([
    dmc.Prism(
        children=
"""from dash import Dash, html, callback, Input, Output, dcc

app = Dash(__name__)

opt = ['Choix 1', 'Choix 2', 'Choix 3']

app.layout = html.Div([
    
    html.H1("Simple dropdown choice :"),
    dcc.Dropdown(id="dropdown", options=opt, value=opt[0]),
    
    html.H1("Multi dropdown choice :"),
    dcc.Dropdown(id="dropdown-multi", options=opt, value=opt[0], multi=True)
    
])

if __name__ == "__main__":
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")
    
])

# Source Exercice
iris = px.data.iris()
var = [{'label':s.replace('_',' ').capitalize(),'value':s}  for s in iris.columns[0:4]]

# Content Exercice
dropdown_exo = html.Div([
    
    dbc.Accordion([
        dbc.AccordionItem(title="Objectif", children=[
            html.P([
                "À l’aide du dataset ",html.Span("iris", className="ds")," disponible dans le package ", html.A("plotly.express", href="https://plotly.com/python/plotly-express/", target="_blank", className="l"), ", créer une application qui permet d'afficher le titre et le graphique ci-dessous.",html.Br(),
                "Afficher un nuage de points qui se met à jour en fonction du choix des quatre premières colonnes de ",html.Span("iris", className="ds")," :", html.I(" Petal length"),",", html.I(" Petal width"),",", html.I(" Sepal length"),",", html.I(" Sepal width"),".",html.Br(),
                "Pour cela, créer deux ",html.A("dropdowns",href="https://dash.plotly.com/dash-core-components/dropdown", target="_blank", className="l")," composés de ces quatre variables. ⚠ Gérer l’affichage du nom des colonnes dans les dropdowns."
            ])
        ])
    ]),

    
    html.H3(children='Dash: A web application framework for your data.'),
    
    html.H5('Horizontal scale :'),
    dcc.Dropdown(id='pg3-x', options=var, value=var[0]['value']),
    
    html.H5('Vertical scale :'),
    dcc.Dropdown(id='pg3-y', options=var, value=var[1]['value']),
    
    dcc.Graph(figure={}, id='pg3-scatter')
])


# Content Correction
dropdown_cor = html.Div([
    
    dmc.Prism(
        children=
"""from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

app = Dash(__name__)

df = px.data.iris()

var = [{'label':s.replace('_',' ').capitalize(),'value':s}  for s in df.columns[0:3]]

app.layout = html.Div(children=[
    
    html.H1(children='Dash: A web application framework for your data.'),
        
    html.H4('Horizontal scale :'),
    dcc.Dropdown(id='x', options=var, value=var[0]['value']),
    
    html.H4('Vertical scale :'),
    dcc.Dropdown(id='y', options=var, value=var[1]['value']),
    
    dcc.Graph(figure={}, id='scatter')
    
])

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

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")

])


#---------------------------------------------------------#
# 3.2 Slider                                              #
#---------------------------------------------------------#


# Content Example
slider_ex = html.Div([
    
    html.H3("Numeric slider from -10 to 10 by 2 and begin with 8 :"),
    dcc.Slider(id="slider-numeric", min = -10, max=10, value=8, step = 2),
    
    html.H3("String slider from State 1 to 10 begin with State 2 :"),
    dcc.Slider(id ="slider-string", min=0, max=9, marks={i: f'State{i}' for i in range(10)}, value=2),
    
    html.H3("Range slider from 0 to 10K by 1K begin between 1K and 5K :"),
    dcc.RangeSlider(id ="slider-range", min=0, max=10000, step=1000, value=[1000,5000])
   
])

# Content Code
slider_code = html.Div([
    dmc.Prism(
        children=
"""from dash import Dash, html, dcc, callback, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    
    html.H1("Numeric slider from -10 to 10 by 2 and begin with 8 :"),
    dcc.Slider(id="slider-numeric", min = -10, max=10, value=8, step = 2),
    
    html.H1("String slider from State 1 to 10 begin with State 2 :"),
    dcc.Slider(id ="slider-string", min=0, max=9, marks={i: f'State{i}' for i in range(10)}, value=2),
    
    html.H1("Range slider from 0 to 10K by 1K begin between 1K and 5K :"),
    dcc.RangeSlider(id ="slider-range", min=0, max=10000, step=1000, value=[1000,5000])

])

if __name__ == "__main__":
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")
    
])

# Source Exercice
gp = px.data.gapminder()
min_pop, max_pop = min(gp['pop']), max(gp['pop'])

# Content Exercice
slider_exo = html.Div([
    
    dbc.Accordion([
        dbc.AccordionItem(title="Objectif", children=[
            html.P([
                "À l’aide du dataset ",html.Span("gapminder", className="ds")," disponible dans le package ", html.A("plotly.express", href="https://plotly.com/python/plotly-express/", target="_blank", className="l"), ", créer une application qui permet d'afficher le titre et le graphique ci-dessous.",html.Br(),
                "Afficher un nuage de points qui représente l’espérance de vie d’un pays (",html.I("life_exp"),") en fonction de son PIB par tête (",html.I("gdpPercap"),") et de sa population (",html.I("pop"),").", html.Br(),
                "Pour cela, créer un ",html.A("range slider",href="https://dash.plotly.com/dash-core-components/rangeslider", target="_blank", className="l")," sur la variable ",html.I("pop"), ". ⚠ Le curseur gauche ne doit pas être bloqué par le curseur droit."
            ])
        ])
    ]),
    
    html.H3("Gapminder dataset :"),   
    
    dcc.Graph(id='pg3-graph-gdp', figure={}),
    
    dcc.RangeSlider(id='pg3-range-slider', min =min_pop , max=max_pop , value=[min_pop, max_pop], pushable=True)

])


# Content Correction
slider_cor = html.Div([
    
    dmc.Prism(
        children=
"""from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px

df = px.data.gapminder()
min_pop, max_pop = min(df['pop']), max(df['pop'])

app = Dash(__name__)

app.layout = html.Div([
    
    html.H1("Gapminder dataset :"),
    
    dcc.Graph(id='graph-gdp', figure={}),
    
    dcc.RangeSlider(id='range-slider', min =min_pop , max=max_pop , value=[min_pop, max_pop], pushable=True)
    
])

@callback(
    Output(component_id='graph-gdp', component_property='figure'),
    Input(component_id='range-slider', component_property="value"),
)
def update_graph(value):
    df_update = df[(df['pop'] >= value[0]) & (df['pop'] <= value[1])]    
    fig = px.scatter(df_update.query("year==2007"), 
                     x="gdpPercap",
                     y="lifeExp", 
                     size="pop",
                     color="continent",
                     hover_name="country",
                     size_max=60,
                     title='Life expectancy by GDP per capita and population in 2007')
    return fig

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")

])

# Source Exercice 2
# Recuperation du minimum et du maximum des annees disponibles
min_year, max_year = gp.year.min(), gp.year.max()

# Creation des markers pour le slider sur les annees
marker_year = {str(year): str(year) for year in gp.year.unique()}

# Recuperation de la liste des continents 
continent = gp.continent.unique()


# Content Exercice 2
slider_exo2 = html.Div([
    
    dbc.Accordion([
        dbc.AccordionItem(title="Objectif", children=[
            html.P([
                "À l’aide du dataset ",html.Span("gapminder", className="ds")," disponible dans le package ", html.A("plotly.express", href="https://plotly.com/python/plotly-express/", target="_blank", className="l"), ", créer une application qui permet d'afficher le titre et le graphique ci-dessous.",html.Br(),
                "Afficher un nuage de points qui représente l’espérance de vie d’un pays (",html.I("life_exp"),") en fonction de son PIB par tête (",html.I("gdpPercap"),") et de sa population (",html.I("pop"),").", html.Br(),
                "L’application doit permettre de :",html.Br(),
                html.Li(["Sélectionner un ou plusieurs continents à l’aide d’un ",html.A("dropdown",href="https://dash.plotly.com/dash-core-components/dropdown", target="_blank", className="l")," à choix multiple (tous les continents sont cochés par défaut)"]),
                html.Li(["Sélectionner une année parmi toutes les années disponibles du dataset à l’aide d’un ",html.A("slider",href="https://dash.plotly.com/dash-core-components/slider", target="_blank", className="l")," (l’année 1982 est sélectionnée par défaut)."]),
                "⚠ L’année du titre du graphique doit se mettre à jour automatiquement lors de la modification de la position du ",html.A("slider",href="https://dash.plotly.com/dash-core-components/slider", target="_blank", className="l"),"."
            ])
        ])
    ]),
    

    # Titre de l'application
    html.H3("Gapminder dataset : Dropdown & Slider"),
    
    # Dropdown permettant de selectionner les continents
    dcc.Dropdown(id="pg3-continent", options=continent, value=continent, multi=True),
    
    # Affichage du graphique LifeExp by GDPperCap
    dcc.Graph(id='pg3-scatter-gdp', figure={}),
    
    # Slider permettant de selectionner l'annee
    dcc.Slider(id='pg3-year', min=min_year , max=max_year , value=min_year,
               marks=marker_year, step = None)

])


# Content Correction 2
slider_cor2 = html.Div([
    
    dmc.Prism(
        children=
"""from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px

#-----------------------------------------------------------------------#
# Initialisation                                                        #
#-----------------------------------------------------------------------#

# Creation de l'objet app contenant l'application dash
app = Dash(__name__)

#-----------------------------------------------------------------------#
# Sources                                                               #
#-----------------------------------------------------------------------#

# Recuperation du dataset Gapminder
df = px.data.gapminder()

# Recuperation du minimum et du maximum des annees disponibles
min_year, max_year = df.year.min(), df.year.max()

# Creation des markers pour le slider sur les annees
slider_marks = {str(year): str(year) for year in df.year.unique()}

# Recuperation de la liste des continents 
opt = df.continent.unique()

#-----------------------------------------------------------------------#
# Interface                                                             #
#-----------------------------------------------------------------------#

app.layout = html.Div([
    
    # Titre de l'application
    html.H1("Gapminder dataset : Dropdown & Slider"),
    
    # Dropdown permettant de selectionner les continents
    dcc.Dropdown(id="dropdown", options=opt, value=opt, multi=True),
    
    # Affichage du graphique LifeExp by GDPperCap
    dcc.Graph(id='graph-gdp', figure={}),
    
    # Slider permettant de selectionner l'annee
    dcc.Slider(id='slider', min=min_year , max=max_year , value=min_year,
               marks=slider_marks, step = None)
])

#-----------------------------------------------------------------------#
# Serveur                                                               #
#-----------------------------------------------------------------------#

@callback(
    Output(component_id='graph-gdp', component_property='figure'),
    Input(component_id='slider', component_property="value"),
    Input(component_id='dropdown', component_property="value")
)
def update_graph(year_value, continent_value):
    df_update = df[(df.year == year_value) & df.continent.isin(continent_value)] 
    fig = px.scatter(df_update, 
                     x="gdpPercap",
                     y="lifeExp", 
                     size="pop",
                     color="continent",
                     hover_name="country",
                     size_max=60,
                     title=f'Life expectancy by GDP per capita and population in {year_value}')
    return fig

#-----------------------------------------------------------------------#
# Run                                                                   #
#-----------------------------------------------------------------------#

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")

])


#---------------------------------------------------------#
# 3.3 Checklist                                           #
#---------------------------------------------------------#


# Content Example
checklist_ex = html.Div([
    
    html.H3('Checklist example :'),
    
    dcc.Checklist(id='pg3-checklist', options=opt, value=opt),
    
    html.H4("Valeurs sélectionnées dans la checklist :"),
    
    html.P(id='pg3-state-out', children='')

   
])

# Content Code
checklist_code = html.Div([
    dmc.Prism(
        children=
"""from dash import Dash, html, dcc, callback, Output, Input

app = Dash(__name__)

opt = ['Choix 1', 'Choix 2', 'Choix 3']

app.layout = html.Div([
    
    html.H1('Checklist example :'),
    
    dcc.Checklist(id='checklist', options=opt, value=opt),
    
    html.H4("Valeurs sélectionnées dans la checklist :"),
    
    html.P(id='state-out', children='')
    
])

@callback(
    Output('state-out', 'children'),
    Input('checklist', 'value')
)
def update_state(values):
    return [html.Li(val) for val in values]

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")
    
])

# Source Exercice
# Definition de l'etat initial de la checklist
continent_init = ['Asia']

# Content Exercice
checklist_exo = html.Div([
    
    dbc.Accordion([
        dbc.AccordionItem(title="Objectif", children=[
            html.P([
                "Répliquer l'application ci-dessous ",html.Span("à partir de l’application de l’exercice 2 de la section 3.2 Slider", className="h"),". Mêmes consignes mais cette fois il faut :",html.Br(),
                html.Li(["Utiliser une ",html.A("checklist",href="https://dash.plotly.com/dash-core-components/checklist", target="_blank", className="l")," plutôt qu’un ",html.A("dropdown",href="https://dash.plotly.com/dash-core-components/dropdown", target="_blank", className="l")," sur la variable ",html.I("continent")]),
                html.Li(["Par défaut, lors du démarrage de l’application, seul le continent Asie doit être coché et l’année doit être la plus récente"]),
                html.Li(["Fixer l’axe des abscisses de -5K à 50K (",html.I("gdpPercap"),")"]),
                html.Li(["Fixer l’axe des ordonnés de 0 à 100 (",html.I("life_exp"),")"])
            ])
        ])
    ]),
    

    # Titre de l'application
    html.H3("Gapminder dataset : Checklist & Slider"),
    
    # Dropdown permettant de selectionner les continents
    dcc.Checklist(id="pg3-list-continent", options=continent, value=continent_init, inline=True),
    
    # Affichage du graphique LifeExp by GDPperCap
    dcc.Graph(id='pg3-graph-exo-checklist', figure={}),
    
    # Slider permettant de selectionner l'annee
    dcc.Slider(id='pg3-slider-exo-checklist', min=min_year , max=max_year , value=max_year,
               marks=marker_year, step = None)

])


# Content Correction
checklist_cor = html.Div([
    
    dmc.Prism(
        children=
"""from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px

#-----------------------------------------------------------------------#
# Initialisation                                                        #
#-----------------------------------------------------------------------#

# Creation de l'objet app contenant l'application dash
app = Dash(__name__)

#-----------------------------------------------------------------------#
# Sources                                                               #
#-----------------------------------------------------------------------#

# Recuperation du dataset Gapminder
df = px.data.gapminder()

# Recuperation du minimum et du maximum des annees disponibles
min_year, max_year = df.year.min(), df.year.max()

# Creation des markers pour le slider sur les annees
slider_marks = {str(year): str(year) for year in df.year.unique()}

# Recuperation de la liste des continents 
opt = df.continent.unique()

# Definition de l'etat initial de la checklist
etat_initial = ['Asia']

#-----------------------------------------------------------------------#
# Interface                                                             #
#-----------------------------------------------------------------------#

app.layout = html.Div([
    
    # Titre de l'application
    html.H1("Gapminder dataset : Checklist & Slider"),
    
    # Dropdown permettant de selectionner les continents
    dcc.Checklist(id="checklist", options=opt, value=etat_initial, inline=True),
    
    # Affichage du graphique LifeExp by GDPperCap
    dcc.Graph(id='graph-gdp', figure={}),
    
    # Slider permettant de selectionner l'annee
    dcc.Slider(id='slider', min=min_year , max=max_year , value=max_year,
               marks=slider_marks, step = None)
])

#-----------------------------------------------------------------------#
# Serveur                                                               #
#-----------------------------------------------------------------------#

@callback(
    Output(component_id='graph-gdp', component_property='figure'),
    Input(component_id='slider', component_property="value"),
    Input(component_id='checklist', component_property="value")
)
def update_graph(year_value, continent_value):
    df_update = df[(df.year == year_value) & df.continent.isin(continent_value)]
    fig = px.scatter(df_update, 
                     x="gdpPercap",
                     y="lifeExp", 
                     size="pop",
                     color="continent",
                     hover_name="country",
                     size_max=60,
                     title=f'Life expectancy by GDP per capita and population in {year_value}')
    fig.update_xaxes(range=[-5000,50000])
    fig.update_yaxes(range=[0, 100])
    return fig

#-----------------------------------------------------------------------#
# Run                                                                   #
#-----------------------------------------------------------------------#

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")

])


#---------------------------------------------------------#
# 3.4 Radio-items                                         #
#---------------------------------------------------------#

# Source Example
radio_opt = [{'label':f'Choix {i}','value':i} for i in range(1,4)]

# Content Example
radio_ex = html.Div([
    
    html.H3("Radio Items examples:"),
    
    dcc.RadioItems(id='pg3-radio-ex', options=radio_opt, value=None),
    
    html.P(id='pg3-radio-ex-out')
    
])


# Content Code
radio_code = html.Div([
    dmc.Prism(
        children=
"""from dash import Dash, html, dcc, callback, Output, Input

app = Dash(__name__)

opt = [{'label':f'Choix {i}','value':i} for i in range(1,4)]

app.layout = html.Div([
    
    html.H1("Radio Items examples:"),
    
    dcc.RadioItems(id='radio', options=opt, value=None),
    
    html.P(id='out')
    
])

@callback(
    Output('out','children'),
    Input('radio','value')
)
def update(value):
    if value is None:
        txt = "Aucun choix n'a encore été sélectionné."
    else:
        txt = f"Le choix numéro {value} a été sélectionné !"
    return(txt)

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")
    
])

# Source Exercice
# Creation des options du radio items pour l'activation du logarithme sur l'axe des x
opt_log = [{'label': 'Activée', 'value': True}, {'label': 'Désactivée', 'value': False}]

# Content Exercice
radio_exo = html.Div([
    
    dbc.Accordion([
        dbc.AccordionItem(title="Objectif", children=[
            html.P([
                "Répliquer l'application ci-dessous ",html.Span("à partir de l’application de l’exercice de la section 3.3 Checklist", className="h"),". Mêmes consignes mais cette fois il faut :",html.Br(),
                html.Li(["Ajouter un ",html.A("radio items",href="https://dash.plotly.com/dash-core-components/radioitems", target="_blank", className="l")," qui permet d’activer la transformation en logarithme de l’axe des abscisses (",html.I("gdpPercap"),")"]),
                html.Li(["Lorsque l’axe des x est en logarithme, les limites vont de 100 à 100K"]),
                html.Li(["Par défaut, tous les continents sont cochés, l’année doit être la plus récente et la transformation en logarithme est activée"])
            ])
        ])
    ]),
    

    # Titre de l'application
    html.H3("Gapminder dataset : Checklist & Slider"),
    
    # Dropdown permettant de selectionner les continents
    html.H6("Sélection des continents :"),
    dcc.Checklist(id='pg3-checklist-exo-radio', options=continent, value=continent, inline=True),
    html.Br(),
    # Radio items permettant de passer l'axe des abscisses en logarithme
    html.H6("Transformation logarithmique du PIB par tête (gdpPercap) :"),
    dcc.RadioItems(id='pg3-radio-log', options=opt_log, value=True),

    # Affichage du graphique LifeExp by GDPperCap
    dcc.Graph(id='pg3-graph-exo-radio', figure={}),
    
    # Slider permettant de selectionner l'annee
    dcc.Slider(id='pg3-slider-exo-radio', min=min_year , max=max_year , value=max_year,
               marks=marker_year, step = None)

])


# Content Correction
radio_cor = html.Div([
    
    dmc.Prism(
        children=
"""from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px

#-----------------------------------------------------------------------#
# Initialisation                                                        #
#-----------------------------------------------------------------------#

# Creation de l'objet app contenant l'application dash
app = Dash(__name__)

#-----------------------------------------------------------------------#
# Sources                                                               #
#-----------------------------------------------------------------------#

# Recuperation du dataset Gapminder
df = px.data.gapminder()

# Recuperation du minimum et du maximum des annees disponibles
min_year, max_year = df.year.min(), df.year.max()

# Creation des markers pour le slider sur les annees
slider_marks = {str(year): str(year) for year in df.year.unique()}

# Recuperation de la liste des continents 
opt_continent = df.continent.unique()

# Creation des options du radio items pour l'activation du logarithme sur l'axe des x
opt_log = [{'label': 'Activée', 'value': True}, {'label': 'Désactivée', 'value': False}]

#-----------------------------------------------------------------------#
# Interface                                                             #
#-----------------------------------------------------------------------#

app.layout = html.Div([
    
    # Titre de l'application
    html.H1("Gapminder dataset : Checklist & Slider"),
    
    # Dropdown permettant de selectionner les continents
    html.H4("Sélection des continents :"),
    dcc.Checklist(id='checklist', options=opt_continent, value=opt_continent, inline=True),
    
    # Radio items permettant de passer l'axe des abscisses en logarithme
    html.H4("Transformation logarithmique du PIB par tête (gdpPercap) :"),
    dcc.RadioItems(id='radio', options=opt_log, value=True),

    # Affichage du graphique LifeExp by GDPperCap
    dcc.Graph(id='graph-gdp', figure={}),
    
    # Slider permettant de selectionner l'annee
    dcc.Slider(id='slider', min=min_year , max=max_year , value=max_year,
               marks=slider_marks, step = None)
               
])

#-----------------------------------------------------------------------#
# Serveur                                                               #
#-----------------------------------------------------------------------#

@callback(
    Output('graph-gdp', 'figure'),
    Input('slider', "value"),
    Input('checklist', "value"),
    Input('radio', 'value')
)
def update_graph(year_value, continent_value, log_boolean):
    df_update = df[(df.year == year_value) & df.continent.isin(continent_value)]
    fig = px.scatter(df_update, 
                     x="gdpPercap",
                     y="lifeExp", 
                     size="pop",
                     color="continent",
                     hover_name="country",
                     log_x=log_boolean,
                     size_max=60,
                     title=f'Life expectancy by GDP per capita and population in {year_value}')
    if log_boolean:
        fig.update_xaxes(type="log", range=[2,5])
    else :
        fig.update_xaxes(range=[-5000,50000])
    fig.update_yaxes(range=[20, 100])

    return fig

#-----------------------------------------------------------------------#
# Run                                                                   #
#-----------------------------------------------------------------------#

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")

])


#---------------------------------------------------------#
# 3.5 Input                                               #
#---------------------------------------------------------#

# Source Example
input_types = ("text", "number", "password", "email",
               "search", "tel", "url", "range", "hidden")

# Content Example
input_ex = html.Div([
    
    html.Div([
        dcc.Input(
            id="pg3-input_{}".format(x),
            type=x,
            placeholder="input type {}".format(x),
        )
        for x in input_types
    ]),
    html.Div(id="pg3-out-all-types")
    
])


# Content Code
input_code = html.Div([
    dmc.Prism(
        children=
"""from dash import Dash, dcc, html, Input, Output, callback

app = Dash(__name__)

input_types = ("text", "number", "password", "email",
               "search", "tel", "url", "range", "hidden")

app.layout = html.Div([
    
    html.Div([
        dcc.Input(
            id="input_{}".format(x),
            type=x,
            placeholder="input type {}".format(x),
        )
        for x in input_types
    ]),
    
    html.Div(id="out-all-types")   
    
])

@callback(
    Output("out-all-types", "children"),
    [Input("input_{}".format(x), "value") for x in input_types],
)
def cb_render(*vals):
    return " | ".join((str(val) for val in vals if val))

if __name__ == "__main__":
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")
    
])

# Source Exercice
pg3_txt = []
    
# Content Exercice
input_exo = html.Div([
    
    dbc.Accordion([
        dbc.AccordionItem(title="Objectif", children=[
            html.P([
                html.Span("Créer une application permettant de générer un texte", className="h")," sans passer par l’écriture dans un fichier extérieur à l’application.",html.Br(),
                "L'idée est d'utiliser un ",html.A("input",href="https://dash.plotly.com/dash-core-components/input", target="_blank", className="l")," de texte et d'incrémenter un objet qui contiendra la liste à puces des n éléments textuels ajoutés."
            ])
        ])
    ]),
    

    html.H3("Ecriture d'un texte :"),
    
    dcc.Input(id='pg3-input-text',type='text', debounce=True),
    
    html.P(id='pg3-txt',children='')

])


# Content Correction
input_cor = html.Div([
    
    dmc.Prism(
        children=
"""from dash import Dash, dcc, html, callback, Input, Output

app = Dash(__name__)

txt = []

app.layout = html.Div([
    
    html.H1("Ecriture d'un texte :"),
    
    dcc.Input(id='input-text',type='text', debounce=True),
    
    html.P(id='out',children='')
    
])

@callback(
    Output('out', 'children'),
    Input('input-text', 'value')
)
def create_txt(value):
    if value is not None:
        txt.append(html.Li(value))
        return txt

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")

])


#---------------------------------------------------------#
# 3.6 Download                                            #
#---------------------------------------------------------#


# Content Example
download_ex = html.Div([
    
    html.H3('Download example:'),
    
    html.Button(id='pg3-btn-download-txt', children='Download Text'),
    
    dcc.Download(id='pg3-download-text')
    
])


# Content Code
download_code = html.Div([
    dmc.Prism(
        children=
"""from dash import Dash, dcc, html, Input, Output, callback

app = Dash(__name__)

app.layout = html.Div([
    
    html.H1('Download example:'),
    
    html.Button(id='btn-download-txt', children='Download Text'),
    
    dcc.Download(id='download-text')
    
])

@callback(
    Output('download-text', 'data'),
    Input('btn-download-txt', 'n_clicks'),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dict(content='Hello world!', filename="hello.txt")

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")
    
])

# Source Exercice
dnl_exo_txt = []
dnl_exo_n = []
    
# Content Exercice
download_exo = html.Div([
    
    dbc.Accordion([
        dbc.AccordionItem(title="Objectif", children=[
            html.P([
                html.Span("En repartant de l’application créée lors de l’exercice de la section 3.5 Input", className="h"),", ajouter un bouton ",html.A("download",href="https://dash.plotly.com/dash-core-components/download", target="_blank", className="l")," permettant d’exporter dans un fichier .txt le texte qui est généré sur l’application.", html.Br(),
                html.Li(["Utiliser un bouton ",html.A("download",href="https://dash.plotly.com/dash-core-components/download", target="_blank", className="l")," pour déclencher le téléchargement du fichier texte"]),
                html.Li(["Ajouter un ",html.A("input",href="https://dash.plotly.com/dash-core-components/input", target="_blank", className="l")," texte pour permettre de saisir le nom du fichier texte"]),
                html.Li(["Le séparateur dans le fichier texte doit être un saut de ligne codifié par “/n”"]),
                "⚠ Lorsqu’on récupère le format du texte créé, on obtient une liste de dictionnaires où chaque dictionnaire correspond à un élément saisi.", html.Br(),
                "L’idée est donc dans un premier temps de voir quels sont les clés du dictionnaire à cibler pour récupérer le contenu des éléments textuels de chaque élément saisi."
            ])
        ])
    ]),
    
    
    # Title
    html.H3("Application permettant la création et l'exportation d'un fichier txt :"),
    
    # Download txt
    html.Button(id='pg3-btn-dnl-exo', children='Download Text'),
    dcc.Download(id='pg3-import-text-dnl-exo'),    
    dcc.Input(id='pg3-file-dnl-exo', type='text', debounce=True, value='Filename'),
    
    html.Br(),
    
    # Create txt
    html.H6("Saisie du texte:"),
    dcc.Input(id='pg3-input-text-dnl-exo', type='text', debounce=True),
    html.P(id='pg3-text-dnl-exo')

])


# Content Correction
download_cor = html.Div([
    
    dmc.Prism(
        children=
"""from dash import Dash, dcc, html, callback, Input, Output

#------------------------------------------------------------#
# 1. INITIALISATION                                          #
#------------------------------------------------------------#

app = Dash(__name__)

txt = []
n = []

#------------------------------------------------------------#
# 2. INTERFACE                                               #
#------------------------------------------------------------#

app.layout = html.Div([
    
    # Title
    html.H1("Application permettant la création et l'exportation d'un fichier txt :"),
    
    # Download txt
    html.Button(id='btn-download-txt', children='Download Text'),
    dcc.Download(id='download-text'),    
    dcc.Input(id='name-download-file', type='text', debounce=True, value='Filename'),
    
    html.Br(),
    
    # Create txt
    html.H4("Saisie du texte:"),
    dcc.Input(id='input-text', type='text', debounce=True),
    html.P(id='text',children='')
    
])

#------------------------------------------------------------#
# 3. CREATE TEXT                                             #
#------------------------------------------------------------#

@callback(
    Output('text', 'children'),
    Input('input-text', 'value')
)
def create_txt(value):
    if value is not None:
        txt.append(html.Li(value))
        return txt

#------------------------------------------------------------#
# 4. DOWNLOAD TEXT                                           #
#------------------------------------------------------------#

@callback(
    Output('download-text', 'data'),
    Input('btn-download-txt', 'n_clicks'),
    Input('text','children'),
    Input('name-download-file', 'value'),
)
def download_txt(n_clicks, text, filename):
    if n_clicks is not None:
        if n_clicks > len(n):
            if text is not None:
                txt = [x['props']['children'] for x in text]
                txt = '\\n'.join(txt)
                n.append(n_clicks)
                return dict(content=txt, filename=filename+".txt")

if __name__ == '__main__':
    app.run(debug=True)

""",
        language="python",
        colorScheme="dark")

])



#---------------------------------------------------------#
# 3.7 Upload                                              #
#---------------------------------------------------------#


# Content Example
upload_ex = html.Div([


    html.H3("Upload data csv example:"),
    
    dcc.Upload(id='pg3-upload-ex', children=html.Button('upload')),
    
    html.Div(id='pg3-out-ex')
    
])


# Content Code
upload_code = html.Div([
    dmc.Prism(
        children=
"""from dash import Dash, html, dcc, callback, Input, Output, State, dash_table
import base64
import datetime
import io
import pandas as pd

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Upload data csv example:"),
    dcc.Upload(id='upload', children=html.Button('upload')),    
    html.Div(id='out')
])

@callback(
    Output('out', 'children'),
    Input('upload', 'contents'),
    State('upload', 'filename'),
    State('upload', 'last_modified')
)
def update(c,n,d):
    if c is not None:
        content_type, content_string = c.split(',')              # Recuperation du contenu sans son type
        decoded = base64.b64decode(content_string)               # Decodage du contenu
        file = io.StringIO(decoded.decode('utf-8'))              # Recuperation du chemin et encodage UTF-8
        df = pd.read_csv(filepath_or_buffer=file, sep=';')       # Lecture du fichier csv avec séparateur ';'
        return html.Div([                                        # Preparation de la mise en page de la table
                    html.H5(n),
                    html.H6(datetime.datetime.fromtimestamp(d)),
                    dash_table.DataTable(
                        df.to_dict('records'),
                     [{'name': i, 'id': i} for i in df.columns]
                )])

if __name__ == '__main__':
    app.run(debug=True)

""",
        language="python",
        colorScheme="dark")
    
])

# Source Exercice
upl_exo_txt = []
upl_exo_n = []
    
# Content Exercice
upload_exo = html.Div([
    
    dbc.Accordion([
        dbc.AccordionItem(title="Objectif", children=[
            html.P([
                html.Span("En repartant de l’application créée lors de l’exercice de la section 3.6 Dowload", className="h"),", ajouter un bouton ",html.A("upload",href="https://dash.plotly.com/dash-core-components/upload", target="_blank", className="l")," permettant d’importer un fichier .txt qui aurait d’abord été téléchargé sur cette même application. L’idée globale de l’application est donc de pouvoir :", html.Br(),
                html.Ol([
                    html.Li(["Créer un texte ligne par ligne"]),
                    html.Li(["Exporter le texte créé via un bouton ",html.A("download",href="https://dash.plotly.com/dash-core-components/download", target="_blank", className="l"),""]),
                    html.Li(["Importer un texte qui a précédemment été créé et exporté depuis l’application via un bouton ",html.A("upload",href="https://dash.plotly.com/dash-core-components/upload", target="_blank", className="l")])
                ]),
                "⚠ Pour la réalisation de cet exercice on pourra :", html.Br(),
                html.Li(["Ajouter un callback qui prendra en input le contenu et le nom du fichier importé par le bouton ",html.A("upload",href="https://dash.plotly.com/dash-core-components/upload", target="_blank", className="l")," et qui alimentera la liste des éléments textuels"]),
                html.Li(["Pour l’importation du fichier texte, il faut s’inspirer de l’exemple de cette rubrique et le répliquer non plus sur un fichier csv mais cette fois sur un fichier txt"]),
                html.Li(["Les callbacks de création d’un texte et d’importation d’un texte doivent avoir le même output, donc il faudra ajouter une option pour accepter cette duplication dans la fonction Output() pour ces deux callbacks (allow_duplicate=True)"])
            ])
        ])
    ]),

    
    # Title
    html.H3("Création d'un fichier texte"),
    
    html.Hr(),

    # Download txt
    html.Button(id='pg3-btn-download-txt-upl-exo', children='Download Text'),
    dcc.Download(id='pg3-download-text-upl-exo'),    
    dcc.Input(id='pg3-name-download-file-upl-exo', type='text', debounce=True, value='Filename', style={'fontStyle': 'italic'}),
    
    html.Hr(),
    
    # Upload txt
    dcc.Upload(id='pg3-upload-text-upl-exo', children=html.Button('upload'), contents=None),
    html.P(id='pg3-p-upl-exo',children=''),    
    html.Hr(),
    
    # Create txt
    html.H6("Saisie du texte:"),
    dcc.Input(id='pg3-input-text-upl-exo', type='text', debounce=True),
    html.P(id='pg3-text-upl-exo',children='')    
    

])


# Content Correction
upload_cor = html.Div([
    
    dmc.Prism(
        children=
"""from dash import Dash, dcc, html, callback, Input, Output, State
import base64
import io
import pandas as pd

#------------------------------------------------------------#
# 1. INITIALISATION                                          #
#------------------------------------------------------------#

app = Dash(__name__)

txt = []
n = []

#------------------------------------------------------------#
# 2. INTERFACE                                               #
#------------------------------------------------------------#

app.layout = html.Div([
    
    # Title
    html.H1("Création d'un fichier texte"),
    
    html.Hr(),

    # Download txt
    html.Button(id='btn-download-txt', children='Download Text'),
    dcc.Download(id='download-text'),    
    dcc.Input(id='name-download-file', type='text', debounce=True, value='Filename', style={'fontStyle': 'italic'}),
    
    html.Hr(),
    
    # Upload txt
    dcc.Upload(id='upload-text', children=html.Button('upload'), contents=None),
    html.P(id='p',children=''),    
    html.Hr(),
    
    # Create txt
    html.H4("Saisie du texte:"),
    dcc.Input(id='input-text', type='text', debounce=True),
    html.P(id='text',children='')
    
])

#------------------------------------------------------------#
# 3. CREATE TEXT                                             #
#------------------------------------------------------------#

@callback(
    Output('text', 'children', allow_duplicate=True),
    Input('input-text', 'value'),
    prevent_initial_call='initial_duplicate'
)
def create_txt(value):
    if value is not None:
        txt.append(html.Li(value))
        return txt

#------------------------------------------------------------#
# 4. DOWNLOAD TEXT                                           #
#------------------------------------------------------------#

@callback(
    Output('download-text', 'data'),
    Input('btn-download-txt', 'n_clicks'),
    Input('text','children'),
    Input('name-download-file', 'value'),
)
def download_txt(n_clicks, text, filename):
    if n_clicks is not None:
        if n_clicks > len(n):
            if text is not None:
                txt = [x['props']['children'] for x in text]
                txt = '\\n'.join(txt)
                n.append(n_clicks)
                return dict(content=txt, filename=filename+".txt")

#------------------------------------------------------------#
# 5. UPLOAD TEXT                                             #
#------------------------------------------------------------#

@callback(
    Output('text', 'children', allow_duplicate=True),
    Input('upload-text', 'contents'),
    State('upload-text', 'filename'),
    prevent_initial_call='initial_duplicate'
)
def upload_txt(c,n):
    if c is not None:
        content_type, content_string = c.split(',')              # Recuperation du contenu sans son type
        decoded = base64.b64decode(content_string)               # Decodage du contenu
        file = io.StringIO(decoded.decode('utf-8'))
        df = pd.read_table(filepath_or_buffer=file, header=None)
        for ligne in df[0]:
            txt.append(html.Li(ligne))
        return txt


if __name__ == '__main__':
    app.run(debug=True)

""",
        language="python",
        colorScheme="dark")

])




    



#-----------------------------------------------------------------------#
# Interface                                                             #
#-----------------------------------------------------------------------#


layout = html.Div([    
    
    html.H1("3. Callbacks"),
    
    html.H2("3.1 Dropdown"),
    
    dcc.Input(type="password", debounce=True, placeholder="Pwd to get correction", id="pg3-input-pwd-dropdown-cor", className="pwd"),
    
    dbc.Tabs([
            dbc.Tab(label="Exemple"   , tab_id="dropdown-ex"  , children=dropdown_ex  , className="tab"),
            dbc.Tab(label="Code"      , tab_id="dropdown-code", children=dropdown_code, className="tab"),
            dbc.Tab(label="Exercice"  , tab_id="dropdown-exo" , children=dropdown_exo , className="tab"),
            dbc.Tab(label="Correction", tab_id="dropdown-cor" , children=dropdown_cor , className="tab", id="pg3-pwd-dropdown-cor", disabled=True)

        ],
        id="dropdown",
        active_tab="dropdown-ex"
    ),
    
    
    html.H2("3.2 Slider"),
    
    dcc.Input(type="password", debounce=True, placeholder="Pwd to get correction 1", id="pg3-input-pwd-slider-cor", className="pwd"),
    
    dcc.Input(type="password", debounce=True, placeholder="Pwd to get correction 2", id="pg3-input-pwd-slider-cor2", className="pwd"),
    
    dbc.Tabs([
            dbc.Tab(label="Exemple"     , tab_id="slider-ex"   , children=slider_ex   , className="tab"),
            dbc.Tab(label="Code"        , tab_id="slider-code" , children=slider_code , className="tab"),
            dbc.Tab(label="Exercice"    , tab_id="slider-exo"  , children=slider_exo  , className="tab"),
            dbc.Tab(label="Correction"  , tab_id="slider-cor"  , children=slider_cor  , className="tab", id="pg3-pwd-slider-cor", disabled=True),
            dbc.Tab(label="Exercice 2"  , tab_id="slider-exo2" , children=slider_exo2 , className="tab"),
            dbc.Tab(label="Correction 2", tab_id="slider-cor2" , children=slider_cor2 , className="tab", id="pg3-pwd-slider-cor2", disabled=True)
        ],
        id="slider",
        active_tab="slider-ex"
    ),
    
    
    html.H2("3.3 Checklist"),
    
    dcc.Input(type="password", debounce=True, placeholder="Pwd to get correction", id="pg3-input-pwd-checklist-cor", className="pwd"),
        
    dbc.Tabs([
            dbc.Tab(label="Exemple"     , tab_id="checklist-ex"   , children=checklist_ex   , className="tab"),
            dbc.Tab(label="Code"        , tab_id="checklist-code" , children=checklist_code , className="tab"),
            dbc.Tab(label="Exercice"    , tab_id="checklist-exo"  , children=checklist_exo  , className="tab"),
            dbc.Tab(label="Correction"  , tab_id="checklist-cor"  , children=checklist_cor  , className="tab", id="pg3-pwd-checklist-cor", disabled=True)
        ],
        id="checklist",
        active_tab="checklist-ex"
    ),


    html.H2("3.4 Radio Items"),
    
    dcc.Input(type="password", debounce=True, placeholder="Pwd to get correction", id="pg3-input-pwd-radio-cor", className="pwd"),
    
    dbc.Tabs([
            dbc.Tab(label="Exemple"     , tab_id="radio-ex"   , children=radio_ex   , className="tab"),
            dbc.Tab(label="Code"        , tab_id="radio-code" , children=radio_code , className="tab"),
            dbc.Tab(label="Exercice"    , tab_id="radio-exo"  , children=radio_exo  , className="tab"),
            dbc.Tab(label="Correction"  , tab_id="radio-cor"  , children=radio_cor  , className="tab", id="pg3-pwd-radio-cor", disabled=True)
        ],
        id="radio",
        active_tab="radio-ex"
    ),
    
    
    html.H2("3.5 Input"),
    
    dcc.Input(type="password", debounce=True, placeholder="Pwd to get correction", id="pg3-input-pwd-input-cor", className="pwd"),
    
    dbc.Tabs([
            dbc.Tab(label="Exemple"     , tab_id="input-ex"   , children=input_ex   , className="tab"),
            dbc.Tab(label="Code"        , tab_id="input-code" , children=input_code , className="tab"),
            dbc.Tab(label="Exercice"    , tab_id="input-exo"  , children=input_exo  , className="tab"),
            dbc.Tab(label="Correction"  , tab_id="input-cor"  , children=input_cor  , className="tab", id="pg3-pwd-input-cor", disabled=True)
        ],
        id="input",
        active_tab="input-ex"
    ),
    
    
    html.H2("3.6 Download"),
    
    dcc.Input(type="password", debounce=True, placeholder="Pwd to get correction", id="pg3-input-pwd-download-cor", className="pwd"),
    
    dbc.Tabs([
            dbc.Tab(label="Exemple"     , tab_id="download-ex"   , children=download_ex   , className="tab"),
            dbc.Tab(label="Code"        , tab_id="download-code" , children=download_code , className="tab"),
            dbc.Tab(label="Exercice"    , tab_id="download-exo"  , children=download_exo  , className="tab"),
            dbc.Tab(label="Correction"  , tab_id="download-cor"  , children=download_cor  , className="tab", id="pg3-pwd-download-cor", disabled=True)
        ],
        id="download",
        active_tab="download-ex"
    ),
    
    
    html.H2("3.7 Upload"),
    
    dcc.Input(type="password", debounce=True, placeholder="Pwd to get correction", id="pg3-input-pwd-upload-cor", className="pwd"),
    
    dbc.Tabs([
            dbc.Tab(label="Exemple"     , tab_id="upload-ex"   , children=upload_ex   , className="tab"),
            dbc.Tab(label="Code"        , tab_id="upload-code" , children=upload_code , className="tab"),
            dbc.Tab(label="Exercice"    , tab_id="upload-exo"  , children=upload_exo  , className="tab"),
            dbc.Tab(label="Correction"  , tab_id="upload-cor"  , children=upload_cor  , className="tab", id="pg3-pwd-upload-cor", disabled=True)
        ],
        id="upload",
        active_tab="upload-ex"
    ),
    
])

#-----------------------------------------------------------------------#
# Serveur                                                               #
#-----------------------------------------------------------------------#


#---------------------------------------------------------#
# 3.1 Dropdown                                            #
#---------------------------------------------------------#


# Serveur de l'application permettant la mise a jour dynamique
@callback(
    Output(component_id='pg3-scatter', component_property='figure'),
    Input(component_id='pg3-x', component_property='value'),
    Input(component_id='pg3-y', component_property='value'),
)
def update_graph(x, y):
    fig = px.scatter(iris, x=x, y=y, color="species",
                     labels={
                         x:x.replace('_',' ').capitalize(),
                         y:y.replace('_',' ').capitalize(),
                        },
                     title="Scatter Plot of the Iris Dataset")
    return fig

@callback(
    Output("pg3-pwd-dropdown-cor", "disabled"),
    Input("pg3-input-pwd-dropdown-cor","value")
)
def password(pwd):
    if pwd==mdp['exo_31']:
        return(False)
    else:
        return(True)


#---------------------------------------------------------#
# 3.2 Slider                                              #
#---------------------------------------------------------#


@callback(
    Output(component_id='pg3-graph-gdp', component_property='figure'),
    Input(component_id='pg3-range-slider', component_property="value"),
)
def update_graph(value):
    df_update = gp[(gp['pop'] >= value[0]) & (gp['pop'] <= value[1])]    
    fig = px.scatter(df_update.query("year==2007"), 
                     x="gdpPercap",
                     y="lifeExp", 
                     size="pop",
                     color="continent",
                     hover_name="country",
                     size_max=60,
                     title='Life expectancy by GDP per capita and population in 2007')
    return fig

@callback(
    Output(component_id='pg3-scatter-gdp', component_property='figure'),
    Input(component_id='pg3-year', component_property="value"),
    Input(component_id='pg3-continent', component_property="value")
)
def update_graph(year_value, continent_value):
    df_update = gp[(gp.year == year_value) & gp.continent.isin(continent_value)] 
    fig = px.scatter(df_update, 
                     x="gdpPercap",
                     y="lifeExp", 
                     size="pop",
                     color="continent",
                     hover_name="country",
                     size_max=60,
                     title=f'Life expectancy by GDP per capita and population in {year_value}')
    return fig

@callback(
    Output("pg3-pwd-slider-cor", "disabled"),
    Input("pg3-input-pwd-slider-cor","value")
)
def password(pwd):
    if pwd==mdp['exo_321']:
        return(False)
    else:
        return(True)

@callback(
    Output("pg3-pwd-slider-cor2", "disabled"),
    Input("pg3-input-pwd-slider-cor2","value")
)
def password(pwd):
    if pwd==mdp['exo_322']:
        return(False)
    else:
        return(True)


#---------------------------------------------------------#
# 3.3 Checklist                                           #
#---------------------------------------------------------#

# Exemple
@callback(
    Output('pg3-state-out', 'children'),
    Input('pg3-checklist', 'value')
)
def update_state(values):
    return [html.Li(val) for val in values]

# Exercice
@callback(
    Output(component_id='pg3-graph-exo-checklist', component_property='figure'),
    Input(component_id='pg3-slider-exo-checklist', component_property="value"),
    Input(component_id='pg3-list-continent', component_property="value")
)
def update_graph(year_value, continent_value):
    df_update = gp[(gp.year == year_value) & gp.continent.isin(continent_value)]
    fig = px.scatter(df_update, 
                     x="gdpPercap",
                     y="lifeExp", 
                     size="pop",
                     color="continent",
                     hover_name="country",
                     size_max=60,
                     title=f'Life expectancy by GDP per capita and population in {year_value}')
    fig.update_xaxes(range=[-5000,50000])
    fig.update_yaxes(range=[0, 100])
    return fig

@callback(
    Output("pg3-pwd-checklist-cor", "disabled"),
    Input("pg3-input-pwd-checklist-cor","value")
)
def password(pwd):
    if pwd==mdp['exo_33']:
        return(False)
    else:
        return(True)

#---------------------------------------------------------#
# 3.4 Radio-items                                         #
#---------------------------------------------------------#

# Example
@callback(
    Output('pg3-radio-ex-out','children'),
    Input('pg3-radio-ex','value')
)
def update(value):
    if value is None:
        txt = "Aucun choix n'a encore été sélectionné."
    else:
        txt = f"Le choix numéro {value} a été sélectionné !"
    return(txt)

# Exercice
@callback(
    Output('pg3-graph-exo-radio', 'figure'),
    Input('pg3-slider-exo-radio', "value"),
    Input('pg3-checklist-exo-radio', "value"),
    Input('pg3-radio-log', 'value')
)
def update_graph(year_value, continent_value, log_boolean):
    df_update = gp[(gp.year == year_value) & gp.continent.isin(continent_value)]
    fig = px.scatter(df_update, 
                     x="gdpPercap",
                     y="lifeExp", 
                     size="pop",
                     color="continent",
                     hover_name="country",
                     log_x=log_boolean,
                     size_max=60,
                     title=f'Life expectancy by GDP per capita and population in {year_value}')
    if log_boolean:
        fig.update_xaxes(type="log", range=[2,5])
    else :
        fig.update_xaxes(range=[-5000,50000])
    fig.update_yaxes(range=[20, 100])

    return fig

@callback(
    Output("pg3-pwd-radio-cor", "disabled"),
    Input("pg3-input-pwd-radio-cor","value")
)
def password(pwd):
    if pwd==mdp['exo_34']:
        return(False)
    else:
        return(True)

#---------------------------------------------------------#
# 3.5 Input                                               #
#---------------------------------------------------------#


# Example
@callback(
    Output("pg3-out-all-types", "children"),
    [Input("pg3-input_{}".format(x), "value") for x in input_types],
)
def cb_render(*vals):
    return " | ".join((str(val) for val in vals if val))


# Exercice
@callback(
    Output('pg3-txt', 'children'),
    Input('pg3-input-text', 'value')
)
def create_txt(value):
    if value is not None:
        pg3_txt.append(html.Li(value))
        return pg3_txt
    
@callback(
    Output("pg3-pwd-input-cor", "disabled"),
    Input("pg3-input-pwd-input-cor","value")
)
def password(pwd):
    if pwd==mdp['exo_35']:
        return(False)
    else:
        return(True)

#---------------------------------------------------------#
# 3.6 Download                                            #
#---------------------------------------------------------#


# Example
@callback(
    Output('pg3-download-text', 'data'),
    Input('pg3-btn-download-txt', 'n_clicks'),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dict(content='Hello world!', filename="hello.txt")


# Exercie 

# CREATE TEXT
@callback(
    Output('pg3-text-dnl-exo', 'children'),
    Input('pg3-input-text-dnl-exo', 'value')
)
def create_txt(value):
    if value is not None:
        dnl_exo_txt.append(html.Li(value))
        return dnl_exo_txt
    
# DOWNLOAD TEXT
@callback(
    Output('pg3-import-text-dnl-exo', 'data'),
    Input('pg3-btn-dnl-exo', 'n_clicks'),
    Input('pg3-text-dnl-exo','children'),
    Input('pg3-file-dnl-exo', 'value'),
)
def download_txt(n_clicks, text, filename):
    if n_clicks is not None:
        if n_clicks > len(dnl_exo_n):
            if text is not None:
                dnl_exo_txt = [x['props']['children'] for x in text]
                dnl_exo_txt = '\n'.join(dnl_exo_txt)
                dnl_exo_n.append(n_clicks)
                return dict(content=dnl_exo_txt, filename=filename+".txt")

@callback(
    Output("pg3-pwd-download-cor", "disabled"),
    Input("pg3-input-pwd-download-cor","value")
)
def password(pwd):
    if pwd==mdp['exo_36']:
        return(False)
    else:
        return(True)            
          
#---------------------------------------------------------#
# 3.7 Upload                                              #
#---------------------------------------------------------#

  
# Example
@callback(
    Output('pg3-out-ex', 'children'),
    Input('pg3-upload-ex', 'contents'),
    State('pg3-upload-ex', 'filename'),
    State('pg3-upload-ex', 'last_modified')
)
def update(c,n,d):
    if c is not None:
        content_type, content_string = c.split(',')              # Recuperation du contenu sans son type
        decoded = base64.b64decode(content_string)               # Decodage du contenu
        file = io.StringIO(decoded.decode('utf-8'))              # Recuperation du chemin et encodage UTF-8
        df_upload_file = pd.read_csv(filepath_or_buffer=file, sep=';')       # Lecture du fichier csv avec séparateur ';'
        return html.Div([                                        # Preparation de la mise en page de la table
                    html.H5(n),
                    html.H6(datetime.datetime.fromtimestamp(d)),
                    dash_table.DataTable(
                        df_upload_file.to_dict('records'),
                     [{'name': i, 'id': i} for i in df_upload_file.columns]
                )])
        
        
        
# Exercice
# CREATE TEXT
@callback(
    Output('pg3-text-upl-exo', 'children', allow_duplicate=True),
    Input('pg3-input-text-upl-exo', 'value'),
    prevent_initial_call='initial_duplicate'
)
def create_txt(value):
    if value is not None:
        upl_exo_txt.append(html.Li(value))
        return upl_exo_txt

# DOWNLOAD TEXT
@callback(
    Output('pg3-download-text-upl-exo', 'data'),
    Input('pg3-btn-download-txt-upl-exo', 'n_clicks'),
    Input('pg3-text-upl-exo','children'),
    Input('pg3-name-download-file-upl-exo', 'value'),
)
def download_txt(n_clicks, text, filename):
    if n_clicks is not None:
        if n_clicks > len(upl_exo_n):
            if text is not None:
                txt = [x['props']['children'] for x in text]
                txt = '\n'.join(txt)
                upl_exo_n.append(n_clicks)
                return dict(content=txt, filename=filename+".txt")


# UPLOAD TEXT
@callback(
    Output('pg3-text-upl-exo', 'children', allow_duplicate=True),
    Input('pg3-upload-text-upl-exo', 'contents'),
    State('pg3-upload-text-upl-exo', 'filename'),
    prevent_initial_call='initial_duplicate'
)
def upload_txt(c,n):
    if c is not None:
        content_type, content_string = c.split(',')              # Recuperation du contenu sans son type
        decoded = base64.b64decode(content_string)               # Decodage du contenu
        file = io.StringIO(decoded.decode('utf-8'))
        df_upl_exo = pd.read_table(filepath_or_buffer=file, header=None)
        for ligne in df_upl_exo[0]:
            upl_exo_txt.append(html.Li(ligne))
        return upl_exo_txt


@callback(
    Output("pg3-pwd-upload-cor", "disabled"),
    Input("pg3-input-pwd-upload-cor","value")
)
def password(pwd):
    if pwd==mdp['exo_37']:
        return(False)
    else:
        return(True)