import os
import subprocess
import shutil

import jinja2

import projinit
from projinit import utils

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(MODULE_DIR, 'templates')


def project_tree(project_name, path='.', **kwargs):
    project = folder_project(project_name, path)

    subdirs = list()

    if kwargs.get('tests', False):
        subdirs.append('tests')

    if kwargs.get('docs', False):
        subdirs.append('docs')

    utils.makedirs(project, subdirs)

    module_name = utils.name_normalizer(project_name)

    if kwargs.get('single_file', False):
        single_file_module(project, module_name)
    else:
        folder_module(project, module_name)

    if kwargs.get('repo', True):
        init_repo(project)


def folder_project(project_name, path='.'):
    """Create folder of project"""
    project_dir = os.path.join(path, project_name)
    if os.path.exists(project_dir):
        raise OSError(f"'{project_dir}' already exists")
    os.mkdir(project_dir)

    return os.path.abspath(project_dir)


def folder_module(project_path, module_name):
    """Create module folder"""
    folder = os.path.join(project_path, module_name)
    os.mkdir(folder)
    init_file_name = os.path.join(folder, '__init__.py')
    with open(init_file_name, 'x'):
        pass


def single_file_module(project_path, module_name):
    """Create module file"""
    file_name = os.path.join(project_path, f'{module_name}.py')
    with open(file_name, 'x'):
        pass


def init_repo(project_path):
    """Init a repository on project"""
    if os.curdir != project_path:
        os.chdir(project_path)
    subprocess.run(['git', 'init'])


def readme_fill(
        project_name, creator_name='', creator_mail='', description='',
        project_path=None):
    """Fill the README file with project infos"""

    template_name = 'readme.j2'
    dest_template_name = 'README'

    if os.curdir != project_path:
        os.chdir(project_path)

    template_path = os.path.join(TEMPLATE_DIR, template_name)
    dest_path = os.path.join(os.curdir, dest_template_name)

    shutil.copy(template_path, dest_path)

    content = {
        'project_name': project_name,
        'creator_name': creator_name,
        'creator_mail': creator_mail,
        'description': description,
        'projinit_name': projinit.name
    }

    template_fill(dest_path, content)


def template_fill(template_name, content):
    """Fill template with new content"""
    with open(template_name, 'r+') as template_file:
        template = jinja2.Template(template_file.read())
        rendered = template.render(**content)

        template_file = __filewrite(template_file, rendered)


def __filewrite(file, content):
    file.seek(0)
    file.write(content)
    file.truncate()
