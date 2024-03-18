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

ttsmaker_title = 'تی تی اس میکر'
ttsmaker_subtitle = ''
ttsmaker_desc = 'با بیشتر از 200 صدای مختلف، متن ورودی را به گفتار تبدیل می‌کند'
ttsmaker_access = 'رایگان'
ttsmaker_link = 'https://ttsmaker.com/'
ttsmaker_tag = 'ttsmaker'

moisesai_title = 'مویزز'
moisesai_subtitle = 'Audio Intelligence Platform'
moisesai_desc = 'این اپلیکیشن هوش مصنوعی ابزارهای مختلفی مثل حذف صدا، تغییر تنالیته و ترکیب آهنگ‌ها را فراهم می‌کند'
moisesai_access = 'رایگان و پولی'
moisesai_link = 'https://moises.ai/'
moisesai_tag = 'moises'

stableaudio_title = 'استیبل آیودیو'
stableaudio_subtitle = 'Stability AI'
stableaudio_desc = 'این سرویس می‌تواند با توصیف سازها و جزییات فنی، یک آهنگ کامل را تولید کند'
stableaudio_access = 'رایگان و پولی'
stableaudio_link = 'https://www.stableaudio.com/' 
stableaudio_tag = 'stableaudio'

suno_title = 'سونو ای آی'
suno_subtitle = ''
suno_desc = 'یک ابزار جالب برای ساخت آهنگ با بیت‌ها و سبک‌های مختلف در زبان‌های مختلف است'
suno_access = 'رایگان و پولی'
suno_link = 'https://suno.ai'
suno_tag = 'Suno Ai'

musicfy_title = 'موزیکفای'
musicfy_subtitle = ''
musicfy_desc = 'ابزاری که می‌تواند آهنگ خوانده شده توسط یک خوانده را با صدای شخص دیگری باز تولید کند'
musicfy_access = 'رایگان و پولی'
musicfy_link = 'https://musicfy.lol'
musicfy_tag = 'Musicfy'


layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(ttsmaker_title),
                    html.H5(ttsmaker_subtitle),
                    html.P(ttsmaker_desc),
                    html.Hr(),
                    html.H6(ttsmaker_access),
                    html.A('امتحان می‌کنم', href=ttsmaker_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(ttsmaker_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(moisesai_title),
                    html.H5(moisesai_subtitle),
                    html.P(moisesai_desc),
                    html.Hr(),
                    html.H6(moisesai_access),
                    html.A('امتحان می‌کنم', href=moisesai_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(moisesai_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(stableaudio_title),
                    html.H5(stableaudio_subtitle),
                    html.P(stableaudio_desc),
                    html.Hr(),
                    html.H6(stableaudio_access),
                    html.A('امتحان می‌کنم', href=stableaudio_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(stableaudio_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(suno_title),
                    html.H5(suno_subtitle),
                    html.P(suno_desc),
                    html.Hr(),
                    html.H6(suno_access),
                    html.A('امتحان می‌کنم', href=suno_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(suno_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(musicfy_title),
                    html.H5(musicfy_subtitle),
                    html.P(musicfy_desc),
                    html.Hr(),
                    html.H6(musicfy_access),
                    html.A('امتحان می‌کنم', href=musicfy_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(musicfy_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
    ], className='browse-overflow', style={'margin-bottom':'70px', 'padding-right':'37px'})
])
