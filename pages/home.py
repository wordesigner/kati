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
                html.A(html.I(className='bi bi-card-list'), style={'font-size':'150px'}, href='/browse', target='_self', id='persian-green'),
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
                html.A(html.I(className='bi bi-search'), style={'font-size':'150px'}, href='/search', target='_self', id='persian-green'),
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
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Img(src='https://www.alirezaoboodiat.com/wp-content/uploads/2024/03/1.jpg', width='100%', height='250px'),
                ], className='bg-primary')
            ], style={'padding-right':'0px', 'padding-left':'0px'}, md=2, sm=2, className='mobile-footer footer-big-screen'),
            dbc.Col([
                html.Div([
                    html.Img(src='https://www.alirezaoboodiat.com/wp-content/uploads/2024/03/3.jpg', width='100%', height='250px'),
                ], className='bg-primary')
            ], style={'padding-right':'0px'}, md=2, sm=2, className='element footer-big-screen'),
            dbc.Col([
                html.Div([
                    html.Img(src='https://www.alirezaoboodiat.com/wp-content/uploads/2024/03/4.jpg', width='100%', height='250px'),
                ], className='bg-primary')
            ], style={'padding-right':'0px'}, md=2, sm=2, className='element footer-big-screen'),
            dbc.Col([
                html.Div([
                    html.Img(src='https://www.alirezaoboodiat.com/wp-content/uploads/2024/03/1.jpg', width='100%', height='250px'),
                ], className='bg-primary')
            ], style={'padding-right':'0px'}, md=2, sm=2, className='element footer-big-screen'),
            dbc.Col([
                html.Div([
                    html.Img(src='https://www.alirezaoboodiat.com/wp-content/uploads/2024/03/3.jpg', width='100%', height='250px'),
                ], className='bg-primary')
            ], style={'padding-right':'0px'}, md=2, sm=2, className='element footer-big-screen'),
            dbc.Col([
                html.Div([
                    html.Img(src='https://www.alirezaoboodiat.com/wp-content/uploads/2024/03/4.jpg', width='100%', height='250px'),
                ], className='bg-primary')
            ], style={'padding-right':'0px', 'left-padding':'0px'}, md=2, sm=2, className='element footer-big-screen'),
        ], className='footer-position')
    ], fluid=True, className='g-0')
])
