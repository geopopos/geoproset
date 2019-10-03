import click, os, shutil

@click.command()
@click.option('-d', '--directory')
@click.option('-r', '--root')
@click.argument('project_name')
def main(directory, root, project_name):
    # Make copy of skeleton project directory to location of new project
    click.echo('Creating new project: {}'.format(project_name))
    if not directory:
        directory = './'
    module_directory = os.path.abspath(os.path.dirname(__file__))
    skeleton_directory = os.path.join(module_directory, 'skeleton/')
    project_directory = '{}{}/'.format(directory, project_name)
    shutil.copytree(skeleton_directory, project_directory)
    # Rename the root module
    initial_module = '{}NAME/'.format(project_directory)
    if root:
        root_module = '{}{}/'.format(project_directory, root)
        click.echo('Renaming root module: {}'.format(root))
    else:
        root_module = '{}{}/'.format(project_directory, project_name)
        click.echo('Renaming root module: {}'.format(project_name))
    shutil.move(initial_module, root_module)
    # Rename the tests file
    initial_test = '{}tests/NAME_test.py'.format(project_directory)
    if root:
        module_test = '{}tests/{}_test.py'.format(project_directory, root)
        click.echo('Renaming {} to {}'.format(initial_test, module_test))
    else:
        module_test = '{}tests/{}_test.py'.format(project_directory, project_name)
        click.echo('Renaming {} to {}'.format(initial_test, module_test))
    os.rename(initial_test, module_test)
