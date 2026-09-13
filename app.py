from dash import html, Dash, page_registry, page_container, callback, Input, Output, callback_context, dcc
import dash_bootstrap_components as dbc
from datetime import datetime

app = Dash(__name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

n_clicks_closing_sidebar = []

server = app.server


link_footer = {
    'color':'white',
    'fontWeight': 'normal',
    'fontSize':'14px'
}



footer = html.Div([
    
    html.Div([

        html.A([
            html.Img(src='assets/img/in.png', style={'width':'36px'}),
            'Léo Dutertre-Ladurée',            
        ], href='https://www.linkedin.com/in/leo-dutertre-laduree-502a5689/', target='_blank', className='l', style = link_footer)
    ], style={'display':'flex', 'alignItems':'center'}),
    
    html.Div([
        html.A([
            html.Img(src='assets/img/mailto.png', style={'width':'36px'}),
            'ldutertreladuree@gmail.com'
        ], href='mailto:ldutertreladuree@gmail.com', target='_blank', className='l', style = link_footer)
    ], style={'display':'flex', 'alignItems':'center'}),
    
    html.Div([
        html.Img(src='assets/img/calendar.png', style={'width':'34px'}),
        html.Div(datetime.today().strftime('%d %B %Y'), className='l', style = link_footer)        
    ], style={'display':'flex', 'alignItems':'center'}),
    

    
    ], className='footer')

sidebar = html.Div([
    dbc.Nav([
            dbc.Button(page["name"], href=page["path"], className="btn-sdb")
            for page in page_registry.values()
        ],
        vertical=True,
        pills=True),
    
    footer
], id='sidebar', className='sidebar')

sidebar_closed = html.Div(id='sidebar', className='sidebarClose')

content = html.Div(page_container, id='body', className='body')



navbar = html.Div([
    html.Div(html.Img(src='assets/img/logo.png', className="logo"), style={'text-align':"center"}),
    dbc.Button("llll", color = "primary", id = "closing-sidebar", className="btn-close-sidebar"),
    html.A(html.Img(src='assets/img/cezane.jpg', className="cezane"), className="circle", href="https://dash.plotly.com/", target="_blank")
], className='navbar')

app.layout = html.Div([navbar, sidebar, content], id="app", className="all")

sd_open = [[navbar, sidebar, content],"sidebar","body"]
sd_close = [[navbar, sidebar_closed, content],"sidebarClose","bodyFull"]


@callback(
    Output("app", "children"),
    Output("sidebar", "className"),
    Output("body", "className"),
    Input("closing-sidebar","n_clicks")
)
def closing_sidebar(n_clicks):        
    if n_clicks is None:
        active = sd_open
    else:
        n_clicks_closing_sidebar.append(n_clicks)
        if len(n_clicks_closing_sidebar) % 2 == 0:
            active = sd_open 
        else:
            active = sd_close
    return active

if __name__ == "__main__":
    app.run(debug=True)
