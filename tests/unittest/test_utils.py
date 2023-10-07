from pygraphgpt.domain.utils import (
    parse_graph_string,
    filter_missing_relationship,
    format_nested_list_to_cytoscape
)


def test_parse_graph_string():
    graph = "[\n    ['Obi Wan Kenobi', 'Mentor', 'Anakin Skywalker'],\n"
    parsed_graph = parse_graph_string(graph)
    assert parsed_graph[0][0] == 'Obi Wan Kenobi'


def test_filter_missing_relationship():
    relations_list = [
        ['Obi Wan Kenobi', 'Mentor', 'Anakin Skywalker'],
        ['Obi Wan Kenobi', 'Mentor', ''],
    ]
    filtered_relations_list = filter_missing_relationship(relations_list)
    assert len(filtered_relations_list) == 1


def test_format_nested_list_to_cytoscape():
    graph = [
        ['Obi Wan Kenobi', 'Mentor', 'Anakin Skywalker'],
    ]
    cyto_graph = format_nested_list_to_cytoscape(graph)
    assert isinstance(cyto_graph[0], dict)
