import setuptools

setuptools.setup(
    name="plugin",
    version="0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    packages=setuptools.find_packages(),
    entry_points={
        'print_text': [
            'plugin_print_text = plugin.entry_points:print_text'
        ]
    }
)