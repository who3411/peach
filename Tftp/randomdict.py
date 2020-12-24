import io

from Peach import generator, group
from Peach.generator import *
from Peach.Generators.dictionary import Dictionary

class RandomDict(Dictionary):
    
    _values = None
    
    def __init__(self, group, fileName):
        """
        @type   group: Group
        @param  group: Group this Generator belongs to
        @type   fileName: string
        @param  fileName: Name of file use
        """
        Dictionary.__init__(self, group, fileName)
        self._fileName = fileName
        self.setGroup(group)
    
    def setRand(self, rand):
        self._rand = rand

    def next(self):
        if self._values is None:
            try:
                self._fd = io.open(self._fileName, 'r', encoding='utf-8')
                if self._fd is None:
                    raise Exception('Unable to open', self._fileName)
                self._values = [i.encode('utf-8').rstrip('\r\n') for i in self._fd.readlines()]
            except Exception as e:
                raise
        oldValue = self._currentValue
        self._currentValue = self._rand.choice(self._values)
        return self._currentValue
    
    def getRawValue(self):
        if self._values is None:
            try:
                self._fd = io.open(self._fileName, 'r', encoding='utf-8')
                if self._fd is None:
                    raise Exception('Unable to open', self._fileName)
                self._values = [i.encode('utf-8') for i in self._fd.readlines()]
            except Exception as e:
                raise
        oldValue = self._currentValue
        self._currentValue = self._rand.choice(self._values)
        return self._currentValue
