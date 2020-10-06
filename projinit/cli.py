import click
from . import initializer as init

LICENSES = click.Choice([
    'APACHE',
    'MIT',
    'GPLv2',
    'GPLv3',
    'MOZILLA'], case_sensitive=False)


@click.command()
@click.option(
    '-p', '--path', default='.', help='Absolute path to location project')
@click.option(
    '--repo/--no-repo',
    'with_repo',
    default=True,
    type=bool,
    help='Init a repository for project')
@click.option('--license', type=LICENSES, default=None)
@click.argument('name')
def initializer_cmd(path, name, with_repo, license):
    project_dir = init.folders_create(name, path)
    if with_repo:
        init.init_repo(project_dir)
    init.copy_stubs(project_dir)

    init.readme_fill(name, project_dir)
