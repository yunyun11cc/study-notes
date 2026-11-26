#include <unordered_set>
#include <vector>

/*
给定一个 m × n 的矩阵 matrix。对原矩阵中的每个 0，将它所在的一整行和一整列置零。
直接修改原矩阵。示例输出展示修改后的矩阵。

示例 1
输入：matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
输出：[[1, 0, 1], [0, 0, 0], [1, 0, 1]]

示例 2
输入：matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
输出：[[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
*/


using namespace std;


// 1. 先遍历原矩阵，用两个集合分别记录 0 所在的行号和列号。
// 2. 扫描完成后，将集合中记录的各行全部置零。
// 3. 再将记录的各列置零。两个集合合计占用 O(m + n) 额外空间。


class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        unordered_set<int> rows;
        unordered_set<int> cols;
        int m=matrix.size();
        int n=matrix[0].size();

        // 先收集原矩阵中的 0，再改动矩阵。
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(matrix[i][j]==0){
                    rows.insert(i);
                    cols.insert(j);
                }
            }
        }

        for(int x : rows){
            for(int y=0; y<n; y++){
                matrix[x][y]=0;
            }
        }

        for(int x=0; x<m; x++){
            for(int j : cols){
                matrix[x][j]=0;
            }
        }
    }
};
