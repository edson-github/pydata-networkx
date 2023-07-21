## Credits: Eric Ma for the installation scripts

# Check that the packages are installed.
from pkgutil import iter_modules
import sys


def check_import(packagename):
    return packagename in (name for _, name, _ in iter_modules())

packages = ['networkx', 'numpy', 'matplotlib', 'pandas',
            'jupyter']

all_passed = True

for p in packages:
    assert check_import(p),\
        '{0} not present. Please install via pip or conda.'.format(p)

assert sys.version_info.major >= 3, 'Please install Python 3!'

# Credit: @zmilicc for requesting this.
if all_passed:
    print('All checks passed. Your environment is good to go!')

