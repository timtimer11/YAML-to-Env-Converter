from typing import Any
import yaml


def transformt_yaml_to_env(yaml_config_file: str) -> str:
    """
    Transforms yaml configuration to environment variables list

    Args:
        yaml_config_file (str): yaml configuration file

    Returns:
        str: environment variables list
    """

    def process_yaml(yaml_config: dict, env_prefix: str = "") -> str:

        env_vars = ""
        for k, v in yaml_config.items():
            if isinstance(v, dict):
                env_vars += process_yaml(v, f"{env_prefix}{k}.")
            else:
                env_vars += f"{env_prefix}{k}={v}\n"

        return env_vars

    yaml_data = yaml.load(yaml_config_file, Loader=yaml.FullLoader)
    return process_yaml(yaml_data)


def transform_env_to_yaml(env_variables: str) -> str:
    """
    Transforms environment variables list to yaml configuration

    Args:
        env_variables (str): environment variables list

    Returns:
        str: yaml configuration
    """

    def interpret_value(val: str) -> Any:
        if val.isnumeric():
            return int(val)
        if val.replace(".", "", 1).isnumeric():
            return float(val)
        if val.lower() in ["true", "false"]:
            return val.lower() == "true"
        return val

    def process_env(env_variables: str, yaml_config: dict = {}) -> dict:
        for env_var in env_variables.splitlines():
            env_key, env_val = env_var.split("=")

            env_val = interpret_value(env_val)

            env_key = env_key.split(".", 1)
            if len(env_key) == 1:
                yaml_config[env_key[0]] = env_val
            else:
                if env_key[0] not in yaml_config:
                    yaml_config[env_key[0]] = {}
                process_env(f"{env_key[1]}={env_val}", yaml_config[env_key[0]])
        return yaml_config

    return yaml.dump(process_env(env_variables), default_style="", default_flow_style=False)
