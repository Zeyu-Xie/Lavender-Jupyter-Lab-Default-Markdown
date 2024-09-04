from setuptools import setup, find_packages

setup(
    name="jupyterlab-default-markdown",
    version="0.1.0",
    description="A simple package to set default JupyterLab cell type to Markdown",
    long_description="This package automatically sets the default cell type in JupyterLab to Markdown by modifying the appropriate configuration file.",
    author="Acan Xie",
    author_email="xie.zeyu20@gmail.com",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'set-default-markdown = jupyterlab_default_markdown.__init__:set_default_cell_type_to_markdown',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
