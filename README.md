# TDD
A simple example on how to use and implement Test Driven Development in Python

## Code Execution
`python -m unittest discover` - to execute all tests cases in test suite and to be able to discover where are we storing tests.

`python -m unittest discover -v` - output for tests is verbose

To be able to import modules from different directories:
* we must create a __init__.py file in each directory to be considered as a package. Since Python 3.0 this is not supposed to be necessary, nevertheless, it didn't work in my environment. Init file is empty, it's only a marker for the interpreter to know there is Python code in the underlying directory.
* Look at line 3 on `test_calculadora.py` to realize how to import modules from other directories.

##### Code, idea, examples taken from:
######
###### * https://realpython.com/absolute-vs-relative-python-imports/
###### * hektorprofe.net/tutorial/ejemplo-muy-facil-tdd-python
###### * Python Official Documentation: https://docs.python.org/


