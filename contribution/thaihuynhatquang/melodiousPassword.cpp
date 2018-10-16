#include <bits/stdc++.h>

using namespace std;

void outPut(string x[], string y[], int n);

int main(){
    int n;
    cin >> n;
    string x[]={"a","e","i","o","u"};
    string y[]={"b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"};
    outPut(x,y,n);
}

void outPut(string x[], string y[], int n)
{
    switch(n)
    {
    case 1:
        {
            for(int i=0; i<5; i++)
                cout << x[i] << endl;
            for(int i=0; i<20; i++)
                cout << y[i] << endl;
            break;
        }
    case 2:
        {
            for(int i=0; i< 5; i++)
            {
                for(int j=0; j<20; j++)
                {
                    cout << x[i] << y[j] << endl;
                }
            }
            for(int i=0; i<20; i++)
            {
                for(int j=0; j<5; j++)
                {
                    cout << y[i] << x[j] << endl;
                }
            }
            break;
        }
    case 3:
        {
            for(int i=0; i< 5; i++)
            {
                for(int j=0; j<20; j++)
                {
                    for(int k=0; k<5; k++)
                    {
                        cout << x[i] << y[j] << x[k] << endl;
                    }
                }
            }
            for(int i=0; i<20; i++)
            {
                for(int j=0; j<5; j++)
                {
                    for(int k=0; k<20; k++)
                    {
                        cout << y[i] << x[j] << y[k] << endl;
                    }
                }
            }
            break;
        }
    case 4:
        {
            for(int i=0; i< 5; i++)
            {
                for(int j=0; j<20; j++)
                {
                    for(int k=0; k<5; k++)
                    {
                        for(int l=0; l<20; l++)
                        {
                            cout << x[i] << y[j] << x[k] << y[l] << endl;
                        }
                    }
                }
            }
            for(int i=0; i<20; i++)
            {
                for(int j=0; j<5; j++)
                {
                    for(int k=0; k<20; k++)
                    {
                        for(int l=0; l<5; l++)
                        {
                            cout << y[i] << x[j] << y[k] << x[l] << endl;
                        }
                    }
                }
            }
            break;
        }
    case 5:
        {
            for(int i=0; i< 5; i++)
            {
                for(int j=0; j<20; j++)
                {
                    for(int k=0; k<5; k++)
                    {
                        for(int l=0; l<20; l++)
                        {
                            for(int m=0; m<5; m++)
                            {
                                cout << x[i] << y[j] << x[k] << y[l] << x[m] << endl;
                            }
                        }
                    }
                }
            }
            for(int i=0; i<20; i++)
            {
                for(int j=0; j<5; j++)
                {
                    for(int k=0; k<20; k++)
                    {
                        for(int l=0; l<5; l++)
                        {
                            for(int m=0; m<20; m++)
                            {
                                cout << y[i] << x[j] << y[k] << x[l] << y[m] << endl;
                            }
                        }
                    }
                }
            }
            break;
        }
    case 6:
        {
            for(int i=0; i< 5; i++)
            {
                for(int j=0; j<20; j++)
                {
                    for(int k=0; k<5; k++)
                    {
                        for(int l=0; l<20; l++)
                        {
                            for(int m=0; m<5; m++)
                            {
                                for(int o=0; o<20; o++)
                                {
                                    cout << x[i] << y[j] << x[k] << y[l] << x[m] << y[o] << endl;
                                }
                            }
                        }
                    }
                }
            }
            for(int i=0; i<20; i++)
            {
                for(int j=0; j<5; j++)
                {
                    for(int k=0; k<20; k++)
                    {
                        for(int l=0; l<5; l++)
                        {
                            for(int m=0; m<20; m++)
                            {
                                for(int o=0; o<5; o++)
                                {
                                    cout << y[i] << x[j] << y[k] << x[l] << y[m] << x[o] << endl;
                                }
                            }
                        }
                    }
                }
            }
        }
        break;
    }
}
