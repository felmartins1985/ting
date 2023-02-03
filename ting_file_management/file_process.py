from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance: Queue):
    path_file_names = [instance.search(index)['nome_do_arquivo']
                       for index in range(len(instance))]

    if path_file not in path_file_names:
        data = txt_importer(path_file)
        dictionary = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len(data),
            'linhas_do_arquivo': data
        }
        instance.enqueue(dictionary)
        print(dictionary, file=sys.stdout)


def remove(instance: Queue):
    try:
        element = instance.dequeue()
    except IndexError:
        print('Não há elementos', file=sys.stdout)
    else:
        element_name = element['nome_do_arquivo']
        print(f'Arquivo {element_name} removido com sucesso', file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
