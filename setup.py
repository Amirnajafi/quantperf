from setuptools import setup, find_packages

from quant_performance.version import Version
import io
from os import path

here = path.abspath(path.dirname(__file__))
with io.open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requirements = [line.rstrip() for line in f]
    
from pathlib import Path
this_directory = Path(__file__).parent
README = (this_directory / "README.md").read_text()

setup(
    name='quant_performance',
    version=Version('0.0.1').number,
    description='This is a package for calculating performance metrics for quantitative finance',
    long_description_content_type="text/markdown",
    long_description=README,
    author='Amir najafi',
    author_email='contact@amirnajafi.com',
    url='https://github.com/amirnajafi/quantperf',
    license='MIT License',
    zip_safe=False,
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples']),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },

    include_package_data=True,
    platforms=['any'],
    keywords="quant algotrading algorithmic-trading quantitative-trading quantitative-analysis algo-trading visualization plotting",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Science/Research',
        'Topic :: Office/Business :: Financial',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        # 'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ])
