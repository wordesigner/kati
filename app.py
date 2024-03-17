import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
from dash import dcc
from dash import html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP], use_pages=True, suppress_callback_exceptions=True, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
server = app.server

app.layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.NavbarSimple(
                    children=[
                        #dbc.NavItem(dbc.NavLink('خانه', href='/')),
                        dbc.NavItem(dbc.NavLink('دسته‌ها', href='/browse')),
                        dbc.NavItem(dbc.NavLink('جستجو', href='/search')),
                        dbc.NavItem(dbc.NavLink('تولید متن', href='/chatbot')),
                        dbc.NavItem(dbc.NavLink('تولید تصویر و ویدیو', href='/visual-art-generation')),
                        dbc.NavItem(dbc.NavLink('تولید صدا', href='/audible-art-generation')),
                        dbc.NavItem(dbc.NavLink('ابزارها', href='/productivity')),
                        #dbc.NavItem(dbc.NavLink('درباره ما', href='/about')),
                        dbc.NavItem(dbc.NavLink('پرامپت‌ها', href='/prompts'))

                    ], brand='کتی', brand_href='/', color='#00a693', dark=True, style={'padding-right':'0px'}
                )
            ], style={'padding-right':'0px', 'padding-left':'0px'})
        ])
    ], fluid=True, className='g-0'),
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H6('کتی؛ راهنمای جیبی هوش مصنوعی', style={'color':'#8cd7ce','padding-top':'15px','text-align':'right', 'padding-right':'40px'})
                ])
            ], style={'height':'50px'})
        ])
    ], fluid=True, style={'background-color':'#008f7e'}, className='main-footer g-0'),
    dash.page_container
], style={'direction':'rtl'})

if __name__ == '__main__':
    app.run_server(debug=True)
