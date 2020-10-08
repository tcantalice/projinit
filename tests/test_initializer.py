import os

from projinit import initializer

PROJECT_NAME_TEST = 'Project'


def test_single_file_module(tmpdir):
    initializer.single_file_module(tmpdir, 'module')
    tree = os.listdir(tmpdir)

    assert 'module.py' in tree


def test_folder_module(tmpdir):
    module_name = 'module'
    initializer.folder_module(tmpdir, module_name)
    tree = os.listdir(tmpdir)

    assert module_name in tree

def test_folder_module_init(tmpdir):
    module_name = 'module'
    initializer.folder_module(tmpdir, module_name)
    module_path = os.path.join(tmpdir, module_name)
    tree = os.listdir(module_path)

    assert '__init__.py' in tree


def test_init_repo(tmpdir):
    initializer.init_repo(tmpdir)

    tree = os.listdir(tmpdir)
    assert '.git' in tree
