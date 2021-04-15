from IPython import get_ipython
ipython = get_ipython()
# ipython.magic("...") is equivalent to % in Jupyter cell

# Find performance bottlenecks by timing Python cell execution
ipython.magic("load_ext autotime")

# Reload all modules (except those excluded by %aimport) every time before executing the Python code typed
# See https://ipython.org/ipython-doc/stable/config/extensions/autoreload.html
ipython.magic("load_ext autoreload")
ipython.magic("autoreload 2")

# Append the root directory to Python path,
# this allows you to store notebooks in `notebooks/` sub-directory and access model Python modules
import sys
sys.path.append("..")
