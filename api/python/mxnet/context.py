# coding: utf-8
""" code for context management """
from __future__ import absolute_import

class Context:
    """Context representing device and device id in mxnet"""
    # static class variable 
    default_ctx = None
    devmask2type = { 1: 'cpu', 2: 'gpu'}
    devtype2mask = {'cpu': 1, 'gpu': 2 }
    
    def __init__(self, device_type, device_id = 0):
        """Constructing a context

        Parameters
        ----------
        device_type : str (can be 'cpu' or 'gpu')
            a string representing the device type

        device_id : int (default=0)
            the device id of the device, needed for GPU
        """
        self.device_mask = Context.devtype2mask[device_type]
        self.device_id = device_id

    @property
    def device_type(self):
        return Context.devmask2type[self.device_mask]

    def __str__(self):
        return 'Context(device_type=%s, device_id=%d)' % (
            self.device_type, self.device_id)

    def __repr__(self):
        return self.__str__()

    def __enter__(self):
        self._old_ctx = Context.default_ctx
        Context.default_ctx = self
        return self

    def __exit__(self, type, value, trace):
        Context.default_ctx= self._old_ctx

# initialize the default context in Context        
Context.default_ctx = Context('cpu', 0)

def current_context():
    """Return the current context"""
    return Context.default_ctx
