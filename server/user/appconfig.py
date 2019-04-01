from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings

MB_ROOT = getattr(settings, 'MEDIA_FILE_ROOT',
                  os.path.join(settings.BASE_DIR, 'media_files'))
MB_STORAGE = FileSystemStorage(location=MB_ROOT)
