class Graph:
    
    def __init__(self):
        self.map = {}
    
            
    def get_info(self, next_index, all_lines):
        
        n1, n2, w = map(int, all_lines[next_index].split())
        next_index += 1
    
        return n1, n2, w, next_index
    
    def add_info(self, total_edges,  n1, n2, w):
        
        if total_edges >= 1:
            if n1 not in self.map:
                self.map[n1] = {}
            
            if n2 not in self.map:
                self.map[n2] = {}
            
        self.map[n1][n2] = w
        
        return self.map