# Model Settings Page

# Import Libraries
import dash
from dash import html, dcc, callback, Input, Output, State
from dash import Dash, html, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

from src.components import create_graph_card
# local imports
from src.components.page_header import create_page_header_box
from src.components.responsibility.metrics_to_explanations import get_explanation_color, get_explanation_text
from src.components.step_progress_bar import create_step_progress_bar

dash.register_page(
    __name__,
    path='/model-responsibility',
    title='Model Responsibility'
)

next_step_btn = dbc.Button(
    "finish",
    color="primary",
    href='/',
    disabled=False
)
# the page header
page_header = create_page_header_box(
    icon='fa fa-2x fa-circle-check',
    title='Model Responsibility Score',
    description='Overall evaluation of all four metrics: Fairness, Privacy leakage, Robustness and Explaianbility.',
    prev_step=None,
    next_step=next_step_btn
)

show_responsibility_chart = create_graph_card(
    card_type='custom_graph',
    card_id='responsibility_rating_output')

responsibility_explanation_card = dbc.Card([
    html.H4("Fairness:"),
    dbc.Alert(color="secondary", id="model_fairness_text", children="..."),
    html.H4("Privacy Leakage:"),
    dbc.Alert(color="secondary", id="model_privacy_text", children="..."),
    html.H4("Robustness:"),
    dbc.Alert(color="secondary", id="model_robustness_text", children="..."),
    html.H4("Explainability:"),
    dbc.Alert(color="secondary", id="model_explainability_text", children="..."),

    html.H4("Level of Responsibility:"),
    dbc.Progress(id="model_responsibility_score", label="", value=0, color="warning", style={"height": "30px", "font-size":"20px"}),
])

disclaimer = dbc.Card([
    dbc.CardHeader("Subjectivity and Limitations of Responsibility Metrics"),
    dbc.CardBody(
        "The final responsibility metrics presented should be considered as individual and subjective evaluations, and it is important to acknowledge the limitations of the current metrics used. It is crucial to note that what may be deemed acceptable or satisfactory for one person might not be for another. Each user's interpretation and assessment of these metrics may vary depending on their context, preferences, and priorities. Furthermore, the existing metrics may not fully capture all aspects of model responsibility, and there could be additional factors that are not considered in the current evaluation. Therefore, it is essential to take into account this subjectivity and the limitations of the metrics when interpreting the overall responsibility score and making informed decisions based on these results.")
])

loading_explainability_content = dcc.Loading([
    dbc.Row(
        [
            dbc.Col([
                show_responsibility_chart
            ],
                width=6,
                className="mb-4",
            ),
            dbc.Col([
                responsibility_explanation_card
            ],
                width=6,
                className="mb-4",
            ),
        ]),
],
    type="circle",
    id="loading_res"
)

layout = dbc.Container([
    create_step_progress_bar(
        ["Start", "Lifecycle", "Use Case", "Data Analysis", "Test Settings", "Fairness", "Privacy", "Security",
         "Explainability", "Results"], 9),
    page_header,
    loading_explainability_content,
    disclaimer
])


@callback(
    Output("responsibility_rating_output", 'figure'),
    Output("model_responsibility_score", 'value'),
    Output("model_responsibility_score", 'label'),
    Output("model_responsibility_score", 'color'),

    Output("model_robustness_text", 'children'),
    Output("model_robustness_text", 'color'),

    Output("model_fairness_text", 'children'),
    Output("model_fairness_text", 'color'),

    Output("model_privacy_text", 'children'),
    Output("model_privacy_text", 'color'),

    Output("model_explainability_text", 'children'),
    Output("model_explainability_text", 'color'),


    # take all of the inputs that are available from the different sores of all models
    # we then look for the model type we have chosen and based on this we can calculate the responsibility score!
    #
    Input('model_type', 'data'),

    Input('fairness_score_tabular', 'data'),
    Input('security_score_tabular', 'data'),
    Input('explainability_score_tabular', 'data'),
    Input('privacy_score_tabular', 'data'),

    Input('fairness_score_nlp', 'data'),
    Input('security_score_nlp', 'data'),
    Input('explainability_score_nlp', 'data'),
    Input('privacy_score_nlp', 'data'),

    Input('fairness_score_img', 'data'),
    Input('security_score_img', 'data'),
    Input('explainability_score_img', 'data'),
    Input('privacy_score_img', 'data'),

)
def update_responsibility_section(
        model_type,

        fairness_score_tabular,
        security_score_tabular,
        explainability_score_tabular,
        privacy_score_tabular,

        fairness_score_nlp,
        security_score_nlp,
        explainability_score_nlp,
        privacy_score_nlp,

        fairness_score_img,
        security_score_img,
        explainability_score_img,
        privacy_score_img
):
    print("model_type ", model_type)

    if model_type:

        if model_type == "tabular":
            fairness_score = fairness_score_tabular
            security_score = security_score_tabular
            explainability_score = explainability_score_tabular
            privacy_score = privacy_score_tabular
        elif model_type == 'nlp':
            fairness_score = fairness_score_nlp
            security_score = security_score_nlp
            explainability_score = explainability_score_nlp
            privacy_score = privacy_score_nlp
        else:
            fairness_score = fairness_score_img
            security_score = security_score_img
            explainability_score = explainability_score_img
            privacy_score = privacy_score_img

        # if we have image or tabular data present
        if type(explainability_score) is int:
            scores = [security_score, explainability_score, fairness_score, privacy_score]
            categories = ['Security', 'Explainability', 'Fairness', 'Privacy']

            print("Results:")
            print("-" * 20)
            print("fairness_score " + str(fairness_score))
            print("security_score " + str(security_score))
            print("explainability_score " + str(explainability_score))
            print("privacy_score " + str(privacy_score))
            print("-" * 20)
            print(scores)
            explainability_text = str(explainability_score) + ": " + get_explanation_text(explainability_score,
                                                                                          'explainability')
            security_text = str(security_score) + ": " + get_explanation_text(security_score, 'security')
            privacy_text = str(privacy_score) + ": " + get_explanation_text(privacy_score, 'privacy')
            fairness_text = str(fairness_score) + ": " + get_explanation_text(fairness_score, 'fairness')

            model_responsibility_score = round(np.mean(scores) * 10,2) # round the averaged score
            model_responsibility_label = str(model_responsibility_score) + "%"
            print("model_responsibility_score: " + str(model_responsibility_score))

            fig = go.Figure()

            fig = px.line_polar({
                str(model_type): scores,
                'direction': categories
            },
                r=str(model_type),
                theta="direction",
                start_angle=360,
                line_close=True,
                text=str(model_type),
            )

            fig.update_traces(textposition='top center', fill='toself')

            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=False,
                        range=[0, 10]
                    )
                ),
                showlegend=False
            )

            return fig, model_responsibility_score, model_responsibility_label, get_explanation_color(
                round(np.mean(scores), 0)), \
                   security_text, get_explanation_color(security_score), \
                   fairness_text, get_explanation_color(fairness_score), \
                   privacy_text, get_explanation_color(privacy_score), \
                   explainability_text, get_explanation_color(explainability_score)

        else:
            scores = [security_score, fairness_score, privacy_score]
            categories = ['Security', 'Fairness', 'Privacy']

            print("Results:")
            print("-" * 20)
            print("fairness_score " + str(fairness_score))
            print("security_score " + str(security_score))
            print("explainability_score " + str(explainability_score))
            print("privacy_score " + str(privacy_score))
            print("-" * 20)

            security_text = str(security_score) + ": " + get_explanation_text(security_score, 'security')
            privacy_text = str(privacy_score) + ": " + get_explanation_text(privacy_score, 'privacy')
            fairness_text = str(fairness_score) + ": " + get_explanation_text(fairness_score, 'fairness')

            model_responsibility_score = round(np.mean(scores) * 10,2) # round the averaged score
            model_responsibility_label = str(model_responsibility_score) + "%"
            print("model_responsibility_score: " + str(model_responsibility_score))

            fig = go.Figure()

            fig = px.line_polar({
                str(model_type): scores,
                'direction': categories
            },
                r=str(model_type),
                theta="direction",
                start_angle=360,
                line_close=True,
                text=str(model_type),
            )

            fig.update_traces(textposition='top center', fill='toself')

            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=False,
                        range=[0, 10]
                    )
                ),
                showlegend=False
            )

            return fig, model_responsibility_score, model_responsibility_label, get_explanation_color(
                round(np.mean(scores), 0)), \
                   security_text, get_explanation_color(security_score), \
                   fairness_text, get_explanation_color(fairness_score), \
                   privacy_text, get_explanation_color(privacy_score), \
                   "None", "light"
