import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
from dash import dcc
from dash import html
from dash import register_page
from dash import callback

register_page(
    __name__
)

a = html.I(className='bi bi-circle-fill', style={'font-size':'200px'})

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.A(a, href='/chatbot', target='_blank')
            ], className='col-md-4 col-sm-6', style={'text-align':'center'}),
            dbc.Col([
                
            ], className='col-md-2', style={'text-align':'center'}),
            dbc.Col([
                
            ], className='col-md-2', style={'text-align':'center'}),
            dbc.Col([
                html.A(a, href='/visual-art-generation', target='_blank')                
            ], className='col-md-4 col-sm-6', style={'text-align':'center'}),
        ]),
        dbc.Row([
            dbc.Col([
                html.A(a, href='/audible-art-generation', target='_blank')
            ], className='col-md-4 col-sm-6', style={'text-align':'center'}),
            dbc.Col([
                
            ], className='col-md-2', style={'text-align':'center'}),
            dbc.Col([
                
            ], className='col-md-2', style={'text-align':'center'}),
            dbc.Col([
                html.A(a, href='/', target='_blank')                
            ], className='col-md-4 col-sm-6', style={'text-align':'center'}),
        ]),
    ])
])