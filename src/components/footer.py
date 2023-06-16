from dash import html
import dash_bootstrap_components as dbc
import dash_dangerously_set_inner_html
from dash_bootstrap_templates import ThemeSwitchAIO

light_theme = dbc.themes.COSMO
dark_theme = dbc.themes.SUPERHERO

PROJECT_NAME = 'VERIFAI'

theme_switch = ThemeSwitchAIO(aio_id="theme",
                              themes=[light_theme, dark_theme],
                              icons={"left": "fa fa-moon", "right": "fa fa-sun"}
                              )
footernav = dbc.Nav(
        [
            dbc.NavItem(
                dbc.NavLink(
                    'Index',
                    href='/'
                )
            ),
            dbc.NavItem(
                dbc.NavLink(
                    'Privacy',
                    href='/privacy'
                )
            ),
            dbc.NavItem(
                dbc.NavLink(
                    'Legal Notice',
                    href='/disclaimer'
                )
            ),
        ])

footer = html.Footer(
    dbc.Container(
        [
            html.Hr(),
            dbc.Row([
                dbc.Col(
                    [
                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                                VERIFAI - A Research Project for supporting the development of more Responsible AI-Systems. 
                        '''),
                    ],
                    width=4,
                ),
                dbc.Col(
                    footernav
                ),
                dbc.Col(
                    html.Div(
                        theme_switch
                    ),
                    width=3,
                    className="justify-content-end d-flex"
                ),
            ]),
        ]
    )
)



