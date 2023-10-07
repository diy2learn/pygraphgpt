from pygraphgpt.domain.graph import find_relations


def test_find_relations():
    text = """
    Obi Wan Kenobi: Mentor to Anakin Skywalker and Luke Skywalker
    Darth Vader: Formerly, Anakin Skywalker. Father of Luke and Leia
    Yoda: Oldest Jedi alive at the time of the original trilogy. Super strong with the force. Luke's teacher.
    """
    found_graph = find_relations(text)

    assert "Obi Wan Kenobi" in found_graph
