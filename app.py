import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
from dash import dcc
from dash import html

"""
external_stylesheets = [
    {  "href": "/customstyle.css"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
    dbc.themes.BOOTSTRAP,
    dbc.icons.BOOTSTRAP
]
"""

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP], use_pages=True, suppress_callback_exceptions=True)

app.layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.NavbarSimple(
                    children=[
                        dbc.NavItem(dbc.NavLink('خانه', href='/')),
                        dbc.NavItem(dbc.NavLink('دسته‌ها', href='/browse')),
                        dbc.NavItem(dbc.NavLink('جستجو', href='/search')),
                        dbc.NavItem(dbc.NavLink('تولید متن', href='/chatbot')),
                        dbc.NavItem(dbc.NavLink('تولید تصویر', href='/visual-art-generation')),
                        dbc.NavItem(dbc.NavLink('تولید ویدیو', href='/text-to-video')),
                        dbc.NavItem(dbc.NavLink('تولید صدا', href='/audible-art-generation')),
                        dbc.NavItem(dbc.NavLink('درباره ما', href='/about')),
                        dbc.NavItem(dbc.NavLink('پرامپت‌ها', href='/prompts'))

                    ], brand='کتی', brand_href='/', color='danger', dark=True
                )
            ], style={'padding-right':'0px'})
        ])
    ], fluid=True, className='g-0'),
    dash.page_container
], style={'direction':'rtl'})

if __name__ == '__main__':
    app.run_server(debug=True)