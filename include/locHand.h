
#include <yaml-cpp/yaml.h>
#include <iostream>
#include <string>
#include <format>
#include <config.h>
using namespace std;

class Localization {
    public:
        string locale;
        string yaml_file;
        YAML::Node local_table;

        static Localization& get_instance() {
            static Localization instance;
            return instance;
        }
        Localization() {
            Config config;
            locale = config.conf_table["interface"]["language"].as<string>();
            yaml_file = format("Localization/{}.yaml", locale);
            local_table = reload_locale_file(yaml_file);
        }

        YAML::Node reload_locale_file(string file) {
            try {
                return YAML::LoadFile(file);
            } catch(...) {
                std::cerr << "Language file cannot loaded: " << yaml_file << std::endl;
                return YAML::LoadFile("Localization/EN.yaml");
            }
            
        }
};

struct TextProxy {
    YAML::Node node;

    TextProxy operator[](const string& key) {
        return {node[key]};
    }

    operator string() const {
        return node.as<string>("");
    }

    const char* c_str() const {
        cout << node.as<string>("").c_str();
        return node.as<string>("").c_str();
    }
};

class Tet {
    public:
        static TextProxy get(const std::string& key) {
            return {Localization::get_instance().local_table[key]};
        }

        TextProxy operator[](const std::string& key) {
            return {Localization::get_instance().local_table[key]};
        }
};

inline Tet Text;