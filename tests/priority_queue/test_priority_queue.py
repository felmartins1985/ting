from ting_file_management.priority_queue import PriorityQueue
import pytest

mock1 = [
    {
        "nome_do_arquivo": "arquivo_teste.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ["valor"],
    },
    {
        "nome_do_arquivo": "arquivo_teste.txt",
        "qtd_linhas": 7,
        "linhas_do_arquivo": ["valor"],
    },
    {
        "nome_do_arquivo": "arquivo_teste.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": ["valor"],
    },
]

mock = {}


def test_basic_priority_queueing():
    pq = PriorityQueue()
    assert len(pq) == 0
    for i in mock1:
        pq.enqueue(i)
    assert len(pq) == len(mock1)
    assert pq.search(0) == mock1[0]
    assert pq.search(1) == mock1[2]
    assert pq.dequeue() == mock1[0]
    with pytest.raises(IndexError):
        pq.search(7)
