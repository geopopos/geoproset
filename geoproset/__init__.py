import click, os, shutil, json

@click.command()
@click.option('-l', '--location')
@click.option('-r', '--root')
@click.option('-d', '--description')
@click.option('-a', '--author')
@click.option('-e', '--email')
@click.argument('project_name')
def main(location, root, description, author, email, project_name):
    # Make copy of skeleton project directory to location of new project
    click.echo('Creating new project: {}'.format(project_name))
    if not location:
        location = './'
    module_directory = os.path.abspath(os.path.dirname(__file__))
    skeleton_directory = os.path.join(module_directory, 'skeleton/')
    project_directory = '{}{}/'.format(location, project_name)
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
    with open(module_test, 'r') as read_file:
        test_file = read_file.read()
    test_file = test_file.replace("NAME", project_name)
    with open(module_test, 'w') as write_file:
        write_file.write(test_file)
    # Update config.json
    click.echo("Updating config file...")
    config_file = '{}config.json'.format(project_directory)
    with open(config_file, 'r') as read_file:
        config = json.load(read_file)
    config["description"] = description or project_name
    config["name"] = project_name
    config["author"] = author or config["author"]
    config["author_email"] = email  or config["author_email"]
    config["packages"].remove("NAME")
    config["packages"].append(project_name)
    with open(config_file, 'w') as write_file:
        json.dump(config, write_file)
