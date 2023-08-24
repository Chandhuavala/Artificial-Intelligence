def map_coloring(graph):
    colors = {}  # Dictionary to store assigned colors for each region
    
    # List of available colors
    available_colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
    
    for region in graph:
        used_colors = set(colors.get(neighbour) for neighbour in graph[region] if neighbour in colors)
        for color in available_colors:
            if color not in used_colors:
                colors[region] = color
                break
    
    return colors

# Example map graph represented as an adjacency list
map_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colored_map = map_coloring(map_graph)
for region, color in colored_map.items():
    print(f"Region {region} is colored {color}")
