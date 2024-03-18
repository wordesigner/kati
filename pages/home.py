import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
from dash import dcc
from dash import html
from dash import register_page
from dash import callback

register_page(
    __name__,
    path='/'
)

layout = html.Div([
    dbc.Container([
        dbc.Row([
            
            dbc.Col([
                html.A(html.I(className='bi bi-card-list'), style={'font-size':'140px'}, href='/browse', target='_self', id='persian-green'),
                dbc.Col([
                    
                ], className='col'),
                dbc.Col([
                    html.A('فهرست ابزارها', href='/browse', target='_self', id='persian-black')
                ], className='col main-page-services'),
                dbc.Col([
                    
                ], className='col'),
            ], className='col mobile-list-icon', style={'text-align':'center'}),
            dbc.Col([
                
            ], className='col', style={'text-align':'center'}),
            dbc.Col([
                
            ], className='col', style={'text-align':'center'}),
            dbc.Col([
                html.A(html.I(className='bi bi-search'), style={'font-size':'140px'}, href='/search', target='_self', id='persian-green'),
                dbc.Col([
                    
                ], className='col' ,style={'text-align':'center'}),
                dbc.Col([
                    html.A('جستجو', href='/search', target='_self', id='persian-black')
                ], className='col main-page-services' ,style={'text-align':'center'}),
                dbc.Col([
                    
                ], className='col' ,style={'text-align':'center'}),
            ], className='col', style={'text-align':'center'})
        ], style={'height':'343px'}),
    ]),
])
        

