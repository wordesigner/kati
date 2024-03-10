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
                html.Div(html.I(className='bi bi-circle-fill'), style={'font-size':'100px'})
            ], className='col-md-3 col-sm-6'),
            dbc.Col([
                html.Div(html.I(className='bi bi-circle-fill'), style={'font-size':'100px'})
            ], className='col-md-3 col-sm-6')
        ]),
    ]),
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    dbc.Carousel(
                        items=[
                            {'key':'1', 'src':'https://www.alirezaoboodiat.com/wp-content/uploads/2024/03/spectrum.jpg'},

                        ], ride='carousel', variant='dark'
                    )
                ], className='bg-primary')
            ], style={'padding-right':'0px'})
        ])
    ], fluid=True, className='g-0')
])