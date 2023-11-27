from dash import Dash, dcc, html, callback, Input, Output, State, register_page
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

register_page(__name__,
    name='Code'
)


#------------------------------------------------------------#
# 1. INITIALISATION                                          #
#------------------------------------------------------------#



#------------------------------------------------------------#
# 2. INTERFACE                                               #
#------------------------------------------------------------#

layout = html.Div([
    
    dmc.Prism(
        children=
            """@requires_authorization
            def somefunc(param1='', param2=0):
            r'''A docstring'''
            
            if param1 > param2: # interesting
                print 'Greater'
                return (param2 - param1 + 1 + 0b10l) or None
            
            class SomeClass:
                pass
            
            >>> message = '''interpreter
            ... prompt'''""",
        language="python",
        colorScheme="dark"
)


])

