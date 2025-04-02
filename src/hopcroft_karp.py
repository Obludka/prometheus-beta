from typing import List, Dict, Set, Optional

def hopcroft_karp_max_matching(graph: Dict[int, List[int]]) -> Dict[int, Optional[int]]:
    """
    Implement the Hopcroft-Karp algorithm for maximum matching in a bipartite graph.
    
    Args:
        graph (Dict[int, List[int]]): A bipartite graph represented as an adjacency list.
                                      Keys are vertices, values are lists of adjacent vertices.
    
    Returns:
        Dict[int, Optional[int]]: A maximum matching where keys are vertices and 
                                  values are their matched partners (or None if unmatched).
    
    Raises:
        ValueError: If the input graph is invalid or empty.
    """
    # Validate input
    if not graph:
        raise ValueError("Input graph cannot be empty")
    
    # Initialize matching and tracking sets
    match = {}  # Stores the current matching
    dist = {}   # Distance for BFS
    
    def bfs() -> bool:
        """
        Breadth-first search to find augmenting paths.
        
        Returns:
            bool: True if an augmenting path exists, False otherwise.
        """
        queue = []
        
        # Check vertices in the first set
        for u in graph:
            if u not in match:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        
        dist[None] = float('inf')
        
        while queue:
            u = queue.pop(0)
            
            if dist[u] < dist[None]:
                for v in graph.get(u, []):
                    # Check if the adjacent vertex is not matched or can be unmatched
                    w = match.get(v)
                    if dist.get(w, float('inf')) == float('inf'):
                        dist[w] = dist[u] + 1
                        queue.append(w)
        
        return dist[None] != float('inf')
    
    def dfs(u: int) -> bool:
        """
        Depth-first search to find and augment matching paths.
        
        Args:
            u (int): Current vertex to explore.
        
        Returns:
            bool: True if an augmenting path is found, False otherwise.
        """
        if u is not None:
            for v in graph.get(u, []):
                w = match.get(v)
                
                # If the adjacent vertex is unmatched or can be rematched
                if dist.get(w, float('inf')) == dist[u] + 1:
                    if dfs(w):
                        match[v] = u
                        match[u] = v
                        return True
            
            # No augmenting path found
            dist[u] = float('inf')
            return False
        
        return True
    
    # Find maximum matching
    while bfs():
        for u in graph:
            if u not in match:
                dfs(u)
    
    # Create result dict only for input vertices, with None for unmatched
    result = {u: match.get(u) for u in graph}
    return result