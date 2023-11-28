from driver import Cli, Tools
import click

CLIENT = Cli()

@click.group()
def aws():
    pass

@aws.command()
def aws_show_profiles():
    return CLIENT.show(CLIENT.profiles)

@aws.command()
def aws_show_regions():
    return CLIENT.show(CLIENT.regions)

@aws.command()
def aws_login():
    profile = CLIENT.select(CLIENT.profiles)
    Tools.run_cmd(f'aws sso login --profile {profile}')

if __name__ == "__main__":
    aws()
