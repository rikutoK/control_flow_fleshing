#include<stdio.h>
#include<fstream>
using namespace std;

extern void run_cfg(int* directions, int* actual_output);

bool cmp(int* expected, int* actual, int size);

void read_in(const char* filename, int** directions, int** expected_output, int** actual_output);

int main(int argc, char** argv) {

	int* expected_output;
	int* actual_output;
	int* directions;
	bool result;

	read_in(argv[1], &directions, &expected_output, &actual_output);

	for(int i = 0; i < 3; i++) {
		printf("expected_output %d is %d\n", i, expected_output[i]);
	}
	run_cfg(directions, actual_output);

	result = cmp(expected_output, actual_output, 3);

	printf("result is %d\n", result);

	for(int i = 0; i < 3; i++) {
		printf("actua_output %d is %d\n", i, actual_output[i]);
	}

	// deallocate memory for dynamic arrays
	delete [] directions;
	delete [] actual_output;
	delete [] expected_output;

	return 0;
}

bool cmp(int* expected, int* actual, int size) {

	for(int i = 0; i < size; i++) {
		if(expected[i] != actual[i]) {
			return false;
		}
	}

	return true;
}

void read_in(const char* filename, int** directions, int** expected_output, int** actual_output) {

	ifstream in;
	int dir_size;
	int out_size;

	// open file
	in.open("input.txt");

	if(in.fail()) {
		printf("Error opening input file\n");
		exit(1);
	}

	// first line in file gives direction array size
	in >> dir_size;

	// second line in file gives expected output array size
	in >> out_size;

	// allocate arrays
	*directions = new int[dir_size];
	*expected_output = new int[out_size];
	*actual_output = new int[out_size];

	// third line in file gives directions
	for(int i = 0; i < dir_size; i++){
		in >> (*directions)[i];
	}

	// fourth line in file gives expected output
	for(int i = 0; i < out_size; i++){
		in >> (*expected_output)[i];
	}

	in.close();

	// initialise actual output to -1
	for(int i = 0; i < out_size; i++) {
		(*actual_output)[i] = -1;
	}
/*
	(*directions)[0] = 0;
	(*expected_output)[0] = 1;
	(*expected_output)[1] = 2;
	(*expected_output)[2] = 4;
*/

}
