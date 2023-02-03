import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        return print(ValueError("Formato inválido"), file=sys.stderr)
    try:
        with open(path_file, mode="r") as file_text:
            text_list = [line.replace("\n", "") for line in file_text]
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    else:
        return text_list
