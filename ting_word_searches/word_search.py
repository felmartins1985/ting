from ting_file_management.queue import Queue
from ting_file_management.file_process import process


def generate_word_report(word, file, occurrences):
    return {"palavra": word, "arquivo": file, "ocorrencias": occurrences}


def create_word_report(word, file, text=False):
    lines_search = []
    for index, line in enumerate(file["linhas_do_arquivo"]):
        if word.lower() in line.lower():
            lines_text = {
                "linha": index + 1,
            }
            if text:
                lines_text["conteudo"] = line
            lines_search.append(lines_text)
    return lines_search


def exists_word(word, instance):
    show_return_exists = []
    for index in range(len(instance)):
        data = instance.search(index)
        lines_search = create_word_report(word, data)
        if len(lines_search) > 0:
            file_path = data["nome_do_arquivo"]
            result = generate_word_report(word, file_path, lines_search)
            show_return_exists.append(result)
    return show_return_exists


def search_by_word(word, instance):
    show_return_exists = []
    for index in range(len(instance)):
        data = instance.search(index)
        lines_search = []
        lines_search = create_word_report(word, data, True)
        if len(lines_search) > 0:
            file_path = data["nome_do_arquivo"]
            result = generate_word_report(word, file_path, lines_search)
            show_return_exists.append(result)
    return show_return_exists
