#include<iostream>
#include<queue>
using namespace std;
struct Node {
	int value;
	int level;
	Node* parent = nullptr;
	Node* left = nullptr;
	Node* right = nullptr;
};
int main(int argc, char** argv)
{
	int test_case;
	int T, V, E, node1, node2, temp1, temp2;
	Node* temp;
	cin >> T;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		cin >> V >> E >> node1 >> node2;
		int ans_node = 0, ans_size = 0;
		++V;
		Node* nodes = new Node[V];
		for (int i = 1; i < V; ++i) {
			nodes[i].value = i;
		}
		for (int i = 0; i < E; ++i) {
			cin >> temp1 >> temp2;
			nodes[temp2].parent = &nodes[temp1];
			if (nodes[temp1].left == nullptr) {
				nodes[temp1].left = &nodes[temp2];
			}
			else {
				nodes[temp1].right = &nodes[temp2];
			}
		}
		temp = &nodes[node1];
		while (temp->parent != nullptr) {
			temp = temp->parent;
		}
		temp->level = 0;
		queue<int> q;
		q.emplace(temp->left->value);
		q.emplace(temp->right->value);
		while (!q.empty()) {
			temp = &nodes[q.front()];
			q.pop();
			temp->level = temp->parent->level + 1;
			if (temp->left != nullptr)
				q.emplace(temp->left->value);
			if (temp->right != nullptr)
				q.emplace(temp->right->value);
		}
		Node* tmp1 = &nodes[node1];
		Node* tmp2 = &nodes[node2];
		while (tmp1->value != tmp2->value) {
			if (tmp1->level < tmp2->level) {
				tmp2 = tmp2->parent;
			}
			else if (tmp1->level > tmp2->level) {
				tmp1 = tmp1->parent;
			}
			else {
				tmp1 = tmp1->parent;
				tmp2 = tmp2->parent;
			}
		}
		ans_node = tmp1->value;
		q.emplace(tmp1->value);
		while (!q.empty()) {
			temp = &nodes[q.front()];
			q.pop();
			++ans_size;
			if (temp->left != nullptr)
				q.emplace(temp->left->value);
			if (temp->right != nullptr)
				q.emplace(temp->right->value);
		}
		cout << '#' << test_case << ' ' << ans_node << ' ' << ans_size << '\n';
	}
	return 0;
}