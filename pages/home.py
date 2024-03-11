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
                html.Div(html.I(className='bi bi-card-list'), style={'font-size':'200px'}),
                dbc.Col([
                    
                ], className='col'),
                dbc.Col([
                    html.P('فهرست ابزار')
                ], className='col'),
                dbc.Col([
                    
                ], className='col'),
            ], className='col', style={'text-align':'center'}),
            dbc.Col([
                
            ], className='col', style={'text-align':'center'}),
            dbc.Col([
                
            ], className='col', style={'text-align':'center'}),
            dbc.Col([
                html.Div(html.I(className='bi bi-search'), style={'font-size':'200px'}),
                dbc.Col([
                    
                ], className='col' ,style={'text-align':'center'}),
                dbc.Col([
                    html.P('جستجو')
                ], className='col' ,style={'text-align':'center'}),
                dbc.Col([
                    
                ], className='col' ,style={'text-align':'center'}),
            ], className='col')
        ]),
    ]),
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Img(src='https://www.alirezaoboodiat.com/wp-content/uploads/2024/03/1.jpg', width='100%', height='250px'),
                ], className='bg-primary')
            ], style={'padding-right':'0px'}, md=2, sm=2),
            dbc.Col([
                html.Div([
                    html.Img(src='https://www.alirezaoboodiat.com/wp-content/uploads/2024/03/3.jpg', width='100%', height='250px'),
                ], className='bg-primary')
            ], style={'padding-right':'0px'}, md=2, sm=2, className='element'),
            dbc.Col([
                html.Div([
                    html.Img(src='https://www.alirezaoboodiat.com/wp-content/uploads/2024/03/4.jpg', width='100%', height='250px'),
                ], className='bg-primary')
            ], style={'padding-right':'0px'}, md=2, sm=2, className='element'),
            dbc.Col([
                html.Div([
                    html.Img(src='https://www.alirezaoboodiat.com/wp-content/uploads/2024/03/1.jpg', width='100%', height='250px'),
                ], className='bg-primary')
            ], style={'padding-right':'0px'}, md=2, sm=2, className='element'),
            dbc.Col([
                html.Div([
                    html.Img(src='https://www.alirezaoboodiat.com/wp-content/uploads/2024/03/3.jpg', width='100%', height='250px'),
                ], className='bg-primary')
            ], style={'padding-right':'0px'}, md=2, sm=2, className='element'),
            dbc.Col([
                html.Div([
                    html.Img(src='https://www.alirezaoboodiat.com/wp-content/uploads/2024/03/4.jpg', width='100%', height='250px'),
                ], className='bg-primary')
            ], style={'padding-right':'0px'}, md=2, sm=2, className='element'),
        ], style={'margin-top':'132px'})
    ], fluid=True, className='g-0')
])
