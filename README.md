# how to
1. create virtualenv with python2 `virtualenv -p python2 pyinstaller-env`
1. activate virtualenv `source pyinstaller/bin/activate`
1. install requirements `pip install -r requirements.txt`
1. Run `./build_plugin.sh`
1. Run `./build_main.sh`
1. build runner with pyinstaller `pyinstaller runner.py`
1. run `./dist/runner/runner`
1. compare binary run with `python runner.py`
