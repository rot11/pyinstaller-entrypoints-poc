import sys
from os.path import abspath, join, dirname, pardir

from main.use_entry_points import use_entry_points

print('Running runner')
if getattr(sys, 'frozen', False):
    plugins_path = abspath(join(dirname(abspath(sys.executable)), pardir, pardir, 'plugins'))
else:
    plugins_path = join(dirname(abspath(__file__)), 'plugins')

use_entry_points(plugins_path)
print('Ending runner')
