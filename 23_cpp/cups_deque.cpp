#include <array>
#include <cstdio>
#include <deque>
#include <iostream>
#include <math.h>
#include <string>
#include <vector>
using namespace std;

deque<int> cups;
int iterations;
// int cup_count = 1000000;
int cup_count = 30;

int moving[3];
int target;

void read_input() {
  string input_line;
  cin >> iterations;
  cin >> input_line;
  int input_cup_count = input_line.length();
  for (int i = 0; i < input_cup_count; i++) {
    cups.push_back(stoi(string(1, input_line[i])));
  }
  for (int i = input_cup_count; i < cup_count; i++) {
    cups.push_back(i + 1);
  }
}

int get_target(int cup) {
  int candidate_target = cup - 1;
  if (candidate_target == 0) {
    candidate_target = cup_count;
  }

  for (int i = 0; i < 3; i++) {
    bool found = false;
    for (int j = 0; j < 3; j++) {
      if (moving[j] == candidate_target) {
        found = true;
      }
    }
    if (!found) {
      return candidate_target;
    }

    candidate_target--;
    if (candidate_target == 0) {
      candidate_target = cup_count;
    }
  }

  return candidate_target;
}

/*
8 9 1 3 4 6 7 2 5 10 11 12 13 14 15 16 17 18 ...
  -----     ^
dest: 7

4 6 7 2 5 10 11 12 13 14 15 16 17 18 ... 8    + 9 1 3
2 5 10 11 12 13 14 15 16 17 18 ... 8 4 6 7    + 9 1 3
9 1 3 2 5 10 11 12 13 14 15 16 17 18 ... 8 4 6 7
4 6 7 9 1 3 2 5 10 11 12 13 14 15 16 17 18 ... 8
*/

void iterate() {
  int latest;
  int current = cups.front();
  cups.pop_front();
  cups.push_back(current);

  moving[0] = cups.front();
  cups.pop_front();
  moving[1] = cups.front();
  cups.pop_front();
  moving[2] = cups.front();
  cups.pop_front();

  target = get_target(current);

  do {
    latest = cups.front();
    cups.pop_front();
    cups.push_back(latest);
  } while (latest != target);

  cups.push_front(moving[2]);
  cups.push_front(moving[1]);
  cups.push_front(moving[0]);

  do {
    cups.pop_back();
    cups.push_front(latest);
    latest = cups.back();
  } while (latest != current);
}

void print_cup_indexes() {
  for (int i = 0; i < cup_count; i++) {
    cout << cups[i] << " ";
  }
  cout << endl;
}

int get_cup_right_of_one() {
  for (int i = 0; i < cup_count; i++) {
    if (cups[i] == 1) {
      return (i + 1) % cup_count;
    }
  }
  return -1;
}

void print_all_in_order() {
  int i = get_cup_right_of_one();
  for (int j = 0; j < cup_count - 1; j++) {
    cout << cups[(i + j) % cup_count];
  }
  cout << endl;
}

void print_product() {
  int idx = get_cup_right_of_one();
  int cup1 = cups[idx];
  int cup2 = cups[(idx + 1) % cup_count];
  cout << "Cups: " << cup1 << " " << cup2 << endl;
  cout << "Product: " << cup1 * cup2 << endl;
}

/*
Start: 54321
5 4 3 2 1 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30

But, instead, offset to next lowest number?
1 1 1 1 1 -1 -1 -1 -1 ... -1

Then
1  4 3  2  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28
29 30 5

Becomes
-2 1 1 -3 -5 -1 -1 .. -1 2

And
 6  7  8  9  10  11 12 13 ... 26 27 28 29 30  4  3  2  5  1
Becomes
-2 -1 -1 -1 ...           ... -1 -1 -1 -1 -1  1  1  2 -3 -2
*/

int main() {
  read_input();
  cout << "Input read" << endl;

  for (int iteration = 0; iteration < iterations; iteration++) {
    print_cup_indexes();
    iterate();
  }

  cout << endl;
  print_all_in_order();
  print_product();

  return 0;
}
