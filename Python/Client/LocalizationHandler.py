import yaml

locale = "TR"

class Localization:
    def __init__(self, locale= locale):
        self.yaml_file = f"Localization/{locale}.yaml" 
        self.loc_tab = self.reload_locale_file(self.yaml_file)

    def reload_locale_file(self, file):
        with open(file, encoding="U8") as loc_file:
            return yaml.safe_load(loc_file)

