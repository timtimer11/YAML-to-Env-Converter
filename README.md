# YAML-to-Env-Converter
This module provides functions to convert YAML configuration files to environment variable lists and vice versa.

## Installation
No installation is required for this module. Simply import the functions into your Python script or application as needed.

## Example (YAML to env):
```
env_list = transform_yaml_to_env("config.yaml")
print(env_list)
```
## Example (env to YAML):
```
env_config = """
    DB_HOST=localhost
    DB_PORT=5432
    DB_USERNAME=admin
    DB_PASSWORD=secretpassword
    DEBUG=true
    LOG_LEVEL=info
    """
yaml_config = transform_env_to_yaml(env_config)
print(yaml_config)
```
