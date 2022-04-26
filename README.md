# Mocker_Unit_Tests_Example
A small repo to explain the use of Pytest Mocker to mock functions during testing. 

Link to **Medium** article that uses this repository - **add link**

# Setting Up

- (1) Clone the repository, https://github.com/Dseal95/Mocker_Unit_Tests_Example.git
- (2) (Optional) Set up a virtual environment by running the following commands:

```
python -m venv .venv
source .venv/bin/activate
```

- (3) Install requirements.txt:

```
cd src
pip install -r requirements.txt
```

- (5) Open up your IDE terminal  / CMD (windows) / terminal (Mac) and navigate to the root `/Mocker_Unit_Tests_Example/`:
- (5) Install the custom Python package `simple-package` by running,

```
pip install ./src
```

Or for installing in editable mode (advised when developing), add a `-e`: 

```
pip install -e ./src
```


Once complete, you will be able to successfully run the unit tests in `/tests`. You will get errors if you try to run /src/main.py as the functions were build to error for demonstrating mocker. 
