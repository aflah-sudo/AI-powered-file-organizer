import os
import argparse
from organizer.scanner import DirectoryScanner
from organizer.mover import FileMover
from organizer.display import SummaryDisplay
from organizer.renamer import FileRenamer


def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default=os.getcwd(), help='Enter path to organize files')
    return parser.parse_args()

def main():
    args = arguments()
    path = args.path
    mover = FileMover()
    scanner = DirectoryScanner(mover)
    
    scanner.file_mover = mover
    scanner.scan_directory(path)

    ansr = input("Enter 'yes' to rename files, or 'no' to skip: ")

    if ansr.lower() == "yes":
        FileRenamer(scanner.organised)


    SummaryDisplay(scanner.organised) 
    print("Files organized successfully")

if __name__ == '__main__':
    main()
