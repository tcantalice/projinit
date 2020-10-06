import os
from os import path
import subprocess
import shutil

MODULE_DIR = path.dirname(path.abspath(__file__))

FOLDERS = ['tests']


def folders_create(project_name, root='.', database=False, resources=False):
    """Create folders tree of project"""
    project_dir = path.join(root, project_name)

    if not path.exists(project_dir):
        os.mkdir(project_dir)
        FOLDERS.append(project_name.lower())

        for folder in FOLDERS:
            folder = path.join(project_dir, folder)
            os.mkdir(folder)

    return path.abspath(project_dir)


def copy_stubs(project_path=None):
    """Copy stubs to root of project dir"""
    if project_path:
        os.chdir(project_path)
    stubs_path = path.join(MODULE_DIR, 'stubs')
    shutil.copytree(stubs_path, '.', dirs_exist_ok=True)


def virtualenv(py_version): ...


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
