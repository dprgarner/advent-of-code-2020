#include <array>
#include <cstdio>
#include <iostream>
#include <math.h>
#include <string>
#include <vector>
using namespace std;

int cups[1000001];
int iterations;
int cup_count = 1000000;
// int cup_count = 9;

int first;
int target;

void read_input() {
  string input_line;
  cin >> iterations;
  cin >> input_line;

  int input_cup_count = input_line.length();
  int input_cups[10];

  for (int i = 0; i < input_cup_count; i++) {
    int value = stoi(string(1, input_line[i]));
    input_cups[i] = value;
  }
  first = input_cups[0];
  for (int i = 0; i < input_cup_count - 1; i++) {
    cups[input_cups[i]] = input_cups[i + 1];
  }

  int last_in_list = input_cups[input_cup_count - 1];
  if (cup_count > input_cup_count) {
    cups[last_in_list] = input_cup_count + 1;
    for (int i = input_cup_count + 1; i < cup_count; i++) {
      cups[i] = i + 1;
    }
    cups[cup_count] = first;
  } else {
    cups[last_in_list] = first;
  }
}

int iterate(int current) {
  int next1 = cups[current];
  int next2 = cups[next1];
  int next3 = cups[next2];

  int target = current;
  cups[current] = cups[next3];

  do {
    target--;
    if (target == 0) {
      target = cup_count;
    }
  } while (next1 == target || next2 == target || next3 == target);

  cups[next3] = cups[target];
  cups[target] = next1;

  return cups[current];
}

void print_cup_indexes() {
  for (int i = 0; i < cup_count + 1; i++) {
    cout << cups[i] << " ";
  }
  cout << endl;
}

void print_all_in_order() {
  int i = 1;
  do {
    i = cups[i];
    if (i == 1) {
      cout << endl;
      return;
    }
    cout << i;
  } while (true);
  cout << endl;
}

void print_product() {
  int cup1 = cups[1];
  int cup2 = cups[cup1];
  long long prod = (long)cup1 * (long)cup2;
  cout << "Cups: " << cup1 << " " << cup2 << endl;
  cout << "Product: " << prod << endl;
}

int main() {
  /*
  I had to look up a hint for this one. :(
  */
  read_input();
  cout << "Input read" << endl;

  int current = first;
  for (int iteration = 0; iteration < iterations; iteration++) {
    // print_all_in_order();
    current = iterate(current);
  }
  // print_all_in_order();

  cout << endl;
  print_product();

  return 0;
}
