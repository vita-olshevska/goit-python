from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1',
    description='Sort files according to their types (extensions).',
    url='https://github.com/vita-olshevska/goit-python/tree/main/Module7',
    author='Vita Olshevska',
    author_email='vaolshevska@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean_folder:clean_folder']}
)
