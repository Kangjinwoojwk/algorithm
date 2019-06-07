#include <iostream>>
using namespace std;
struct Node {
	int data;
	Node* next;
};
class queue {
private:
	Node data;
	Node* start;
	Node* end;
public:
	queue() {
		start = new Node;
		end = new Node;
		start->next = end;
		end->next = end;
	}
	~queue() {
		while (!Empty()) {
			Node* temp = start;
			start = start->next;
			if (start == NULL)
				return;
			delete temp;
		}
	}
	void Push(int data) {
		Node* temp = start;
		while (temp->next != end)
			temp = temp->next;
		temp->data = data;


	}
	bool Empty() {
		return start->next == end;
	}
};
int N, M, K, A, B;
int a[10], b[10];
int customer[1001][2] = { 0, };
int main(void) {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {

	}

}