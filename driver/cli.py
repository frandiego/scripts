from questionary import select
import click
import yaml
import os

from .tools import Tools
from . import (
    AWS_CONFIG_PATH, 
    AWS_CONFIGS_PATH, 
    REGIONS, 
    CODENAMES, 
    KUBE_CONFIG_PATH, 
)

class Cli:
    codenames: list = CODENAMES
    regions: list = REGIONS

    @property
    def kubeconfig(self):
        return yaml.safe_load(open(os.path.expanduser(KUBE_CONFIG_PATH), 'r'))
    
    @property
    def kube_contexts(self):
        return list(map(lambda i: i['name'], self.kubeconfig['contexts']))

    @property
    def roles(self):
        return os.listdir(os.path.expanduser(AWS_CONFIGS_PATH))
    
    @property
    def profiles(self):
        return list(Tools.read_profiles_from_config(AWS_CONFIG_PATH))

    @staticmethod
    def show(ls: list):
        return click.secho(Tools.to_lines(ls), blink=True, bold=True)
    
    @staticmethod
    def select(ls: list):
        return select("Select ",choices=ls).ask()
      