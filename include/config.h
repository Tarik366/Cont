#include <yaml-cpp/yaml.h>
#include <iostream>
#include <fstream> 
#include <filesystem>
namespace fs = std::filesystem;

class Config {
    public:
        YAML::Node conf_table;
        Config() {
            if (!fs::exists("default_config.yaml")) {
                std::cerr << "Default config file missing. Please reinstall app from github.com";
            }
            if (fs::exists("config.yaml")){
                std::cout << "Loading config file";
                conf_table = YAML::LoadFile("config.yaml");
            }
            else {
                std::cout << "Config file missing. Copying from the default...";
                fs::copy_file("default_config.yaml", "config.yaml");
                conf_table = YAML::LoadFile("config.yaml");
            }
        }
};

