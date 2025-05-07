import os 
import shutil 
class FileMover:
  def __init__(self):
    pass
  def organize(self,file_to_organize, category_of_file):
    if not os.path.exists(os.path.join(os.getcwd(), category_of_file)):
        path = os.path.join(os.getcwd(), category_of_file)
        os.makedirs(path, exist_ok=True)
    path = os.path.join(os.getcwd(), category_of_file)
    try:
      shutil.move(file_to_organize, path)
    except Exception as e:
      print(f"an error occured while ntrying to move file {file_to_organize} : {e}")