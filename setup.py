"""
setup.py
==========

Sets up the project as a package
"""

# importing the needed libraries
from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'

# defining the function to install
def get_requirements(file_path) -> List[str]:
    """Installs the requirements file"""

    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


# setting up the project package
setup(
    name='math_score_model',
    version='0.0.1',
    author='Irene Busah',
    author_email='ibusah@andrew.cmu.edu',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
