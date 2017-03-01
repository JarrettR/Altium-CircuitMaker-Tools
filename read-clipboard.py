from ctypes import *
from binascii import hexlify
from sys import getsizeof
import csv


with open("test.csv", "wb") as f:
    csv.writer(f).writerows((k, v) for k, v in coordDict.iteritems())

def what():
    kernel32 = windll.kernel32
    user32 = windll.user32

    user32.OpenClipboard(0)

    print user32
    format = 0
    formats = []
    max_size = 500
    buffer_ = create_unicode_buffer(max_size+1)

    while 1:
        format = user32.EnumClipboardFormats(format)
        if not format:
            break
        formats.append(format)

    print formats
    # Verify that the given formats are valid.
    try:
        for format in formats:
            if not isinstance(format, int):
                raise TypeError("Invalid clipboard format: %r"
                                % format)
            print '----  '
            print "Format:      ", format
            print "Format name: ", user32.GetClipboardFormatNameW(format, byref(buffer_), max_size)
            data = user32.GetClipboardData(format)
            data_locked = kernel32.GlobalLock(data)
            print "Data:        ", data
            print "Data locked: ", data_locked
            text = c_char_p(data_locked)
            print "Text:        ", text
            print "Hex Text:    ", hexlify(text)
            print hexlify(string_at(id(data_locked), getsizeof(data_locked)))
            print(hexlify(string_at(id(text), getsizeof(text))))
            print(hexlify(string_at(id(repr(text)), getsizeof(repr(text)))))
            kernel32.GlobalUnlock(data_locked)
    except Exception, e:
        raise
        
    user32.CloseClipboard()