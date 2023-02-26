package_name = pywobble

#test:
#	python -m pytest -s tests/

#coverage:
#	coverage run --source=$(package_name) -m pytest tests/
#	coverage report -m
#	coverage html
#	xdg-open htmlcov/index.html

lint:
	black *.py
	flake8 *.py
#	black $(package_name) tests setup.py --line-length 80
#	flake8 $(package_name) tests

#clean:
#	rm -rvf cover $(package_name).egg-info/ htmlcov dist *~

#dist_test:
#	rm -rvf dist
#	python setup.py sdist
#	twine upload -r test dist/*

#dist_production:
#	rm -rvf dist
#	python setup.py sdist
#	twine upload dist/*
