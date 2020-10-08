#!/usr/bin/python
import os
import subprocess
import shutil

from projinit import utils

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))



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
        raise FileExistsError(f"'{project_dir}' already exists")
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


def copy_stubs(project_path=None):
    """Copy stubs to root of project dir"""
    if project_path:
        os.chdir(project_path)
    stubs_path = os.path.join(MODULE_DIR, 'stubs')
    shutil.copytree(stubs_path, '.', dirs_exist_ok=True)


def init_repo(project_path=None):
    """Init a repository on project"""
    if project_path:
        os.chdir(project_path)
    subprocess.run(['git', 'init'])


def readme_fill(project_name, project_path=None):
    """Fill the README file with project infos"""
    if project_path:
        os.chdir(project_path)

    with open('README', 'r+') as readme:
        file_text = readme.read()
        file_text = file_text.replace('<project_name>', project_name)
        readme.seek(0)
        readme.write(file_text)
        readme.truncate()
