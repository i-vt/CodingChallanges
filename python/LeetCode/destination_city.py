"""
1436. Destination City
Easy
1.7K
86
Companies

You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

 """

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        arr1, arr2 = [], []
        for path in paths:
            arr1.append(path[0])
            arr2.append(path[1])
        
        return list(set(arr2) - set(arr1))[0]
        
