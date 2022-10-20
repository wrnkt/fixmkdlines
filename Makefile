TEST_FILE=./test.md

setup:
	echo "TODO: create virtual python3 environment & install dependencies";
	python3 -m venv ./fixmkdvenv; echo "Virtual python3 environment created";
	source ./fixmkdvenv/bin/activate;
	pip3 install -r requirements.txt; echo "Install requirements";


test: fixmkdlines.py
	source ./fixmkdvenv/bin/activate;
	python3 fixmkdlines.py $(TEST_FILE)
	
