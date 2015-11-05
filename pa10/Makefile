run:
	python blacklist.py < input.txt > output.txt

test:
	python test.py

cover:
	coverage run --branch blacklist.py < input.txt
	coverage report > coverage_report.txt
	coverage html
