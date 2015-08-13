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

```
./pydeep.py base64
WARNING: sys (base64.re.sys)
```

```
./pydeep.py enum
WARNING: sys (enum.sys)
```

```
./pydeep.py getpass
WARNING: sys (getpass.sys)
WARNING: sys (getpass.warnings.sys)
WARNING: os (getpass.os)

./pydeep.py numpy
WARNING: sys (numpy.rec.sb.pickle.codecs.sys)
WARNING: sys (numpy.rec.sb.pickle.re.sys)
WARNING: os (numpy.rec.sb.os)
WARNING: os (numpy.rec.os)
```

```
./pydeep.py uuid
WARNING: sys (uuid.ctypes.util.contextlib.sys)
WARNING: sys (uuid.ctypes.util.re.sys)
WARNING: os (uuid.ctypes.util.subprocess.os)
WARNING: os (uuid.ctypes.util.os)
```

```
./pydeep.py yaml
WARNING: sys (yaml.constructor.sys)
WARNING: sys (yaml.constructor.re.sys)
```
