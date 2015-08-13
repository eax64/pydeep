# pydeep
Search for a sensivive module inside an other module.

You're writing a python jail and want to let the user access a whole python module. (without the private attributes)
It could be safe, but some modules are importing sensible modules (like `re` importing `sys`).

This little script try to find unsafe module imported inside your safe-looking module.

```
$> ./pydeep.py re
WARNING: sys (re.sys)
```

```
$> ./pydeep.py json
WARNING: sys (json.scanner.re.sys)
WARNING: sys (json.encoder.re.sys)
```

```
$> ./pydeep.py logging
WARNING: sys (logging.warnings.sys)
WARNING: sys (logging.sys)
WARNING: os (logging.os)
WARNING: os (logging.traceback.linecache.os)
```
