"YAMLファイルの読み込みテスト"

from each_template_rate import GetTemplateRate


def test_YMLファイルを読み込み設定をインスタンス変数で保持できる(settings_yml_path):
    get_template_rate = GetTemplateRate(settings_yml_path)

    expected_combination_thresholds = {
        "high": 50,
        "middle": 30,
        "low": 10
    }

    expected_template_rates = {
        "high": 0.1,
        "middle": 0.5,
        "low": 0.9
    }

    assert get_template_rate.COMBINATION_THRESHOLDS == expected_combination_thresholds
    assert get_template_rate.TEMPLATE_RATES == expected_template_rates

