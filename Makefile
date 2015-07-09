install:
	python setup.py install

develop:
	python setup.py develop

pypi-test-register:
	python setup.py register -r pypitest

pypi-test-upload:
	python setup.py sdist upload -r pypitest

pypi-live-register:
	python setup.py register -r pypi

pypi-live-upload:
	python setup.py sdist upload -r pypi

