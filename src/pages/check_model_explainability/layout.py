# import dash
# import dash_dangerously_set_inner_html
# import pandas as pd
# from dash_bootstrap_templates import ThemeSwitchAIO
# from dash import html, dcc, callback, Input, Output, State
# from dash import Dash, html, dcc, dash_table
# import dash_bootstrap_components as dbc
# import plotly.express as px
# from skimage import io
# import numpy as np
# import plotly.graph_objects as go
#
# from src.components import create_graph_card, create_explanation_card, measure_explanation_on_images, \
#     calc_explainability_score, get_explanation_text, to_styled_bar_chart, load_and_show_image, \
#     measure_explanation_on_text, measure_explanation_on_tabular_data
# # local imports
# from src.components.page_header import create_page_header_box
# from src.components.step_progress_bar import create_step_progress_bar
#
# dash.register_page(
#     __name__,
#     path='/check-model-explainability',
#     title='Check Model Explainability'
# )
#
# # the page header
# page_header = create_page_header_box(
#     icon='fa fa-2x fa-search',
#     title='Model Explainability',
#     description='Explainability is the most important feature for users trust in your AI System. ',
#     prev_step='/check-model-security',
#     next_step='/check-model-responsibility'
# )
#
# explainability_graph = create_graph_card(
#     card_type='custom_graph',
#     card_id='explainability_graph')
#
# plot_explanations = create_graph_card(
#     card_type='custom_graph',
#     card_id='plot_explanations')
#
# explanation = create_explanation_card(
#     card_title='Qualitative and Quantitative Evaluation of Explainability',
#     explanation='This tests your model to see if it explains the decisions well. '
#                 'In this case, the explaibnability of a model is evaluated using an explainability method and different metrics, which measure the quality. ',
#     metric_result='explanation_metric_result',
#     metric_explanation='explanation_metric_explanation',
#     image_name='xai_methods'
# )
#
# show_html_explanation = create_graph_card(
#     card_type='html_div',
#     card_id='show_html_explanation')
#
#
# loading_explainability_content = dcc.Loading([
#     dbc.Row(
#         [
#             dbc.Col([
#                 explanation,
#             ],
#                 width=12,
#                 className="mb-4",
#             ),
#             dbc.Col([
#                 show_html_explanation,
#             ],
#                 width=6,
#                 className="mb-4",
#             ),
#             dbc.Col([
#                 explainability_graph,
#             ],
#                 width=6,
#                 className="mb-4",
#             ),
#             dbc.Col([
#                 plot_explanations
#             ],
#                 width=6,
#                 className="mb-4",
#                 id="plot_explanations_container"
#             ),
#         ]),
# ],
#     type="circle",
#     id="loading_exp"
# )
#
# layout = html.Div([
#     create_step_progress_bar(["Start", "Lifecycle", "Use Case", "Data Analysis", "Test Settings", "Fairness", "Privacy", "Security", "Explainability", "Results"], 8),
#     page_header,
#     loading_explainability_content
# ])
#
#
# @callback(
#     Output('explainability_graph', 'figure'),
#     Output('plot_explanations', 'figure'),
#
#     Output('explanation_metric_result', 'children'),
#     Output('explanation_metric_explanation', 'children'),
#     Output('show_html_explanation', 'children'),
#     Output('explainability_score', 'data'),
#
#     Input('dataset_choice', 'data'),
#     Input('dataset_size', 'data'),
#     Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
#
# )
# def update_selected(dataset_choice, dataset_size, theme_switch):
#     print(dataset_choice)
#     if dataset_choice is None:
#         print("no update privacy")
#         return dash.no_update
#
#     elif dataset_choice:
#         template = "cosmo" if theme_switch else "superhero"
#         # images:
#         if dataset_choice == 'skin-cancer' or dataset_choice == 'alzheimer':
#             # for static tests:
#             results_agg = {'IntegratedGradients': {'Robustness': 0.6298981663798691, 'Complexity': 0.8860982597616784, 'Faithfulness': 0.04655679344792017, 'Randomisation': 0.8715156038421596}}
#             # results_agg = {'IntegratedGradients': {'Robustness': np.nan, 'Complexity': 0.8860982597616784, 'Faithfulness': np.nan, 'Randomisation': 0.8715156038421596}}
#             df_results = pd.DataFrame([results_agg['IntegratedGradients']])
#
#             # run analysis:
#             #df_results = measure_explanation_on_images(dataset_choice,dataset_size)
#             #df_results = df_results.dropna(axis=1, how='all')
#             print(df_results)
#
#             explainability_graph = to_styled_bar_chart(df_results, 'Explanation', template)
#             path = io.imread('assets/plots/' + dataset_choice + 'explanations.jpg')
#             plot_explanations = load_and_show_image(path, "Integrated Gradients and Attributions", template)
#             score = np.mean(df_results.values)
#             explainability_score = calc_explainability_score(score)
#             explanation_metric_result = str(round(score, 2))
#             explanation_metric_explanation = get_explanation_text(explainability_score, 'explainability')
#
#             return explainability_graph, plot_explanations, explanation_metric_result, explanation_metric_explanation, None, explainability_score
#
#         if dataset_choice == 'medical-reviews':
#             show_html_explanation = measure_explanation_on_text(dataset_choice)
#
#             placeholder = px.scatter_3d().add_annotation(
#                 text="The metrics are not available for this kind of explanation.",
#                 showarrow=False,
#                 font={"size": 15, 'color': 'white'},
#             )
#             # transparent bg
#             placeholder.update_layout(
#                 plot_bgcolor="rgba(0,0,0,0)",
#                 paper_bgcolor='rgba(0,0,0,0)',
#             )
#
#             iframe = html.Iframe(
#                 # Javascript is disabled from running in an Iframe for security reasons
#                 # Static HTML only!!!
#                 srcDoc=show_html_explanation.as_html(),
#                 width='100%',
#                 height='500px',
#                 style={'color': 'white'},
#             )
#
#             return placeholder, placeholder, "Not available", "Not available", iframe, None
#
#         if dataset_choice == 'heart-disease':
#             single_explanation, single_explanation_faith, single_explanation_mono, monoton_results, faith_results, finalscore = measure_explanation_on_tabular_data(
#                 dataset_choice,dataset_size)
#
#             explanation = html.Div([
#                 html.H4("Single Explanation"),
#                 html.P("Faithfulness: " + str(single_explanation_faith) +
#                        ", Monotonicity: " + str(single_explanation_mono)),
#                 html.Iframe(
#                     srcDoc=single_explanation.as_html(),
#                     width='100%',
#                     height='500px',
#                     style={'color': 'white'},
#                 )
#             ])
#
#             # histogram faithfulness
#             bins1 = [-1.0, -0.5, 0, 0.5, 1.0]
#             counts, bins2 = np.histogram(faith_results, bins=bins1)
#             bins2 = 0.5 * (bins1[:-1] + bins2[1:])
#
#             # specify sensible widths
#             widths = []
#             for i, b1 in enumerate(bins1[1:]):
#                 widths.append(b1 - bins2[i])
#
#             # plotly figure
#             faith_histo = go.Figure(
#                 go.Bar(
#                     x=bins2,
#                     y=counts,
#                     width=widths,
#                     marker=dict(
#                         color=counts,
#                         colorscale='blues')
#                 ))
#
#             faith_histo.update_layout(
#                 title_text='Distribution of Faithfulness Metric',  # title of plot
#                 xaxis_title_text='Value',  # xaxis label
#                 yaxis_title_text='Count',  # yaxis label
#                 plot_bgcolor="rgba(0,0,0,0)",
#                 paper_bgcolor='rgba(0,0,0,0)'
#             )
#
#             faith_histo.add_vline(
#                 x=np.mean(faith_results),
#                 line_dash='dash',
#                 line_color="firebrick",
#                 annotation_text="mean")
#
#             # monotonicity chart
#             columns = ['Monotonicity False', 'Monotonicity True']
#             unique, counts = np.unique(monoton_results, return_counts=True)
#             zeros = counts[0]
#             if len(counts) > 1:
#                 ones = counts[1]
#             else:
#                 ones = 0
#             mono_df = pd.DataFrame([[zeros, ones]], columns=columns)
#
#             mono_barchart = to_styled_bar_chart(mono_df, "Monotonicity", template)
#             explainability_score = calc_explainability_score(finalscore)
#             explanation_metric_explanation = get_explanation_text(explainability_score, 'explainability')
#             explanation_metric_result = str(round(finalscore, 2))
#
#             return faith_histo, mono_barchart, explanation_metric_result, explanation_metric_explanation, explanation, explainability_score
