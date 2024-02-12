from dash import Dash, html, dcc, callback, Input, Output, register_page, dash_table
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import plotly.express as px
import pandas as pd 


register_page(__name__,
    name='4. Layout'
)


#-----------------------------------------------------------------------#
# Sources                                                               #
#-----------------------------------------------------------------------#


#---------------------------------------------------------#
# 4.1 Segmentation                                        #
#---------------------------------------------------------#


# Content Example
segmentation_ex = html.Div([
    
    html.Header([
        html.H3('Segmentation de ma page Web :')
        ]),
    
    dbc.Row([
        dbc.Col(html.Div("Zone A"), align="start" , style={'backgroundColor':'green'}),
        dbc.Col(html.Div("Zone B"), align="center", style={'backgroundColor':'red'}),
        dbc.Col(html.Div("Zone C"), align="end"   , style={'backgroundColor':'pink'}),
        ], style={'height': '120px', 'borderStyle': 'dotted'}),
    

    
    dbc.Row([
                dbc.Col(html.Div("Zone D"), align="start" , style={'backgroundColor':'blue', 'height': '100%'}, width=2),
                dbc.Col(html.Center("Zone E"), align="center", style={'backgroundColor':'yellow', 'height': '50%'}, width=9),
                dbc.Col(html.Div("Zone F"), align="end"   , style={'backgroundColor':'orange'}, width=1),
            ], style={'height': '200px', 'borderStyle': 'double'})
    
])

# Content Code
segmentation_code = html.Div([
    
    dmc.Prism(
        children=
"""from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    
    html.Header([
        html.H1('Segmentation de ma page Web :')
        ]),
    
    dbc.Row([
        dbc.Col(html.Div("Zone A"), align="start" , style={'backgroundColor':'green'}),
        dbc.Col(html.Div("Zone B"), align="center", style={'backgroundColor':'red'}),
        dbc.Col(html.Div("Zone C"), align="end"   , style={'backgroundColor':'pink'}),
        ], style={'height': '120px', 'borderStyle': 'dotted'}),
    
    dbc.Row([
                dbc.Col(html.Div("Zone D"), align="start" , style={'backgroundColor':'blue', 'height': '100%'}, width=2),
                dbc.Col(html.Center("Zone E"), align="center", style={'backgroundColor':'yellow', 'height': '50%'}, width=9),
                dbc.Col(html.Div("Zone F"), align="end"   , style={'backgroundColor':'orange'}, width=1),
            ], style={'height': '200px', 'borderStyle': 'double'})
    
])

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")

])


# Source Exercice

# Recuperation du dataset Gapminder
gp = px.data.gapminder()

# Recuperation du minimum et du maximum des annees disponibles
min_year, max_year = gp.year.min(), gp.year.max()

# Creation des markers pour le slider sur les annees
marks_years = {str(year): str(year) for year in gp.year.unique()}

# Recuperation de la liste des continents 
opt_continent = gp.continent.unique()

# Creation des options du radio items pour l'activation du logarithme sur l'axe des x
opt_log = [{'label': 'Activée', 'value': True}, {'label': 'Désactivée', 'value': False}]



# Content Exercice
segmentation_exo = html.Div([
    
    html.Div([
        
        html.P(["Objectif : En repartant de l’application créée lors de l’exercice de la section 3.4 RadioItems, placer les trois callbacks suivants dans une colonne à droite de la colonne du graphique :"]),

        html.Ol([
            html.Li(["La checklist contenant la sélection des continents"]),
            html.Li(["Le radio-items permettant le transformation du PIB par tête en logarithme"]),
            html.Li(["Le slider permettant de sélectionne l’année"])
        ]),


        html.P(["⚠ Remarque : Pour la réalisation de cet exercice on pourra :"]),
        
        html.Ul([
            html.Li(["Placer le titre de l’application dans un header"]),
            html.Li(["Créer une ligne et y insérer une colonne pour le graphique de largeur 7 et une colonne pour les composantes de sélection de largeur 4"]),
            html.Li(["Dans la colonne des composantes de sélection, création de deux lignes. La première ligne contient 2 colonnes d’une largeur égale contenant respectivement la checklist du choix des continents et le radio item de la transformation du PIB par tête en logarithme. La seconde ligne contient la sélection de l’année"]),
            html.Li(["Le titre de chaque composante de sélection est de type H6"])
        ])
    ]),
    
    html.H3('Gapminder dataset'),
    
    dbc.Row(
        children=[
        
            # Affichage du graphique LifeExp by GDPperCap
            dbc.Col(
                children=[dcc.Graph(id='pg4-seg-graph-gdp', figure={})],
                align="start",
                width=7
            ),
        
            # Affichage des composantes de selection
            dbc.Col(
                
                children=[
                    
                    # Ligne contenant le choix des continents et de la transformation log
                    dbc.Row(
                        children=[
                            
                            # Choix des continents
                            dbc.Col(
                                children=[
                                    html.H6("Choix des Continents :"),
                                    dcc.Checklist(id='pg4-seg-checklist', options=opt_continent, value=opt_continent)
                                ],
                                width = 6
                            ),
                            
                            # Transformation logarithmique
                            dbc.Col(
                                children=[
                                    html.H6("Transformation Log (PIB par tête) :"),
                                    dcc.RadioItems(id='pg4-seg-radio', options=opt_log, value=True)
                                ],
                                width = 6
                            )
                        ]
                    ),
                    
                    html.Br(),
                    
                    # Ligne contenant le choix de l'annee
                    dbc.Row(
                        children=[
                            html.H6("Sélection de l'année :"),
                            dcc.Slider(id='pg4-seg-slider', min=min_year , max=max_year , value=max_year, marks=marks_years, step = None)
                        ]
                    )
                ],
                align="center",
                width=4
            )
        ]
    )   

])


# Content Correction
segmentation_cor = html.Div([
    
    dmc.Prism(
        children=
"""from dash import Dash, html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

#-----------------------------------------------------------------------#
# Initialisation                                                        #
#-----------------------------------------------------------------------#

# Creation de l'objet app contenant l'application dash
app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

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
    
    html.Header(
        children=[html.H1('Gapminder dataset')]
    ),
    
    dbc.Row(
        children=[
        
            # Affichage du graphique LifeExp by GDPperCap
            dbc.Col(
                children=[dcc.Graph(id='graph-gdp', figure={})],
                align="start",
                width=7
            ),
        
            # Affichage des composantes de selection
            dbc.Col(
                
                children=[
                    
                    # Ligne contenant le choix des continents et de la transformation log
                    dbc.Row(
                        children=[
                            
                            # Choix des continents
                            dbc.Col(
                                children=[
                                    html.H6("Choix des Continents :"),
                                    dcc.Checklist(id='checklist', options=opt_continent, value=opt_continent)
                                ],
                                width = 6
                            ),
                            
                            # Transformation logarithmique
                            dbc.Col(
                                children=[
                                    html.H6("Transformation Log (PIB par tête) :"),
                                    dcc.RadioItems(id='radio', options=opt_log, value=True)
                                ],
                                width = 6
                            )
                        ]
                    ),
                    
                    html.Br(),
                    
                    # Ligne contenant le choix de l'annee
                    dbc.Row(
                        children=[
                            html.H6("Sélection de l'année :"),
                            dcc.Slider(id='slider', min=min_year , max=max_year , value=max_year, marks=slider_marks, step = None)
                        ]
                    )
                ],
                align="center",
                width=4
            )
        ]
    )   
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
# 4.2 Accordion                                           #
#---------------------------------------------------------#


# Content Example
accordion_ex = html.Div([
    
    dbc.Accordion([
        dbc.AccordionItem(
            title="Item 1", 
            children=[
                html.P("This is the content of the first section"),
                dbc.Button("Click here")
            ]
        ),
        
        dbc.AccordionItem(
            title="Item 2",
            children=[
                html.P("This is the content of the second section"),
                dbc.Button("Don't click me!", color="danger"),
            ]
        ),
        
        dbc.AccordionItem(
            title="Item 3",
            children="This is the content of the third section"
        )
    ])
    
])

# Content Code
accordion_code = html.Div([
    
    dmc.Prism(
        children=
"""from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([]
    dbc.Accordion([
        dbc.AccordionItem(
            title="Item 1", 
            children=[
                html.P("This is the content of the first section"),
                dbc.Button("Click here")
            ]
        ),
        
        dbc.AccordionItem(
            title="Item 2",
            children=[
                html.P("This is the content of the second section"),
                dbc.Button("Don't click me!", color="danger"),
            ]
        ),
        
        dbc.AccordionItem(
            title="Item 3",
            children="This is the content of the third section"
        )
    ])
])

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")

])


# Content Exercice
accordion_exo = html.Div([
    
    html.Div([
        
        html.P(["Objectif : En repartant de l’application créée lors de l’exercice de la section 3.4 RadioItems, placer les trois callbacks suivant dans des accordions:"]),

        html.Ol([
            html.Li(["La checklist contenant la sélection des continents"]),
            html.Li(["Le radio-items permettant le transformation du PIB par tête en logarithme"]),
            html.Li(["Le slider permettant de sélectionne l’année"])
        ])
    ]),
    
    # Titre de l'application
    html.H3("Gapminder dataset : Checklist & Slider"),
    
        dbc.Accordion([
        dbc.AccordionItem(
            title="Sélection des continents", 
            children=[dcc.Checklist(id='pg4-acc-checklist', options=opt_continent, value=opt_continent, inline=True)]
        ),
        
        dbc.AccordionItem(
            title="Transformation logarithmique du PIB par tête (gdpPercap)",
            children=[dcc.RadioItems(id='pg4-acc-radio', options=opt_log, value=True)]
        ),
        
        dbc.AccordionItem(
            title="Sélection de l'année",
            children=[dcc.Slider(id='pg4-acc-slider', min=min_year , max=max_year , value=max_year,
               marks=marks_years, step = None)]
        )
    ]),
    
    # Affichage du graphique LifeExp by GDPperCap
    dcc.Graph(id='pg4-acc-graph-gdp', figure={})

])


# Content Correction
accordion_cor = html.Div([
    
    dmc.Prism(
        children=
"""from dash import Dash, html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

#-----------------------------------------------------------------------#
# Initialisation                                                        #
#-----------------------------------------------------------------------#

# Creation de l'objet app contenant l'application dash
app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

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
    
        dbc.Accordion([
        dbc.AccordionItem(
            title="Sélection des continents", 
            children=[dcc.Checklist(id='checklist', options=opt_continent, value=opt_continent, inline=True)]
        ),
        
        dbc.AccordionItem(
            title="Transformation logarithmique du PIB par tête (gdpPercap)",
            children=[dcc.RadioItems(id='radio', options=opt_log, value=True)]
        ),
        
        dbc.AccordionItem(
            title="Sélection de l'année",
            children=[dcc.Slider(id='slider', min=min_year , max=max_year , value=max_year,
               marks=slider_marks, step = None)]
        )
    ]),
    
    # Affichage du graphique LifeExp by GDPperCap
    dcc.Graph(id='graph-gdp', figure={})
        
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
# 4.3 Tabs                                                #
#---------------------------------------------------------#


# Source Example

pg4_tab1_content = dbc.Card(
    dbc.CardBody([
            html.P("This is tab 1!", className="card-text"),
            dbc.Button("Click here", color="success"),
        ]),
    className="mt-3"
)

pg4_tab2_content = dbc.Card(
    dbc.CardBody([
            html.P("This is tab 2!", className="card-text"),
            dbc.Button("Don't click here", color="danger"),
        ]),
    className="mt-3",
)


# Content Example
tabs_ex = html.Div([

    dbc.Tabs([
            dbc.Tab(label="Tab 1", tab_id="pg4-tab-1", children=pg4_tab1_content),
            dbc.Tab(label="Tab 2", tab_id="pg4-tab-2", children=pg4_tab2_content),
        ],
        id="tabs",
        active_tab="pg4-tab-1"
    )
    
])
    


# Content Code
tabs_code = html.Div([
    
    dmc.Prism(
        children=
"""import dash_bootstrap_components as dbc
from dash import Dash, html

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

tab1_content = dbc.Card(
    dbc.CardBody([
            html.P("This is tab 1!", className="card-text"),
            dbc.Button("Click here", color="success"),
        ]),
    className="mt-3"
)

tab2_content = dbc.Card(
    dbc.CardBody([
            html.P("This is tab 2!", className="card-text"),
            dbc.Button("Don't click here", color="danger"),
        ]),
    className="mt-3",
)

app.layout = html.Div([
    
    dbc.Tabs([
            dbc.Tab(label="Tab 1", tab_id="tab-1", children=tab1_content),
            dbc.Tab(label="Tab 2", tab_id="tab-2", children=tab2_content),
        ],
        id="tabs",
        active_tab="tab-1"
    )
    
])

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")

])


# Source Exercice

pg4_exo_tab1_content = dbc.Card(
    dbc.CardBody(
        className="mt-3",
        children=[dcc.Checklist(id='pg4-tab-exo-checklist', options=opt_continent, value=opt_continent, inline=True)]
    )
)

pg4_exo_tab2_content = dbc.Card(
    dbc.CardBody(
        className="mt-3",
        children=[dcc.RadioItems(id='pg4-tab-exo-radio', options=opt_log, value=True)]
    )
)

pg4_exo_tab3_content = dbc.Card(
    dbc.CardBody(
        className="mt-3",
        children=[dcc.Slider(id='pg4-tab-exo-slider', min=min_year , max=max_year , value=max_year,
                             marks=marks_years, step = None)]
    )
)


# Content Exercice
tabs_exo = html.Div([
    
    
    html.Div([
        
        html.P(["Objectif : En repartant de l’application créée lors de l’exercice de la section 3.4 RadioItems, placer les trois callbacks suivant dans des tabs:"]),

        html.Ol([
            html.Li(["La checklist contenant la sélection des continents"]),
            html.Li(["Le radio-items permettant le transformation du PIB par tête en logarithme"]),
            html.Li(["Le slider permettant de sélectionne l’année"])
        ])
    ]),
    
    # Titre de l'application
    html.H3("Gapminder dataset : Checklist & Slider"),
    
    dbc.Tabs(
        id="pg4-tab-exo-tabs",
        children=[
            dbc.Tab(label="Sélection des continents", tab_id="pg4-tab-exo-tab-1",
                    children=pg4_exo_tab1_content),
            dbc.Tab(label="Transformation logarithmique du PIB par tête (gdpPercap)", tab_id="pg4-tab-exo-tab-2",
                    children=pg4_exo_tab2_content),
            dbc.Tab(label="Sélection de l'année", tab_id="pg4-tab-exo-tab-3",
                    children=pg4_exo_tab3_content)
        ],
        active_tab="pg4-tab-exo-tab-1"),
        
    # Affichage du graphique LifeExp by GDPperCap
    dcc.Graph(id='pg4-tab-exo-graph-gdp', figure={}),
        
])



# Content Correction
tabs_cor = html.Div([
    
    dmc.Prism(
        children=
"""from dash import Dash, html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

#-----------------------------------------------------------------------#
# Initialisation                                                        #
#-----------------------------------------------------------------------#

# Creation de l'objet app contenant l'application dash
app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

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

tab1_content = dbc.Card(
    dbc.CardBody(
        className="mt-3",
        children=[dcc.Checklist(id='checklist', options=opt_continent, value=opt_continent, inline=True)]
    )
)

tab2_content = dbc.Card(
    dbc.CardBody(
        className="mt-3",
        children=[dcc.RadioItems(id='radio', options=opt_log, value=True)]
    )
)

tab3_content = dbc.Card(
    dbc.CardBody(
        className="mt-3",
        children=[dcc.Slider(id='slider', min=min_year , max=max_year , value=max_year,
                             marks=slider_marks, step = None)]
    )
)



app.layout = html.Div([
    
    # Titre de l'application
    html.H1("Gapminder dataset : Checklist & Slider"),
    
    dbc.Tabs(
        id="tabs",
        children=[
            dbc.Tab(label="Sélection des continents", tab_id="tab-1",
                    children=tab1_content),
            dbc.Tab(label="Transformation logarithmique du PIB par tête (gdpPercap)", tab_id="tab-2",
                    children=tab2_content),
            dbc.Tab(label="Sélection de l'année", tab_id="tab-3",
                    children=tab3_content)
        ],
        active_tab="tab-1")
    
    # Affichage du graphique LifeExp by GDPperCap
    dcc.Graph(id='graph-gdp', figure={}),
        
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
# 4.4 Navbar                                              #
#---------------------------------------------------------#


# Source Example
pg4_navlink_nav = dbc.Nav([
        dbc.NavItem(dbc.NavLink("Doc Dash", active=True, href="https://dash.plotly.com/")),
        dbc.NavItem(dbc.NavLink("Target 1", href="#pg4-navlink-target1", external_link=True)),
        dbc.NavItem(dbc.NavLink("Target 2", href="#pg4-navlink-target2", external_link=True)),
        dbc.NavItem(dbc.NavLink("Disabled", disabled=True, href="#")),
        dbc.DropdownMenu(
            [dbc.DropdownMenuItem("Github", href="https://github.com/"),
             dbc.DropdownMenuItem("Gitlab", href="https://about.gitlab.com/")],
            label="Dropdown",
            nav=True,
        ),
    ])

pg4_navlink_content = html.Div([
    html.Div([html.H1("Titre") for x in range(20)]),
    html.H1('Target 1', id='pg4-navlink-target1'),
    html.Div([html.H1("Titre") for x in range(20)]),
    html.H1('Target 2', id='pg4-navlink-target2'),
])

# Content Example
navlink_ex = html.Div([pg4_navlink_nav, pg4_navlink_content])    


# Content Code
navlink_code = html.Div([
    
    dmc.Prism(
        children=
"""from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

nav = dbc.Nav([
        dbc.NavItem(dbc.NavLink("Doc Dash", active=True, href="https://dash.plotly.com/")),
        dbc.NavItem(dbc.NavLink("Target 1", href="#target1", external_link=True)),
        dbc.NavItem(dbc.NavLink("Target 2", href="#target2", external_link=True)),
        dbc.NavItem(dbc.NavLink("Disabled", disabled=True, href="#")),
        dbc.DropdownMenu(
            [dbc.DropdownMenuItem("Github", href="https://github.com/"),
             dbc.DropdownMenuItem("Gitlab", href="https://about.gitlab.com/")],
            label="Dropdown",
            nav=True,
        ),
    ])

content = html.Div([
    html.Div([html.H1("Titre") for x in range(20)]),
    html.H1('Target 1', id='target1'),
    html.Div([html.H1("Titre") for x in range(20)]),
    html.H1('Target 2', id='target2'),
])

app.layout = html.Div([nav, content])

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")

])


# Source Exercice
iris = px.data.iris()

pg4_nav_fig1 = px.scatter(iris, x="sepal_width", y="petal_length", color="species")

lab = {"species_id"   : "Species"       ,
       "sepal_width"  : "Sepal Width"   ,
       "sepal_length" : "Sepal Length"  ,
       "petal_width"  : "Petal Width"   , 
       "petal_length" : "Petal Length"  }

pg4_nav_fig2 = px.parallel_coordinates(iris, color="species_id", labels=lab,
                    color_continuous_scale=px.colors.diverging.Tropic, 
                    color_continuous_midpoint=2)

pg4_navlink_exo_navbar = dbc.Nav([
        dbc.NavItem(dbc.NavLink("ENT Rennes 1", href="https://ent.univ-rennes1.fr")),
        dbc.NavItem(dbc.NavLink("Iris Scatter Plot", href="#pg4-navlink-exo-iris", external_link=True)),
        dbc.NavItem(dbc.NavLink("Iris Parrallel Coordinates", href="#pg4-navlink-exo-parrallel", external_link=True)),
])


pg4_navlink_exo_content = html.Div([
    html.H3('Iris Scatter Plot', id='pg4-navlink-exo-iris'),
    html.H6(children='Hello Dash'),
    html.P(children='Dash: A web application framework for your data.'),
    dcc.Graph(id='pg4-navlink-exo-graph1', figure=pg4_nav_fig1),
    html.H3('Iris Parrallel Coordinates', id='pg4-navlink-exo-parrallel'),
    html.H6('Iris dataset : Parrallel coordinates'),
    dcc.Graph(id='pg4-navlink-exo-graph2', figure=pg4_nav_fig2)
])

# Content Exercice
navlink_exo = html.Div([
    
    html.Div([
        
        html.P(["Objectif : Répliquer l'application ci-dessous en reprenant les deux graphiques réalisés dans la section 2.2 Graph. Créer un navlink avec trois composantes :"]),

        html.Ol([
            html.Li(["ENT Rennes 1 : lien vers l’ent de Rennes 1"]),
            html.Li(["Iris Scatter Plot : lien dans l’application vers le titre du même nom"]),
            html.Li(["Iris Parrallel Coordinates : lien dans l’application vers le titre du même nom"])
        ])
    ]),
    
    # Titre de l'application
    html.Div([pg4_navlink_exo_navbar, pg4_navlink_exo_content])
        
])


# Content Correction
navlink_cor = html.Div([
    
    dmc.Prism(
        children=
"""from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

nav = dbc.Nav([
        dbc.NavItem(dbc.NavLink("ENT Rennes 1", href="https://ent.univ-rennes1.fr")),
        dbc.NavItem(dbc.NavLink("Iris Scatter Plot", href="#iris", external_link=True)),
        dbc.NavItem(dbc.NavLink("Iris Parrallel Coordinates", href="#parrallel", external_link=True)),
])

df = px.data.iris()

fig1 = px.scatter(df, x="sepal_width", y="petal_length", color="species")

lab = {"species_id"   : "Species"       ,
       "sepal_width"  : "Sepal Width"   ,
       "sepal_length" : "Sepal Length"  ,
       "petal_width"  : "Petal Width"   , 
       "petal_length" : "Petal Length"  }

fig2 = px.parallel_coordinates(df, color="species_id", labels=lab,
                    color_continuous_scale=px.colors.diverging.Tropic, 
                    color_continuous_midpoint=2)

iris_scatter_content = html.Div(children=[
    html.H3(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(id='graph1', figure=fig1)
])


iris_parrallel_content = html.Div([
    
    html.H3('Iris dataset : Parrallel coordinates'),
    dcc.Graph(id='graph2', figure=fig2)

])

content = html.Div([
    html.H1('Iris Scatter Plot', id='iris'),
    html.Div(iris_scatter_content),
    html.H1('Iris Parrallel Coordinates', id='parrallel'),
    html.Div(iris_parrallel_content)
])

app.layout = html.Div([nav, content])

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")

])


#---------------------------------------------------------#
# 4.5 Navbar                                              #
#---------------------------------------------------------#


# Content Example
navbar_ex = html.Div([
    
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Page 1", href="#")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("More pages", header=True),
                    dbc.DropdownMenuItem("Page 2", href="#"),
                    dbc.DropdownMenuItem("Page 3", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],
        brand="NavbarSimple",
        brand_href="#",
        color="primary",
        dark=True,
    )
    
])
    

# Content Code
navbar_code = html.Div([
    
    dmc.Prism(
        children=
"""from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="NavbarSimple",
    brand_href="#",
    color="primary",
    dark=True,
)

app.layout = html.Div([navbar])

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")

])


# Source Exercice
pg4_nav_navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Iris Scatter", href="#pg4-nav-exo-scatter", external_link=True)),
        dbc.NavItem(dbc.NavLink("Iris Parallel", href="#pg4-nav-exo-parrallel", external_link=True)),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("ENT Rennes 1", href="https://ent.univ-rennes1.fr"),
                dbc.DropdownMenuItem("Github", href="https://github.com/"),
            ],
            nav=True,
            in_navbar=True,
            label="Liens Utiles",
        ),
    ],
    brand="Iris",
    brand_href="#pg4-nav-exo-scatter",
    brand_external_link=True,
    color="primary",
    dark=True,
)


pg4_nav_content = html.Div([
    html.H3('Iris Scatter Plot', id='pg4-nav-exo-scatter'),
    html.H6('Iris dataset : Parrallel coordinates'),
    dcc.Graph(id='pg4-nav-exo-graph2', figure=pg4_nav_fig2),
    html.H3('Iris Parrallel Coordinates', id='pg4-nav-exo-parrallel'),
    html.H6(children='Hello Dash'),
    html.P(children='Dash: A web application framework for your data.'),
    dcc.Graph(id='pg4-nav-exo-graph1', figure=pg4_nav_fig1)
])

# Content Exercice
navbar_exo = html.Div([
    
    html.Div([
        
        html.P(["Objectif : Répliquer l'application ci-dessous en reprenant les deux graphiques réalisés dans la section 2.2 Graph. Créer un navbar avec trois composantes :"]),

        html.Ol([
            html.Li(["Iris Scatter Plot : lien dans l’application vers le titre du même nom"]),
            html.Li(["Iris Parrallel Coordinates : lien dans l’application vers le titre du même nom"]),
            html.Li(["Un menu déroulant avec un lien vers l'ENT Rennes 1 et un lien vers Github"]),
        ])
    ]),
    
    # Titre de l'application
    html.Div([pg4_nav_navbar, pg4_nav_content])
        
])



# Content Correction
navbar_cor = html.Div([
    
    dmc.Prism(
        children=
"""from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Iris Scatter", href="#scatter", external_link=True)),
        dbc.NavItem(dbc.NavLink("Iris Parallel", href="#parrallel", external_link=True)),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("ENT Rennes 1", href="https://ent.univ-rennes1.fr"),
                dbc.DropdownMenuItem("Github", href="https://github.com/"),
            ],
            nav=True,
            in_navbar=True,
            label="Liens Utiles",
        ),
    ],
    brand="Iris",
    brand_href="#scatter",
    brand_external_link=True,
    color="primary",
    dark=True,
)

df = px.data.iris()

fig1 = px.scatter(df, x="sepal_width", y="petal_length", color="species")


lab = {"species_id"   : "Species"       ,
       "sepal_width"  : "Sepal Width"   ,
       "sepal_length" : "Sepal Length"  ,
       "petal_width"  : "Petal Width"   , 
       "petal_length" : "Petal Length"  }

fig2 = px.parallel_coordinates(df, color="species_id", labels=lab,
                    color_continuous_scale=px.colors.diverging.Tropic, 
                    color_continuous_midpoint=2)


iris_scatter_content = html.Div(children=[
    html.H3(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(id='graph1', figure=fig1)
])

iris_parrallel_content = html.Div([
    
    html.H3('Iris dataset : Parrallel coordinates'),
    dcc.Graph(id='graph2', figure=fig2)

])


content = html.Div([
    html.H1('Iris Scatter Plot', id='scatter'),
    html.Div(iris_scatter_content),
    html.H1('Iris Parrallel Coordinates', id='parrallel'),
    html.Div(iris_parrallel_content)
])

app.layout = html.Div([navbar, content])

if __name__ == '__main__':
    app.run(debug=True)""",
        language="python",
        colorScheme="dark")

])



#---------------------------------------------------------#
# 4.5 Project Structure                                   #
#---------------------------------------------------------#




SIDEBAR_STYLE = {
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20%",
    "padding": "1rem 1rem",
    "background-color": "orange",
}

CONTENT_STYLE = {
    "top": 0,
    "right": 0,
    "bottom": 0,
    "width": "80%",
    "padding": "1rem 1rem",
    "background-color":"green"
}


#----------------------------------------------------------------#
# 2. Interface                                                   #
#----------------------------------------------------------------#

ps_ex_sidebar = html.Div(
    [
        html.H2("Sidebar"),
        html.Hr(),
        html.P("A simple sidebar layout with navigation links"),
        dbc.Nav(
            children=[
                dbc.NavLink("Home", id="pg4-ps-home", active="exact"),
                dbc.NavLink("Page 1", id="pg4-ps-page1", active="exact"),
                dbc.NavLink("Page 2", id="pg4-ps-page2", active="exact")
            ],
            vertical=True,
            pills=True,
            id="pg4-ps-ex-nav",
        ),
    ],
    style=SIDEBAR_STYLE,
)

ps_ex_content = html.Div(id="ps-ex-page-content", style=CONTENT_STYLE)

# Content Example
ps_ex = html.Div([ps_ex_sidebar, ps_ex_content])
    

# Content Code
ps_code = html.Div([
    
    dmc.Prism(
        children=
"""
""",
        language="python",
        colorScheme="dark")

])


# Source Exercice


# Content Exercice
ps_exo = html.Div([
    
    html.Div([
        
        html.P(["Objectif : Répliquer l'application ci-dessous en reprenant les deux graphiques réalisés dans la section 2.2 Graph. Créer un navbar avec trois composantes :"]),

        html.Ol([
            html.Li(["Iris Scatter Plot : lien dans l’application vers le titre du même nom"]),
            html.Li(["Iris Parrallel Coordinates : lien dans l’application vers le titre du même nom"]),
            html.Li(["Un menu déroulant avec un lien vers l'ENT Rennes 1 et un lien vers Github"]),
        ])
    ]),
    
    # Titre de l'application

])



# Content Correction
ps_cor = html.Div([
    
    dmc.Prism(
        children=
"""
""",
        language="python",
        colorScheme="dark")

])



#-----------------------------------------------------------------------#
# Interface                                                             #
#-----------------------------------------------------------------------#


layout = html.Div([    
    
    html.H1("4. Layout"),
    
    html.H2("4.1 Segmentation"),
    
    dbc.Tabs([
            dbc.Tab(label="Exemple"   , tab_id="segmentation-ex"  , children=segmentation_ex  , className="tab"),
            dbc.Tab(label="Code"      , tab_id="segmentation-code", children=segmentation_code, className="tab"),
            dbc.Tab(label="Exercice"  , tab_id="segmentation-exo" , children=segmentation_exo , className="tab"),
            dbc.Tab(label="Correction", tab_id="segmentation-cor" , children=segmentation_cor , className="tab")
        ],
        id="segmentation",
        active_tab="segmentation-ex"
    ),
    
    
    html.H2("4.2 Accordion"),
    
    dbc.Tabs([
            dbc.Tab(label="Exemple"   , tab_id="accordion-ex"  , children=accordion_ex  , className="tab"),
            dbc.Tab(label="Code"      , tab_id="accordion-code", children=accordion_code, className="tab"),
            dbc.Tab(label="Exercice"  , tab_id="accordion-exo" , children=accordion_exo , className="tab"),
            dbc.Tab(label="Correction", tab_id="accordion-cor" , children=accordion_cor , className="tab")
        ],
        id="accordion",
        active_tab="accordion-ex"
    ),

    html.H2("4.3 Tabs"),
    
    dbc.Tabs([
            dbc.Tab(label="Exemple"   , tab_id="tabs-ex"  , children=tabs_ex  , className="tab"),
            dbc.Tab(label="Code"      , tab_id="tabs-code", children=tabs_code, className="tab"),
            dbc.Tab(label="Exercice"  , tab_id="tabs-exo" , children=tabs_exo , className="tab"),
            dbc.Tab(label="Correction", tab_id="tabs-cor" , children=tabs_cor , className="tab")
        ],
        id="tabs",
        active_tab="tabs-ex"
    ),

    html.H2("4.4 Navlink"),
    
    dbc.Tabs([
            dbc.Tab(label="Exemple"   , tab_id="navlink-ex"  , children=navlink_ex  , className="tab"),
            dbc.Tab(label="Code"      , tab_id="navlink-code", children=navlink_code, className="tab"),
            dbc.Tab(label="Exercice"  , tab_id="navlink-exo" , children=navlink_exo , className="tab"),
            dbc.Tab(label="Correction", tab_id="navlink-cor" , children=navlink_cor , className="tab")
        ],
        id="navlink",
        active_tab="navlink-ex"
    ),    
    
    html.H2("4.5 Navbar"),
    
    dbc.Tabs([
            dbc.Tab(label="Exemple"   , tab_id="navbar-ex"  , children=navbar_ex  , className="tab"),
            dbc.Tab(label="Code"      , tab_id="navbar-code", children=navbar_code, className="tab"),
            dbc.Tab(label="Exercice"  , tab_id="navbar-exo" , children=navbar_exo , className="tab"),
            dbc.Tab(label="Correction", tab_id="navbar-cor" , children=navbar_cor , className="tab")
        ],
        id="navbar",
        active_tab="navbar-ex"
    ),
    
    html.H2("4.6 Project Structure"),
    
    dbc.Tabs([
            dbc.Tab(label="Exemple"   , tab_id="ps-ex"  , children=ps_ex  , className="tab"),
            dbc.Tab(label="Code"      , tab_id="ps-code", children=ps_code, className="tab"),
            dbc.Tab(label="Exercice"  , tab_id="ps-exo" , children=ps_exo , className="tab"),
            dbc.Tab(label="Correction", tab_id="ps-cor" , children=ps_cor , className="tab")
        ],
        id="ps",
        active_tab="ps-ex"
    ),
    
])

#-----------------------------------------------------------------------#
# Serveur                                                               #
#-----------------------------------------------------------------------#


#---------------------------------------------------------#
# 4.1 Segmentation                                        #
#---------------------------------------------------------#


@callback(
    Output('pg4-seg-graph-gdp', 'figure'),
    Input('pg4-seg-slider', "value"),
    Input('pg4-seg-checklist', "value"),
    Input('pg4-seg-radio', 'value')
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


#---------------------------------------------------------#
# 4.2 Accordion                                           #
#---------------------------------------------------------#


@callback(
    Output('pg4-acc-graph-gdp', 'figure'),
    Input('pg4-acc-slider', "value"),
    Input('pg4-acc-checklist', "value"),
    Input('pg4-acc-radio', 'value')
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


#---------------------------------------------------------#
# 4.3 Tabs                                                #
#---------------------------------------------------------#


@callback(
    Output('pg4-tab-exo-graph-gdp', 'figure'),
    Input('pg4-tab-exo-slider', "value"),
    Input('pg4-tab-exo-checklist', "value"),
    Input('pg4-tab-exo-radio', 'value')
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


#---------------------------------------------------------#
# 4.6 Project Structure                                   #
#---------------------------------------------------------#


@callback(
    Output("ps-ex-page-content", "children"),
    Input("pg4-ps-home","n_clicks")
    )
def render_page_content(home):
    return(html.P("Paragraphe."))
