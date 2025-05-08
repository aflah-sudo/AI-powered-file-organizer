import os

class SummaryDisplay:
    def __init__(self, organized_files):
        self.organized_files = organized_files
        self.display()

    def display(self):
        print("=" * 50)
        print("ORGANIZED FILES SUMMARY")
        print("=" * 50)
        for category, files in self.organized_files.items():
            print(f"{category.upper()}:")
            if not files:
                print("  - (empty)")
            else:
                total_size = 0
                for file_path in files:
                    size = os.path.getsize(file_path)
                    size_in_mb = round(size / (1024 * 1024), 2)
                    print(f"  - {os.path.basename(file_path)} : size: {size_in_mb} MB")
                    total_size += size_in_mb
                print(f"  Count of files: {len(files)}")
                print(f"  Total folder size: {round(total_size, 2)} MB")
            print()  # Blank line for spacing
