#include <array>
#include <cstdio>
#include <iostream>
#include <math.h>
#include <string>
#include <vector>
using namespace std;

int cups[1000000];
int iterations;
int cup_count = 1000000;
// int cup_count = 9;

int moving[3];
int target;

void read_input() {
  string input_line;

  cin >> iterations;
  cin >> input_line;
  int input_cup_count = input_line.length();
  for (int i = 0; i < input_cup_count; i++) {
    cups[i] = stoi(string(1, input_line[i]));
  }
  for (int i = input_cup_count; i < cup_count; i++) {
    cups[i] = i + 1;
  }
}

// int get_target(int cup) {
//   int target = cup - 1;
//   if (target == 0) {
//     target = cup_count;
//   }

//   for (int i = 0; i < 3; i++) {
//     bool found = false;
//     for (int j = 0; j < 3; j++) {
//       if (moving[j] == target) {
//         found = true;
//       }
//     }
//     if (!found) {
//       return target;
//     }

//     target--;
//     if (target == 0) {
//       target = cup_count;
//     }
//   }

//   return target;
// }

// void iterate(int current) {
//   int i;
//   for (i = 0; i < 3; i++) {
//     moving[i] = cups[(current + i + 1) % cup_count];
//   }
//   target = get_target(cups[current]);

//   i = current;
//   do {
//     i = (i + 1) % cup_count;
//     cups[i] = cups[(i + 3) % cup_count];
//   } while (cups[(i + 3) % cup_count] != target);

//   for (int j = 0; j < 3; j++) {
//     cups[(i + j + 1) % cup_count] = moving[j];
//   }
// }

int get_cup_right_of_one() {
  for (int i = 0; i < cup_count; i++) {
    if (cups[i] == 1) {
      return (i + 1) % cup_count;
    }
  }
  return -1;
}

void print_cup_indexes() {
  for (int i = 0; i < cup_count; i++) {
    cout << cups[i] << " ";
  }
  cout << endl;
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

int main() {
  read_input();
  int current;
  int target;
  int iteration;
  int i;
  bool found;
  int j;

  int k;

  for (iteration = 0; iteration < iterations; iteration++) {
    current = iteration;
    if (current == cup_count) {
      current = 0;
    }
    // print_cups();

    for (i = 0; i < 3; i++) {
      k = (current + i + 1);
      if (k >= cup_count) {
        k -= cup_count;
      }
      moving[i] = cups[k];
    }
    target = cups[current] - 1;
    if (target == 0) {
      target = cup_count;
    }

    for (i = 0; i < 3; i++) {
      found = false;
      for (j = 0; j < 3; j++) {
        if (moving[j] == target) {
          found = true;
        }
      }
      if (!found) {
        break;
      }

      target--;
      if (target == 0) {
        target = cup_count;
      }
    }

    i = current;
    j = (current + 3);
    if (j >= cup_count) {
      j -= cup_count;
    }
    do {
      i++;
      j++;
      if (i == cup_count) {
        i = 0;
      }
      if (j == cup_count) {
        j = 0;
      }
      cups[i] = cups[j];
    } while (cups[j] != target);

    for (j = 0; j < 3; j++) {
      k = (i + j + 1);
      if (k >= cup_count) {
        k -= cup_count;
      }
      cups[k] = moving[j];
    }
  }

  print_product();

  return 0;
}
