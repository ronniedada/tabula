from setuptools import setup, find_packages

version = '1.0.2'

setup(
    name = 'tabula',
    version = version,
    description = "Ascii table",
    url = "https://github.com/ronniedada/tabula",
    long_description = open("README.md").read(),
    classifiers = [
        "Intended Audience :: Developers",
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        "Operating System :: POSIX",
        "License :: OSI Approved :: Apache Software License",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Terminals'
        ],
    keywords = ['couchbase', 'terminal', 'ascii', 'table', 'numpy', 'curses'],
    author = "Ronnie Sun",
    author_email = "ronnie@couchbase.com",
    license="Apache Software License",
    packages = find_packages(exclude=['ez_setup']),
    include_package_data = True,
    install_requires = [
        'setuptools',
        'numpy',
        ],
)
