from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Malatesh Kittur',
    author_email='malateshsony@gmail.com',
    install_requirements= ["openai", "langchain", "stremlite", "python-dotenv","PyPDF2"],
    package=find_packages()
)