from myModule import my_func
from myMainPackage import someMainScript
from myMainPackage.subPackage import mySubScript

# init__.py file is required,
# that python will understand, that it's module folder

my_func()
someMainScript.main_report()
mySubScript.sub_report()
