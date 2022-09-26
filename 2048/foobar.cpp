int b(int foo);

int a(){
    b(3);
}
int b(){
    a();
}

