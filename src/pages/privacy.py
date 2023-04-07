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
                        html.H1("PRIVACY NOTICE / DATENSCHUTZERKLÄRUNG"),
                        html.H2("This privacy notice is held in German language accordingly to DSGVO."),
                        html.H3("Kontaktdaten des Verantwortlichen"),
                        html.P(

                            "Der Verantwortliche im Sinne der Datenschutz-Grundverordnung und anderer nationaler "
                            "Datenschutzgesetze der Mitgliedsstaaten sowie sonstiger datenschutzrechtlicher "
                            "Bestimmungen ist "

                        ),

                       html.P("Sabrina Göllner,"),
                       html.P("Department of Computer Science"),
                       html.P("HAW Hamburg Berliner Tor 7"),
                       html.P("D-20099 Hamburg, Germany"),
                       html.P("sabrina.goellner(@)haw-hamburg.de"),

                        html.H3("Umfang der Verarbeitung personenbezogener Daten"),
                        html.P("Wir verarbeiten personenbezogene Daten unserer Nutzer (Logfiles, Cookies u.ä.) "
                               "grundsätzlich nur, soweit dies zur Bereitstellung einer funktionsfähigen Website "
                               "sowie unserer Inhalte und Leistungen erforderlich ist. Die Verarbeitung "
                               "personenbezogener Daten unserer Nutzer erfolgt regelmäßig nur nach Einwilligung des "
                               "Nutzers. Eine Ausnahme gilt in solchen Fällen, in denen eine vorherige Einholung "
                               "einer Einwilligung aus tatsächlichen Gründen nicht möglich ist und die Verarbeitung "
                               "der Daten durch gesetzliche Vorschriften gestattet ist."),

                        html.H3("Rechtsgrundlage für die Verarbeitung personenbezogener Daten"),

                        html.P("Soweit wir für Verarbeitungsvorgänge personenbezogener Daten eine Einwilligung der "
                               "betroffenen Person einholen, dient Art. 6 Abs. 1 lit. a EU-Datenschutzgrundverordnung "
                               "(DSGVO) als Rechtsgrundlage. Bei der Verarbeitung von personenbezogenen Daten, "
                               "die zur Erfüllung eines Vertrages, dessen Vertragspartei die betroffene Person ist, "
                               "erforderlich ist, dient Art. 6 Abs. 1 lit. b DSGVO als Rechtsgrundlage. Dies gilt "
                               "auch für Verarbeitungsvorgänge, die zur Durchführung vorvertraglicher Maßnahmen "
                               "erforderlich sind. Soweit eine Verarbeitung personenbezogener Daten zur Erfüllung "
                               "einer rechtlichen Verpflichtung erforderlich ist, der unser Unternehmen unterliegt, "
                               "dient Art. 6 Abs. 1 lit. c DSGVO als Rechtsgrundlage. Für den Fall, "
                               "dass lebenswichtige Interessen der betroffenen Person oder einer anderen natürlichen "
                               "Person eine Verarbeitung personenbezogener Daten erforderlich machen, dient Art. 6 "
                               "Abs. 1 lit. d DSGVO als Rechtsgrundlage. Ist die Verarbeitung zur Wahrung eines "
                               "berechtigten Interesses unseres Unternehmens oder eines Dritten erforderlich und "
                               "überwiegen die Interessen, Grundrechte und Grundfreiheiten des Betroffenen das "
                               "erstgenannte Interesse nicht, so dient Art. 6 Abs. 1 lit. f DSGVO als Rechtsgrundlage "
                               "für die Verarbeitung."),

                        html.H3("Datenlöschung und Speicherdauer"),

                        html.P("Die personenbezogenen Daten der betroffenen Person werden gelöscht oder gesperrt, "
                               "sobald der Zweck der Speicherung entfällt. Eine Speicherung kann darüber hinaus "
                               "erfolgen, wenn dies durch den europäischen oder nationalen Gesetzgeber in "
                               "unionsrechtlichen Verordnungen, Gesetzen oder sonstigen Vorschriften, "
                               "denen der Verantwortliche unterliegt, vorgesehen wurde. Eine Sperrung oder Löschung "
                               "der Daten erfolgt auch dann, wenn eine durch die genannten Normen vorgeschriebene "
                               "Speicherfrist abläuft, es sei denn, dass eine Erforderlichkeit zur weiteren "
                               "Speicherung der Daten für einen Vertragsabschluss oder eine Vertragserfüllung "
                               "besteht.")
                    ],
                    md=12,
                ),

            ]
        )
    ],
    className="mt-4",
)
