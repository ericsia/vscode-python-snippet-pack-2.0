import json
import sys

"""
VS-Code Snippet Syntax
    Example:
    "Print to console": {
        "prefix": "log",
        "body": [
            "console.log('$1');",
            "$2"
        ],
        "description": "Log output to console"
    }
"""

if __name__ == "__main__":
    """
        This is a helper script to convert python or any language code to body of VS-Code snippet body"
        This wont include tabstops and variables for snippet body

        Collect the body string from the stdout and past it to VS-Code snippet body
    """
    default_file_path = "test.py"
    if len(sys.argv) > 1:
        default_file_path = sys.argv[1]  # if argument is provided use the argument one
    # end if

    try:
        with open(default_file_path, 'r') as code:
            for line in code:
                # assume using 4 spaces as tab
                line = line.replace("    ", "\t").strip()
                line = json.dumps(line)
                print(line, end=",\n")
    except FileNotFoundError:
        raise ValueError("""file not found, check command line argument of file path
    Usage:
        python vscode_ext_gen.py <file_path>
    If <file_path> not specify, test.py will be the default file""")