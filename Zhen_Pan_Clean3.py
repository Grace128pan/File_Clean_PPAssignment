#function3
#create new file with file name _cleaned.txt, read each lines from the source file folder, keep lines contain the word "Mary", "like" and exclude lines containing the word "cross", "angry"
import os

def clean_folder_many_texts(src_folder, dest_folder, src_postfix=".txt", dest_postfix="_cleaned.txt", good_texts=(), bad_texts=()):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    try:
        for filename in os.listdir(src_folder):
            if filename.endswith(src_postfix):
                src_file_path = os.path.join(src_folder, filename)
                dest_file_name = os.path.splitext(filename)[0] +dest_postfix
                dest_file_path = os.path.join(dest_folder, dest_file_name)
                
                with open(src_file_path, "r", encoding="utf-8") as infile, open(dest_file_path, "w", encoding="utf-8") as outfile:
                    for line in infile:
                        if all(good_text.lower() in line.lower() for good_text in good_texts) and not any(bad_text.lower() in line.lower() for bad_text in bad_texts):
                            outfile.write(line)
                            outfile.write("\n")
        print(f"Files in {src_folder} are cleaned and saved to {dest_folder}")
    except FileNotFoundError:
        print(f"Source folder {src_folder} is not found.")
    except IOError as e:
        print(f"An IOError occurred: {e}.")

if __name__ == "__main__":
    clean_folder_many_texts("src", "dest", good_texts=("Mary", "like"), bad_texts=("angry", "cross"))