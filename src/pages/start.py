# package imports
import dash
from dash import html, dcc, callback, Input, Output, get_asset_url
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO

from src.components import create_page_header_box
from src.components.step_progress_bar import create_step_progress_bar

dash.register_page(__name__)

prev_step_btn = dbc.Button("back", outline=True, color="primary", href="/", disabled=False)
next_step_btn = dbc.Button(
    "next step",
    id='next_step',
    color="primary",
    href='/select-data',  # changes dynamically
    disabled=False
)
# the page header
card_content = create_page_header_box(
    icon='fa fa-2x fa-info',
    title='VERIFAI- Lifecycle',
    description='We first check the data for different aspects, then we choose the model we want to evaluate for '
                'ethical issues, privacy leakage, security risks and the ability to explain a prediction properly. '
                'Finally, we determine the level of responsibility using the calculated metrics.',
    prev_step=prev_step_btn,
    next_step=next_step_btn
)

layout = dbc.Container(
    dbc.Row(
        [
            create_step_progress_bar(
                ["Start", "Lifecycle", "Use Case", "Data Analysis", "Test Settings", "Fairness", "Privacy", "Security",
                 "Explainability", "Results"], 1),
            dbc.Col(
                card_content,
                width=12,
                className="mb-4  mt-4",
            ),
            dbc.Col(
                id="ds_image",
                width={"size": 8, 'offset': 2},
            ),
        ]
    )
)


@callback(
    Output("ds_image", "children"),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)
def update_graph_theme(toggle):
    light_image = get_asset_url('infographics/lifecycle.svg')
    # dark_image = get_asset_url('infographics/lifecycle_dark.svg')

    # image = dark_image if toggle else light_image

    fig = dbc.CardImg(src=light_image)

    return fig
