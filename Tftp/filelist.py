from Peach.Mutators.string import _SimpleGeneratorMutator
from Peach.Engine.dom import *
from Peach.Engine.common import *

from Tftp.randomdict import RandomDict

class FileListMutator(_SimpleGeneratorMutator):
    def __init__(self, peach, node):
        _SimpleGeneratorMutator.__init__(self, peach, node)
        FileListMutator.weight = 2
        self.name = "FileListMutator"
        self._generator = RandomDict(None, None)

    @staticmethod
    def supportedDataElement(node):
        return False
    
    def randomMutation(self, node, rand):
        self.changedName = node.getFullnameInDataModel()
        self._generator.setRand(rand)
        node.currentValue = self._generator.next()


class DownloadFileListMutator(FileListMutator):
    """
    Example: <String><Hint name="type" value="downloadfilelist"></String>
    """
    def __init__(self, peach, node):
        FileListMutator.__init__(self, peach, node)
        DownloadFileListMutator.weight = 2
        self.name = "DownloadFileListMutator"
        self._generator.setFilename("Tftp/downloadFileList.txt")

    @staticmethod
    def supportedDataElement(node):
        if isinstance(node, String) and node.isMutable:
            for child in node.hints:
                if child.name == 'type' and child.value == 'downloadfilelist':
                    return True
        return False


class UploadFileListMutator(FileListMutator):
    """
    Example: <String><Hint name="type" value="uploadfilelist"></String>
    """
    def __init__(self, peach, node):
        FileListMutator.__init__(self, peach, node)
        UploadFileListMutator.weight = 2
        self.name = "UploadFileListMutator"
        self._generator.setFilename("Tftp/uploadFileList.txt")

    @staticmethod
    def supportedDataElement(node):
        if isinstance(node, String) and node.isMutable:
            for child in node.hints:
                if child.name == 'type' and child.value == 'uploadfilelist':
                    return True
        return False
