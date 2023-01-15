"""テンプレート率を得るテスト"""

from each_template_rate import GetTemplateRate


def test_組み合わせ数が50の時テンプレート率1割を返す(settings_yml_path):
    get_template_rate = GetTemplateRate(settings_yml_path)
    result = get_template_rate.get_template_rate(combination_num=50)

    expected = 0.1
    assert result == expected


def test_組み合わせ数が30の時テンプレート率5割を返す(settings_yml_path):
    get_template_rate = GetTemplateRate(settings_yml_path)
    result = get_template_rate.get_template_rate(combination_num=30)

    expected = 0.5
    assert result == expected


def test_組み合わせ数が10の時テンプレート率9割を返す(settings_yml_path):
    get_template_rate = GetTemplateRate(settings_yml_path)
    result = get_template_rate.get_template_rate(combination_num=10)

    expected = 0.9
    assert result == expected

