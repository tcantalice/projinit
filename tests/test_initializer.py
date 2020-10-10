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


def test_readme_fill(tmpdir):
    name = 'Project'
    creator = 'John Doe'
    mail = 'mail@mail.com'

    initializer.readme_fill(
        name,
        creator_name=creator,
        creator_mail=mail,
        project_path=tmpdir
    )

    tree = os.listdir(tmpdir)
    assert 'README' in tree

    file_path = os.path.join(tmpdir, 'README')

    content = ''
    with open(file_path, 'r') as file:
        content = file.read()

    assert name in content
    assert mail in content
    assert creator in content