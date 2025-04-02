import pytest
from src.hopcroft_karp import hopcroft_karp_max_matching

def test_simple_bipartite_graph():
    """Test a simple bipartite graph with clear matching possibilities."""
    graph = {
        1: [3, 4],
        2: [3, 4],
        3: [1, 2],
        4: [1, 2]
    }
    
    result = hopcroft_karp_max_matching(graph)
    
    # Check that the maximum matching is found
    matches = {k: v for k, v in result.items() if v is not None}
    
    # Ensure exactly 2 vertices are matched
    assert len(matches) == 2
    
    # Verify the matches
    assert set(matches.keys()).issubset(graph.keys())
    for k, v in matches.items():
        assert v in graph[k]

def test_unbalanced_bipartite_graph():
    """Test a graph with more vertices in one set."""
    graph = {
        1: [4, 5],
        2: [4],
        3: [5],
        4: [1, 2],
        5: [1, 3]
    }
    
    result = hopcroft_karp_max_matching(graph)
    
    # Verify maximum matching
    matches = {k: v for k, v in result.items() if v is not None}
    
    # Ensure the number of matches is correct
    assert len(matches) == 2
    
    # Verify valid matches
    for k, v in matches.items():
        assert v in graph[k]

def test_disconnected_graph():
    """Test a graph with some disconnected vertices."""
    graph = {
        1: [3],
        2: [],
        3: [1],
        4: []
    }
    
    result = hopcroft_karp_max_matching(graph)
    
    # Check matching
    matches = {k: v for k, v in result.items() if v is not None}
    
    # Ensure matches are valid
    for k, v in matches.items():
        assert v in graph[k]

def test_empty_graph_raises_error():
    """Verify that an empty graph raises a ValueError."""
    with pytest.raises(ValueError):
        hopcroft_karp_max_matching({})

def test_single_vertex_graph():
    """Test a minimal graph with single connections."""
    graph = {
        1: [2],
        2: [1]
    }
    
    result = hopcroft_karp_max_matching(graph)
    
    # Check perfect matching
    matches = {k: v for k, v in result.items() if v is not None}
    assert len(matches) == 1
    
    # Verify the match is valid
    for k, v in matches.items():
        assert v in graph[k]

def test_complex_bipartite_graph():
    """Test a more complex bipartite graph with multiple possible matchings."""
    graph = {
        1: [3, 4, 5],
        2: [3, 4, 5],
        3: [1, 2],
        4: [1, 2],
        5: [1, 2]
    }
    
    result = hopcroft_karp_max_matching(graph)
    
    # Check maximum matching
    matches = {k: v for k, v in result.items() if v is not None}
    
    # Ensure matches are valid
    for k, v in matches.items():
        assert v in graph[k]