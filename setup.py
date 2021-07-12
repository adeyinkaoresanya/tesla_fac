from setuptools import setup, find_packages


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="tesla",
    version="0.1.1",
    description="demo tesla car factory",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/adeyinkaoresanya/tesla_fac",
    author="AdeyinkaOresanya",
    author_email="adeyinkaoresanya@gmail.com",
    keywords="core package",
    license="MIT",
    py_modules = ["tesla"],
    packages= find_packages('src'), 
    install_requires=[]
)
