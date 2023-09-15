from importlib import import_module
from logging import getLogger

from Magic.plugins import sortir

getLogger(__name__)


async def loadPlugins():
    xx = sortir()
    for x in xx:
        import_module(f"Magic.plugins.{x}")
    print("Succesfully Importing Modules")
