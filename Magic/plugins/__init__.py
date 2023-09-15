from glob import glob
from os.path import basename, dirname, isfile

def loadPlugins():
    jalur = glob(f"{dirname(__file__)}/*.py")
    return sorted(
        [
            basename(f)[:-3]
            for Magic in jalur
            if isfile(Magic) and Magic.endswith(".py") and not Magic.endswith("__init__.py")
        ]
    )
