import dash
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from dash import callback, Input, Output
from dash import html, dcc
from dash_bootstrap_templates import ThemeSwitchAIO

from src.components import create_graph_card, create_explanation_card, get_explanation_text, to_styled_bar_chart #, measure_explanation_on_tabular_data

# local imports
from src.components.page_header import create_page_header_box
from src.components.step_progress_bar import create_step_progress_bar

dash.register_page(
    __name__,
    path='/model-explainability/tabular',
    title='Model Explainability (Tabular)'
)

next_step_btn = dbc.Button(
    "next step",
    color="primary",
    href='/model-responsibility',
    disabled=False
)
# the page header
page_header = create_page_header_box(
    icon='fa fa-2x fa-search',
    title='Model Explainability (Tabular)',
    description='Explainability is the most important feature for users trust in your AI System. ',
    prev_step=None,
    next_step=next_step_btn
)

explainability_graph_tabular = create_graph_card(
    card_type='custom_graph',
    title='Faithfulness Metric',
    description='A high Faithfulness score indicates that LIME is effectively capturing the contribution of each attribute to the models predictions. Values are in range [-1, 1]',
    card_id='explainability_graph_tabular')

plot_explanations_tabular = create_graph_card(
    card_type='custom_graph',
    title='Monotonicity Metric',
    description='The falsy monotonicity shows, it doesnt guarantee that the importance assigned to each attribute '
                'will always be the same across different instances or scenarios.Monotonic explanations are generally '
                'considered more intuitive and easier to understand, as they show a consistent relationship between '
                'the importance of attributes and their impact on the models predictions.',
    card_id='plot_explanations_tabular')

explanation = create_explanation_card(
    card_title='Quantitative Evaluation of Explainability',
    explanation='This tests the model according to its explainability. '
                'In this case, the explaibnability of a model is evaluated using an explainability method and different metrics, which measure the quality. ',
    metric_result='explanation_metric_result_tabular',
    metric_explanation='explanation_metric_explanation_tabular',
    image_name='xai_methods'
)

show_html_explanation_tabular = create_graph_card(
    card_type='html_div',
    title='Single Explanation',
    description='A single LIME explanation.',
    card_id='show_html_explanation_tabular')


loading_explainability_content = dcc.Loading([
    dbc.Row(
        [
            dbc.Col([
                explanation,
            ],
                width=12,
                className="mb-4",
            ),
            dbc.Col([
                show_html_explanation_tabular,
            ],
                width=6,
                className="mb-4",
            ),
            dbc.Col([
                explainability_graph_tabular,
            ],
                width=6,
                className="mb-4",
            ),
            dbc.Col([
                plot_explanations_tabular
            ],
                width=6,
                className="mb-4",
                id="plot_explanations_tabular_container"
            ),
        ]),
],
    type="circle",
    id="loading_exp"
)

layout = dbc.Container([
    create_step_progress_bar(["Start", "Lifecycle", "Use Case", "Data Analysis", "Test Settings", "Fairness", "Privacy", "Security", "Explainability", "Results"], 8),
    page_header,
    loading_explainability_content
])


@callback(
    Output('explainability_graph_tabular', 'figure'),
    Output('plot_explanations_tabular', 'figure'),

    Output('explanation_metric_result_tabular', 'children'),
    Output('explanation_metric_explanation_tabular', 'children'),
    Output('show_html_explanation_tabular', 'children'),
    Output('explainability_score_tabular', 'data'),

    Input('model_type', 'data'),
    Input('dataset_size', 'data'),
    Input('selected_model', 'data'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)
def update_selected(model_type, dataset_size, selected_model, theme_switch):
    print(model_type)

    if model_type is None:
        return dash.no_update

    else:
        template = "cosmo" if theme_switch else "superhero"


        ## load static files:
        single_explanation_faith = 0.47065295082193387
        single_explanation_mono = False
        single_explanation_file = open("assets/plots/explainability/lime/lime_tabular.html", "r")
        single_explanation = single_explanation_file.read()

        monoton_results = np.load("assets/plots/explainability/lime/mon_new.npy",allow_pickle=True)
        faith_results = np.load("assets/plots/explainability/lime/fait_new.npy",allow_pickle=True)
        finalscore = 0.5768808969434545



        explanation = html.Div([
            #html.H4("Single Explanation"),
            html.P("Faithfulness: " + str(single_explanation_faith) +
                   ", Monotonicity: " + str(single_explanation_mono)),
            html.Iframe(
                srcDoc=single_explanation,
                width='100%',
                height='500px',
                style={'color': 'white'},
            )
        ])

        # histogram faithfulness
        bins1 = [-1.0, -0.5, 0, 0.5, 1.0]
        counts, bins2 = np.histogram(faith_results, bins=bins1)
        bins2 = 0.5 * (bins1[:-1] + bins2[1:])

        # specify sensible widths
        widths = []
        for i, b1 in enumerate(bins1[1:]):
            widths.append(b1 - bins2[i])

        # plotly figure
        faith_histo = go.Figure(
            go.Bar(
                x=bins2,
                y=counts,
                width=widths,
                marker=dict(
                    color=counts,
                    colorscale='blues')
            ))

        faith_histo.update_layout(
            #title_text='Distribution of Faithfulness Metric',  # title of plot
            xaxis_title_text='Value',  # xaxis label
            yaxis_title_text='Count',  # yaxis label
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor='rgba(0,0,0,0)'
        )

        faith_histo.add_vline(
            x=np.mean(faith_results),
            line_dash='dash',
            line_color="firebrick",
            annotation_text="mean")

        # monotonicity chart
        columns = ['Monotonicity False', 'Monotonicity True']
        unique, counts = np.unique(monoton_results, return_counts=True)
        zeros = counts[0]
        if len(counts) > 1:
            ones = counts[1]
        else:
            ones = 0
        mono_df = pd.DataFrame([[zeros, ones]], columns=columns)

        mono_barchart = to_styled_bar_chart(mono_df, "Monotonicity", template)

        explainability_score = 6

        explanation_metric_explanation_tabular = get_explanation_text(explainability_score, 'explainability')
        explanation_metric_result_tabular = str(round(finalscore, 2))
        privacy_metric_ui = str(explanation_metric_result_tabular) + " (" + str(explainability_score) + "/10)"

        return faith_histo, mono_barchart, privacy_metric_ui, explanation_metric_explanation_tabular, explanation, explainability_score
