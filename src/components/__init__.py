# pull in components from files in the current directory to make imports cleaner
#from .location import loc

from .navbar import navbar
from .footer import footer

from .page_header import create_page_header_box
from .prepare_dataset_charts import *

# from .model_card import create_model_card
from .graph_card import create_graph_card
from .explanation_card import create_explanation_card
#
# from .file_management import load_model, get_test_data, get_train_data
#
# from .fairness.fairness import measure_fairness_on_tabular_data, measure_fairness_on_tensorflow_model
#
# from .privacy.privacy import perform_mia_on_nn, perform_mia_on_tabular_data, calc_privacy_score
#
# from .security.security import adversarial_attack_on_images, adversarial_attack_on_text
#
# from .explainability.explainability import measure_explanation_on_images, measure_explanation_on_text, measure_explanation_on_tabular_data, calc_explainability_score
#

from .responsibility.metrics_to_explanations import get_explanation_text




