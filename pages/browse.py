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

bot = html.I(className='bi bi-robot', style={'font-size':'200px'})
art = html.I(className='bi bi-easel2-fill', style={'font-size':'200px'})
audio = html.I(className='bi bi-soundwave', style={'font-size':'200px'})
work = html.I(className='bi bi-person-workspace', style={'font-size':'200px'})

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.A(bot, href='/chatbot', target='_blank'),
                html.Br(),
                html.P('چت بات')
            ], className='col-md-4 col-sm-6', style={'text-align':'center'}),
            dbc.Col([
                
            ], className='col-md-2', style={'text-align':'center'}),
            dbc.Col([
                
            ], className='col-md-2', style={'text-align':'center'}),
            dbc.Col([
                html.A(art, href='/visual-art-generation', target='_blank'),
                html.Br(),
                html.P('هنر')                
            ], className='col-md-4 col-sm-6', style={'text-align':'center'}),
        ]),
        dbc.Row([
            dbc.Col([
                html.A(audio, href='/audible-art-generation', target='_blank'),
                html.Br(),
                html.P('آوا و موسیقی')  
            ], className='col-md-4 col-sm-6', style={'text-align':'center'}),
            dbc.Col([
                
            ], className='col-md-2', style={'text-align':'center'}),
            dbc.Col([
                
            ], className='col-md-2', style={'text-align':'center'}),
            dbc.Col([
                html.A(work, href='/', target='_blank'),
                html.Br(),
                html.P('کار و پروژه')                 
            ], className='col-md-4 col-sm-6', style={'text-align':'center'}),
        ]),
    ])
])
