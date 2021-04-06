#include <bits/stdc++.h>
using namespace std;

vector < vector <int> > arr = {{-1,-1,-1},{-1,-1,-1},{-1,-1,-1}};

bool rowCrossed() 
{ 
    for (int i=0; i<3; i++) 
    { 
        if (arr[i][0] == arr[i][1] && 
            arr[i][1] == arr[i][2] &&  
            arr[i][0] != -1) 
            return (true); 
    } 
    return (false); 
} 
  
bool columnCrossed() 
{ 
    for (int i=0; i<3; i++) 
    { 
        if (arr[0][i] == arr[1][i] && 
            arr[1][i] == arr[2][i] &&  
            arr[0][i] != -1) 
            return (true); 
    } 
    return(false); 
} 
  

bool diagonalCrossed() 
{ 
    if (arr[0][0] == arr[1][1] && 
        arr[1][1] == arr[2][2] &&  
        arr[0][0] != -1) 
        return(true); 
          
    if (arr[0][2] == arr[1][1] && 
        arr[1][1] == arr[2][0] && 
         arr[0][2] != -1) 
        return(true); 
  
    return(false); 
} 

int checkwin() 
{ 
 	if(rowCrossed() || columnCrossed() || diagonalCrossed()){
 		return 1;
 	}

 	for(int i=0;i<3;i++){
 		for(int j=0;j<3;j++)
 			if(arr[i][j] == -1)
 				return -1;
 	}

 	return 0;
} 

vector <vector <int> > last;

vector <int> alpha_beta(int turn, int alpha, int beta){

	// Minimizer
	if(turn == 0){

		vector <int> M = {(int)1e7,-1,-1};

		for(int i=0;i<3;i++){
			for(int j=0;j<3;j++){

				if(arr[i][j] == -1){

					int val = 0;
					arr[i][j] = 0;
					int x = checkwin();

					if(x == 1)
						val = -20;
					else if(x == -1)
						val = alpha_beta(1, alpha, beta)[0];


					arr[i][j] = -1;
					if(M[0] > val){
						M = {val, i ,j};
					}

		            if(M[0] <= alpha)
		            	return M;

		            beta = min(beta, M[0]);
				}

			}
		}

		return M;

	}

	vector <int> M = {(int)-1e7,-1,-1};
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){

			int val = 0;
			if(arr[i][j] == -1){

				arr[i][j] = 1;
				int x = checkwin();
				
				if(x == 1)
					val = 20;
				else if(x == -1)
					val = alpha_beta(0, alpha, beta)[0];

				arr[i][j] = -1;
				if(M[0] < val)
					M = {val, i, j};

	            if(M[0] >= beta)
	            	return M;

	            alpha = max(alpha, M[0]);

			}

		}
	}

	return M;

}


int32_t main(){


    char t;
    // cin >> t;
    int turn = 1;
    if(t == 'X')
        turn = 0;

    // for(int i=0;i<3;i++){
    //     for(int j=0;j<3;j++){
    //         char t;
    //         cin >> t;
    //         if(t == 'X')
    //             arr[i][j] = 0;
    //         else if(t == 'O')
    //             arr[i][j] = 1;
            
    //     }
    // }
	auto x = alpha_beta(1, -1e8, 1e8);
    
    cout << x[1] << " " << x[2] << endl;

	 
}
