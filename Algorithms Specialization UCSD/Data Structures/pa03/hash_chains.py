# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = {}

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            if query.ind in self.elems.keys():
                self.write_chain([self.elems[query.ind][word] for word in range(len(self.elems[query.ind])-1,-1,-1)])
            else:
                print('')
        else:
            key = self._hash_func(query.s) 
            if query.type == 'find':
                was_found = 0
                if key in self.elems.keys():
                    if query.s in self.elems[key]:
                        was_found = 1
                self.write_search_result(was_found)
            elif query.type == 'add':
                if key not in self.elems.keys():
                    self.elems[key] = [query.s]
                elif query.s not in self.elems[key]:
                    self.elems[key].append(query.s)
            else:
                if key in self.elems.keys():
                    for cur in self.elems[key]:
                        if cur == query.s:
                            self.elems[key].pop(self.elems[key].index(cur))
                    if not self.elems[key]:
                            self.elems.pop(key)
#            print(key, self.elems)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
