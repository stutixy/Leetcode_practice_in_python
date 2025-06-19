class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
            zeroes = 0
            ones = 0

            for student in students:
                if student == 0:
                    zeroes += 1
                else:
                    ones += 1
            
            for i in range(len(sandwiches)):
                if sandwiches[i] == 0:
                    if zeroes == 0:
                        return len(sandwiches)-i
                    zeroes -= 1
                else:
                    if ones == 0:
                        return len(sandwiches)-i
                    ones -= 1
            return 0
                