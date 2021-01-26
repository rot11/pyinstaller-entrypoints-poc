cd plugin
rm -rf build
rm -rf dist
rm -rf plugin.egg-info
python setup.py bdist_egg
cd ..
cp plugin/dist/plugin-0.1-py2.7.egg plugins
