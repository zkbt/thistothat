# set the version of this package
__version__ = '0.1'

# are we setting up initially, or actually importing the package?
try:
    __THISTOTHAT_SETUP__
except NameError:
    __THISTOTHAT_SETUP__ = False

# this is where you could import things to have at the ready
if not __THISTOTHAT_SETUP__:
    from .Mamajek import Mamajek
    from .Covey import Covey
    from .Davenport import Davenport
    from .Baraffe import Baraffe
    from .Parsec import PARSEC

    def available():
        print('The variables defined in `thistothat` include:')
        print(locals())
