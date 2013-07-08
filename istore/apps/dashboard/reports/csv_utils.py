# -*- coding: utf-8 -*-
import codecs
from io import TextIOWrapper
import csv
from six.moves import cStringIO


# These classes are copied from http://docs.python.org/2/library/csv.html


class CsvUnicodeWriter(object):
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()
        # Write BOM into file
        self.stream.write(codecs.BOM_UTF8)

    def cast_to_str(self, obj):
        if isinstance(obj, str):
            return obj.encode('utf-8')
        elif isinstance(obj, str):
            return obj
        elif hasattr(obj, '__str__'):
            # return unicode(obj).encode('utf-8')
            return str(obj)
            # return bytes(obj).encode('utf-8')
        elif hasattr(obj, '__str__'):
            return str(obj)
        else:
            raise TypeError('Expecting unicode, str, or object castable'
                            ' to unicode or string, got: %r' % type(obj))

    def writerow(self, row):
        self.writer.writerow([self.cast_to_str(s) for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


class UTF8Recoder(object):
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """

    def __init__(self, f, encoding):
        # self.reader = codecs.getreader(encoding)(f)
        self.reader = TextIOWrapper(f, encoding = encoding)

    def __iter__(self):
        return self

    def __next__(self):
        # return self.reader.__next__().encode("utf-8")
        return self.reader.__next__()


class CsvUnicodeReader(object):
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwargs):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwargs)

    def __next__(self):
        row = self.reader.__next__()
        # return [unicode(s, "utf-8") for s in row]
        return [str(s) for s in row]

    def __iter__(self):
        return self
