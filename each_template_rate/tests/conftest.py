"""const"""

import pytest
import os
import yaml


@pytest.fixture
def settings_yml_path():
    settings_yml_path = "./assets/test_settings.yml"
    settings = {
        "combination_thresholds": {
            "high": 50,
            "middle": 30,
            "low": 10
        },
        "each_combination_template_rates": {
            "high": 0.1,
            "middle": 0.5,
            "low": 0.9,
        }
    }
    with open(settings_yml_path, "w", encoding="utf-8") as f_out:
        yaml.dump(settings, f_out)

    yield settings_yml_path

    if os.path.exists(settings_yml_path):
        os.remove(settings_yml_path)

