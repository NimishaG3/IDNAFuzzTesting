import atheris
import sys

with atheris.instrument_imports(): #instrument only this library
    import idna                     # we don't want to trigger other library

@atheris.instrument_func
def TestOneInput(data):
    try:
        idna.decode(data)   #this is the function we're testing
    except idna.IDNAError:  #catch around function -- is part of norm handling
        pass

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
