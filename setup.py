from setuptools import setup, find_packages
import os

here = os.path.dirname(os.path.realpath(__file__))

def read_file(filename: str):
    try:
        lines = []
        with open(filename) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines if not line.startswith('#')]
        return lines
    except:
        return []

DESCRIPTION = "🕸️ ControlNet - Adding Conditional Control to Text-to-Image Diffusion Models"

setup(name="controlnet",
    version="0.0.1.dev0",
    author="Shadow Walker",
    author_email="shadowwalker2718@gmail.com",
    description=DESCRIPTION,
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    install_requires=read_file(f"{here}/requirements.txt"),
    keywords=[
        "ControlNet",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    url="https://github.com/shadowwalker2718/ControlNet",
    packages=find_packages()
    )





