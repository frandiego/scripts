from questionary import select
import click

from .tools import Tools
from . import CONFIG_PATH, REGIONS

class Cli:

    _profiles: list = []
    _regions: list = []

    @property
    def profiles(self) -> list:
        if not self._profiles:
            self._profiles = list(Tools.read_profiles_from_config(CONFIG_PATH))
        return self._profiles
     
    @property
    def regions(self) -> list:
        if not self._regions:
            self._regions = list(REGIONS)
        return self._regions
    
    @staticmethod
    def show(ls: list):
        return click.secho(Tools.to_lines(ls), blink=True, bold=True)
    
    @staticmethod
    def select(ls: list):
        return select("Select ",choices=ls).ask()
      