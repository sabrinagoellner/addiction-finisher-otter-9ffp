import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import get_asset_url

dash.register_page(__name__)

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("Publisher"),
                       html.P("Sabrina Göllner,"),
                       html.P("Department of Computer Science"),
                       html.P("HAW Hamburg Berliner Tor 7"),
                       html.P("D-20099 Hamburg, Germany"),
                       html.P("sabrina.goellner(@)haw-hamburg.de"),

                        html.H3("DISCLAIMER"),

                        html.H4("Online-contents:"),

                        html.P("The author reserves the right not to be responsible for the topicality, correctness, completeness or quality of the information provided. Liability claims regarding damage caused by the use of any information provided, including any kind of information which is incomplete or incorrect, will therefore be rejected. All offers are not-binding and without obligation. Parts of the pages or the complete publication including all offers and information might be extended, changed or partly or completely deleted by the author without separate announcement."),

                        html.H4("Referrals and links:"),

                        html.P("The Author is not responsible for any contents linked or referred to from his pages – unless he has full knowlegde of illegal contents and would be able to prevent the visitors of his site from viewing those pages. If any damage occurs by the use of information presented there, only the author of the respective pages might be liable, not the one who has linked to these pages. Furthermore the author is not liable for any postings or messages published by users of discussion boards, guestbooks or mailinglists provided on his page."),

                        html.H4("Copyright"),

                        html.P("The author intended not to use any copyrighted material for the publication or, if not possible, to indicate the copyright of the respective object. The copyright for any material created by the author is reserved. Any duplication or use of such diagrams, sounds or texts in other electronic or printed publications is not permitted without the author’s agreement."),

                        html.H4("Data security"),

                        html.P("If the possibility for the input of personal or business data (email addresses, name, addresses) exists, the input of these data takes place voluntarily. The use and payment of all offered services are permitted – if and so far technically possible and reasonable – without specification of such data or under specification of anonymizated data or an alias."),

                        html.H4("Legal force of this disclaimer"),

                        html.P("This disclaimer is to be regarded as part of the internet publication which you were referred from. If sections or individual formulations of this text are not legal or correct, the content or validity of the other parts remain uninfluenced by this fact."),

                    ],
                    md=12,
                ),

            ]
        )
    ],
    className="mt-4",
)
