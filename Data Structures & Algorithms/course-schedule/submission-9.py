class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 'visited' tracks courses in the CURRENT DFS path to detect cycles.
        visited = set()

        # Adjacency list: maps each course to a list of its prerequisites.
        mapping = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites: 
            mapping[course].append(pre)
        
        def dfs(course): 
            # If the course is already in the current path, we found a cycle!
            if course in visited: 
                return False 
            
            # Base Case: If a course has no prerequisites (or we've already 
            # confirmed it's "safe"), we don't need to check it again.
            if mapping[course] == []: 
                return True 
            
            # 1. Add course to current path (mark as being visited)
            visited.add(course)
            
            # 2. Recursively check all prerequisites for this course
            for pre in mapping[course]: 
                if not dfs(pre): 
                    return False 

            # 3. Backtrack: Remove the course from the current path.
            # We also set its mapping to [] to "memoize" that this course is safe.
            visited.remove(course)
            mapping[course] = []

            return True 

        # We must call DFS on every course because the graph might be disconnected
        # (e.g., courses 0 and 1 are a pair, and courses 2 and 3 are separate).
        for course in range(numCourses):
            if not dfs(course): 
                return False 
        
        return True

    """
    CORE PATTERNS & INTUITION:

    1. Algorithm: Depth First Search (DFS) for Cycle Detection
       In a Directed Acyclic Graph (DAG), you can always find a linear ordering. 
       If a cycle exists, a linear order is impossible.

    2. Data Structure: Adjacency List
       We convert the edge list 'prerequisites' into a hash map (dictionary) 
       to allow O(1) lookups of a course's requirements.

    3. The "Visited" vs. "Safe" Distinction:
       - The 'visited' set acts as a "recursion stack." It only tracks nodes 
         in the current branch. If you hit a node twice in one branch, it's a cycle.
       - 'mapping[course] = []' acts as memoization (Completely Optional, but better for understanding). Once we know a course can 
         be completed, we clear its requirements so we never re-process its 
         sub-tree again, ensuring O(V + E) time complexity.

    4. Intuition: 
       Think of this like a "deadlock" check in operating systems. We are 
       traversing the dependency chain. If we ever end up back where we 
       started before finishing the chain, the system is deadlocked.
    """