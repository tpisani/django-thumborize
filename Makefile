install:
	@pip install -e .

clean:
	@find . -name "*.pyc" -print0 | xargs -0 rm -rf
	@rm -rf dist build

test: clean
	@python runtests.py

sdist:
	@python setup.py sdist
