class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = self.createGraph(numCourses, prerequisites)
        visited = set()
        visiting = set()
        
        
        def dfs(course):
            if course in visiting:
                return True
            if len(courses[course]) == 0:
                return False
            visiting.add(course)
            for preCourse in courses[course]:
                if preCourse not in visited:
                    hasCycle = dfs(preCourse)
                    if hasCycle:
                        return True
            visited.add(course)
            return False 

        for i in range(numCourses):
            if i not in visited:
                hasCycle = dfs(i)
                if hasCycle:
                    return False
        return True
                
    
    def createGraph(self, numCourses, prerequisites):
        courses = {i:[] for i in range(numCourses)}
        for src, dst in prerequisites:
            courses[src].append(dst)
        return courses



        
        