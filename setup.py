from setuptools import setup

install_requires = [
    "grequests==0.7.0",
    "feedparser==6.0.11",
    "beautifulsoup4==4.13.4",
    "terminaltables==3.1.10"
]

setup(
    name='cricket-cli',
    description='Command-line interface for cricket enthusiasts',
    long_description=open('README.rst').read(),
    version='1.0.0b4',
    packages=['cricket'],
    url='http://github.com/pgmac/cricket-cli',
    author='Paul Macdonnell',
    author_email='paulymac@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=install_requires,
    entry_points={
        "console_scripts": ['cricket = cricket.__main__:main'],
    }
)
