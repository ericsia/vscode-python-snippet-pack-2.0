import json
import sys

"""
VS-Code Snippet Sytax
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
        This is a helper script to convert python or any launguage code to body of VS-Code snippet body"

        Usage:
            python vscode_ext_gen.py <file_path>

        This wont include tabstops and variables for snippet body

        Collect the body string from the stdout and past it to VS-Code snippet body
    """
    if len(sys.argv) > 1:

        file_path = sys.argv[1]
        with open(file_path, 'r') as code:
            content = code.read()
            body = []
            for line in content.splitlines():
                line = line.replace("    ", "\t")
                line = json.dumps(line)
                body.append(line)

        for line in body:
            print(line, ",")

    else:
        raise ValueError("pass file path as command line argument")
