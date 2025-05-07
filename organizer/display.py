import os 

class SummaryDisplay:
  def __init__(self,organized_files):
    self.organized_files = organized_files
    self.display()
  def display(self):
    print("="*50)
    print("ORGANIZED FILES SUMMERY")
    print("="*50)
    for category,files in organaised.items():
        print(f"{category.upper()} : ")
        if not files:
            print(f"  -(empty)")
        else:
            total_size = 0
            for i in files:
                size=os.path.getsize(i)
                size_in_mb=size/(1024*1024)
                print(f"  -{i} : size : {size_in_mb} mb")
                total_size+=size_in_mb
            print(f" count of total files in folder : {len(files)}")
            print(f" total size of folder : {total_size} mb")