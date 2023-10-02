# # Model Settings Page
#
# # Import Libraries
# import dash
# import pandas as pd
# from dash import html, dcc, callback, Input, Output, State, get_asset_url
# from dash import Dash, html, dcc, dash_table
# import dash_bootstrap_components as dbc
# import plotly.express as px
# from dash_bootstrap_templates import ThemeSwitchAIO
# import dash_dangerously_set_inner_html
#
# from src.components import create_graph_card, create_explanation_card, get_explanation_text, to_styled_dict_table, \
#     to_styled_line_chart, to_styled_bar_chart
# # local imports
# from src.components.page_header import create_page_header_box
# from src.components.security.security import adversarial_attack_on_images, calc_security_score, \
#     adversarial_attack_on_text, adversarial_attack_on_tabular_data
# from src.components.step_progress_bar import create_step_progress_bar
#
# dash.register_page(
#     __name__,
#     path='/check-model-security',
#     title='Check Model Security'
# )
#
# # the page header
# page_header = create_page_header_box(
#     icon='fa fa-2x fa-shield-halved',
#     title='Model Security',
#     description='Secure is defined as robust against any kind of attacks.',
#     prev_step='/check-model-privacy',
#     next_step='/check-model-explainability'
# )
#
# robustness_attack = create_graph_card(
#     card_type='custom_graph',
#     card_id='robustness_attack')
#
# table_robustness_attack = create_graph_card(
#     card_type='table',
#     card_id='table_robustness_attack')
#
# explanation = create_explanation_card(
#     card_title='Adversarial Attack Robustness',
#     explanation='This tests your model with perturbed input data to see if it robust against malicious attacks. '
#                 'In this case, the robustness of a model is evaluated as classification accuracy on the corrupted images. ',
#     metric_result='image_robustness_results',
#     metric_explanation='sec_metric_explanation',
#     image_name='adversarial_attack'
# )
#
# image_perturbations = create_graph_card(
#     title="Image Perturbations",
#     description="The images compare added perturbation rates with epsilons of 0.0003, 0.003 and 0.03 (the final metric).",
#     card_type='html_div',
#     card_id='image_perturbations')
#
# loading_security_content = dcc.Loading([
#     dbc.Row(
#         [
#             dbc.Col(
#                 explanation,
#                 width=12,
#                 className="mb-4",
#             ),
#             dbc.Col([
#                 robustness_attack,
#             ],
#                 width=8,
#                 className="mb-4",
#             ),
#             dbc.Col(
#                 image_perturbations,
#                 width=4,
#                 className="mb-4",
#             ),
#             dbc.Col(
#                 table_robustness_attack,
#                 width=12,
#                 className="mb-4",
#             ),
#         ]),
# ],
#     type="circle",
#     id="loading-5"
# )
#
# layout = html.Div([
#     create_step_progress_bar(
#         ["Start", "Lifecycle", "Use Case", "Data Analysis", "Test Settings", "Fairness", "Privacy", "Security",
#          "Explainability", "Results"], 7),
#     page_header,
#     loading_security_content
# ])
#
#
# @callback(
#     Output('robustness_attack', 'figure'),
#     Output('table_robustness_attack', 'children'),
#     Output('image_robustness_results', 'children'),
#     # here we post the result metric as a number next to the explanation
#     Output('sec_metric_explanation', 'children'),  # here we post the result metric as a number next to the explanation
#     Output('security_score', 'data'),
#     Output('image_perturbations','children'),
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
#         # TODO if data_type == 'image':
#         # if dataset_choice == 'alzheimer':
#         #     # we need to load the results statically, since we get errors on M1 chip.
#         #     # It works fine on CUDA therefore we have the results here:
#         #     attack_results = adversarial_attack_on_images(dataset_choice, dataset_size,load_static=True)
#         #     score = attack_results['worst_case'][10]
#         #     plot = to_styled_line_chart(attack_results, "Adversarial Robustness", template, metric=True)
#         #     adv_robust_metric = str(round(score, 2))
#         #     text_attack_stats = None
#         #     security_score = calc_security_score(score)
#         #     metric_explanation = get_explanation_text(security_score, 'security')
#
#         #    return plot, text_attack_stats, adv_robust_metric, metric_explanation, security_score,None
#
#         if dataset_choice == 'skin-cancer':
#             attack_result = adversarial_attack_on_images(dataset_choice, dataset_size, load_static=False)
#             score = attack_result['worst_case'][3]  # test value = 0.03
#             attack_result.drop("worst_case", inplace=True, axis=1)
#             plot = to_styled_line_chart(attack_result, "Adversarial Robustness", template, metric=True)
#             adv_robust_metric = str(round(score, 2))
#             security_score = calc_security_score(score)
#             metric_explanation = get_explanation_text(security_score, 'security')
#             image_perturbations = dbc.CardImg(src=get_asset_url('plots/image_perturbations.png'))
#
#             return plot, None, adv_robust_metric, metric_explanation, security_score, image_perturbations
#
#         # if data = text
#         elif dataset_choice == 'medical-reviews':
#
#             attack_result, attacker_examples, best_attack_stats = adversarial_attack_on_text(dataset_choice, dataset_size)
#             plot = to_styled_bar_chart(attack_result, "Adversarial Text Robustness", template,
#                                        attack_result["Attack Name"], attack_result["Success Rate"])
#
#             if template == "superhero":
#                 text_perturbations = dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
#                                             <div class="table__dark_template">''' + attacker_examples.to_html(
#                                             escape=False) + '''</div>''')
#             else:
#                 text_perturbations = dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
#                                             <div class="table__light_template">''' + attacker_examples.to_html(
#                                             escape=False) + '''</div>''')
#
#
#             max_result = attack_result["Success Rate"].max()
#             security_score = calc_security_score(1 - (max_result / 100))
#             adv_robust_metric = str(round(1 - (max_result / 100), 2))
#             metric_explanation = get_explanation_text(security_score, 'security')
#
#             return plot, text_perturbations, adv_robust_metric, metric_explanation, security_score, None
#
#         elif dataset_choice == 'heart-disease':
#             plot, score = adversarial_attack_on_tabular_data(dataset_choice, template, dataset_size)
#             security_score = calc_security_score(score)
#             adv_robust_metric = str(round(score, 2))
#             metric_explanation = get_explanation_text(security_score, 'security')
#
#             return plot, None, adv_robust_metric, metric_explanation, security_score, None
