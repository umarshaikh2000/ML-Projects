from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='ML_Project',
    packages=find_packages(),
    version='0.0.1',
    description='This is a project for the MLOps Zoomcamp',
    author='Gurpreet Singh',
    author_email='umar.shaikh02@outlook.com',
    license='MIT',
    install_requires=[get_requirements('requirements.txt')]
)