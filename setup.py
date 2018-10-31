from setuptools import setup

setup(
    name='deltaP',
    description=(
        'Calculate pressure drop in a straight pipe.'),
    keywords=['pipe', 'pressure drop', 'calculation', 'incompressible'],
    url='',
    author='Richard Bell',
    author_email='',
    version='0.1',
    license='',
    install_requires=[
        ''
    ],
    extras_require={
        'test': ['flake8', 'pytest', 'pytest-cov']
    },
    entry_points={
        'console_scripts': [
            'deltaP=deltaP:main'
        ]
    }
)
