import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
from dash import dcc
from dash import html
from dash import register_page
from dash import callback

register_page(
    __name__
)

katiData = [
    {
        'title': 'چت جی پی تی',
        'subtitle': 'OpenAi',
        'desc': 'چت جی پی تی، امکانی برای چت کردن با هوش مصنوعی است که بر اساس یک مدل زبانی بزرگ به وجود آمده است',
        'access': 'رایگان و پولی',
        'link': 'https://chat.openai.com/',
        'tag': 'chatgpt'
    },
    {
        'title': 'جمینای',
        'subtitle': 'Google',
        'desc': 'جمینای بر اساس یک مدل چندگانه زبانی ایجاد شده و با قابلیت‌های هوش مصنوعی به پرسش‌های کاربران پاسخ می‌دهد',
        'access': 'رایگان',
        'link': 'https://gemini.google.com',
        'tag': 'gemini'
    },
    {
        'title' : 'کوپایلوت',
        'subtitle' : 'Microsoft',
        'desc' : 'این چت بات به طیف وسیعی از پرسش‌ها و درخواست‌ها جواب مثبت می دهد و روی سیستم‌های اندروید و ویندوز قابل دسترس است',
        'access' : 'رایگان و پولی',
        'link' : 'https://copilot.microsoft.com/',
        'tag' : 'copilot'
    },
    {
        'title' : 'چت پی دی اف',
        'subtitle' : '',
        'desc' : 'محتوای فایل پی دی اف را تحلیل می‌کند و به پرسش‌های شما در مورد آن پاسخ می‌دهد',
        'access' : 'نیمه رایگان',
        'link' : 'https://www.chatpdf.com/',
        'tag' : 'chatpdf'
    },
    {
        'title' : 'فارادی',
        'subtitle' : 'Ahoy Labs',
        'desc' : 'با استفاده از هوش مصنوعی و بدون نیاز به اینترنت امکان ساخت و تعامل با کارکترهای مختلف را فراهم می‌کند',
        'access' : 'رایگان',
        'link' : 'https://faraday.dev/',
        'tag' : 'faraday'
    },
    {
        'title' : 'چت توب',
        'subtitle' : '',
        'desc' : 'امکان تحلیل و پاسخگویی به پرسش‌ها درباره محتوای فایل‌های ویدیویی یوتوب را دارد',
        'access' : 'نیمه رایگان',
        'link' : 'https://chattube.io/',
        'tag' : 'Chattube'
    },
    {
        'title' : 'چتینگ',
        'subtitle' : '',
        'desc' : 'با استفاده از منابع داده‌ای شما، می‌تواند چت بات های اختصاصی بسازد که در اپلیکیشن های مختلف قابل استفاده است',
        'access' : 'رایگان و پولی',
        'link' : 'https://chatthing.ai/',
        'tag' : 'chat thing'
    },
    {
        'title' : 'پیپل ای آی',
        'subtitle' : 'chatbotkit',
        'desc' : 'این اپلیکیشن با استفاده از پروفایل‌های توییتر برای کاربران چت بات شخصی ایجاد می‌کند که می‌تواند به جای آنها پرسش‌های دیگران را پاسخ دهد. همچنین امکان گفتگو با بسیاری از شخصیت‌های تاریخی را دارد',
        'access' : 'رایگان و پولی',
        'link' : 'https://chatbotkit.com/apps/peopleai',
        'tag' : 'peopleai'
    },
    {
        'title' : 'تی تی اس میکر',
        'subtitle' : '',
        'desc' : 'با بیشتر از 200 صدای مختلف، متن ورودی را به گفتار تبدیل می‌کند',
        'access' : 'رایگان',
        'link' : 'https://ttsmaker.com/',
        'tag' : 'ttsmaker'
    },
    {
        'title' : 'مویزز',
        'subtitle' : 'Audio Intelligence Platform',
        'desc' : 'این اپلیکیشن هوش مصنوعی ابزارهای مختلفی مثل حذف صدا، تغییر تنالیته و ترکیب آهنگ‌ها را فراهم می‌کند',
        'access' : 'رایگان و پولی',
        'link' : 'https://moises.ai/',
        'tag' : 'moises'
    },
    {
        'title' : 'استیبل آیودیو',
        'subtitle' : 'Stability AI',
        'desc' : 'این سرویس می‌تواند با توصیف سازها و جزییات فنی، یک آهنگ کامل را تولید کند',
        'access' : 'رایگان و پولی',
        'link' : 'https://www.stableaudio.com/', 
        'tag' : 'stableaudio'
    },
    {
        'title' : 'سونو ای آی',
        'subtitle' : '',
        'desc' : 'یک ابزار جالب برای ساخت آهنگ به زبان‌ها و سبک‌های مختلف است',
        'access' : 'رایگان و پولی',
        'link' : 'https://suno.ai',
        'tag' : 'Suno Ai'
    },
    {
        'title' : 'موزیکفای',
        'subtitle' : '',
        'desc' : 'ابزاری که می‌تواند یک آهنگ را با صدای هوش مصنوعی باز تولید کند',
        'access' : 'رایگان و پولی',
        'link' : 'https://musicfy.lol',
        'tag' : 'Musicfy'
    },
    {
        'title' : 'دیستیلری',
        'subtitle' : 'followfox',
        'desc' : 'یکی از راهکارهای موثر برای تولید تصاویر از متن بر بستر هوش مصنوعی با استفاده از پارامترهای متنوع است', 
        'access' : 'رایگان',
        'link' : 'https://followfox.ai/',
        'tag' : 'distillery'
    },
    {
        'title' : 'تصویرساز بینگ',
        'subtitle' : 'Bing powered by dall-e3',
        'desc' : 'برای تولید تصویر از متن از جدیدترین قابلیت‌های هوش مصنوعی استفاده می‌کند و امکان اعمال‌ سبک‌های مختلف هنری را نیز دارد',
        'access' : 'رایگان و پولی',
        'link' : 'https://www.bing.com/images/create',
        'tag' : 'bing image creator'
    },
    {
        'title' : 'آیدیوگرام', 
        'subtitle' : '',
        'desc' : 'این ابزار هوش مصنوعی توسط یکی از کارمندان سابق گوگل توسعه داده شده و به خوبی می‌تواند متن‌ها را در قالب تصاویر قرار دهد',
        'access' : 'رایگان و پولی',
        'link' : 'https://ideogram.ai/',
        'tag' : 'Ideogram'
    },
    {
        'title' : 'پیکاسو',
        'subtitle' : 'freepik',
        'desc' : 'قابلیت فوق‌العاده این ابزار تبدیل طرح‌های ساده و اولیه به تصاویر کامل و پیشرفته با کمک هوش مصنوعی است',
        'access' : 'رایگان و پولی',
        'link' : 'https://www.freepik.com/ai/pikaso-ai-drawing',
        'tag' : 'Pikaso'
    },
    {
        'title' : 'اوپن ای آی',
        'subtitle' : '',
        'desc' : 'با استفاده از قابلیت‌های هوش مصنوعی ضمن تولید تصویر، پرامپت‌های پیشنهادی نیز ارائه می‌دهد',
        'access' : 'رایگان',
        'link' : 'https://www.open.ai/',
        'tag' : 'open ai'
    },
    {
        'title' : 'اوپن آرت',
        'subtitle' : '',
        'desc' : 'علاوه بر تولید تصویر از متن و طراحی‌های ساده، امکان ویرایش تصویر و تبدیل تصویر به ویدیو را نیز دارد',
        'access' : 'رایگان و پولی',
        'link' : 'https://openart.ai/',
        'tag' : 'openart'
    },
    {
        'title' : 'کیوریجینالز',
        'subtitle' : 'Arthur Eberie',
        'desc' : 'این سایت یک سرویس جالب را توسعه داده که به کسب و کارها و فریلنسرها کمک می‌کند برای سایت‌‌شان با هوش مصنوعی، کیوآر کد بسازند',
        'access' : 'نیمه رایگان',
        'link' : 'https://www.qriginals.com/',
        'tag' : 'qriginals'
    },
    {
        'title' : 'آن‌استبیلیتی',
        'subtitle' : '',
        'desc' : 'این ابزار تولید تصویر از متن بر اساس مدل استیبل دیفیوژن ساخته شده اما محدودیت‌های این مدل را حذف کرده است',
        'access' : 'رایگان و پولی',
        'link' : 'https://www.unstability.ai/',
        'tag' : 'unstability'
    },
    {
        'title' : 'تاکینگ‌هدز',
        'subtitle' : 'Rosebud AI',
        'desc' : 'پرتره‌های بدون حرکت را به صورت‌های متحرک تبدیل می‌کند که چشمک می‌زنند، آواز می‌خوانند و ...',
        'access' : 'رایگان و پولی',
        'link' : 'https://app.tokkingheads.com/',
        'tag' : 'tokkingheads'
    },
    {
        'title' : 'جنمو',
        'subtitle' : '', 
        'desc' : 'این ابزار از تصاویر ثابت ایجاد شده با هوش مصنوعی ویدیوهای متحرک می‌سازد و امکانات مختلفی برای افزودن زاویه‌های دوربین و افکت‌های متنوع دارد',
        'access' : 'رایگان و پولی',
        'link' : 'https://www.genmo.ai/',
        'tag' : 'genmo'
    },
    {
        'title' : 'فایرفلای',
        'subtitle' : 'adobe', 
        'desc' : 'ادوبی با طیف متنوعی از سبک‌های طراحی امکان تولید تصویر از متن و پیشنهاد پرامپت برای دریافت نتایج بهتر را فراهم کرده است',
        'access' : 'رایگان و پولی',
        'link' : 'https://firefly.adobe.com/',
        'tag' : 'firefly'
    },
    {
        'title' : 'وانا', 
        'subtitle' : 'CORSALI',
        'desc' : 'با این ابزار می‌توانید نماینده، منشی یا دستیار شخصی را داشته باشید که با قابلیت‌های هوش مصنوعی، درست مثل شما با مشتری‌ها تعامل می‌کند',
        'access' : 'پولی',
        'link' : 'https://www.vana.com/',
        'tag' : 'vana'
    },
    {
        'title' : 'آیدیامپ',
        'subtitle' : '',
        'desc' : 'یک ابزار جالب برای اجرای جلسه‌های طوفان فکری است که با هوش مصنوعی قابلیت‌های جدیدی به آن افزوده شده است',
        'access' : 'پولی و رایگان',
        'link' : 'https://ideamap.ai/',
        'tag' : 'ideamap'
    },
    {
        'title' : 'استیو',
        'subtitle' : '',
        'desc' : 'با استفاده از یک پرامپت می‌تواند طیف متنوعی از ویدیوها از جمله انیمیشن و یا ویدیوی زنده را تولید کند',
        'access' : 'پولی و رایگان',
        'link' : 'https://www.steve.ai/',
        'tag' : 'steveai'
    },
    {
        'title' : 'ویدیا',
        'subtitle' : '',
        'desc' : 'این ابزار می‌تواند یک ویدیو بلند را به چند ویدیو کوتاه تبدیل کرده و به آنها عبارت کلیدی اضافه کند',
        'access' : 'پولی و رایگان',
        'link' : 'https://app.vidyo.ai/',
        'tag' : 'vidyo'
    },
    {
        'title' : 'الای',
        'subtitle' : '',
        'desc' : 'این ابزار با استفاده از مجری های ساخته شده از هوش مصنوعی، ویدیوهای تبلیغاتی و آموزشی می‌سازد',
        'access' : 'پولی و رایگان',
        'link' : 'https://elai.io/',
        'tag' : 'elai'
    },
    {
        'title' : 'ای آی دیتکتر',
        'subtitle' : '',
        'desc' : 'ممکن است شما تولید یک محتوا را سفارش داده باشید. این ابزار متن تولید شده را بررسی می‌کند و به شما می‌گوید که با هوش مصنوعی تولید شده است یا خیر',
        'access' : 'پولی و رایگان',
        'link' : 'https://undetectable.ai/',
        'tag' : 'undetectable',
    },
    {
        'title' : 'لکسیکا',
        'subtitle' : '',
        'desc' : 'لکسیکا از پرامپت‌های شما تصویر تولید می‌کند و به شما امکان می‌دهد بر اساس سبک هر تصویر، در میان تصویر‌های مشابه هم جستجو کنید',
        'access' : 'رایگان و پولی',
        'link' : 'https://lexica.art/',
        'tag' : 'lexica',
    },
    {
        'title' : 'لوما',
        'subtitle' : '',
        'desc' : 'ابزارهای تبدیل متن به ویدیو از گروه ابزارهای فوق‌العاده جذاب هوش مصنوعی هستند. ماشین رویاساز لوما از متن ورودی، ویدیو های پنج ثانیه‌ای فوق‌العاده می‌سازد',
        'access' : 'رایگان و پولی',
        'link' : 'https://lumalabs.ai/dream-machine',
        'tag' : 'luma',
    }
]
"""
layout = html.Div([
    dcc.Input(type='text', placeholder='کلمه مورد نظر را وارد کنید...', id='search-input', debounce=False),
    html.Div(id='search-result')
])
"""
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Input(type='text', placeholder='جستجو کنید ...', id='search-input', debounce=False, size='lg', style={'margin-top':'42px'}),
                html.Div(id='search-result', className='result-overflow')
            ], md=6),
            dbc.Col([
                html.P(
                        '''
"من یک مدل زبانی هوش مصنوعی هستم که توسط OpenAI توسعه یافته‌ام. با استفاده از پردازش زبان طبیعی و مدل‌های یادگیری عمیق، می‌توانم به سوالات شما پاسخ دهم، متون را تحلیل کرده و اطلاعات را ارائه کنم. مهارت‌های من شامل موضوعات گوناگونی از فناوری و علم تا هنر و زندگی روزمره می‌شود. هدفم ارائه پاسخ‌های دقیق و مفید برای کمک به شما در یادگیری و اطلاعات‌دهی است."
چت جی پی تی
'''
                    )
            ], className='gpt-intro hide-on-mobile', md=6)
        ])
    ])       
])


@callback(
    Output('search-result', 'children'),
    [Input('search-input', 'value')]
)
def search(search_term):
    if not search_term:
        return ''

    matched_strings = []
    for entry in katiData:
        for key, value in entry.items():
            if isinstance(value, str) and search_term in value:
                matched_strings.append(entry)
                break

    if matched_strings:
        return [
            dbc.Card([
                dbc.CardHeader(item['title'], className='card-title'),
                dbc.CardBody([
                    html.H4(item['subtitle'], className='card-subtitle'),
                    html.P(item['desc'], className='card-text'),
                    html.P(item['access'], className='card-text'),
                ]),
                dbc.CardFooter(dbc.Button('برو اینجا', id='bg-persian-green', href=item['link'], external_link=True, target='_blank', className='border-less'))
            ], className='mb-3') for item in matched_strings
        ]        
    else:
        return html.P('گشتیم نبود، نگردید فعلا نیست')

