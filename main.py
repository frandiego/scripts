from driver.aws import AWS
from subprocess import run
import questionary
import click



def run_cmd(cmd:str) -> None:
    print(cmd)
    run(cmd.split())



@click.group()
def aws():
    pass


@aws.command()
def aws_show_profiles():
    ls = AWS.list_profiles()
    return click.secho("\n".join(ls), blink=True, bold=True)


@aws.command()
def aws_login():
    ls = AWS.list_profiles()
    profile = questionary.select("Login Profile",choices=ls).ask()
    run_cmd(f'aws sso login --profile {profile}')

if __name__ == "__main__":
    aws()
