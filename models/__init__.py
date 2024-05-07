from models.engine import file_storage
#from models.bas_model import BaseModel

storage = file_storage.FileStorage()
#Create a new instance of BaseModel and save it to the JSON file
#new_instance = BaseModel()
#new_instance.save()
# Reload the FileStorage instance to deserialize the JSON file
storage.reload()
