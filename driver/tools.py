from subprocess import run


def run_cmd(cmd:str) -> None:
    print(cmd)
    run(cmd.split())


def to_lines(ls: list) -> str:
    return "\n".join(ls)
