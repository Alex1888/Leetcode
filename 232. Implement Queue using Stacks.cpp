// 232. Implement Queue using Stacks.cpp : Defines the entry point for the console application.
//
/*
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
*/


#include "stdafx.h"
#include <stack>
#include <iostream>
using namespace std;

class Queue {
public:
	// Push element x to the back of queue.
	void push(int x) {
		if (instack.empty()){
			_peek = x;
		}

		instack.push(x);
	}

	// Removes the element from in front of queue.
	void pop(void) {
		if (!outstack.empty()) {
			outstack.pop();
			if (!outstack.empty()) _peek = outstack.top();
			return;
		}
		while (instack.size() > 1){
			outstack.push(instack.top());
			instack.pop();
		}

		instack.pop();
		if (!outstack.empty()) _peek = outstack.top();
	}

	// Get the front element.
	int peek(void) {
		return _peek;
	}

	// Return whether the queue is empty.
	bool empty(void) {
		return instack.empty() && outstack.empty();
	}

private:
	stack<int> instack;
	stack<int> outstack;
	int _peek;
};


int main()
{
	Queue q;
	q.push(1);
	q.push(2);
	q.pop();
	q.push(3);
	q.push(4);
	q.pop();
	cout << "Quese front is " << q.peek(); // 3


	return 0;
}
