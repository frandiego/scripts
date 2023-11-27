from subprocess import check_output
from re import finditer

class AWS:
    config_path = "~/.aws/config"

    @classmethod
    def list_profiles(cls) -> list:
        string = str(check_output(f"cat {cls.config_path}", shell=True))
        positions = [(m.start(), m.end()) for m in finditer('profile', string)]
        res = []
        for start, _ in positions:
            end = start + string[start:].find(']')
            word = string[start:end].replace('profile', "")
            word = word.replace(']', "")
            res.append(word.strip())
        assert res, f'No profiles found, check {cls.config_path} file'
        return res
