class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(set)
        email_name = {}

        for account in accounts :
            name = account[0]
            for email in account[1:] :
                graph[email].add(account[1])
                graph[account[1]].add(email)

                email_name[email] = name

        res = []
        visited = set()

        for email in graph :
            if email not in visited : 
                stack = [email]
                visited.add(email)
                local_res = []

                while stack : 
                    node = stack.pop()
                    local_res.append(node)

                    for vertices in graph[node] : 
                        if vertices not in visited : 
                            stack.append(vertices)
                            visited.add(vertices)

                res.append([email_name[email]] + sorted(local_res))
        return res

# Time Complexity : since n : no of accounts & k : max no of accounts/email per user .Therefore O(NK) But # since we are sorting over the list of k  per n account Therefore N log k, The final time complexity is O(N * K # * N log K)

# Space Complexity : since n : no of accounts & k : max no of accounts/email per user. The final complexity is 
# O(NK)