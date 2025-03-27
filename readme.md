# Comment Generator

## Overview
The **Comment Generator** is a simple tool that adds comment headers specified in `comment.txt` to all `.html`, `.css`, and `.js` files within a directory. This ensures that all files have consistent and structured comment headers.

## Features
- Automatically adds comment headers from `comment.txt`.
- Processes `.html`, `.css`, and `.js` files.
- Maintains consistency across project files.
- Supports bulk file processing.

## Installation
No installation is required. Ensure you have Python, the OS module should come with it out of the box.

## Usage
1. Place your desired comment header in `comment.txt`.
2. Run the script in the directory containing the files.
3. The script will prepend the header to all `.html`, `.css`, and `.js` files.

### Example
```
project-folder/
│-- comment.txt
│-- example-files/
│   │-- index.html
│   │-- styles.css
│   │-- script.js
│-- FileComenter.py
```

Running the script will insert the content of `comment.txt` at the beginning of each supported file type, the comment will be modifed to fit each file type.

## Example Comment File (`comment.txt`)
```
blahaj loves everyone :3
```

## Example Processed File (`index.html`)
```
<!--
blahaj loves everyone :3
-->

<!DOCTYPE html>
<html>
<head>
    <title>Example</title>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>
```

## Directory Structure
- `comment.txt` - Contains the comment header to be added.
- `example-files/` - Sample files before and after processing.
- `FileComenter.py` - The script that applies headers.

## License
This project is open-source and available under the MIT License.
The licence itself can be found in the `licence.txt` file.

## Contributing
Feel free to submit issues or pull requests to improve functionality.