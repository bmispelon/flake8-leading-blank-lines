import setuptools


def get_version():
    with open('flake8_leading_blank_lines.py') as f:
        lines = [line.strip() for line in f if line.startswith('__version__')]

    for line in lines:
        _, versionstr = line.split('=', 1)
        return versionstr.strip(' "\'')

    raise Exception("__version__ not found in flake8_leading_blank_lines.py")


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="flake8-leading-blank-lines",
    license="MIT",
    version=get_version(),
    description="A flake8 plugin to detect blank lines at the start of a file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Baptiste Mispelon",
    author_email="bmispelon@gmail.com",
    url="https://github.com/bmispelon/flake8-leading-blank-lines",
    project_urls={
        "Bug Tracker": "https://github.com/bmispelon/flake8-leading-blank-lines/issues",
    },
    py_modules=["flake8_leading_blank_lines"],
    install_requires=[
        "flake8 > 3.0.0",
    ],
    entry_points={
        'flake8.extension': [
            'LBL001 = flake8_leading_blank_lines:plugin',
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
