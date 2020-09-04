import os
import sys


def format_file(in_file, out_file):
    with open(in_file, 'r') as infile, open(out_file, 'w') as outfile:
        for line in infile:
            new_line = line.replace('.', ';')
            outfile.write(new_line)


def for_txt_to_csv(infile, outfile):
    format_file(infile, outfile)


def list_all_dirs(location):
    if os.listdir(location):
        return os.listdir(location)
    else:
        print('The directory is empty.....')
        sys.exit(1)


def get_project_root():
    from pathlib import Path
    return Path(__file__).parent.parent


def convert_text_to_csv(all_files, location):
    for file in all_files:
        new_filename = file.replace('.txt', '.csv')
        original_file = location + '/' + file
        new_file = location + '/' + new_filename
        format_file(original_file, new_file)


def main():
    project_root = get_project_root()
    # location = os.path.join(project_root, 'resources')
    location = 'export'
    all_files = list_all_dirs(location)
    convert_text_to_csv(all_files, location)


if __name__ == '__main__':
    main()
