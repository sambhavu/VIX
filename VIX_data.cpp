#include<algorithm>
#include<cmath>
#include<iostream>
#include<fstream>
#include<vector>
#include<string>

using namespace std; 



class VIX{
    public: 
    
    const double pi = 3.1415926535897932384626433;
    const int size = 7518;


    std::vector<double> open;
    std::vector<double> high;
    std::vector<double> low;
    std::vector<double> close;
    
    VIX();
    void data();
};

VIX::VIX(){
    data();
}

void VIX :: data(){
    double value; 
    std::ifstream infile;
    infile.open("/users/USER/Desktop/vix_open.txt", std::ifstream::binary);
    for(int i = 0; i<size; i++)
    {
        infile>>value;
        open.push_back(value);
    }
    
    infile.open("/users/USER/Desktop/vix_high.txt", std::ifstream::binary);
    for(int i = 0; i<size; i++)
    {
        infile>>value;
        high.push_back(value);
    }
    
    infile.open("/users/USER/Desktop/vix_low.txt", std::ifstream::binary);
    for(int i = 0; i<size; i++)
    {
        infile>>value;
        low.push_back(value);
    }
    
    infile.open("/users/USER/Desktop/vix_close.txt", std::ifstream::binary);
    for(int i = 0; i<size; i++)
    {
        infile>>value;
        close.push_back(value);
    }
}


int main(){
    
    VIX vol; 
    return 0;
}
