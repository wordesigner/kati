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
ideamap_desc = 'یک ابزار جالب برای اجرای جلسه‌های طوفان فکری است که با هوش مصنوعی کیفیت و سرعت برگزاری این جلسه‌ها را افزایش می‌دهد'
ideamap_access = 'پولی و رایگان'
ideamap_link = 'https://ideamap.ai/'
ideamap_tag = 'ideamap'

aidetector_title = 'ای آی دیتکتر'
aidetector_subtitle = ''
aidetector_desc = 'ممکن است شما تولید یک محتوا را سفارش داده باشید. این ابزار متن تولید شده را بررسی می‌کند و به شما می‌گوید که با هوش مصنوعی تولید شده است یا خیر'
aidetector_access = 'پولی و رایگان'
aidetector_link = 'https://undetectable.ai/'
aidetector_tag = 'undetectable'

perplexity_title = 'پرپلکسیتی'
perplexity_subtitle = 'Perplexity AI'
perplexity_desc = 'این یک موتور جستجو است با این تفاوت که نتایج را برای شما خلاصه می‌کند و در یک قالب کاربر پسند به شما ارائه می‌دهد. اینجا خبری از لینک‌ها نیست، به جستجوی شما پاسخ داده می‌شود'
perplexity_access = 'پولی و رایگان'
perplexity_link = 'https://www.perplexity.ai/'
perplexity_tag = 'perplexity'


layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(vana_title),
                    html.H5(vana_subtitle),
                    html.P(vana_desc),
                    html.Hr(style={'margin-right':'1rem', 'margin-left':'1rem'}),
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
                    html.Hr(style={'margin-right':'1rem', 'margin-left':'1rem'}),
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
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(aidetector_title),
                    html.H5(aidetector_subtitle),
                    html.P(aidetector_desc),
                    html.Hr(style={'margin-right':'1rem', 'margin-left':'1rem'}),
                    html.H6(aidetector_access),
                    html.A('امتحان می‌کنم', href=aidetector_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(aidetector_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(perplexity_title),
                    html.H5(perplexity_subtitle),
                    html.P(perplexity_desc),
                    html.Hr(style={'margin-right':'1rem', 'margin-left':'1rem'}),
                    html.H6(perplexity_access),
                    html.A('امتحان می‌کنم', href=perplexity_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(perplexity_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
       
    ], style={'margin-bottom':'70px', 'padding-right':'37px'})
])
