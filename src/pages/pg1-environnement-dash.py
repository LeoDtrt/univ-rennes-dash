from dash import Dash, html, dcc, callback, Input, Output, register_page
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import plotly.express as px


register_page(__name__,
    path='/',
    name='1. Environnement Dash'
)


#-----------------------------------------------------------------------#
# Sources                                                               #
#-----------------------------------------------------------------------#



#-----------------------------------------------------------------------#
# Interface                                                             #
#-----------------------------------------------------------------------#


layout = html.Div([    
    
    html.H1('1. Environnement Dash'),
    
    html.H2('1.1 Intérêts'),
    html.P("Pourquoi faire du Dash ?"),
    html.Ul([
        html.Li("Faire de la visualisation de données et créer des dashboards automatisés"),
        html.Li("Effectuer des tâches sur une interface en clique bouton"),
        html.Li("Automatisation des processus de traitement de données via une interface web"),
        html.Li("Alternative simplifiée pour faire du développement web: pas de javascript"),
        html.Li("La librairie Dash est une librairie équivalente à R Shiny mais en Python"),
        html.Li("Dash c’est beaucoup trop cool")
    ]),


    html.H2('1.2 Installation de Python'),   
    html.P("Python est téléchargeable à l’adresse suivante : https://www.python.org/downloads/"),
    html.Img(src="assets/img/download-python.png", className= "img"),
 
 
    html.H2('1.3 Installation de VSCode'),   
    html.P("Visual Studio Code est téléchargeable à l’adresse suivante : https://code.visualstudio.com/download"),
    html.Img(src="assets/img/download-vsc.png", className= "img"),


    html.H2('1.4 Installation de VSCode'),   
    html.P("La page d’accueil de VSCode ressemble à ceci :"),
    html.Img(src="assets/img/vsc-accueil.png", className= "img"),
    html.P("Entrer le raccourci clavier CTRL+Shift+X sur Windows ou Cmd+Shift+X sur Mac puis installer python sur VSCode :"),
    html.Img(src="assets/img/vsc-install-python.png", className= "img"),
   
   
    html.H2('1.5 Créer un environnement virtuel via le terminal'),
    html.P("Création et activation de l’environnement virtuel .venv sur Windows :"),
    dmc.Prism(
        children=
"""# Installer virtualenv sur VSCode
pip install virtualenv

# Créer un environnement virtuel .venv
python -m venv .venv

# Se déplacer dans le répertoire Scripts
cd .venv/Scripts

# Activer l'environnement virtuel
.\\activate

# Désactiver l'environnement
deactivate""",
        language="python",
        colorScheme="dark"),
    html.P("Création et activation de l’environnement virtuel .venv sur Mac :"),
    dmc.Prism(
        children=
"""# Installer virtualenv sur VSCode
pip install virtualenv

# Créer un environnement virtuel .venv
python -m venv .venv

# Activer l'environnement virtuel
source .venv/bin/activate

# Désactiver l'environnement
deactivate""",
        language="python",
        colorScheme="dark",
        className="tab"),
    html.P("Liste non exhaustive des packages à installer pour l’utilisation de dash :"),
    dmc.Prism(
        children=
"""pip install dash
pip install jupyter-dash
pip install pandas
pip install plotly.express
pip install dash-bootstrap-components
pip install dash-mantine-components
pip list""",
        language="python",
        colorScheme="dark",
        className="tab"),
    html.Img(src="assets/img/pip-list.png", className= "img"),
    html.P("⚠ Remarque : Il est nécessaire d’activer un environnement virtuel pour pouvoir ensuite y installer des librairies."),

   
    html.H2("1.6 Automatiser la création d'un environnement virtuel"),   
    html.P("Avant de pouvoir créer un environnement virtuel sous VSCode, il faut exécuter les tâches suivantes :"),
    html.Ol([
        html.Li("Aller dans File > Preferences > Settings"),
        html.Li("Entrer “venv path” dans la bar de recherche"),
        html.Li("Puis saisir : “${workspaceFolder}/.venv”") 
    ]),
    html.Img(src="assets/img/setting-venv.png", className= "img"),
    html.P("⚠ Remarque : Les actions décrites ci-dessus permettent à VSCode d’activer un environnement contenu dans un dossier .venv à la racine du répertoire d’un projet."),
   
    html.P("La création d’un environnement virtuel suppose la création d’un dossier qui contiendra l’ensemble de votre projet. Ce dossier contiendra donc également l’environnement virtuel python associé."),
    
    html.Ol(
        children=([
            html.Li("Cliquer sur File puis Open Folder..."),
            html.Li("Sélectionner le répertoire courant de votre projet (ex: dash)"),
            html.Li("Faites ensuite le raccourci clavier CTRL+Shift+P"),
            html.Li("Sélectionner Python: Create Environment..."),
            html.Img(src="assets/img/vsc-create-venv-1.png", className= "img"),
            html.Li("Sélectionner Venv: Creates a “.venv” virtual environment in the current workspace"),
            html.Img(src="assets/img/vsc-create-venv-2.png", className= "img"),
            html.Li("Sélectionner la version de Python souhaitée"),
            html.Li("Un dossier .venv s’est créé à la racine de votre répertoire courant"),
            html.Img(src="assets/img/vsc-create-venv-3.png", className= "img"),
            html.Li("Pour activer l'environnement virtuel il faut ensuite ouvrir un Terminal puis taper les lignes suivantes :"),
            dmc.Prism(
        children=
"""# Sur Windows
cd .venv/Scripts
.\\activate
            
# Sur Mac
source bin/activate
            
# Pour désactiver un environnement
deactivate""",
        language="python",
        colorScheme="dark",
        className="tab")
        ])
    ),


    html.H2('1.6 Run & Kill une session dash'),
    html.P("Pour run une application dash il faut :"),

   html.Ol([
        html.Li("Se placer à la racine de l’application dans un terminal"),
        dmc.Prism(
            children=
"""# Créer le répertoire projet à la racine
mkdir projet

# Changer de direction en entrant dans le répertoire projet
cd projet

# Revenir d'un pas en arrière et sortir du répertoire projet
cd ..""",
            language="python",
            colorScheme="dark",
            className="tab"),
        html.Li("Activer un environnement virtuel python avec toutes les librairies nécessaires au lancement de l’application"),
        html.Li("Taper la commande suivante dans le terminal pour lancer l'application app.py :"),
        dmc.Prism(
            children="""python app.py""",
            language="python",
            colorScheme="dark"),
        html.Img(src="assets/img/run-app.png", className= "img"),
    ]),
   
   
   
   
   










 
])

#-----------------------------------------------------------------------#
# Serveur                                                               #
#-----------------------------------------------------------------------#


