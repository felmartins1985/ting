def exists_word(word, instance):
    show_return_exists = []
    for index in range(len(instance)):
        data = instance.search(index)
        show_lines_word = []
        for index, line in enumerate(data["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                show_lines_word.append(
                    {
                        "linha": index + 1,
                    }
                )
        if len(show_lines_word) > 0:
            show_return_exists.append(
                {
                    "palavra": word,
                    "arquivo": data["nome_do_arquivo"],
                    "ocorrencias": show_lines_word,
                }
            )
    return show_return_exists


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
