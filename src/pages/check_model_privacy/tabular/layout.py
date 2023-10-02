import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import callback, Input, Output
from dash import html, dcc
from dash_bootstrap_templates import ThemeSwitchAIO

from src.components import to_styled_roc_plot
from src.components.explanation_card import create_explanation_card
from src.components.graph_card import create_graph_card
# local imports
from src.components.page_header import create_page_header_box
from src.components.responsibility.metrics_to_explanations import get_explanation_text
from src.components.step_progress_bar import create_step_progress_bar

#TODO
# from src.components.privacy.privacy import calc_privacy_score #, perform_mia_on_tabular_data

dash.register_page(
    __name__,
    path='/model-privacy/tabular',
    title='Check Model Privacy'
)

next_step_btn = dbc.Button(
    "next step",
    color="primary",
    href='/model-security/tabular',  # default! changes dynamically if selected
    disabled=False
)
# the page header
page_header = create_page_header_box(
    icon='fa fa-2x fa-lock',
    title='Model Privacy (Tabular)',
    description='Privacy Leakage belongs to the big issues in the AI Landscape. Therefore we check if our model values privacy. ',
    prev_step=None,
    next_step=next_step_btn
)

privacy_roc_plot_tabular = create_graph_card(
    card_type='custom_graph',
    title='Area Under the Curve',
    description='An AUC of 0.6 suggests a level of discrimination that is slightly better than random guessing but is '
                'still generally considered poor. In the context of membership inference attacks, this indicates that '
                'the attack model is not particularly effective at distinguishing between data that was in the '
                'training set (members) and data that was not (non-members).',
    card_id='privacy_roc_plot_tabular')


explanation = create_explanation_card(
    card_title='Membership Inference Attack Performance',
    explanation='The metric used here is "Area Under the Curve (AUC)" calculated using FPR and TPR and refers to the probability with which an attacker '
                ' can determine the membership of a data point in the data set used to train the model. ',
    metric_result='mia_results_tabular',
    metric_explanation='metric_explanation_tabular',
    image_name='membership_inference'
)

loading_privacy_content = dcc.Loading([
    dbc.Row(
        [
            dbc.Col(
                explanation,
                width=12,
                className="mb-4",
            ),
            dbc.Col(
                privacy_roc_plot_tabular,
                width=12,
                className="mb-4",
            ),

        ]),
],
    type="circle",
    id="loading-5"
)

layout = dbc.Container([
    create_step_progress_bar(["Start", "Lifecycle", "Use Case", "Data Analysis", "Test Settings", "Fairness", "Privacy", "Security", "Explainability", "Results"], 6),
    page_header,
    loading_privacy_content
])


@callback(
    Output('privacy_roc_plot_tabular', 'figure'),
    Output('mia_results_tabular', 'children'),
    Output('metric_explanation_tabular', 'children'),
    Output('privacy_score_tabular', 'data'),

    Input('model_type', 'data'),
    Input('dataset_size', 'data'),
    Input('selected_model', 'data'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value")
)
def update_selected(model_type, dataset_size, selected_model, theme_switch):
    print(model_type)

    if model_type is None:
        return dash.no_update
    else:
        template = "cosmo" if theme_switch else "superhero"

        result_df = pd.read_csv("components/privacy/privacy_art/results_tabular.csv")

        auc = result_df.AUC[0]
        attack_name = result_df.attack_name[0]
        fpr = result_df.FPR
        tpr = result_df.TPR
        membership_inference_metric = str(round(auc, 2))
        roc_plot = to_styled_roc_plot(template, fpr, tpr, membership_inference_metric, attack_name)

        privacy_score = 8 # static

        metric_explanation = get_explanation_text(privacy_score, 'privacy')
        privacy_metric_ui = str(membership_inference_metric) + " (" + str(privacy_score) + "/10)"

        return roc_plot, privacy_metric_ui, metric_explanation, privacy_score
