# 🗂️ File Organizer with AI Renaming

*Tired of Having Messy Files? Let’s Organize Them!*

This Python script helps you organize your files into folders like Documents, Images, and so on. Plus, if you want, it can **rename your `.txt` files** using **AI** (powered by the **Google Gemini 1.5 Flash API**), so your files have more meaningful names based on their content.

---

## 🚀 Features

* Organizes your files into folders based on their type (Documents, Images, etc.).
* Lets you choose which folder to organize with the `--path` argument.
* Option to rename `.txt` files using **AI**.
* Displays a quick summary of what was organized.
* Clean code with separate sections for scanning, moving, renaming, and showing results.

---

## 🛠️ How to Use

1. **Clone the repo** (or download the project):

   ```bash
   git clone <repo_url>
   cd <repo_directory>
   ```

2. **Install dependencies**:

   Make sure you have Python 3.6+ installed. Then, run:

   ```bash
   pip install google
   ```

3. **Run the script** with the `--path` option to specify the folder to organize:

   ```bash
   python main.py --path "C:\Users\YourName\Downloads"
   ```

   If you don’t provide the `--path` argument, it will default to the folder you're currently in.

4. When it’s done scanning, you’ll get this prompt:

   ```text
   Enter 'yes' to use AI to rename files, or 'no' to skip:
   ```

---

### 🧠 **AI Renaming Feature**

If you want, you can use the AI feature to **rename `.txt` files**. The script will send the content of those files to **Google Gemini 1.5 Flash API**, and the AI will suggest a new name based on the file’s content.

* You’ll need an **API key** from [Google Gemini](https://makersuite.google.com/app/apikey) to use this feature.
* Only `.txt` and `.json` files are supported for AI renaming right now.

---

## 📂 Project Structure

```
file-organizer/
│
├── main.py                      # Main entry point for running the program
├── organizer/
│   ├── scanner.py               # Scans and categorizes files
│   ├── mover.py                 # Moves files into folders
│   ├── renamer.py               # Optionally renames files using AI
│   └── display.py               # Shows a summary of the organized files
└── README.md                    # This file
```

---

## ✅ Requirements

* Python 3.6+
* Install the required libraries:

  ```bash
  pip install google
  ```

---

## 📜 License

MIT License. Feel free to use and modify as needed.

---

## 🤝 Contributing

If you spot any bugs or have ideas for improvement, feel free to open an issue or send a pull request.

---

## 🧑‍💻 Example

Before running the script, your `Downloads` folder might look something like this:

```
Downloads/
├── image1.jpg
├── document1.txt
├── video.mov
```

After running the script, the files will be organized into the right folders:

```
Downloads/
├── Images/
│   └── image1.jpg
├── Documents/
│   └── document1.txt
├── videos/
│   └── video.mov
```

And if you choose to use the AI renaming feature, your `.txt` file might be renamed like this:

Before AI renaming:

```
document1.txt
```

After AI renaming:

```
SuggestedTitleFromAI.txt
```

---

## 🔧 How It Works

1. **Scanning**: The script scans the folder and categorizes files by type (like Documents, Images, etc.).
2. **Moving**: It then moves the files into the right folders.
3. **Renaming**: If you choose, it will use the AI to rename `.txt` files based on their content.
4. **Summary**: Finally, it shows you a summary of everything that was organized and renamed.

---

### 🎯 Example Command:

```bash
python main.py --path "C:\Users\YourName\Downloads"
```
