import sys
import gdb

# Update module path.
dir_ = '/home/work/cross/arm-2014.05/arm-none-linux-gnueabi/libc/usr/share/glib-2.0/gdb'
if not dir_ in sys.path:
    sys.path.insert(0, dir_)

from glib import register
register (gdb.current_objfile ())
