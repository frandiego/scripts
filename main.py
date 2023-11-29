from driver.cl import Cli
from driver.tools import Tools
import click


CLIENT = Cli()

@click.group()
def cli():
    pass

@cli.command()
def aws_show_roles():
    return CLIENT.show(CLIENT.roles)

@cli.command()
def aws_show_profiles():
    return CLIENT.show(CLIENT.profiles)

@cli.command()
def aws_show_regions():
    return CLIENT.show(CLIENT.regions)

@cli.command()
def aws_show_codenames():
    return CLIENT.show(CLIENT.codenames)

@cli.command()
def aws_select_role():
    return Tools.select_role(CLIENT.select(CLIENT.roles))

@cli.command()
def aws_login():
    Tools.run_cmd(f'aws sso login --profile {CLIENT.select(CLIENT.profiles)}')

@cli.command()
def kube_show_contexts():
     return CLIENT.show(CLIENT.kube_contexts)

@cli.command()
def kube_switch_context():
    Tools.run_cmd(f'kubectl config use-context {CLIENT.select(CLIENT.kube_contexts)}')



@cli.command()
def kube_pods():
    Tools.run_cmd(f'kubectl get pods -n {CLIENT.select(CLIENT.codenames)}')


@cli.command()
def test():
    print(CLIENT.kubeconfig)






if __name__ == "__main__":
    cli()
