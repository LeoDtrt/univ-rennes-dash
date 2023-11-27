from dash import Dash, dcc, html, callback, Input, Output, State, register_page
import base64
import io
import pandas as pd


register_page(__name__,
    name='Text Creation'
)


#------------------------------------------------------------#
# 1. INITIALISATION                                          #
#------------------------------------------------------------#


txt = []
n = []

#------------------------------------------------------------#
# 2. INTERFACE                                               #
#------------------------------------------------------------#

layout = html.Div([
    
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
                txt = '\n'.join(txt)
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


