import yaml
import os

def get_config():
    with open('configuration.yaml', 'r') as f:
        config = yaml.safe_load(f)
        
    if os.getenv('ENVIRONMENT') == 'prod':
        return config['prod']
    
    else:
        return config['dev']