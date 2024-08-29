from setuptools import find_packages,setup
from typing import List


HYPHEN_EDOT =  '-e . '

def get_requirements(file_path:str)->List[str]:
    
    requirements=[]
    with open (file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if  HYPHEN_EDOT in requirements:
            requirements.remove(HYPHEN_EDOT)
                
    return requirements
    
            


setup(
name='mymlproject', 
version='0.0.1',
author = 'Javvad',
author_email = 'javvadraza456@gmail.com',
packages=find_packages(),
install_requires= get_requirements('requirements.txt')
)

