"""テンプレート率を得るモジュール"""
# NOTE: 値オブジェクトを作っていない、保守性を高めるなら作る
#       -> 設定にhigh, middle, low が全て含まれているか、率は0.0~1.0の間か、確認していない
# vo: 設定（settings）、組み合わせ数(combination_num)、テンプレート率(template_rate)

from typing import Text
import yaml


class GetTemplateRate:
    """テンプレート率を得るクラス"""
    def __init__(self, setting_yml_path: Text):
        settings = self.load_yml(setting_yml_path)

        self.COMBINATION_THRESHOLDS = settings["combination_thresholds"]
        self.TEMPLATE_RATES = settings["each_combination_template_rates"]

    def load_yml(self, setting_yml_path: Text, encoding="utf-8") -> dict:
        """YAMLファイルを読み込むメソッド"""
        with open(setting_yml_path, "r", encoding=encoding) as f_in:
            settings = yaml.safe_load(f_in)
        return settings

    def get_template_rate(self, combination_num: int) -> float:
        """組み合わせ数に合ったテンプレート率を返すメソッド"""
        if combination_num >= self.COMBINATION_THRESHOLDS["high"]:
            return self.TEMPLATE_RATES["high"]
        if combination_num >= self.COMBINATION_THRESHOLDS["middle"]:
            return self.TEMPLATE_RATES["middle"]
        return self.TEMPLATE_RATES["low"]
