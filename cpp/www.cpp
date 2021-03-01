#include<iostream>
using namespace std;
int main(){
    string a,b;
    getline(cin,a);
    for(int i=0;i<a.size();i++){
        if(a[i]>'/' && a[i]<':'){
            b+=a[i];
        }else{
            if(i==0){
                b+='*';
                a[i]='*';
            }else{
                if(a[i-1]!='*'){
                    b+='*';
                    a[i]='*';
                }else{
                    a[i]='*';
                }
            }
        }
    }
    cout<<b;
}