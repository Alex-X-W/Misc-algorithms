/*
an implementation of Heap and related operations, and heapsort
*/

#include <iostream>

using namespace std;

class Maxheap {
private:
  int* heap;
  int size;
  void swap(int& a, int& b) {
    int buf = a;
    a = b;
    b = buf;
  }
public:
  int left(const int& i) { return (i<<1) + 1; }
  int right(const int& i) { return (i<<1) + 2; }

  void initialize(int* data, int N) {
    heap = new int[N];
    size = N;
    for (int i = 0; i < N; ++i) {
      heap[i] = data[i];
    }
  }

  void display() {
    for (int i = 0; i < size; ++i) {
      cout << heap[i] << " ";
    }
  }

  void maxHeapify(const int& i, const int& N) {
    int l = left(i);
    int r = right(i);
    int maxIdx = i;

    if (l > N - 1) { // i is a leaf
      return;
    } else if (r > N - 1) { // i only has left child
      if (heap[l] > heap[i]) {
        swap(heap[l], heap[i]);
        maxHeapify(l, N);
      }
    } else { // i has both children
      maxIdx = heap[l] > heap[i] ? l: i;
      maxIdx = heap[r] > heap[maxIdx] ? r: maxIdx;
      if (maxIdx != i) {
        swap(heap[maxIdx], heap[i]);
        maxHeapify(maxIdx, N);
      }
    }
  }

  void buildMaxHeap() {
    for (int i = (size - 1)/2 ; i >= 0; --i) {
      maxHeapify(0, i);
    }
  }

  void heapSort() {
    buildMaxHeap();
    if (size < 2) { return; }
    for (int i = size - 1; i >= 1; --i ) {
      swap(heap[0], heap[i]);
      maxHeapify(0, i);
    }
  }
};


int main() {
  int data[10] = {16, 14, 10, 8, 7, 9, 3, 2, 4, 1};
  Maxheap heap;
  heap.initialize(data, 10);
  cout << "before:" << endl;
  heap.display();
  cout << endl;

  heap.heapSort();
  cout << "after" << endl;
  heap.display();
  cout << endl;
  return 0;
}