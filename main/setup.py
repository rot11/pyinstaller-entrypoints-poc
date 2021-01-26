import setuptools

setuptools.setup(
    name="main",
    version="0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    packages=setuptools.find_packages(),
    entry_points={
        'print_text': [
            'main_print_text = main.entry_points:print_text'
        ]
    }
)