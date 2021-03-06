from setuptools import setup


setup(
    name='GIG',
    version='1.0',
    py_modules=['cli'],
    install_requires=[
        'Click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        gig=cli:cli
    ''',
    include_package_data=True,
)