from subprocess import check_output
from re import finditer
from . import CONFIG_PATH, REGIONS

class AWS:

    @staticmethod
    def list_profiles() -> list:
        string = str(check_output(f"cat {CONFIG_PATH}", shell=True))
        positions = [(m.start(), m.end()) for m in finditer('profile', string)]
        res = []
        for start, _ in positions:
            end = start + string[start:].find(']')
            word = string[start:end].replace('profile', "")
            word = word.replace(']', "")
            res.append(word.strip())
        assert res, f'No profiles found, check {CONFIG_PATH} file'
        return res
    
    def list_regions() -> list:
        return REGIONS
 