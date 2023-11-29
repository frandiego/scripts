from subprocess import run, check_output
from re import finditer
import os

from . import AWS_CONFIG_PATH, AWS_CONFIGS_PATH

class Tools:


    @staticmethod  
    def run_cmd(cmd:str) -> None:
        print(cmd)
        run(cmd.split())

    @staticmethod
    def to_lines(ls: list) -> str:
        return "\n".join(ls)

    @staticmethod
    def read_profiles_from_config(path):
        string = str(check_output(f"cat {path}", shell=True))
        positions = [(m.start(), m.end()) for m in finditer('profile', string)]
        res = []
        for start, _ in positions:
            end = start + string[start:].find(']')
            word = string[start:end].replace('profile', "")
            word = word.replace(']', "")
            res.append(word.strip())
        assert res, f'No profiles found, check {path} file'
        return res

    @classmethod
    def select_role(cls, role: str):
        config_role = os.path.join(os.path.expanduser(AWS_CONFIGS_PATH),role)
        cls.run_cmd(f'cp {config_role} {os.path.expanduser(AWS_CONFIG_PATH)}')

