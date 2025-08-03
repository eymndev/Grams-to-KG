from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='Grams-to-KG',
    version='0.1.0',
    python_requires<='3.9'
    author='eymndev',
    author_email='eymenyildirim13@icloud.com',
    description='auto convert Grams to KG',
    url='https://github.com/eymndev/Grams-to-KG',
    license='GPLv3',
    install_requires=requirements,
    py_modules=[
        'packages=['lib_Grams_to_KG']',
    ],
)
