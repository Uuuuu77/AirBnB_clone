#!/usr/bin/python3
"""
    module/__init__.py module
"""


from models.engine.file_storage import FileStorage
store = FileStorage()
storage.reload()
