
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {

        int n = grid.size();
        int m = grid[0].size();

        queue<pair<int, int>> q;

        int minutes = 0;
        int fresh = 0;

        // Count fresh oranges and store rotten oranges
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {

                if(grid[i][j] == 1)
                    fresh++;

                if(grid[i][j] == 2)
                    q.push({i, j});
            }
        }

        int delRow[] = {-1, 1, 0, 0};
        int delCol[] = {0, 0, -1, 1};

        while(!q.empty() && fresh > 0) {

            int sz = q.size();

            for(int k = 0; k < sz; k++) {

                pair<int, int> coords = q.front();
                q.pop();

                for(int i = 0; i < 4; i++) {

                    int newRow = coords.first + delRow[i];
                    int newCol = coords.second + delCol[i];

                    if(newRow >= 0 && newRow < n &&
                       newCol >= 0 && newCol < m &&
                       grid[newRow][newCol] == 1) {

                        grid[newRow][newCol] = 2;
                        fresh--;

                        q.push({newRow, newCol});
                    }
                }
            }

            minutes++;
        }

        return fresh == 0 ? minutes : -1;
    }
};
