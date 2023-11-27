from driver import AWS, run_cmd, to_lines
import questionary
import click


@click.group()
def aws():
    pass


@aws.command()
def aws_show_profiles():
    return click.secho(to_lines(AWS.list_profiles()), blink=True, bold=True)

@aws.command()
def aws_show_regions():
    return click.secho(to_lines(AWS.list_regions()), blink=True, bold=True)

@aws.command()
def aws_login():
    ls = AWS.list_profiles()
    profile = questionary.select("Login Profile",choices=ls).ask()
    run_cmd(f'aws sso login --profile {profile}')

if __name__ == "__main__":
    aws()
