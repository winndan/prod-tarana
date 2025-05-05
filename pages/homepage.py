from fasthtml.common import *
from monsterui.all import *

def home():
    return Html(
    Head(
        Meta(charset='UTF-8'),
        Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
        Link(href='https://cdn.jsdelivr.net/npm/remixicon@4.6.0/fonts/remixicon.css', rel='stylesheet'),
        Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css'),
        Link(rel='stylesheet', href='/assets/styles.css'),
        Title('Web Design Mastery | Advanto')
    ),
    Body(
        Nav(
            Div(
                Div(
                    A(
                        Img(src='assets/logo.png', alt='logo'),
                        href='#'
                    ),
                    cls='nav__logo'
                ),
                Div(
                    I(cls='ri-menu-3-line'),
                    id='menu-btn',
                    cls='nav__menu__btn'
                ),
                cls='nav__header'
            ),
            Ul(
                Li(
                    A('Home', href='#home')
                ),
                Li(
                    A('About', href='#about')
                ),
                Li(
                    A('Tours', href='#tour')
                ),
                Li(
                    A('Contacts', href='#contact')
                ),
                Li(
                    Button(
                        'Sign In',
                        Span(
                            I(cls='ri-arrow-right-long-line')
                        ),
                        cls='btn',
                        onclick="window.location.href='/signin';"
                    )
                ),
                id='nav-links',
                cls='nav__links'
            )
        ),
        Header(
            Div(
                Img(src='assets/header.png', alt='header'),
                cls='header__image'
            ),
            Div(
                Img(src='assets/plane.png', alt='plane'),
                H1('Explore The World And Enjoy Your Trip'),
                P("Discover breathtaking destinations and create unforgettable memories\r\n          with Advanto. From scenic landscapes to vibrant cities, your next\r\n          adventure awaits. Let's make your dream trip a reality!", cls='section__description'),
                Form(
                    Div(
                        Label(
                            Span(
                                I(cls='ri-map-pin-line')
                            ),
                            'Location',
                            fr='location'
                        ),
                        Input(type='text', name='location', placeholder='Sahara Desert, Algeria'),
                        cls='input__group'
                    ),
                    Div(
                        Label(
                            Span(
                                I(cls='ri-calendar-line')
                            ),
                            'Date',
                            fr='date'
                        ),
                        Input(type='text', name='location', placeholder='18th, December 2024'),
                        cls='input__group'
                    ),
                    Button(
                        I(cls='ri-search-line'),
                        cls='btn'
                    ),
                    action='/'
                ),
                cls='header__content'
            ),
            id='home',
            cls='section__container header__container'
        ),
        Section(
            Div(
                Div(
                    Img(src='assets/about.jpg', alt='about'),
                    cls='about__image'
                ),
                Div(
                    H2(
                        "It's Time For a",
                        Span('New Adventure!'),
                        "Don't Wait Any Longer.",
                        cls='section__header'
                    ),
                    P("At Advanto, we believe every journey is a story waiting to be told.\r\n            Whether you're seeking the tranquility of nature, the charm of\r\n            historic cities, or the excitement of new cultures, we're here to\r\n            turn your travel dreams into reality. So why wait? Pack your bags,\r\n            step out of your comfort zone, and let Advanto guide you to your\r\n            next great experience!", cls='section__description'),
                    Div('Howard', cls='about__signature'),
                    cls='about__content'
                ),
                cls='section__container about__container'
            ),
            id='about',
            cls='about'
        ),
        Section(
            H3('Tour Type', cls='section__subheader'),
            H2('Pick A Tour Type', cls='section__header'),
            Div(
                Div(
                    Img(src='assets/tour-1.jpg', alt='tour'),
                    H4('Forest Adventures'),
                    P('15 Tours+'),
                    cls='tour__card'
                ),
                Div(
                    Img(src='assets/tour-2.jpg', alt='tour'),
                    H4('Mountain Climbing'),
                    P('10 Tours+'),
                    cls='tour__card'
                ),
                Div(
                    Img(src='assets/tour-3.jpg', alt='tour'),
                    H4('Beach Vacations'),
                    P('18 Tours+'),
                    cls='tour__card'
                ),
                Div(
                    Img(src='assets/tour-4.jpg', alt='tour'),
                    H4('City Tours'),
                    P('12 Tours+'),
                    cls='tour__card'
                ),
                cls='tour__grid'
            ),
            Div(
                Button(
                    'Show All',
                    Span(
                        I(cls='ri-arrow-right-long-line')
                    ),
                    cls='btn'
                ),
                cls='tour__btn'
            ),
            id='tour',
            cls='section__container tour__container'
        ),
        Section(
            Div(
                H3('Top Destination', cls='section__subheader'),
                H2('Our Top Destinations', cls='section__header'),
                Div(
                    Div(
                        Img(src='assets/destination-1.jpg', alt='destination'),
                        Div(
                            H4('Enjoy the tour of the City of Love'),
                            H5('Paris, France'),
                            Div(
                                H6('$2300'),
                                P('(6 days)'),
                                cls='destination__card__footer'
                            ),
                            cls='destination__card__content'
                        ),
                        cls='destination__card'
                    ),
                    Div(
                        Img(src='assets/destination-2.jpg', alt='destination'),
                        Div(
                            H4('Enjoy the tour of paradise with pristine beaches'),
                            H5('Bali, Indonesia'),
                            Div(
                                H6('$1800'),
                                P('(7 days)'),
                                cls='destination__card__footer'
                            ),
                            cls='destination__card__content'
                        ),
                        cls='destination__card'
                    ),
                    Div(
                        Img(src='assets/destination-3.jpg', alt='destination'),
                        Div(
                            H4('Enjoy the tour of luxury and innovation'),
                            H5('Dubai, UAE'),
                            Div(
                                H6('$2500'),
                                P('(5 days)'),
                                cls='destination__card__footer'
                            ),
                            cls='destination__card__content'
                        ),
                        cls='destination__card'
                    ),
                    cls='destination__grid'
                ),
                Div(
                    Button(
                        'Show All',
                        Span(
                            I(cls='ri-arrow-right-long-line')
                        ),
                        cls='btn'
                    ),
                    cls='destination__btn'
                ),
                cls='section__container destination__container'
            ),
            cls='destination'
        ),
        Section(
            Div(
                Img(src='assets/review.png', alt='review'),
                cls='review__image'
            ),
            Div(
                H3('Top Reviews', cls='section__subheader'),
                H2('Our Valuable Clients Say Abour Us', cls='section__header'),
                Div(
                    Div(
                        Div(
                            Div(
                                Span(
                                    I(cls='ri-double-quotes-l')
                                ),
                                P('Advanto made my dream vacation a reality! From the moment I\r\n                  started planning, their team provided excellent\r\n                  recommendations and tailored my itinerary to perfection. Every\r\n                  experience felt personalized, and I loved how seamless the\r\n                  entire journey was.', cls='section__description'),
                                H4('Emily Roberts'),
                                H5('Travel Blogger'),
                                Div(
                                    Span(
                                        I(cls='ri-star-fill')
                                    ),
                                    Span(
                                        I(cls='ri-star-fill')
                                    ),
                                    Span(
                                        I(cls='ri-star-fill')
                                    ),
                                    Span(
                                        I(cls='ri-star-fill')
                                    ),
                                    Span(
                                        I(cls='ri-star-fill')
                                    )
                                ),
                                cls='review__card'
                            ),
                            cls='swiper-slide'
                        ),
                        Div(
                            Div(
                                Span(
                                    I(cls='ri-double-quotes-l')
                                ),
                                P("Exploring new destinations with Advanto was a game-changer. As\r\n                  a photographer, I'm always looking for breathtaking views and\r\n                  unique cultural experiences. Advanto didn't disappoint! From\r\n                  scenic landscapes to vibrant local markets, every destination\r\n                  was a delight to capture.", cls='section__description'),
                                H4('Michael Johnson'),
                                H5('Photographer'),
                                Div(
                                    Span(
                                        I(cls='ri-star-fill')
                                    ),
                                    Span(
                                        I(cls='ri-star-fill')
                                    ),
                                    Span(
                                        I(cls='ri-star-fill')
                                    ),
                                    Span(
                                        I(cls='ri-star-fill')
                                    ),
                                    Span(
                                        I(cls='ri-star-fill')
                                    )
                                ),
                                cls='review__card'
                            ),
                            cls='swiper-slide'
                        ),
                        Div(
                            Div(
                                Span(
                                    I(cls='ri-double-quotes-l')
                                ),
                                P("I've traveled a lot for work, but Advanto gave me the\r\n                  opportunity to enjoy a stress-free vacation. Their attention\r\n                  to detail was remarkable, ensuring everything from airport\r\n                  transfers to guided tours was perfectly arranged. The\r\n                  personalized itinerary was well-balanced with adventure and\r\n                  relaxation!", cls='section__description'),
                                H4('Sophia Lee'),
                                H5('Business Consultant'),
                                Div(
                                    Span(
                                        I(cls='ri-star-fill')
                                    ),
                                    Span(
                                        I(cls='ri-star-fill')
                                    ),
                                    Span(
                                        I(cls='ri-star-fill')
                                    ),
                                    Span(
                                        I(cls='ri-star-fill')
                                    ),
                                    Span(
                                        I(cls='ri-star-fill')
                                    )
                                ),
                                cls='review__card'
                            ),
                            cls='swiper-slide'
                        ),
                        cls='swiper-wrapper'
                    ),
                    cls='swiper'
                ),
                cls='review__content'
            ),
            cls='section__container review__container'
        ),
        Section(
            Div(
                H3('Latest News & Blogs', cls='section__subheader'),
                H2('Our Latest News & Blogs', cls='section__header'),
                Div(
                    Div(
                        Img(src='assets/blog-1.jpg', alt='blog'),
                        Div(
                            H4('Top 10 Must-Visit Destinations for Your Next Adventure'),
                            Button(
                                'Read More',
                                Span(
                                    I(cls='ri-arrow-right-long-line')
                                ),
                                cls='btn'
                            ),
                            cls='blog__content'
                        ),
                        cls='blog__card'
                    ),
                    Div(
                        Img(src='assets/blog-2.jpg', alt='blog'),
                        Div(
                            H4('Travel Smart: Essential Tips for Stress-Free Vacations'),
                            Button(
                                'Read More',
                                Span(
                                    I(cls='ri-arrow-right-long-line')
                                ),
                                cls='btn'
                            ),
                            cls='blog__content'
                        ),
                        cls='blog__card'
                    ),
                    Div(
                        Img(src='assets/blog-3.jpg', alt='blog'),
                        Div(
                            H4('Hidden Gems: Discover Offbeat Locations for Unique Experience'),
                            Button(
                                'Read More',
                                Span(
                                    I(cls='ri-arrow-right-long-line')
                                ),
                                cls='btn'
                            ),
                            cls='blog__content'
                        ),
                        cls='blog__card'
                    ),
                    cls='blog__grid'
                ),
                Div(
                    Button(
                        'Show All',
                        Span(
                            I(cls='ri-arrow-right-long-line')
                        ),
                        cls='btn'
                    ),
                    cls='blog__btn'
                ),
                cls='section__container blog__container'
            ),
            cls='blog'
        ),
        Section(
            Div(
                Img(src='assets/banner-1.jpg', alt='banner'),
                Img(src='assets/banner-2.jpg', alt='banner'),
                Img(src='assets/banner-3.jpg', alt='banner'),
                Img(src='assets/banner-4.jpg', alt='banner'),
                Img(src='assets/banner-5.jpg', alt='banner'),
                Img(src='assets/banner-6.jpg', alt='banner'),
                Img(src='assets/banner-7.jpg', alt='banner'),
                Img(src='assets/banner-8.jpg', alt='banner'),
                cls='banner__wrapper'
            ),
            cls='banner'
        ),
        Footer(
            Div(
                Div(
                    Img(src='assets/logo.png', alt='logo'),
                    cls='footer__logo'
                ),
                Ul(
                    Li(
                        A('Home', href='#home')
                    ),
                    Li(
                        A('About', href='#about')
                    ),
                    Li(
                        A('Tours', href='#tour')
                    ),
                    Li(
                        A('Contacts', href='#contact')
                    ),
                    cls='footer__links'
                ),
                Ul(
                    Li(
                        A(
                            I(cls='ri-facebook-fill'),
                            href='#'
                        )
                    ),
                    Li(
                        A(
                            I(cls='ri-twitter-fill'),
                            href='#'
                        )
                    ),
                    Li(
                        A(
                            I(cls='ri-instagram-line'),
                            href='#'
                        )
                    ),
                    Li(
                        A(
                            I(cls='ri-linkedin-fill'),
                            href='#'
                        )
                    ),
                    cls='footer__socials'
                ),
                cls='section__container footer__container'
            ),
            Div('Copyright © 2025 tarana. All rights reserved.', cls='footer__bar'),
            id='contact'
        ),
        Script(src='https://unpkg.com/scrollreveal'),
        Script(src='https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js'),
        Script(src='/assets/main.js')
    ),
    lang='en'
)