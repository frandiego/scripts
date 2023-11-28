CONFIG_PATH = "~/.aws/config"
REGIONS = [
    'eu-west-1', 
    'us-east-1'
]


from .aws import AWS
from .tools import Tools
from .cli import Cli