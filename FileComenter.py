import os

class CommentManager:
    def __init__(self, comment_file="comment.txt"):
        self.comment = self.get_comment(comment_file)

    def get_comment(self, comment_file):
        try:
            with open(comment_file, "r", encoding="utf-8") as file:
                return file.read().strip()
        except FileNotFoundError:
            print(f"{comment_file} not found. Please create the file and add a comment.")
            exit(1)
    
    def get_comment_syntax(self, file_ext):
        if file_ext == ".html":
            return f"<!-- {self.comment} -->\n\n"
        elif file_ext in [".css", ".js"]:
            return f"/* {self.comment} */\n\n"
        return None
    
    def remove_existing_comments(self, content, file_ext):
        new_content = []
        comment_count = 0
        comment_symbols = {
            ".html": "<!--",
            ".css": "/*",
            ".js": "/*"
        }
        comment_end_symbols = {
            ".html": "-->",
            ".css": "*/",
            ".js": "*/"
        }

        in_comment_block = False
        for line in content:
            stripped_line = line.strip()
            if comment_count < 15:
                if stripped_line.startswith(comment_symbols.get(file_ext, "")):
                    in_comment_block = True
                if in_comment_block:
                    comment_count += 1
                if stripped_line.endswith(comment_end_symbols.get(file_ext, "")):
                    in_comment_block = False
                    continue
                if in_comment_block:
                    continue
            new_content.append(line)
        return new_content
    
    def add_comment_to_file(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.readlines()
        
        file_ext = os.path.splitext(file_path)[1]
        formatted_comment = self.get_comment_syntax(file_ext)
        if not formatted_comment:
            return

        content = self.remove_existing_comments(content, file_ext)
        
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(formatted_comment + "".join(content))
        print(f"Updated comment in {file_path}")

    def process_files(self):
        for root, _, files in os.walk("."):
            for file in files:
                if file.endswith((".html", ".css", ".js")):
                    self.add_comment_to_file(os.path.join(root, file))

if __name__ == "__main__":
    manager = CommentManager()
    manager.process_files()