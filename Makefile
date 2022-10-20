setup:
	echo "TODO: create virtual python3 environment & install dependencies"

test: fixmkdlines.py
	python3 fixmkdlines.py $(file_path)
