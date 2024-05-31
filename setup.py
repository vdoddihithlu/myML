from setuptools import find_packages, setup
from typing import List

def get_pypackages(file_path:str) -> List[str]:
    '''
    list all packages to be installed
    '''
    pkglist =[]
    with open (file_path) as file_obj:
        pkglist = file_obj.readlines()
        pkglist = [pkg.replace("\n"," ") for pkg in pkglist]
      #  for pkg in pkgs:
      #      pkg=pkg.replace("/n","")
      #      pkglist.append(pkg)

        if "-e ." in pkglist:
            pkglist.remove("-e .")

    return pkglist



setup (
    name = 'mlproject',
    version='0.0.1',
    author='vidya',
    packages=find_packages(),
    install_requires=get_pypackages('requirments.txt')
)