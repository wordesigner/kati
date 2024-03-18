import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
from dash import dcc
from dash import html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP], use_pages=True, suppress_callback_exceptions=True, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1", 'charset':'UTF-8'}])
server = app.server
app.title = 'کتی؛ دستیار جیبی هوش مصنوعی'

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
                        dbc.NavItem(dbc.NavLink('پرامپت‌ها', href='/')), dbc.Badge('به زودی', color='red', className='mobile-badge big-badge')

                    ], brand='کتی', brand_href='/', color='#00a693', dark=True, style={'padding-right':'0px'}
                )
            ], style={'padding-right':'0px', 'padding-left':'0px'})
        ])
    ], fluid=True, className='g-0 main'),
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Navbar(
                    children=[
                        #dbc.NavItem(dbc.NavLink('خانه', href='/')),
                        dbc.NavItem(dbc.NavLink('کتی؛ دستیار جیبی هوش مصنوعی', style={'padding-right':'88px', 'color':'#8cd7ce'})),
                    ], color='#00a693', dark=True, style={'padding-right':'0px', 'height':'45px'}
                )
            ], style={'padding-right':'0px', 'padding-left':'0px'})
        ])
    ], fluid=True, className='g-0', style={'position':'fixed', 'bottom':'0px', 'z-index':'1'}),
    dash.page_container
], style={'direction':'rtl'}, lang='fa')

if __name__ == '__main__':
    app.run_server(debug=True)
