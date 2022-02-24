rm -rf build dist QuantPerf.egg-info
twine check dist/*
python setup.py check
python setup.py sdist  
python setup.py bdist_wheel --universal
python setup.py bdist_wheel       
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*
twine upload  dist/*