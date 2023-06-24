from django.core.files.storage import FileSystemStorage

class VercelFileSystemStorage(FileSystemStorage):
    def __init__(self, location=None, **kwargs):
        super().__init__(location, **kwargs)
        self.location = '/tmp'