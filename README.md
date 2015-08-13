# pydeep
Search for a module inside an other module

You're writing a python jail and want to let the user access a whole python module. (without the private attribute)
It could be safe, but some modules are importing sensible modules (like re importing sys).

This little script try to find unsafe module imported inside your safe looking one.

```
$> ./pydeep.py re
WARNING: sys (re.sys)
```
