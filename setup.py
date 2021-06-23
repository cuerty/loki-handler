# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="loki-handler",
    version="0.1.0",
    description="Python logging handler for Grafana Loki.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Angel Freire",
    author_email="cuerty@gmail.com",
    url="https://github.com/cuerty/loki-handler",
    packages=setuptools.find_packages(exclude=("tests",)),
    python_requires=">=2.7",
    install_requires=["rfc3339>=6.1", "requests"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Logging",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
