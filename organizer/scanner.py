from organizer.config import files 
import os 

class DirectoryScanner:
  def __init__(self, file_mover):
    self.organaised = {'images': [], 'videos': [], 'docs': [], 'others': []}
    self.file_mover =file_mover
  def scan_directory(self, path):
    if not os.path.exists(path):
        print(f"path {path} does not exist ")
        return
    print(f"files in {path} ")
    print('*' * 100)

    for files1 in os.listdir(path):
        full_path = os.path.join(path, files1)
        if os.path.isfile(full_path):
            found = False
            size = os.path.getsize(full_path)
            #print(f"file name : {files1} size : {size}")
            file_type = os.path.splitext(files1)[1].lower()
            for category, ext in files.items():
                if file_type in ext:
                    self.organaised[category].append(files1)
                    found = True
                    self.file_mover.organize(full_path, category)
                    break

            if not found:
                self.organaised['others'].append(files1)
                self.file_mover.organize(full_path, 'others')

