from dash import Dash, html, dcc, callback, Input, Output, register_page, dash_table
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import plotly.express as px
import pandas as pd 


register_page(__name__,
    name='2. Premiers Pas'
)


#-----------------------------------------------------------------------#
# Sources                                                               #
#-----------------------------------------------------------------------#


#---------------------------------------------------------#
# 2.1 Begin                                               #
#---------------------------------------------------------#

# Content example
begin_ex = html.Div(html.H3('My first app with Dash'))

# Content code
begin_code = html.Div([
    dmc.Prism(
        children=
"""from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.H1('My first app with Dash')
])

app.run(debug=True)""",
        language="python",
        colorScheme="dark")
    
])


#---------------------------------------------------------#
# 2.2 Graph                                               #
#---------------------------------------------------------#

# Source Exemple
iris = px.data.iris()

fig_graph_ex = px.scatter(iris, x="sepal_width", y="petal_length", color="species")

# Content Exemple
graph_ex = html.Div([
    
    html.H3(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(id='pg2-scatter', figure=fig_graph_ex)
    
])

# Content Code
graph_code = html.Div([
    
    dmc.Prism(
        children=
"""from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="petal_length", color="species")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(id='graph', figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")

])

# Source Exercice
lab = {"species_id"   : "Species"       ,
       "sepal_width"  : "Sepal Width"   ,
       "sepal_length" : "Sepal Length"  ,
       "petal_width"  : "Petal Width"   , 
       "petal_length" : "Petal Length"  }

fig_graph_exo = px.parallel_coordinates(iris, color="species_id", labels=lab,
                    color_continuous_scale=px.colors.diverging.Tropic, 
                    color_continuous_midpoint=2)

# Content Exercice
graph_exo = html.Div([
    
    html.P([
        "Répliquez la capture d’écran ci-dessous à l’aide du dataset iris disponible dans le package plotly.express. N’hésitez pas à aller faire un tour dans la documentation de plotly.express pour vous aider à réaliser ce graphique : https://plotly.com/python/plotly-express/"
    ]),
    
    html.H3('Iris dataset : Parrallel coordinates'),
    dcc.Graph(id='pg2-parallel', figure=fig_graph_exo)
    
])

# Content Correction
graph_cor = html.Div([
    
    dmc.Prism(
        children=
"""from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

df = px.data.iris()

lab = {"species_id"   : "Species"       ,
       "sepal_width"  : "Sepal Width"   ,
       "sepal_length" : "Sepal Length"  ,
       "petal_width"  : "Petal Width"   , 
       "petal_length" : "Petal Length"  }

fig = px.parallel_coordinates(df, color="species_id", labels=lab,
                    color_continuous_scale=px.colors.diverging.Tropic, 
                    color_continuous_midpoint=2)

app.layout = html.Div([
    
    html.H1('Iris dataset : Parrallel coordinates'),
    dcc.Graph(id='parallel-coord', figure=fig)

])

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")

])


#---------------------------------------------------------#
# 2.3 DataTable                                           #
#---------------------------------------------------------#

# Source Exemple
df = pd.DataFrame(iris)

# Content Exemple
dt_ex = html.Div([
     
    html.H3("Iris Dataset"),
    
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df.columns],
        style_table={"borderStyle": "groove"},
        page_size=10
)

    
])

# Content Code
dt_code = html.Div([
    dmc.Prism(
        children=
"""from dash import Dash, html, dash_table
import plotly.express as px
import pandas as pd

df = pd.DataFrame(px.data.iris())

app = Dash(__name__)

app.layout = html.Div([
    
    html.H1("Iris Dataset"),
    
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df.columns],
        style_table={"borderStyle": "groove"},
        page_size=10
)
    
])

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")
    
])


#---------------------------------------------------------#
# 2.4 Composantes html                                    #
#---------------------------------------------------------#


# Content Exemple
html_ex = html.Div([
     
    html.Header("Header"),
    
    html.H3("Titre Niveau 1"),
    
    html.H4("Titre Niveau 2"),
            
    html.H5("Titre Niveau 3"),
    
    html.Br(),

    html.P("Paragraphe 1"),    
    
    html.Hr(),
    
    html.P("Paragraphe 2"),  
    
    html.Hr(),
        
    html.P("Paragraphe 3")

    
])

# Content Code
html_code = html.Div([
    dmc.Prism(
        children=
"""from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([

    html.Header("Header"),
    
    html.H1("Titre Niveau 1"),
    
    html.H2("Titre Niveau 2"),
            
    html.H3("Titre Niveau 3"),
    
    html.Br(),

    html.P("Paragraphe 1"),    
    
    html.Hr(),
    
    html.P("Paragraphe 2"),  
    
    html.Hr(),
        
    html.P("Paragraphe 3")

])

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")
    
])


#---------------------------------------------------------#
# 2.5 Activation CSS                                      #
#---------------------------------------------------------#


# Content Exemple
css_ex = html.Div([
     
    html.Header("Header", style={'borderStyle':'dotted'}),
    
    html.H3("Titre Niveau 1", style={'color':'blue'}),
    
    html.H4("Titre Niveau 2", style={'backgroundColor':'orange'}),
            
    html.H5("Titre Niveau 3", style={'textDecoration' : 'green wavy underline'}),
    
    html.Br(),

    html.P("Paragraphe 1", style={'textAlign': 'center'}),    
    
    html.Hr(),
    
    html.P("Paragraphe 2", style={'textAlign': 'end'}),  
    
    html.Hr(),
        
    html.P("Paragraphe 3", style={'marginLeft':'100px'})
    
])

# Content Code
css_code = html.Div([
    dmc.Prism(
        children=
"""from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([

    html.Header("Header", style={'borderStyle':'dotted'}),
    
    html.H1("Titre Niveau 1", style={'color':'blue'}),
    
    html.H2("Titre Niveau 2", style={'backgroundColor':'orange'}),
            
    html.H3("Titre Niveau 3", style={'textDecoration' : 'green wavy underline'}),
    
    html.Br(),

    html.P("Paragraphe 1", style={'textAlign': 'center'}),    
    
    html.Hr(),
    
    html.P("Paragraphe 2", style={'textAlign': 'end'}),  
    
    html.Hr(),
        
    html.P("Paragraphe 3", style={'marginLeft':'100px'})

])

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")
    
])

  
#---------------------------------------------------------#
# 2.6 Callback                                            #
#---------------------------------------------------------#


# Content Presentation
callback_pres = html.Div([
    
    html.P("Une application dash est composée de deux éléments :"),
    
    html.Ol([
        html.Li("Interface : Partie permettant la mise en forme de l’application"),
        html.Li("Serveur : Partie permettant de rendre l’application dynamique")
    ]),
    
    html.P("L’interface et le serveur sont en inter-dépendance :"),
    
    html.Ul([
        html.Li("Activation d’une composante de l’interface comme un radio button"),
        html.Li("Déclenchement du callback, récupération du nouvel état du radio button et mise à jour d’un objet via une fonction"),
        html.Li("Envoi du nouvel état de l’objet dans l’interface")
    ]),
    
    html.P("L’input d’un callback prend en paramètre :"),
    
    html.Ol([
        html.Li("component_id : L’id de l’objet en input (dash core component)"),
        html.Li("component_property : La propriété cible de l’objet en input. S’il n’y a pas de propriété cible, alors la valeur par défaut est children")
    ]),
 
    html.P("L’output d’un callback prend en paramètre :"),
    
    html.Ol([
        html.Li("component_id : L’id de l’objet cible à mettre à jour dans l’application"),
        html.Li("component_property : La propriété à mettre à jour dans l’objet cible de l’application. S’il n’y a pas de propriété cible, alors la valeur par défaut est children")
    ]),

    
])


# Source Exemple
choix_possibles = ['Choix 1','Choix 2', 'Choix 3']
etat_initial = choix_possibles[0]

# Content Exemple
callback_ex = html.Div([
         
    # Titre de l'application
    html.H3("My firt callback with dash"),
    
    # Objet permettant de selectionner un input
    dcc.Dropdown(id='pg2-nom-objet-input',
                 options=choix_possibles,
                 value=etat_initial),

    # Objet qui se met a jour suivant l'etat de l'input
    html.Div(id='pg2-nom-objet-output')
    
])


# Content Code
callback_code = html.Div([
    dmc.Prism(
        children=
"""from dash import Dash, html, callback, Input, Output, dcc

# Initialisation de l'application
app = Dash(__name__)

# Initialisation des variables
choix_possibles = ['Choix 1','Choix 2', 'Choix 3']
etat_initial = choix_possibles[0]

# Creation de l'interface de l'application
app.layout = html.Div([
    
    # Titre de l'application
    html.H1("My firt callback with dash"),
    
    # Objet permettant de selectionner un input
    dcc.Dropdown(id='nom-objet-input',
                 options=choix_possibles,
                 value=etat_initial),

    # Objet qui se met a jour suivant l'etat de l'input
    html.Div(id='nom-objet-output')
])

# Serveur de l'application permettant la mise a jour dynamique
@callback(
    Output(component_id='nom-objet-output', component_property='children'),
    Input(component_id='nom-objet-input' , component_property='value')
)
def update_objet_en_sortie(value):
    return f"Nouvel état de l'objet en sortie: {value}"

# Code permettant de run l'application
if __name__ == "__main__":
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")
    
])
 
 
 
 
 
 




#-----------------------------------------------------------------------#
# Interface                                                             #
#-----------------------------------------------------------------------#


layout = html.Div([    
    
    html.H1("2. Premiers Pas"),
    
    html.H2("2.1 Begin"),
    
    dbc.Tabs([
            dbc.Tab(label="Exemple" , tab_id="begin-ex"  , children=begin_ex  , className="tab"),
            dbc.Tab(label="Code"    , tab_id="begin-code", children=begin_code, className="tab")
        ],
        id="begin",
        active_tab="begin-ex"
    ),


    html.H2("2.2 Graph"),
    
    dbc.Tabs([
            dbc.Tab(label="Exemple"   , tab_id="graph-ex"  , children=graph_ex  , className="tab"),
            dbc.Tab(label="Code"      , tab_id="graph-code", children=graph_code, className="tab"),
            dbc.Tab(label="Exercice"  , tab_id="graph-exo" , children=graph_exo , className="tab"),
            dbc.Tab(label="Correction", tab_id="graph-cor" , children=graph_cor , className="tab")
        ],
        id="graph",
        active_tab="graph-ex"
    ),


    html.H2("2.3 DataTable"),
    
    dbc.Tabs([
            dbc.Tab(label="Exemple"   , tab_id="dt-ex"  , children=dt_ex  , className="tab"),
            dbc.Tab(label="Code"      , tab_id="dt-code", children=dt_code, className="tab")
        ],
        id="dt",
        active_tab="dt-ex"
    ),
    

    html.H2("2.4 Composantes HTML"),
    
    dbc.Tabs([
            dbc.Tab(label="Exemple"   , tab_id="html-ex"  , children=html_ex  , className="tab"),
            dbc.Tab(label="Code"      , tab_id="html-code", children=html_code, className="tab")
        ],
        id="html",
        active_tab="html-ex"
    ),
    

    html.H2("2.5 Activation CSS"),
    
    dbc.Tabs([
            dbc.Tab(label="Exemple"   , tab_id="css-ex"  , children=css_ex  , className="tab"),
            dbc.Tab(label="Code"      , tab_id="css-code", children=css_code, className="tab")
        ],
        id="css",
        active_tab="css-ex"
    ),
    
    
    html.H2("2.6 Callback"),
    
    dbc.Tabs([
            dbc.Tab(label="Présentation", tab_id="callback-pres", children=callback_pres, className="tab"),
            dbc.Tab(label="Exemple"     , tab_id="callback-ex"  , children=callback_ex  , className="tab"),
            dbc.Tab(label="Code"        , tab_id="callback-code", children=callback_code, className="tab")
        ],
        id="callback",
        active_tab="callback-pres",
    )
    
])

#-----------------------------------------------------------------------#
# Serveur                                                               #
#-----------------------------------------------------------------------#


#---------------------------------------------------------#
# 2.6 Callback                                            #
#---------------------------------------------------------#


# Serveur de l'application permettant la mise a jour dynamique
@callback(
    Output(component_id='pg2-nom-objet-output', component_property='children'),
    Input(component_id='pg2-nom-objet-input' , component_property='value')
)
def update_objet_en_sortie(value):
    return f"Nouvel état de l'objet en sortie: {value}"