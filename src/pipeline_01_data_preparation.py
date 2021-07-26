import os
import argparse
import yaml
import logging


def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def main(config_path, datasource):
    config = read_params(config_path)
    print(config)






if __name__ == "__main__":
    args = argparse.ArgumentParser()
    default_config_path = os.path.join("config","params.yaml")
    args.add_argument("--config", default=default_config_path)
    args.add_argument("--datasource", default=None)

    parse_args = args.parse_args()
    #print(parse_args.config, parse_args.datasource)
    main(config_path= parse_args.config, datasource= parse_args.datasource)