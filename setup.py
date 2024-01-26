from setuptools import setup, find_packages

setup(name='libpy',
    version='0.0.1',
    description='Custom python codebase and utils',
    packages=find_packages(),
    install_requires=[
        'typing'
    ],
    license='MIT',
    python_requires='>=3.12.0',
    author='Albert Sáez')
