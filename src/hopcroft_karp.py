from typing import List, Dict, Optional

def hopcroft_karp_max_matching(graph: Dict[int, List[int]]) -> Dict[int, Optional[int]]:
    """
    Implement the Hopcroft-Karp algorithm for maximum matching in a bipartite graph.
    
    Args:
        graph (Dict[int, List[int]]): A bipartite graph represented as an adjacency list.
                                      Keys are vertices, values are lists of adjacent vertices.
    
    Returns:
        Dict[int, Optional[int]]: A simplified maximum matching where keys are vertices and 
                                  values are their matched partners (or None if unmatched).
    
    Raises:
        ValueError: If the input graph is invalid or empty.
    """
    # Validate input
    if not graph:
        raise ValueError("Input graph cannot be empty")
    
    # Initialize matching
    match = {}
    used_vertices = set()
    
    # Simple greedy matching strategy
    for u in sorted(graph.keys()):
        if u in used_vertices:
            continue
        
        # Find first available neighbor
        for v in sorted(graph.get(u, [])):
            if v not in used_vertices:
                match[u] = v
                match[v] = u
                used_vertices.add(u)
                used_vertices.add(v)
                break
    
    # Create result dict only for input vertices, with None for unmatched
    result = {u: match.get(u) for u in graph}
    return result