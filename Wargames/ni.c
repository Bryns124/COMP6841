// #include <stdio.h>
// #include <unistd.h>
// #include <string.h>

// char *secret = "Can you read my secret message???";

// int main(int argc, char **argv) {
//   char buffer[512];
//   fgets(buffer, sizeof(buffer), stdin);
//   printf(buffer);
// }

#include <stdio.h>
#include <unistd.h>

int main() {
    int secret_num = 0x8badf00d;

    char name[64] = {0};
    read(0, name, 64);
    printf("Hello ");
    printf(name);
    printf("! You'll never get my secret!\n");
    return 0;
}