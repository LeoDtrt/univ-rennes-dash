from dash import Dash, html, dcc, callback, Input, Output, register_page
import dash_bootstrap_components as dbc
from assets.pkg.util import *
import plotly.express as px


register_page(__name__,
    name='6. Déployer une App'
)


#-----------------------------------------------------------------------#
# Sources                                                               #
#-----------------------------------------------------------------------#

src_render = "assets/render/render-deploy-dash.zip"

git_clone_code = """
# Cloner le projet
git clone https://github.com/LeoDtrt/render-deploy-dash.git

# Se place dans le projet
cd render-deploy-dash
"""


app_server_code = """
from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

server = app.server

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
    app.run(debug=True)"""

render_yaml_code = """
services:
  # See https://render.com/docs/blueprint-spec for more info on render blueprints
  - type: web
    name: render-deploy-dash
    env: python
    plan: free
    # A requirements.txt file must exist
    buildCommand: pip install -r requirements.txt
    # A app.py file must exist and contain `server=app.server`
    startCommand: gunicorn app:server
    envVars:
      - key: PYTHON_VERSION
        value: 3.14.7
"""

requirements_code = """
dash==4.4.1
dash_bootstrap_components==2.0.4
pandas==3.0.5
plotly==7.0.0
gunicorn
"""

pip_install_code = """
pip install dash
pip install jupyter-dash
pip install pandas
pip install plotly.express
pip install dash-bootstrap-components
pip list"""

active_env_windows_code = """
# Sur Windows
cd .venv/Scripts
.\\activate
            
# Sur Mac
source bin/activate
            
# Pour désactiver un environnement
deactivate"""

active_env_mac_code = """
# Sur Mac
source .venv/bin/activate"""

deactive_env_windows_code = """
# Sur Windows
cd .venv/Scripts
deactivate"""

deactive_env_mac_code = """
# Sur Mac
cd .venv/bin
deactivate"""

racine_code = """
# Créer le répertoire projet à la racine
mkdir projet

# Changer de direction en entrant dans le répertoire projet
cd projet

# Revenir d'un pas en arrière et sortir du répertoire projet
cd .."""

#-----------------------------------------------------------------------#
# Interface                                                             #
#-----------------------------------------------------------------------#


layout = html.Div([    
    
    html.H1('6. Déployer une application Dash'),
    
    html.H2('6.1 Présentation', className="h2s"),
    html.P(children=[html.Span("Objectif : ", className="h"),"Déployer un application dash sur un server (mise en production)"]),
    html.P(children=[html.Span("Intérêt : ", className="h"),"Diffuser votre application dash via un lien (URL)"]),
    html.P(children=[html.Span("Outils : ", className="h"),"Le package python dash, le site Github et la plateforme gratuite Render"]),
    html.P(children=[html.Span("Pré-requis :", className="h")]),
    html.Ul([
        html.Li("Une application dash fonctionnelle"),
        html.Li(["Un compte sur Github (",html.A("https://github.com/", href="https://github.com/", target='_blank' , className="l"),")"]),
        html.Li(["Un compte sur Render (",html.A("https://dashboard.render.com/login", href="https://dashboard.render.com/login", target='_blank' , className="l"),")"])
    ]),
    html.P(["⚠ ", html.U("Remarque :")," Créer d’abord votre compte sur Github puis créer votre compte sur Render en utilisant votre compte Github."]),
    html.Img(src="assets/img/pg6-render-login.png", className= "img", style={'width':'50%'}),

    html.H2('6.2 Créer un projet sur Github', className="h2s"),
    html.P(["S'authentifier sur le site ",html.A("Github", href="https://github.com/", target='_blank' , className="l")," puis créer un nouveau répertoire public avec un README"]),
    html.Img(src="assets/img/pg6-repo-github.png", className= "img", style={'width':'50%'}),

    html.P(["Cloner ce nouveau répertoire sur votre machine"]),
    html.Img(src="assets/img/pg6-clone-repo.png", className= "img", style={'width':'50%'}),

    boxCode('virtualenv-windows', git_clone_code),
    html.Br(),

    html.P(["Télécharger le fichier ", html.Span(html.I("render-deploy-dash.zip"), className='h'), ", extraire et déplacer ces fichiers à la racine de votre projet."]),

    html.Button([html.Img(src="assets/img/dnl.png", style={'width':'10%'}), "  render-deploy-dash.zip"], id="btn-render"),
    dcc.Download(id="dnl-render"),

    html.H2('6.3 Architecture et pipeline de déploiement', className="h2s"),

    html.P(["La réussite du déploiement du projet nécessite une architecture et un formalisme pour pouvoir utiliser le pipeline de Render. Il est nécessaire d'avoir les fichiers suivants à la racine du projet :"]),

    html.Ol(
        children=([
            html.Li([html.Span("app.py :", className="h"), " Ajouter la ligne ", html.I('server = app.server')," juste après la création de l’objet ",html.I('Dash(__name__)'), " dans le script app.py"]),
            html.Br(),
            boxCode('app-server', app_server_code),
            html.Br(),
            html.Li([html.Span("render.yaml :", className="h"), " Renseigner la version de python et le nom du projet sur Render"]),
            html.Br(),
            boxCode('render-yaml', render_yaml_code),
            html.Br(),
            html.Li([html.Span("requirements.txt :", className="h"), " Contient la liste des numéros de version et des packages nécessaires au fonctionnement de l'application ainsi que le package ", html.Span("gunicorn",className="h")]),
            html.Br(),
            boxCode('require', requirements_code),
            html.Br(),
        ])
    ),

    html.H2("6.4 Qu’est-ce qu’un pipeline ?", className="h2s"),

    html.P(["Un ",html.Span("pipeline", className="h"), " dans le cadre du déploiement d’une application Dash avec Render (ou tout autre service similaire) est ", html.Span("une suite automatisée d’étapes", className="h"), " qui permet de :"]),

    html.Ol(
        children=([
            html.Li([html.Span("Préparer le code :", className="h"), " Vérifier et préparer le code source de votre application."]),
            html.Li([html.Span("Construire l’application :", className="h"), " Installer les dépendances et configurer l’environnement pour exécuter l’application"]),
            html.Li([html.Span("Déployer :", className="h"), " Transférer l’application sur un server et la rendre disponible aux utilisateurs via une URL ou un domaine"]),
        ])
    ),

    html.P(["Étapes principales d’un pipeline pour une application Dash avec Render :"]),

    html.Ol(
        children=([
            html.Li([html.Span("Récupération du code :", className="h"), " Render récupère automatiquement votre application depuis un dépôt Git (par exemple, GitHub ou GitLab"]),
            html.Li([html.Span("Installation des dépendances :", className="h"), " Render lit un fichier comme requirements.txt pour installer les bibliothèques nécessaires"]),
            html.Li([html.Span("Configuration et démarrage :", className="h"), " Render exécute une commande, comme gunicorn app:server, pour lancer l’application Dash"]),
            html.Li([html.Span("Mise en ligne :", className="h"), " Le server de Render héberge l’application et la rend accessible via une URL publique"]),
        ])
    ),

    html.P(["En résumé, un pipeline de déploiement est une séquence structurée d’étapes automatisées qui simplifie et fiabilise le processus de mise en ligne de votre application."]),

    html.H2('6.5 Connecter ce projet sur Render', className="h2s"),

    html.P(["S'authentifier sur le site ",html.A("Render", href="https://dashboard.render.com/login", target='_blank' , className="l")," puis sur la barre latérale à gauche de la home page :"]),
    
    html.Ol(
        children=([
            html.Li(["Aller dans ", html.Span("Projects", className="h"), " puis cliquer sur ",html.Span("+ New", className="h")," puis ",html.Span("Web Service", className="h")]),
            html.Img(src="assets/img/pg6-render-home.png", className= "img"),
            html.Li(["Copier/coller le lien vers le dépôt Github"]),
            html.Img(src="assets/img/pg6-connect-deploy.png", className= "img"),
            html.Li(["Cliquer sur Connect"]),
            html.Img(src="assets/img/pg6-connect-param-1.png", className= "img"),
            html.Li(["Sélectionner la branch main de votre dépôt et la région Virginia (US East)"]),
            html.Img(src="assets/img/pg6-connect-param-2.png", className= "img"),
            html.Li([html.Span(["⚠ ", html.U("Remarque :")], className='w')," Sélectionner la version GRATUITE"]),
            html.Img(src="assets/img/pg6-connect-param-3.png", className= "img", style={'width':'50%'}),
            html.Li(["Cliquer sur Deploy web service"]),
            html.Img(src="assets/img/pg6-connect-param-4.png", className= "img", style={'width':'50%'}),
        ])
    ),

    html.H2("6.6 Déploiement de l'App", className="h2s"),

    html.P(["Après avoir cliqué sur Deploy web service, la pipeline se déclenche pour build l'app et la déployer sur le server de Render"]),
    html.Img(src="assets/img/pg6-deploy-ok.png", className= "img"),

    html.P(["Si le build et le deploy ont réussi : "]),
    html.Ul([
        html.Li("Aller dans la rubrique Deploys dans la barre latérale à gauche"),
        html.Li(["Puis cliquer sur le lien de l'applicatin ",html.A("https://render-deploy-dash.onrender.com", href="https://render-deploy-dash.onrender.com", target='_blank' , className="l")])
    ]),
    html.Img(src="assets/img/pg6-deploy-link.png", className= "img"),
    html.P(["Sinon il faut se rendre dans les logs pour analyser les messages d'erreur."])
 
])

#-----------------------------------------------------------------------#
# Server                                                               #
#-----------------------------------------------------------------------#

@callback(
    Output("dnl-render", "data"),
    Input("btn-render", "n_clicks"),
    prevent_initial_call=True,
)
def download_render_zip(n_clicks):
    return dcc.send_file(src_render)
