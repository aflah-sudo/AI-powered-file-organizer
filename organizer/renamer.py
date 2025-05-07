import os

class FileRenamer:
  def __init__(self,organized_files):
    self.renamed_files = organized_files
  def rename(self):
    for category, files in self.renamed_files.items():
        for file in files:
          answr=input("enter yes to use ai to rename else enter no")
          if answr.lower()==yes:
            from google import genai
            print("entert your gemini 1.5 flash api key : (if you dont have one, get it from https://makersuite.google.com/app/apikey)")
            api = input()
            client = genai.Client(api_key=api)
            if category == docs:
              ext=os.path.splitext(file)[1]
              if ext.lower()==txt:
                content = open(file,"r").read()
                if len(content)>1000:
                  content=content[:1000]
                response = client.models.generate_content(
                    model="gemini-1.5-flash", contents=f"suugest a a suitable name for title for this file{content}"
                )
                name = f"{response.text}.txt"
                os.rename(file,name)
                print(f"changed file to {name}")
          else:
            name = f"{os.path.get.time(file)}.{os.path.splitext(file)[1]}"
            os.rename(file)
            print(f"file renamed to {name}")
          
            
              

            