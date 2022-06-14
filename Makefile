test:
	pytest

clean:
	find . -name __pycache__ | xargs rm -r
	find . -name .pytest_cache | xargs rm -r
