from dash import html, Dash, page_registry, page_container, callback, Input, Output, callback_context
import dash_bootstrap_components as dbc

app = Dash(__name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

n_clicks_closing_sidebar = []

server = app.server

sidebar = html.Div([
    html.Div(children=[html.Img(src='assets/img/logo-univ-rennes.png', className="logo")]),
    html.Hr(),
    dbc.Nav(
        children=[
            dbc.NavLink(
                children=[html.Div(page["name"], className="ms-6")],
                href=page["path"],
                active="exact"
            )
            for page in page_registry.values()
        ],
        vertical=True,
        pills=True)
], id='sidebar', className='sidebar')

sidebar_closed = html.Div(id='sidebar', className='sidebarClose')

content = html.Div([
    dbc.Button("llll", color = "primary", id = "closing-sidebar"),
    
    html.Div([
        page_container
    ])
], id='body', className='body')


app.layout = html.Div([sidebar, content], id="app")

sd_open = [[sidebar, content],"sidebar","body"]
sd_close = [[sidebar_closed, content],"sidebarClose","bodyFull"]


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
