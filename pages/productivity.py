import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
from dash import dcc
from dash import html
from dash import register_page
from dash import callback

# This page needs a sorting mechanism <<<

register_page(
    __name__
)

vana_title = 'وانا' 
vana_subtitle = 'CORSALI'
vana_desc = 'با این ابزار می‌توانید نماینده، منشی یا دستیار شخصی را داشته باشید که با قابلیت‌های هوش مصنوعی درست مثل شما با مشتری‌ها تعامل می‌کند'
vana_access = 'پولی'
vana_link = 'https://www.vana.com/'
vana_tag = 'vana'

ideamap_title = 'آیدیامپ'
ideamap_subtitle = ''
ideamap_desc = 'یک ابزار جالب برای اجرای جلسه‌های طوفان فکری است که با هوش مصنوعی قابلیت‌های جدیدی به آن افزوده شده است'
ideamap_access = 'پولی و رایگان'
ideamap_link = 'https://ideamap.ai/'
ideamap_tag = 'ideamap'


layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(vana_title),
                    html.H5(vana_subtitle),
                    html.P(vana_desc),
                    html.Hr(),
                    html.H6(vana_access),
                    html.A('امتحان می‌کنم', href=vana_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(vana_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(ideamap_title),
                    html.H5(ideamap_subtitle),
                    html.P(ideamap_desc),
                    html.Hr(),
                    html.H6(ideamap_access),
                    html.A('امتحان می‌کنم', href=ideamap_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(ideamap_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
       
    ], style={'margin-bottom':'70px', 'padding-right':'37px'})
])
