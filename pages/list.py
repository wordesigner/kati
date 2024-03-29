import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
from dash import dcc
from dash import html
from dash import register_page
from dash import callback

# This page needs a sorting mechanism <<<

register_page(
    __name__
)

gpt_title = 'چت جی پی تی'
gpt_subtitle = 'OpenAi'
gpt_desc = 'چت جی پی تی، امکانی برای چت کردن با هوش مصنوعی است که بر اساس یک مدل زبانی بزرگ ایجاد شده است'
gpt_access = 'رایگان و پولی'
gpt_link = 'https://chat.openai.com/'
gpt_tag = 'chatgpt'

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(gpt_title),
                    html.H5(gpt_subtitle),
                    html.P(gpt_desc),
                    html.Hr(),
                    html.H6(gpt_access),
                    html.A('امتحان می‌کنم', href=gpt_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='/chatgpt', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(gpt_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(gpt_title),
                    html.H5(gpt_subtitle),
                    html.P(gpt_desc),
                    html.Hr(),
                    html.H6(gpt_access),
                    html.A('امتحان می‌کنم', href=gpt_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='/chatgpt', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(gpt_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ])
    ])
])
"""
@callback(
    Output('goto','style'),
    [Input('goto','n_clicks')]
)

def linkHover(n_clicks):
    if n_clicks:
        return {'filter':'blur(3px)'}
    else:
        return {'filter':'blur(0px)'}
"""
