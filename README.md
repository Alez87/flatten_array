The provided answer is based on a recursive solution that will scan and go deeper into the input array, until a primitive value is found.

For a more detailed explanation please refer to the Jupiter notebook file 'application_description.ipynb'

Automated tests code inside the file 'unittest_flatten_array.py'
To run the automated test, execute the script run_test.sh:
	bash run_test

How to run the code:
	python3 array_to_flatten.py [options] array
	es: python3 flatten_array.py '[[1, 2, [3]], 4]'
	The array attribute is optional. If not specified, is considered the default list [[1,2,[3]],4]

Code tested on Python 3.7.3.
