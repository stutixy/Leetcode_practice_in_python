class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        numOfprerequisites = [0 for i in range(numCourses)]
        courses = self.createGraph(numCourses, prerequisites, numOfprerequisites)
        queue = []
        for i in range(len(numOfprerequisites)):
            if numOfprerequisites[i] == 0:
                queue.append(i)   
                
        completedCourse = 0
        while len(queue) > 0:
            course = queue.pop(0)
            completedCourse += 1
            for dep in courses[course]:
                numOfprerequisites[dep] -= 1
                if numOfprerequisites[dep] == 0:
                    queue.append(dep)
        return completedCourse == numCourses


    def createGraph(self, numCourses, dependencies, numOfprerequisites):
        courses = {i:[] for i in range(numCourses)}
        for dep, course in dependencies:
            courses[course].append(dep)
            numOfprerequisites[dep] += 1
        return courses



        
        