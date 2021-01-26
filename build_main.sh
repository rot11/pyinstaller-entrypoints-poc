cd main
rm -rf build
rm -rf dist
rm -rf main.egg-info
python setup.py bdist_wheel
cd ..
pip uninstall -y main
pip install main/dist/main-0.1-py2-none-any.whl
