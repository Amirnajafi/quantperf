import setuptools
from quantperf.version import Version
import io
from os import path

here = path.abspath(path.dirname(__file__))
with io.open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requirements = [line.rstrip() for line in f]


setuptools.setup(name='QuantPerf',
                 version=Version('1.0.0').number,
                 description='This is a package for calculating performance metrics for quantitative finance',
                 long_description=open('README.md').read().strip(),
                 author='Amir najafi',
                 author_email='contact@amirnajafi.com',
                 url='https://github.com/amirnajafi/quantperf',
                 py_modules=['quantperf'],
                 install_requires=requirements,
                license='MIT License',
                zip_safe=False,
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
