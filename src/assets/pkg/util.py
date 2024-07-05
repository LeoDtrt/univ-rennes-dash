from dash import html, dcc

def boxCode(id, code):
    box_code = html.Div([
        dcc.Markdown(f"```python\n{code}\n```", id=f'{id}-container', className='code-container'),
        dcc.Clipboard(target_id=f'{id}-container', className='copy-button'),
    ], className='box-code')
    return box_code