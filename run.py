import os
import sys

# Get the path to the main.py file
main_py_file = os.path.join(os.getcwd(), '../main.py')

# Run the main.py file
sys.argv = ['python', main_py_file]

# Execute the main.py file
if __name__ == '__main__':
  import src.main as main