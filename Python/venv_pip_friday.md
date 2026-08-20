# Check python version
python --version

# Create virtual environment
python -m venv myenv

# Activate venv
myenv\Scripts\activate

# Check pip
pip --version

# Upgrade pip
python -m pip install --upgrade pip

# Install numpy
pip install numpy

# Install pandas
pip install pandas

# See installed packages
pip list

# Get package details
pip show numpy

# Save packages
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Remove a package
pip uninstall numpy

# Exit venv
deactivate