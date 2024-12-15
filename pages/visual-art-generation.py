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

luma_title = 'لوما'
luma_subtitle = ''
luma_desc = 'ابزارهای تبدیل متن به ویدیو از گروه ابزارهای فوق‌العاده جذاب هوش مصنوعی هستند. ماشین رویاساز لوما از متن ورودی، ویدیو های پنج ثانیه‌ای فوق‌العاده می‌سازد'
luma_access = 'رایگان و پولی'
luma_link = 'https://lumalabs.ai/dream-machine'
luma_tag = 'luma dream machine'

lexica_title = 'لکسیکا'
lexica_subtitle = ''
lexica_desc = 'لکسیکا از پرامپت‌های شما تصویر تولید می‌کند و به شما امکان می‌دهد بر اساس سبک هر تصویر، در میان تصویر‌های مشابه هم جستجو کنید'
lexica_access = 'رایگان و پولی'
lexica_link = 'https://lexica.art/'
lexica_tag = 'lexica'

distillery_title = 'دیستیلری'
distillery_subtitle = 'followfox'
distillery_desc = 'یکی از راهکارهای موثر برای تولید تصاویر از متن بر بستر هوش مصنوعی با استفاده از پارامترهای متنوع است' 
distillery_access = 'رایگان'
distillery_link = 'https://followfox.ai/'
distillery_tag = 'distillery'

bingimage_title = 'تصویرساز بینگ'
bingimage_subtitle = 'Bing powered by dall-e3'
bingimage_desc = 'برای تولید تصویر از متن از جدیدترین قابلیت‌های هوش مصنوعی استفاده می‌کند و امکان اعمال‌ سبک‌های مختلف هنری را نیز دارد'
bingimage_access = 'رایگان و پولی'
bingimage_link = 'https://www.bing.com/images/create'
bingimage_tag = 'bing image creator'

ideogram_title = 'آیدیوگرام' 
ideogram_subtitle = ''
ideogram_desc = 'این ابزار هوش مصنوعی توسط یکی از کارمندان سابق گوگل توسعه داده شده و به خوبی می‌تواند متن ها در قالب تصاویر قرار دهد'
ideogram_access = 'رایگان و پولی'
ideogram_link = 'https://ideogram.ai/' 
ideogram_tag = 'Ideogram'

pikaso_title = 'پیکاسو'
pikaso_subtitle = 'freepik'
pikaso_desc = 'می‌توانید نقاشی های بسیار ساده و کودکانه‌ای بکشید که با هوش مصنوعی به تصویر های پیشرفته و با جزییات زیاد تبدیل شوند'
pikaso_access = 'رایگان و پولی'
pikaso_link = 'https://www.freepik.com/ai/pikaso-ai-drawing'
pikaso_tag = 'Pikaso'

open_title = 'اوپن ای آی'
open_subtitle = ''
open_desc = 'با استفاده از قابلیت‌های هوش مصنوعی ضمن تولید تصویر از متن، پرامپت‌های پیشنهادی نیز ارائه می‌دهد'
open_access = 'رایگان'
open_link = 'https://www.open.ai/'
open_tag = 'open ai'

openart_title = 'اوپن آرت'
openart_subtitle = ''
openart_desc = 'علاوه بر تولید تصویر از متن و طراحی‌های ساده، امکان ویرایش تصویر و تبدیل تصویر به ویدیو را نیز دارد'
openart_access = 'رایگان و پولی'
openart_link = 'https://openart.ai/'
openart_tag = 'openart'

qriginals_title = 'کیوریجینالز'
qriginals_subtitle = 'Arthur Eberie'
qriginals_desc = 'این سایت یک سرویس جالب را توسعه داده که به کسب و کارها و فریلنسرها کمک می‌کند برای سایت‌‌شان با هوش مصنوعی، کیوآر کد بسازند'
qriginals_access = 'نیمه رایگان'
qriginals_link = 'https://www.qriginals.com/'
qriginals_tag = 'qriginals'

unstability_title = 'آن‌استبیلیتی'
unstability_subtitle = ''
unstability_desc = 'این ابزار تولید تصویر از متن بر اساس مدل استیبل دیفیوژن ساخته شده اما محدودیت‌های این مدل را حذف کرده است'
unstability_access = 'رایگان و پولی'
unstability_link = 'https://www.unstability.ai/'
unstability_tag = 'unstability'

tokkingheads_title = 'تاکینگ‌هدز'
tokkingheads_subtitle = 'Rosebud AI'
tokkingheads_desc = 'پرتره‌های بدون حرکت را به صورت‌های متحرک تبدیل می‌کند که چشمک می‌زنند، آواز می‌خوانند و ...'
tokkingheads_access = 'رایگان و پولی'
tokkingheads_link = 'https://app.tokkingheads.com/'
tokkingheads_tag = 'tokkingheads'

genmo_title = 'جنمو'
genmo_subtitle = '' 
genmo_desc = 'این ابزار از تصاویر ثابت ایجاد شده با هوش مصنوعی ویدیوهای متحرک می‌سازد و امکانات مختلفی برای افزودن زاویه‌های دوربین و افکت‌های مختلف دارد'
genmo_access = 'رایگان و پولی'
genmo_link = 'https://www.genmo.ai/'
genmo_tag = 'genmo'

firefly_title = 'فایرفلای'
firefly_subtitle = 'adobe' 
firefly_desc = 'ادوبی با طیف متنوعی از سبک‌های طراحی امکان تولید تصویر از متن و پیشنهاد پرامپت برای دریافت نتایج بهتر را فراهم کرده است'
firefly_access = 'رایگان و پولی'
firefly_link = 'https://firefly.adobe.com/'
firefly_tag = 'firefly'

steveai_title = 'استیو'
steveai_subtitle = 'Animaker'
steveai_desc = 'با استفاده از یک پرامپت می‌تواند طیف متنوعی از ویدیوها از جمله انیمیشن و یا ویدیوی زنده را تولید کند'
steveai_access = 'پولی و رایگان'
steveai_link = 'app.steve.ai'
steveai_tag = 'Steve ai'

vidyoai_title = 'ویدیا'
vidyoai_subtitle = ''
vidyoai_desc = 'این ابزار می‌تواند یک ویدیو بلند را به چند ویدیو کوتاه تبدیل کرده و به آنها عبارت کلیدی اضافه کند'
vidyoai_access = 'پولی و رایگان'
vidyoai_link = 'https://app.vidyo.ai/'
vidyoai_tag = 'vidyo'

elai_title = 'الای'
elai_subtitle = ''
elai_desc = 'این ابزار با استفاده از مجری های ساخته شده از هوش مصنوعی، ویدیوهای تبلیغاتی و آموزشی می‌سازد' 
elai_access = 'پولی و رایگان'
elai_link = 'https://elai.io/'
elai_tag = 'elai'

grok_title = 'گراک'
grok_subtitle = 'x.ai'
grok_desc = 'با پاسخ‌دهی سریع و با کیفیت بالا، این سرویس هوش مصنوعی به کاربران ایکس (توییتر) امکان می‌دهد متن را به تصویر تبدیل کنند یا تصویر های آپلود شده را تحلیل نمایند' 
grok_access = 'پولی'
grok_link = 'https://x.ai/'
grok_tag = 'grok'

glif_title = 'گلیف'
glif_subtitle = 'Spellcasters'
glif_desc = 'این سرویس تقریبا توانایی هر نوع محتوای به محتوای دستکاری شده با هوش مصنوعی را دارد. اگرچه تجربه کاربری گلیف چندان جالب نیست اما قابلیت‌های چشمگیری در ایجاد تصویر، کمیک، طراحی کارکتر، صداسازی و ساخت ویدیو دارد' 
glif_access = ' پولی و رایگان'
glif_link = 'https://glif.app/glifs'
glif_tag = 'glif'


layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(distillery_title),
                    html.H5(distillery_subtitle),
                    html.P(distillery_desc),
                    html.Hr(style={'margin-right':'1rem', 'margin-left':'1rem'}),
                    html.H6(distillery_access),
                    html.A('امتحان می‌کنم', href=distillery_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(distillery_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(bingimage_title),
                    html.H5(bingimage_subtitle),
                    html.P(bingimage_desc),
                    html.Hr(style={'margin-right':'1rem', 'margin-left':'1rem'}),
                    html.H6(bingimage_access),
                    html.A('امتحان می‌کنم', href=bingimage_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(bingimage_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(ideogram_title),
                    html.H5(ideogram_subtitle),
                    html.P(ideogram_desc),
                    html.Hr(style={'margin-right':'1rem', 'margin-left':'1rem'}),
                    html.H6(ideogram_access),
                    html.A('امتحان می‌کنم', href=ideogram_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(ideogram_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(pikaso_title),
                    html.H5(pikaso_subtitle),
                    html.P(pikaso_desc),
                    html.Hr(style={'margin-right':'1rem', 'margin-left':'1rem'}),
                    html.H6(pikaso_access),
                    html.A('امتحان می‌کنم', href=pikaso_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(pikaso_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(open_title),
                    html.H5(open_subtitle),
                    html.P(open_desc),
                    html.Hr(style={'margin-right':'1rem', 'margin-left':'1rem'}),
                    html.H6(open_access),
                    html.A('امتحان می‌کنم', href=open_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(open_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(openart_title),
                    html.H5(openart_subtitle),
                    html.P(openart_desc),
                    html.Hr(style={'margin-right':'1rem', 'margin-left':'1rem'}),
                    html.H6(openart_access),
                    html.A('امتحان می‌کنم', href=openart_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(openart_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(qriginals_title),
                    html.H5(qriginals_subtitle),
                    html.P(qriginals_desc),
                    html.Hr(style={'margin-right':'1rem', 'margin-left':'1rem'}),
                    html.H6(qriginals_access),
                    html.A('امتحان می‌کنم', href=qriginals_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(qriginals_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(unstability_title),
                    html.H5(unstability_subtitle),
                    html.P(unstability_desc),
                    html.Hr(style={'margin-right':'1rem', 'margin-left':'1rem'}),
                    html.H6(unstability_access),
                    html.A('امتحان می‌کنم', href=unstability_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(unstability_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(tokkingheads_title),
                    html.H5(tokkingheads_subtitle),
                    html.P(tokkingheads_desc),
                    html.Hr(style={'margin-right':'1rem', 'margin-left':'1rem'}),
                    html.H6(tokkingheads_access),
                    html.A('امتحان می‌کنم', href=tokkingheads_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(tokkingheads_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(genmo_title),
                    html.H5(genmo_subtitle),
                    html.P(genmo_desc),
                    html.Hr(style={'margin-right':'1rem', 'margin-left':'1rem'}),
                    html.H6(genmo_access),
                    html.A('امتحان می‌کنم', href=genmo_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(genmo_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(firefly_title),
                    html.H5(firefly_subtitle),
                    html.P(firefly_desc),
                    html.Hr(style={'margin-right':'1rem', 'margin-left':'1rem'}),
                    html.H6(firefly_access),
                    html.A('امتحان می‌کنم', href=firefly_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(firefly_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(steveai_title),
                    html.H5(steveai_subtitle),
                    html.P(steveai_desc),
                    html.Hr(style={'margin-right':'1rem', 'margin-left':'1rem'}),
                    html.H6(steveai_access),
                    html.A('امتحان می‌کنم', href=steveai_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(steveai_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(vidyoai_title),
                    html.H5(vidyoai_subtitle),
                    html.P(vidyoai_desc),
                    html.Hr(style={'margin-right':'1rem', 'margin-left':'1rem'}),
                    html.H6(vidyoai_access),
                    html.A('امتحان می‌کنم', href=vidyoai_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(vidyoai_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(elai_title),
                    html.H5(elai_subtitle),
                    html.P(elai_desc),
                    html.Hr(style={'margin-right':'1rem', 'margin-left':'1rem'}),
                    html.H6(elai_access),
                    html.A('امتحان می‌کنم', href=elai_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(elai_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(lexica_title),
                    html.H5(lexica_subtitle),
                    html.P(lexica_desc),
                    html.Hr(style={'margin-right':'1rem', 'margin-left':'1rem'}),
                    html.H6(lexica_access),
                    html.A('امتحان می‌کنم', href=lexica_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(lexica_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(luma_title),
                    html.H5(luma_subtitle),
                    html.P(luma_desc),
                    html.Hr(style={'margin-right':'1rem', 'margin-left':'1rem'}),
                    html.H6(luma_access),
                    html.A('امتحان می‌کنم', href=luma_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(luma_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(grok_title),
                    html.H5(grok_subtitle),
                    html.P(grok_desc),
                    html.Hr(style={'margin-right':'1rem', 'margin-left':'1rem'}),
                    html.H6(grok_access),
                    html.A('امتحان می‌کنم', href=grok_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(grok_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H2(glif_title),
                    html.H5(glif_subtitle),
                    html.P(glif_desc),
                    html.Hr(style={'margin-right':'1rem', 'margin-left':'1rem'}),
                    html.H6(glif_access),
                    html.A('امتحان می‌کنم', href=glif_link, target='_blank', id='goto', className='vislink'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button('بیشتر بدانید', href='', color='#00a693', size='sm', outline=True),
                        ], md=3, width={'offset':7}),
                        dbc.Col([
                            dbc.Button(glif_tag, color='#00a693', size='sm', outline=True),
                        ], md=2)
                    ])
                ], className='mb-1')
            ], md=6, className='whole-card'),
        ]),
    ], className='vabo', style={'margin-bottom':'70px', 'padding-right':'37px'})
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
