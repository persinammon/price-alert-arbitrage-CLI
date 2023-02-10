# Run make 'command' for manual trigger of init and test. CI/CD pipeline also runs tests after push to main

init:
	python3 -m venv venv
	. venv/bin/activate
    pip install -r requirements.txt

test:
	. venv/bin/activate
	flake8 --exclude=venv* --statistics
	pytest -v --cov

