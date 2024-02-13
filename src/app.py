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
], className='sidebar')


content = html.Div([
    
    dbc.Button("llll", color = "primary", id = "closing-sidebar", n_clicks=0),
    
    html.Div([
        page_container
    ])
], className='body')


app.layout = html.Div([sidebar, content], id="app")


@callback(
    Output("app", "children"),
    Input("closing-sidebar","n_clicks")
)
def closing_sidebar(click):
    n_clicks_closing_sidebar.append(click)    
    if len(n_clicks_closing_sidebar) % 2 == 0:
        return [content]
    else:
        return [sidebar, content]


if __name__ == "__main__":
    app.run(debug=True)
