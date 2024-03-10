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

gpt_title = 'چت جی پی تی'
gpt_subtitle = 'OpenAi'
gpt_desc = 'چت جی پی تی، امکانی برای چت کردن با هوش مصنوعی است که بر اساس یک مدل زبانی بزرگ ایجاد شده است'
gpt_access = 'رایگان و پولی'
gpt_link = 'https://chat.openai.com/'
gpt_tag = 'chatgpt'

gemini_title = 'جمینای'
gemini_subtitle = 'Google'
gemini_desc = 'جمینای بر اساس یک مدل چندگانه زبانی ایجاد شده و با قابلیت‌های هوش مصنوعی به پرسش‌های کاربران پاسخ می‌دهد'
gemini_access = 'رایگان'
gemini_link = 'https://gemini.google.com'
gemini_tag = 'gemini'

copilot_title = 'کوپایلوت'
copilot_subtitle = 'Microsoft'
copilot_desc = 'این چت بات به طیف وسیعی از پرسش‌ها و درخواست‌ها جواب مثبت می دهد و روی سیستم‌های اندروید و ویندوز قابل دسترس است'
copilot_access = 'رایگان و پولی'
copilot_link = 'https://copilot.microsoft.com/'
copilot_tag = 'copilot'

chatpdf_title = 'چت پی دی اف'
chatpdf_subtitle = ''
chatpdf_desc = 'محتوای فایل پی دی اف را تحلیل می‌کند و به پرسش‌های شما در مورد آن پاسخ می‌دهد'
chatpdf_access = 'نیمه رایگان'
chatpdf_link = 'https://www.chatpdf.com/'
chatpdf_tag = 'chatpdf'

faraday_title = 'فارادی'
faraday_subtitle = 'Ahoy Labs'
faraday_desc = 'با استفاده از هوش مصنوعی و بدون نیاز به اینترنت امکان ساخت و تعامل با کارکترهای مختلف را فراهم می‌کند'
faraday_access = 'رایگان'
faraday_link = 'https://faraday.dev/'
faraday_tag = 'faraday'

chattube_title = 'چت توب'
chattube_subtitle = ''
chattube_desc = 'امکان تحلیل و پاسخگویی به پرسش‌ها درباره محتوای فایل‌های ویدیویی یوتوب را دارد'
chattube_access = 'نیمه رایگان'
chattube_link = 'https://chattube.io/'
chattube_tag = 'Chattube'

chatthing_title = 'چتینگ'
chatthing_subtitle = ''
chatthing_desc = 'با استفاده از منابع داده‌ای شما، می‌تواند چت بات های اختصاصی بسازد که در اپلیکیشن های مختلف قابل استفاده است'
chatthing_access = 'رایگان و پولی'
chatthing_link = 'https://chatthing.ai/'
chatthing_tag = 'chat thing'

peopleai_title = 'پیپل ای آی'
peopleai_subtitle = 'chatbotkit'
peopleai_desc = 'این اپلیکیشن با استفاده از پروفایل‌های توییتر برای کاربران چت بات شخصی ایجاد می‌کند که می‌تواند به جای آنها پرسش‌های دیگران را پاسخ دهد. همچنین امکان گفتگو با بسیاری از شخصیت‌های تاریخی را دارد'
peopleai_access = 'رایگان وو پولی'
peopleai_link = 'https://chatbotkit.com/apps/peopleai'
peopleai_tag = 'peopleai'


layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(gpt_title),
                    html.H5(gpt_subtitle),
                    html.P(gpt_desc),
                    html.Hr(),
                    html.H6(gpt_access),
                    html.A('امتحان می‌کنم', href=gpt_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(gpt_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(gemini_title),
                    html.H5(gemini_subtitle),
                    html.P(gemini_desc),
                    html.Hr(),
                    html.H6(gemini_access),
                    html.A('امتحان می‌کنم', href=gemini_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(gemini_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(copilot_title),
                    html.H5(copilot_subtitle),
                    html.P(copilot_desc),
                    html.Hr(),
                    html.H6(copilot_access),
                    html.A('امتحان می‌کنم', href=copilot_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(copilot_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(chatpdf_title),
                    html.H5(chatpdf_subtitle),
                    html.P(chatpdf_desc),
                    html.Hr(),
                    html.H6(chatpdf_access),
                    html.A('امتحان می‌کنم', href=chatpdf_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(chatpdf_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(faraday_title),
                    html.H5(faraday_subtitle),
                    html.P(faraday_desc),
                    html.Hr(),
                    html.H6(faraday_access),
                    html.A('امتحان می‌کنم', href=faraday_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(faraday_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(chattube_title),
                    html.H5(chattube_subtitle),
                    html.P(chattube_desc),
                    html.Hr(),
                    html.H6(chattube_access),
                    html.A('امتحان می‌کنم', href=chattube_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(chattube_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(chatthing_title),
                    html.H5(chatthing_subtitle),
                    html.P(chatthing_desc),
                    html.Hr(),
                    html.H6(chatthing_access),
                    html.A('امتحان می‌کنم', href=chatthing_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(chatthing_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(peopleai_title),
                    html.H5(peopleai_subtitle),
                    html.P(peopleai_desc),
                    html.Hr(),
                    html.H6(peopleai_access),
                    html.A('امتحان می‌کنم', href=peopleai_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(peopleai_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
    ])
])
"""
@callback(
    Output('goto','style'),
    [Input('goto','n_clicks')]
)

def linkHover(n_clicks):
    if n_clicks:
        return {'filter':'blur(3px)'}
    else:
        return {'filter':'blur(0px)'}
"""
