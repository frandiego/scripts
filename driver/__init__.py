AWS_HOME = '~/.aws'
AWS_CONFIGS_PATH = f'{AWS_HOME}/configs'
AWS_CONFIG_PATH = f'{AWS_HOME}/config'

KUBE_HOME = '~/.kube'
KUBE_CONFIG_PATH = f'{KUBE_HOME}/config'

REGIONS = [
    'eu-west-1', 
    'us-east-1', 
]

CODENAMES = [
    'bute', 
    'mull', 
    'fara', 
]

AWS_PATH = '~/.aws'


from .tools import Tools
from .cli import Cli