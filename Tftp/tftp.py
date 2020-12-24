import os
import tftpy
from tftpy.TftpShared import TftpTimeout
import time
import socket
import struct
import sys

from Peach.publisher import Publisher
import Peach


class Tftp(Publisher):
    """
    A simple TFTP client publisher.
    """


    def __init__(self, host, port):
        """
        @type	host: string
        @param	host: Remote host
        @type	port: number
        @param	port: Remote port
        """
        Publisher.__init__(self)
        self.host = host
        self.port = int(port)
        self.withNode = True
        self.client = tftpy.TftpClient(self.host, self.port)

    def start(self):
        pass

    def stop(self):
        pass

    def connect(self):
        """
        Create connection.
        """
        pass

    def close(self):
        """
        Close connection if open.
        """
        pass

    #def send(self, data):
    #    """ 
    #    Send data via sendall.
    #    @type   data: string
    #    @param  data: Data to send
    #    """
    #    try:
    #        self.client.rawdata(data)
    #    except TftpTimeout:
    #        raise PublisherSoftException("failed: " + str(sys.exc_info()[1]))

    def sendWithNode(self, data, dataNode):
        '''
        Publish some data

        @type   data: string
        @param  data: Data to publish
        @type   dataNode: DataElement
        @param  dataNode: Root of data model that produced data
        '''
        params = dict()
        param_list = ["opcode", "filename", "mode"]
        for child in dataNode.getAllChildDataElements():
            if child.name in param_list:
                if child.get_Value() is None:
                    params[child.name] = ""
                else:
                    params[child.name] = child.get_Value()
        
        try:
            self.client.rawdata(params["opcode"], params["filename"], params["mode"])
        except KeyboardInterrupt:
            raise
        except:
            pass
