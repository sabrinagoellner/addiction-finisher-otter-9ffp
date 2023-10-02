# import dash
# from dash import callback, Input, Output
# from dash_bootstrap_templates import ThemeSwitchAIO
# from dash import html, dcc
# import dash_bootstrap_components as dbc
# import numpy as np
# import plotly.graph_objects as go
# from src.components import to_styled_roc_plot
# # local imports
# from src.components.page_header import create_page_header_box
# from src.components.graph_card import create_graph_card
# from src.components.explanation_card import create_explanation_card
# from src.components.privacy.privacy import calc_privacy_score, perform_mia_on_tabular_data, perform_mia_on_nn
# from src.components.responsibility.metrics_to_explanations import get_explanation_text
# from src.components.step_progress_bar import create_step_progress_bar
#
# dash.register_page(
#     __name__,
#     path='/check-model-privacy',
#     title='Check Model Privacy'
# )
#
# # the page header
# page_header = create_page_header_box(
#     icon='fa fa-2x fa-lock',
#     title='Model Privacy',
#     description='Privacy Leakage belongs to the big issues in the AI Landscape. Therefore we check if our model values privacy. ',
#     prev_step='/check-model-fairness',
#     next_step='/check-model-security'
# )
#
# privacy_roc_plot = create_graph_card(
#     card_type='custom_graph',
#     card_id='privacy_roc_plot')
#
#
# explanation = create_explanation_card(
#     card_title='Membership Inference Attack Performance',
#     explanation='The metric used here is "Area Under the Curve (AUC)" calculated using FPR and TPR and refers to the probability with which an attacker '
#                 ' can determine the membership of a data point in the data set used to train the model. '
#                 'An AUC of close to 0.5 means that the attack was not able to identify training samples, which means that the model does not have privacy issues according to this test. '
#                 'Higher values, on the contrary, indicate potential privacy issues.',
#     metric_result='mia_results',
#     metric_explanation='metric_explanation',
#     image_name='membership_inference'
# )
#
# loading_privacy_content = dcc.Loading([
#     dbc.Row(
#         [
#             dbc.Col(
#                 explanation,
#                 width=12,
#                 className="mb-4",
#             ),
#             dbc.Col(
#                 privacy_roc_plot,
#                 width=6,
#                 className="mb-4",
#             ),
#
#         ]),
#     # store the final score in a global variable for the 'level of responsibility'
#     # dcc.Store(id="security_score", data=[], storage_type="session"),
# ],
#     type="circle",
#     id="loading-5"
# )
#
# layout = html.Div([
#     create_step_progress_bar(["Start", "Lifecycle", "Use Case", "Data Analysis", "Test Settings", "Fairness", "Privacy", "Security", "Explainability", "Results"], 6),
#     page_header,
#     loading_privacy_content
# ])
#
#
# @callback(
#     Output('privacy_roc_plot', 'figure'),
#     Output('mia_results', 'children'),  # here we post the result metric as a number next to the explanation
#     Output('metric_explanation', 'children'),  # here we post the result metric as a number next to the explanation
#     # Output('result_all_attacks', 'children'),  # result_all_attacks data table
#     Output('privacy_score', 'data'),
#
#     Input('dataset_choice', 'data'),
#     Input('dataset_size', 'data'),
#     Input(ThemeSwitchAIO.ids.switch("theme"), "value")
# )
# def update_selected(dataset_choice, dataset_size, theme_switch):
#     print(dataset_choice)
#
#     if dataset_choice is None:
#         print("no update privacy")
#         return dash.no_update
#
#     elif dataset_choice:
#         template = "cosmo" if theme_switch else "superhero"
#
#         if dataset_choice == "heart-disease":
#             # on tabular data:
#             result_df = perform_mia_on_tabular_data(dataset_choice,dataset_size)
#             auc = result_df.AUC[0]
#             attack_name = result_df.attack_name[0]
#             fpr = result_df.FPR
#             tpr = result_df.TPR
#             roc_plot = to_styled_roc_plot(template, fpr, tpr, auc, attack_name)
#             privacy_score = calc_privacy_score(auc)
#             membership_inference_metric = str(round(auc, 2))
#             metric_explanation = get_explanation_text(privacy_score, 'privacy')
#
#             return roc_plot, membership_inference_metric, metric_explanation, privacy_score
#
#         else:
#             # mia on image and text neural networks
#             attack_results_population_metric, attack_results_shadow_metric = perform_mia_on_nn(dataset_choice,dataset_size)
#
#             auc_pop = attack_results_population_metric.AUC[0]
#             attack_name_pop = attack_results_population_metric.attack_name[0]
#             fpr_pop = attack_results_population_metric.FPR
#             tpr_pop = attack_results_population_metric.TPR
#
#             auc_shadow = attack_results_shadow_metric.AUC[0]
#             attack_name_shadow = attack_results_shadow_metric.attack_name[0]
#             fpr_shadow = attack_results_shadow_metric.FPR
#             tpr_shadow = attack_results_shadow_metric.TPR
#
#
#             # if we have 2 curves:
#             roc_plot =go.Figure()
#             roc_plot.add_shape(
#                 type='line', line=dict(dash='dash'),
#                 x0=0, x1=1, y0=0, y1=1
#             )
#
#             roc_plot.add_trace(go.Scatter(x=fpr_pop, y=tpr_pop, name=f"{attack_name_pop} (AUC={auc_pop:.2f})", mode='lines'))
#             roc_plot.add_trace(go.Scatter(x=fpr_shadow, y=tpr_shadow, name=f"{attack_name_shadow} (AUC={auc_shadow:.2f})", mode='lines'))
#
#             roc_plot.update_layout(
#                 plot_bgcolor="rgba(0,0,0,0)",
#                 paper_bgcolor='rgba(0,0,0,0)',
#                 xaxis_title='False Positive Rate',
#                 yaxis_title='True Positive Rate',
#                 yaxis=dict(scaleanchor="x", scaleratio=1),
#                 xaxis=dict(constrain='domain'),
#                 height=500,
#                 title_text="Membership Inference Attack Results",
#                 template=template,
#             )
#
#             # taking worst case (highest auc)
#             max_auc = np.max(np.array([auc_pop,auc_shadow]))
#             privacy_score = calc_privacy_score(max_auc)
#             membership_inference_metric = str(round(max_auc, 2))
#             metric_explanation = get_explanation_text(privacy_score, 'privacy')
#
#             return roc_plot, membership_inference_metric, metric_explanation, privacy_score
