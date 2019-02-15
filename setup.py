from setuptools import setup, find_packages

setup(
    name='korkuts-translater',
    version='0.1',
    author='Kanstantsin Koruts',
    author_email='znemozero@mail.ru',
    py_modules=['app'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'yandex-translater',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        korkuts-translater=app:translate
    '''
)
