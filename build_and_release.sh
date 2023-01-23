rm -rf build/ dist/
rm -rf src/**/__pycache__/

python setup.py bdist_wheel
twine upload dist/*.whl