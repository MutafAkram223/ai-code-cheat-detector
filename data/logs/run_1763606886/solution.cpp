#include <stack>
using namespace std;

class MinStack {
private:
    stack<int> st;       // main stack
    stack<int> minSt;    // keeps track of minimums

public:
    MinStack() { }

    void push(int val) {
        st.push(val);

        // If min stack is empty OR val is <= current minimum, push it
        if(minSt.empty() || val <= minSt.top()) {
            minSt.push(val);
        }
    }

    void pop() {
        if(st.top() == minSt.top()) {
            minSt.pop();
        }
        st.pop();
    }

    int top() {
        return st.top();
    }

    int getMin() {
        return minSt.top();
    }
};
