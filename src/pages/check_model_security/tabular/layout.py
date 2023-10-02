# Model Settings Page

# Import Libraries
import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import callback, Input, Output
from dash import html, dcc
from dash_bootstrap_templates import ThemeSwitchAIO
import plotly.graph_objects as go

from src.components import create_graph_card, create_explanation_card, get_explanation_text
# local imports
from src.components.page_header import create_page_header_box
from src.components.step_progress_bar import create_step_progress_bar

## TODO
# from src.components.security.security import calc_security_score #, adversarial_attack_on_tabular_data

dash.register_page(
    __name__,
    path='/model-security/tabular',
    title='Check Model Security (Tabular)'
)

next_step_btn = dbc.Button(
    "next step",
    color="primary",
    href='/model-explainability/tabular',
    disabled=False
)
page_header = create_page_header_box(
    icon='fa fa-2x fa-shield-halved',
    title='Model Security (Tabular)',
    description='Secure is defined as robust against any kind of attacks.',
    prev_step=None,
    next_step=next_step_btn
)

robustness_attack_tabular = create_graph_card(
    card_type='custom_graph',
    title='Adversarial Examples',
    description='The visualization, as seen in the image, displays features such as age versus maximum heart rate, '
                'with the black lines representing the difference vectors between the original and modified data '
                'points. These difference vectors help users better comprehend how adversarial attacks manipulate the '
                'data to potentially mislead the model.',
    card_id='robustness_attack_tabular')

explanation = create_explanation_card(
    card_title='Adversarial Attack Robustness',
    explanation='This tests your model with perturbed input data to see if it robust against malicious attacks. '
                'The robustness of a model is evaluated as classification accuracy on the corrupted input. ',
    metric_result='image_robustness_results_tabular',
    metric_explanation='sec_metric_explanation_tabular',
    image_name='adversarial_attack'
)


loading_security_content = dcc.Loading([
    dbc.Row(
        [
            dbc.Col(
                explanation,
                width=12,
                className="mb-4",
            ),
            dbc.Col([
                robustness_attack_tabular,
            ],
                width=8,
                className="mb-4",
            ),

        ]),
],
    type="circle",
    id="loading-5"
)

layout = dbc.Container([
    create_step_progress_bar(
        ["Start", "Lifecycle", "Use Case", "Data Analysis", "Test Settings", "Fairness", "Privacy", "Security",
         "Explainability", "Results"], 7),
    page_header,
    loading_security_content
])


@callback(
    Output('robustness_attack_tabular', 'figure'),
    Output('image_robustness_results_tabular', 'children'),
    Output('sec_metric_explanation_tabular', 'children'),
    Output('security_score_tabular', 'data'),

    Input('model_type', 'data'),
    Input('dataset_size', 'data'),
    Input('selected_model', 'data'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value")
)
def update_selected(model_type, dataset_size,selected_model, theme_switch):
    print(model_type)

    if model_type is None:
        return dash.no_update

    elif model_type:
        template = "cosmo" if theme_switch else "superhero"

        # load static files
        df_merged = pd.read_csv("components/security/security_art/df_merged.csv")
        df_adv_merged = pd.read_csv("components/security/security_art/df_adv_merged.csv")
        score = 0.8

        df_merged.target_name = df_merged["target"].apply(lambda x: "Healthy" if x == 0 else "Heart Patient")
        df_adv_merged.target_name = df_adv_merged["target"].apply(lambda x: "Healthy" if x == 0 else "Heart Patient")

        symbols = []
        for x in range(dataset_size):
            symbols.append('x')
        scatterplot = go.Figure()

        for i in range(dataset_size):
            if df_merged.thalach[i] != df_merged.age[i] or df_adv_merged.thalach[i] != df_adv_merged.age[i]:
                scatterplot.add_trace(go.Scatter(x=[df_merged.thalach[i], df_adv_merged.thalach[i]],
                                                 y=[df_merged.age[i], df_adv_merged.age[i]],
                                                 mode='lines',
                                                 showlegend=False,
                                                 line=dict(color='black')))

        scatterplot.add_trace(
            go.Scatter(x=df_adv_merged.thalach,
                       y=df_adv_merged.age,
                       mode='markers',
                       marker_symbol=symbols,
                       #marker_size=8,
                       text=df_adv_merged.target_name,
                       showlegend=False,
                       marker=dict(
                           color=df_adv_merged.target,
                           colorscale=['red', 'darkred'],
                           line_width=0
                       )
                       ),
        )
        scatterplot.add_trace(
            go.Scatter(x=df_merged.thalach,
                       y=df_merged.age,
                       mode='markers',
                       #marker_size=8,
                       text=df_merged.target_name,
                       showlegend=False,
                       marker=dict(
                           color=df_merged.target,
                           colorscale=['lightblue', 'blue'],
                           line_width=0
                       )
                       ),
        )
        scatterplot.update_xaxes(title_text="Max. Heart Rate")
        scatterplot.update_yaxes(title_text="Age")
        scatterplot.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False),
            height=500,
            title_text="Adversarial Examples (Zeroth Order Optimization Attack)",
            template=template,
          )


        # security_score = calc_security_score(score)
        security_score = 8

        adv_robust_metric = str(round(score, 2))
        metric_explanation = get_explanation_text(security_score, 'security')
        privacy_metric_ui = str(adv_robust_metric) + " (" + str(security_score) + "/10)"

        return scatterplot, privacy_metric_ui, metric_explanation, security_score
