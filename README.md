# psgc_etl
ETL process for loading PSGC data into database

#### Start of Pre-requisites ####
# Setup WSL venv
sudo apt install python-is-python3
sudo apt install python 3.12-venv

# Activate the venv on VSCode
source .venv/bin/activate

# Install the requirements first
pip install -r requirements.txt

#### End of Pre-requisites ####


#### Start of Doing Git ####
git init
git status
nano .gitignore //for ignoring .venv files 
git add .
git commit -m "[commit message]"

# Create git repo on browser then 
git remote add origin https://github.com/stephanopineda/psgc_etl.git
git branch -M main
git push -u origin main
#### End of Doing Git ####


#### Start of Running the Scripts ####
cd dev_projects/psgc_etl/
python etl/extract.py

#### End of Running the Scripts