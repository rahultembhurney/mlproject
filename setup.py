from setuptools import find_packages, setup

EXCLUSION = "-e ."

def get_requirements(file_path):
    requirements =[]

    with open(file_path) as file_obj:
        lines = file_obj.readlines()
        lines = [line.strip() for line in lines]

        for line in lines:
            if line in EXCLUSION:
                pass
            else:
                requirements.append(line)
    
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Rahul Tembhurney",
    author_email="rtembhurney7@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)

