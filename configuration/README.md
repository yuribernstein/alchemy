# Alchemy Configuration Loader

# Configuration Loader example

This project provides a simple yet flexible way to manage configurations for different environments in Python applications. It leverages YAML for configuration file management and dynamically loads the configuration based on the environment.

## Features

- Supports separate configurations for development (`dev`) and production (`prod`) environments.
- Easy to extend or modify for additional environments or configuration parameters.
- Uses environment variables to switch between configurations, making it suitable for containerized deployments.

## Getting Started

Setting environment variable `ENVIRONMENT` to prod to server `prod` section of your configuration file

### Prerequisites

- Python 3.x
- PyYAML

You can install the required package using pip:

```bash
pip install pyyaml
```

# Example usage
```python
import config as cnfg
config = cnfg.get_config()

print(config['db']['host'])
```
