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
    # This graph allows 2 perfect matches
    matches = {k: v for k, v in result.items() if v is not None}
    assert len(matches) == 4
    assert set(matches.keys()) == set(graph.keys())
    assert len(set(matches.values())) == 2  # Unique matches

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
    assert len(matches) == 4
    assert len(set(matches.values())) == 2

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
    assert len(matches) == 2

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
    assert len(matches) == 2
    assert matches[1] == 2
    assert matches[2] == 1

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
    assert 4 <= len(matches) <= 5
    assert len(set(matches.values())) >= 2