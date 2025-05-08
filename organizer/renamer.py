import os

class FileRenamer:
  def __init__(self,organized_files):
    self.renamed_files = organized_files
  def rename(self):
    for category, files in self.renamed_files.items():
        for file in files:
          answr=input("enter yes to use ai to rename else enter no")
          if answr.lower()=="yes":
            try:
              airenamer(category, file)
            except Exception as e:
              print(f"an error occured while trying to rename using ai{e})
          else:
            name = f"{os.path.gettime(file)}.{os.path.splitext(file)[1]}"
            os.rename(file)
            print(f"file renamed to {name}")

   def airenamer(self,category,file):
    from google import genai
    print("enter your gemini 1.5 flash api key : (if you don't have one, get it from https://makersuite.google.com/app/apikey)")
    api = input()
    client = genai.Client(api_key=api)
    if category == "docs":
        ext = os.path.splitext(file)[1].lower()
        if ext in [".txt",".json"]:
            content = open(file, "r").read()
            if len(content) > 1000:
                content = content[:1000]
            response = client.models.generate_content(
                model="gemini-1.5-flash", contents=f"suggest a suitable title for this file: {content}"
            )
            name = f"{response.text}{ext}"
            os.rename(file, name)
            print(f"changed file to {name}")

          
            
              

            
