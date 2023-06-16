import os
import pandas as pd
from glob import glob
from dash import dash_table, get_asset_url
from sklearn.metrics import confusion_matrix
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from random import randint
import numpy as np
import plotly.figure_factory as ff

# plotly
import plotly.express as px

# local


def get_dataframe(name):
    if name == 'medical-reviews':
        df = pd.read_csv('assets/datasets/nlp/medical_reviews/drug_reviews_filtered.csv')
    elif name == 'skin-cancer':
        df = pd.read_csv('assets/datasets/image/skin_cancer/HAM10000_metadata.csv')
    elif name == 'heart-disease':
        df = pd.read_csv('assets/datasets/tabular_data/heart_disease/heart.csv')
    else:
        return 'not implemented'
    return df


def basic_EDA(df):
    size = df.shape
    sum_duplicates = df.duplicated().sum()
    sum_null = df.isnull().sum().sum()
    is_NaN = df.isnull()
    row_has_NaN = is_NaN.any(axis=1)
    rows_with_NaN = df[row_has_NaN]
    count_NaN_rows = rows_with_NaN.shape

    data = {'Number of Samples': [size[0]],
            'Number of Features': [size[1]],
            'Duplicated Entries': [sum_duplicates],
            'Null Entries': [sum_null],
            'Number of Rows with Null Entries': [count_NaN_rows[0]],
            'Percentage': [(count_NaN_rows[0] / df.shape[0]) * 100],
            }
    eda = pd.DataFrame(data)
    return eda


def summary_table(df):
    summary = pd.DataFrame(df.dtypes, columns=['dtypes'])
    summary = summary.reset_index()
    summary['Name'] = summary['index']
    summary = summary[['Name', 'dtypes']]
    summary['Missing'] = df.isnull().sum().values
    summary['Uniques'] = df.nunique().values
    summary = summary[['Name', 'Missing', 'Uniques']]
    return summary


### only SKIN DF
def prepare_dataframe_skin(skin_df):
    # Lesion Dictionary
    lesion_type_dict = {
        'nv': 'Melanocytic nevi',
        'mel': 'Melanoma',
        'bkl': 'Benign keratosis-like lesions ',
        'bcc': 'Basal cell carcinoma',
        'akiec': 'Actinic keratoses',
        'vasc': 'Vascular lesions',
        'df': 'Dermatofibroma'
    }

    base_skin_dir = os.path.join('../', 'tasks')
    # Dictionary for Image Classification Names
    imageid_path_dict = {os.path.splitext(os.path.basename(x))[0]: x for x in
                         glob(os.path.join(base_skin_dir, '*', '*', '*.jpg'))}

    # Create useful Columns - Images Path, Lesion Type and Lesion Categorical Code
    skin_df['path'] = skin_df['image_id'].map(imageid_path_dict.get)
    skin_df['cell_type'] = skin_df['dx'].map(lesion_type_dict.get)
    skin_df['cell_type_idx'] = pd.Categorical(skin_df['cell_type']).codes

    # print(skin_df.head())

    return skin_df


def get_summary_table(df):
    summary = summary_table(df)
    return summary


def to_styled_dict_table(input, theme):
    # superhero is the dark template
    color = 'white' if theme == 'superhero' else 'gray'

    output = dash_table.DataTable(
        data=input.to_dict('records'),
        style_data={
            'backgroundColor': 'rgba(0,0,0,0)',
            'color': color
        },
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(220, 220, 220)',
                'color': '#222',
            }
        ],
        style_header={
            'backgroundColor': 'rgb(210, 210, 210)',
            'color': '#222',
            'fontWeight': 'bold'
        }
    )
    return output


def to_styled_line_chart(dataframe, title, template, metric=False):
    plot = px.line(data_frame=dataframe,
                   title=title,
                   height=300,
                   template=template,
                   markers=True,
                   color_discrete_sequence=px.colors.sequential.Blues_r
                   )
    if metric:
        plot.add_vline(x=3, line_width=3, line_dash="dash", line_color="cyan", annotation_text="eps=8/255")
    # transparent bg
    plot.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor='rgba(0,0,0,0)',
    )

    return plot


def to_styled_bar_chart(dataframe, title, template, x=None, y=None):
    # bar chart
    barchart = px.bar(
        dataframe,
        x,
        y,
        barmode='group',
        title=title,
        width=500, height=500,
        color_discrete_sequence=px.colors.sequential.Blues_r,
        template=template
    )
    # transparent bg
    barchart.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor='rgba(0,0,0,0)',
    )
    return barchart


def to_styled_roc_plot(template, FPR, TPR, AUC, attack_name):
    roc_plot = px.area(
        x=FPR, y=TPR,
        title=f'ROC Curve (AUC={AUC}, {attack_name})',
        labels=dict(x='False Positive Rate', y='True Positive Rate'),
        width=500, height=500,
        template=template,
        color_discrete_sequence=px.colors.sequential.Blues_r,
    )
    roc_plot.add_shape(
        type='line', line=dict(dash='dash'),
        x0=0, x1=1, y0=0, y1=1
    )
    roc_plot.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor='rgba(0,0,0,0)',
    )

    return roc_plot


def to_styled_pie_chart(dataframe, title, values, classes, template):
    # bar chart
    piechart = px.pie(
        dataframe,
        values=values,
        names=classes,
        title=title,
        template=template,
        color_discrete_sequence=px.colors.sequential.Blues_r,
    )
    # transparent bg
    piechart.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor='rgba(0,0,0,0)',
    )
    return piechart


# TODO make for other dataframes!
def skin_heatmap(df, template):
    df = df[df['cell_type'] == 'Melanoma']
    skin_local = df.groupby(['localization']).size().sort_values(ascending=False,
                                                                 inplace=False).reset_index()
    skin_local.columns = ['localization', 'count']
    sort_by = skin_local['localization']
    skin_heat = df.groupby(['age', 'localization']).size().reset_index()
    skin_heat.columns = ['age', 'localization', 'count']
    skin_heat.sort_values('count', ascending=False, inplace=True)
    df_wide = skin_heat.pivot(index='localization', columns='age', values='count')
    df_wide = df_wide.reindex(index=sort_by)

    px_heatmap = px.imshow(df_wide, title="Heatmap Localization - Age", template=template,
                           color_continuous_scale=px.colors.sequential.Blues_r)
    # transparent bg
    px_heatmap.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor='rgba(0,0,0,0)',
    )
    return px_heatmap


def create_wordcloud(df, title, template):
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(background_color='blue', stopwords=stopwords, width=1200, height=800).generate(str(df))
    px_wordcloud = px.imshow(wordcloud, title=title, template=template,
                             color_continuous_scale=px.colors.sequential.Blues_r)
    # transparent bg
    px_wordcloud.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor='rgba(0,0,0,0)',
    )
    px_wordcloud.update_xaxes(showticklabels=False)  # hide all the xticks
    px_wordcloud.update_yaxes(showticklabels=False)  # hide all the yticks

    return px_wordcloud


# TODO make for all images datasets
# def show_images_grid(dataset):
#     """
#     Input: An image generator,predicted labels (optional)
#     Output: Displays a grid of 9 images with lables
#     """
#     cls = ['NonDemented',
#            'VeryMildDemented',
#            'MildDemented',
#            'ModerateDemented']
#
#     data, labels = get_train_data(dataset)
#
#     # get image lables
#     labels = dict(zip([0, 1, 2, 3], cls))
#
#     # get a batch of images
#     x, y = data, labels
#
#     # display a grid of 9 images
#     plt.figure(figsize=(10, 10))
#
#     for i in range(9):
#         ax = plt.subplot(3, 3, i + 1)
#         idx = randint(0, len(labels) - 1)
#         plt.imshow(x[idx])
#         plt.axis("off")
#         plt.title("Class:{}".format(y[idx]))
#         plt.tight_layout()
#
#     plt.savefig("assets/datasets/image/alzheimer/image_grid.png")


def load_and_show_image(path, title, template):
    img = px.imshow(img=path,
                    title=title,
                    width=500, height=500,
                    template=template)
    img.update_xaxes(showticklabels=False)  # hide all the xticks
    img.update_yaxes(showticklabels=False)  # hide all the yticks

    return img


def create_confusion_matrix(CMatrix, categories):
    fig = ff.create_annotated_heatmap(CMatrix, x=categories, y=categories, colorscale='Blues')
    fig.add_annotation(dict(font=dict(color="white", size=14),
                            x=0.5,
                            y=-0.15,
                            showarrow=False,
                            text="Predicted label",
                            xref="paper",
                            yref="paper"))

    # add custom yaxis title
    fig.add_annotation(dict(font=dict(color="white", size=14),
                            x=-0.15,
                            y=0.5,
                            showarrow=False,
                            text="True label",
                            textangle=-90,
                            xref="paper",
                            yref="paper"))

    # adjust margins to make room for yaxis title
    fig.update_layout(margin=dict(t=50, l=200))

    # transparent bg
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor='rgba(0,0,0,0)',
        height=500,
        width=600
    )
    return fig


def create_signal_histogram(values, labels, threshold):
    histogram = px.histogram(
        data_frame=pd.DataFrame({
            'Signal': values,
            'Membership': ['Member' if y == 1 else 'Non-member' for y in labels]
        }),
        x='Signal',
        color='Membership',
        width=600, height=500,
        color_discrete_sequence=px.colors.sequential.Blues_r,
        title="Signal Histogram",
    )
    histogram.add_vline(x=threshold, line_width=2, line_dash="dash", line_color="cyan", annotation_text="threshold")
    histogram.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor='rgba(0,0,0,0)',
    )
    return histogram
