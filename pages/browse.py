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

bot = html.I(className='bi bi-robot', style={'font-size':'180px'}, id='persian-green')
art = html.I(className='bi bi-easel2-fill', style={'font-size':'180px'}, id='persian-green')
audio = html.I(className='bi bi-soundwave', style={'font-size':'180px'}, id='persian-green')
work = html.I(className='bi bi-person-workspace', style={'font-size':'180px'}, id='persian-green')

chatbot_string = 'چت بات'
art_string = 'هنرهای تصویری'
audio_string = 'آوا و موسیقی'
work_string = 'ابزارها'

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.A(bot, href='/chatbot', target='_blank'),
                html.Br(),
                html.A(chatbot_string, href='/chatbot', target='_blank', id='persian-black')
            ], className='col-md-4 col-sm-6', style={'text-align':'center'}),
            dbc.Col([
                
            ], className='col-md-2', style={'text-align':'center'}),
            dbc.Col([
                
            ], className='col-md-2', style={'text-align':'center'}),
            dbc.Col([
                html.A(art, href='/visual-art-generation', target='_blank'),
                html.Br(),
                html.A(art_string, href='/chatbot', target='_blank', id='persian-black')
            ], className='col-md-4 col-sm-6', style={'text-align':'center'}),
        ]),
        dbc.Row([
            dbc.Col([
                html.A(audio, href='/audible-art-generation', target='_blank'),
                html.Br(),
                html.A(audio_string, href='/chatbot', target='_blank', id='persian-black')
            ], className='col-md-4 col-sm-6', style={'text-align':'center'}),
            dbc.Col([
                
            ], className='col-md-2', style={'text-align':'center'}),
            dbc.Col([
                
            ], className='col-md-2', style={'text-align':'center'}),
            dbc.Col([
                html.A(work, href='/', target='_blank'),
                html.Br(),
                html.A(work_string, href='/productivity', target='_blank', id='persian-black')
            ], className='col-md-4 col-sm-6', style={'text-align':'center'}),
        ]),
    ])
])
