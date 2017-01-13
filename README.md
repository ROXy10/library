# How to run project

### In command line
##### create directory project
`mkdir library`

`cd library`
##### create virtualenv
`virtualenv --no-site-packages -p python3.5 venv_library`
##### create virtualenv
`source venv_library/bin/activate`
##### install Django frameworks
`pip install Django==1.10.5`
##### clone project with GitHub and start django project
`django-admin.py startproject --template=https://github.com/ROXy10/Library.git --name=Procfile library`

`cd library`
##### install Django packages
`pip install -r requirements.txt`