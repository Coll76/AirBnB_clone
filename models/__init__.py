#!/usr/bin/python3
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.__file_path = "file.json"
storage.reload()
