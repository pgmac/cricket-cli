cricket-cli
===========

.. image:: https://travis-ci.org/cbirajdar/cricket-cli.svg
    :target: https://travis-ci.org/cbirajdar/cricket-cli

.. image:: https://img.shields.io/pypi/pyversions/cricket-cli.svg
    :target: https://pypi.python.org/pypi/cricket-cli

Command line interface for cricket enthusiasts


Installation
------------

pip install cricket-cli

Demo
----

.. image:: https://github.com/cbirajdar/cricket-cli/blob/master/cricket-cli.gif


Usage
-----

* cricket -h
    usage: cricket [-h] {scores,rankings,standings}

* cricket scores
    Live cricket scores

* cricket --team=Australia scores
    Specify a team name to get only their scores

* cricket rankings
    ICC player rankings

* cricket standings
    ICC team standings

Building cricket-cli
--------------------

* Install setuptools and wheel
    python3 -m pip install --user --upgrade setuptools wheel

* python3 setup.py sdist bdist_wheel

Installing from built package
-----------------------------

* python3 -m pip install dist/cricket-cli-<version>.tar.gz
