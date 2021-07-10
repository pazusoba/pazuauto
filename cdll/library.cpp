
extern "C" void sortArray(int* list, int size) {
    int temp, i, j;

    for (i = 0; i < size; i++) {
        for (j = i + 1; j < size; j++) {
            if (list[i] > list[j]) {
                temp = list[i];
                list[i] = list[j];
                list[j] = temp;
            }
        }
    }
}