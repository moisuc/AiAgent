import os
from google.genai import types

def get_files_info(working_directory, directory="."):

    # If the absolute path to the directory is outside the working_directory
    absolute_path_working = os.path.abspath(working_directory)
    absolute_path_directory = os.path.abspath(os.path.join(working_directory, directory))
    if not os.path.commonpath([absolute_path_working, absolute_path_directory]) == absolute_path_working:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    try:
        contents = ''
        for entry in os.listdir(absolute_path_directory):
            entry_path = os.path.join(absolute_path_directory, entry)
            # - README.md: file_size=1032 bytes, is_dir=False
            contents += f"- {entry}: file_size={os.path.getsize(entry_path)} bytes, is_dir={os.path.isdir(entry_path)}\n"
    except Exception as e:
        return f'Error: An unexpected error occurred: {str(e)}'
    return contents.strip()

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

if __name__ == "__main__":
    get_files_info("calculator", ".")