# python3
class StockCharts:
    def read_data(self):
        n, k = map(int, input().split())
        stock_data = [list(map(int, input().split())) for i in range(n)]
        return stock_data

    def write_response(self, result):
        print(result)

    def min_charts(self, stock_data):
        # Replace this incorrect greedy algorithm with an
        # algorithm that correctly finds the minimum number
        # of charts on which we can put all the stock data
        # without intersections of graphs on one chart.
        '''
        n = len(stock_data)
        k = len(stock_data[0])
        charts = []
        for new_stock in stock_data:
            added = False
            for chart in charts:
                fits = True
                for stock in chart:
                    above = all([x > y for x, y in zip(new_stock, stock)])
                    below = all([x < y for x, y in zip(new_stock, stock)])
                    if (not above) and (not below):
                        fits = False
                        break
                if fits:
                    added = True
                    chart.append(new_stock)
                    break
            if not added:
                charts.append([new_stock])
        return len(charts)
        '''
        n = len(stock_data)
        m = len(stock_data[0])
        compare_stocks = [[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                compare_stocks[i][j] = True
                for k in range(m):
                    compare_stocks[i][j] &= (stock_data[i][k] <
                                             stock_data[j][k])
                    if not compare_stocks[i][j]:
                        break
        bipartite_matching = [[-1]*n for _ in range(2)]
        path = 0
        for i in range(n):
            if self.dfs(i, [False]*n, bipartite_matching, compare_stocks):
                path += 1
        return n - path

    def dfs(self, i, visited, bipartite_matching, compare_stocks):
        if i == -1 :
            return True
        if visited[i] :
            return False
        visited[i] = True
        for j in range(len(compare_stocks)):
            if compare_stocks[i][j] and self.dfs(bipartite_matching[1][j],
                                                 visited, bipartite_matching,
                                                 compare_stocks):
                bipartite_matching[0][i] = j
                bipartite_matching[1][j] = i
                return True
        return False


    def solve(self):
        stock_data = self.read_data()
        result = self.min_charts(stock_data)
        self.write_response(result)

if __name__ == '__main__':
    stock_charts = StockCharts()
    stock_charts.solve()
