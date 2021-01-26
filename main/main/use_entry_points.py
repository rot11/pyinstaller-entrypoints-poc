from os.path import dirname, join, pardir, abspath

import pkg_resources


def use_entry_points(plugins_path):
    print('Plugins path is ' + plugins_path)
    distributions, errors = pkg_resources.working_set.find_plugins(pkg_resources.Environment([plugins_path]))
    for dist in distributions:
        print('Found dist ' + str(dist))
        pkg_resources.working_set.add(dist)

    for entrypoint in pkg_resources.iter_entry_points('print_text'):
        print_text_meth = entrypoint.resolve()
        print('Entrypoint ' + str(entrypoint))
        print_text_meth('Europe')


if __name__ == '__main__':
    plugins_path = abspath(join(dirname(abspath(__file__)), pardir, pardir, 'plugins'))
    use_entry_points(plugins_path)
