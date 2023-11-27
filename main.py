from driver.aws import AWS
from subprocess import run
import questionary
import click




@click.group()
def aws():
    print


@aws.command()
def aws_show_profiles():
    ls = AWS.list_profiles()
    if ls:
        return click.secho("\n".join(ls), blink=True, bold=True)
    return click.error('No profiles found')

@aws.command()
def aws_login():
    ls = AWS.list_profiles()
    profile = questionary.select("Login Profile",choices=ls).ask()
    cmd = f'aws sso login --profile {profile}'
    print(cmd)
    run(cmd.split())

if __name__ == "__main__":
    aws()
