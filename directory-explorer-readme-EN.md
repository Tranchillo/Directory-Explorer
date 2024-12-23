# Directory Explorer

A Python tool for generating a textual representation of directory structures, specifically designed to facilitate communication with LLMs (ChatGPT, Claude) during project development.

## Primary Use Case
This tool was specifically developed to enhance interactions with Large Language Models (LLMs) such as Claude, ChatGPT, or other AI assistants. When working on complex projects, like website development or applications, it's often necessary to communicate the exact directory structure of your project to LLMs.

The script automatically generates a clear, hierarchical text representation of your folders and files organization, which can be easily copied and pasted into conversations with LLMs. This enables AI assistants to:
- Better understand your project architecture
- Provide more relevant and contextualized suggestions
- Identify potential organizational issues
- Propose optimizations in file structure

It's particularly useful during:
- Website development phases
- Existing project reorganization
- File structure consultation requests
- Project structure documentation

## Features
- Recursive directory exploration
- Alphabetical sorting of files and folders
- Hierarchical formatting with indentation
- Error handling for inaccessible folders
- Unicode (UTF-8) support

## Prerequisites
- Python 3.x
- No external dependencies required (uses only Python standard library modules)

## Installation & Usage
1. Download the `directory-explorer.py` file
2. Place the file in the directory you want to explore
3. Open a terminal or command prompt
4. Navigate to the directory:
   ```bash
   cd path/to/your/directory
   ```
5. Run the script:
   ```bash
   python directory-explorer.py
   ```

The script will generate a `directory_structure.txt` file in the same directory, containing the complete structure.

## Output Example
```
Complete directory structure: C:/example
|-- documents/
    |-- project1/
        |-- file1.txt
        |-- file2.pdf
    |-- notes.txt
|-- images/
    |-- photo1.jpg
    |-- photo2.png
|-- readme.md
```

## Notes & Limitations
### Notes
- Directories are indicated with a "/" at the end
- If there are errors accessing specific directories, an error message will be shown in the report
- The output file is always saved in UTF-8 format

### Limitations
- Does not show file sizes
- Does not show modification dates
- Does not ignore hidden files or folders

### Common Error Messages
- "Permission denied": The script doesn't have access rights to a directory
- "File not found": The specified path doesn't exist
- "Path too long": Path exceeds system's maximum length limit

## Future Improvements
- File size display
- Last modified date
- Option to ignore specific folders/files
- Export in different formats (JSON, XML)
- Command-line arguments for customization

## Contributing
Feel free to:
1. Fork the repository
2. Create a branch for your modifications
3. Submit a pull request

## License
This project is distributed under the MIT license. Feel free to use and modify it as you prefer.
