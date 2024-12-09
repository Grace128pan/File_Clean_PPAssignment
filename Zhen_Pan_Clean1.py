#function1
#the original text file is chapter1.txt
#I will keep lines contain the word "Mary" and exclude lines containing the word "cry", deal with casesensitive issues

def clean_file(src_file, dest_file, good_text="", bad_text=""):
    try:
        with open(src_file, 'r', encoding="utf-8") as src:
            lines = src.readlines()
        
        cleaned_paragraphs = []
        current_paragraph = []
        
        for line in lines:
            stripped_line = line.strip()
            if stripped_line:
                line_lower = stripped_line.lower()
                good_text_lower = good_text.lower()
                bad_text_lower = bad_text.lower()
                if good_text_lower in line_lower and bad_text_lower not in line_lower:
                    current_paragraph.append(stripped_line)
            else:
                if current_paragraph:
                    cleaned_paragraphs.append("".join(current_paragraph))
                    current_paragraph = []
        
        if current_paragraph:
            cleaned_paragraphs.append("".join(current_paragraph))
            
        with open(dest_file, 'w', encoding="utf-8") as dest:
            dest.write("\n\n".join(cleaned_paragraphs))
        
        print(f"File {src_file} is cleaned and saved to {dest_file}.")
    except FileNotFoundError:
        print(f"File {src_file} is not found.")
    except IOError as e:
        print(f"An IOerror occurred: {e}")
        
if __name__ == "__main__":
    clean_file("chapter1.txt", "chapter1_cleaned1.txt", good_text="Mary", bad_text="cry")