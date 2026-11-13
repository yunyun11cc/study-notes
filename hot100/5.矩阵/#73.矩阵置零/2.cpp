#include<iostream>
#include <vector>
#include<unordered_set>
using namespace std;




class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        unordered_set<int> rows;
        unordered_set<int> cols;
        int m=matrix.size();
        int n=matrix[0].size();

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