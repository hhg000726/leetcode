class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        tovisit = rooms[0]
        visited = [False for _ in range(len(rooms))]
        visited[0] = True
        while tovisit:
            t = tovisit.pop(0)
            if visited[t] == False:
                visited[t] = True
                for i in rooms[t]:
                    tovisit.append(i)
        if False in visited:
            return False
        return True