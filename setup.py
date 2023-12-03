from setuptools import setup


def readfile(filename):
    with open(filename, 'r+') as f:
        return f.read()


setup(
    name="lipandas",
    version="1.0.0",
    description="Load a CSV file into a Pandas DataFrame and open it in IPython.",
    long_description=readfile('README.md'),
    author="João Nogueira",
    author_email="joaopcnogueira@gmail.com",
    url="",
    py_modules=['lipandas'],
    license=readfile('LICENSE'),
    install_requires=['pandas', 'ipython'],
    long_description_content_type = 'text/markdown',
    entry_points={
        'console_scripts': [
            'lipandas = lipandas:main'
        ]
    },
)