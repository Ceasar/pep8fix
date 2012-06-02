import os
import shutil


class swap(file):
    """Swap file context manager.

    Creates a swap file that can be written to and upon termination,
    if no errors are raised, the swap file will replace the original.
    """
    def __init__(self, name, mode='w', buffering=None):
        self.prime_name = name
        if buffering:
            super(swap, self).__init__(name + '$', mode, buffering)
        else:
            super(swap, self).__init__(name + '$', mode)

    def __exit__(self, type, value, traceback):
        super(swap, self).__exit__(type, value, traceback)
        if traceback is None:  # Copies the content if no exception was thrown
            print "Write succeeded."
            shutil.copyfile(self.name, self.prime_name)
        else:
            print "Write failed."
        os.remove(self.name)
