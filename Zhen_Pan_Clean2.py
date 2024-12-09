#function2
#the original text file is chapter1.txt
#I will keep lines contain the word "Mary", "ayah" and exclude lines containing the word "cry", "Crying", "cried", "Cries", "CRY", "Cried", "crying", "CRYING", deal with casesensitive issues

def clean_file_many(src_file, dest_file, good_texts=(), bad_texts=()):
    try:
        with open(src_file, 'r', encoding="utf-8") as infile, open(dest_file, 'w', encoding="utf-8") as outfile:
            for line in infile:
                if any(good_text.lower() in line.lower() for good_text in good_texts) and not any(bad_text.lower() in line.lower() for bad_text in bad_texts):
                    outfile.write(line)
                    outfile.write("\n")
        print(f"File {src_file} is cleaned and saved to {dest_file}.")
    except FileNotFoundError:
        print(f"File {src_file} is not found.")
    except IOError as e:
        print(f"An IOerror occurred: {e}")
        
if __name__ == "__main__":
    clean_file_many("chapter1.txt", "chapter1_cleaned2.txt", good_texts=("Mary", "ayah"), bad_texts=("cry", "Crying", "cried", "Cries", "CRY", "Cried", "crying", "CRYING"))
