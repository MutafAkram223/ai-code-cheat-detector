class MinStack {
public:
    stack<int> stk;
    stack<int> minstack;

    MinStack() {   
    }
    
    void push(int val) {
        stk.push(val);
        val = min(val, minstack.empty() ? val : minstack.top());
        minstack.push(val);
    }
    
    void pop() {
        stk.pop();
        minstack.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return minstack.top();
    }
};



// Approach:
// 1: I am making two stacks, one will store integers while other stack will store minumum value till, that insertion. 
// 2: For Example: If I am pushing 2nd element in stack, then 2nd element of minstack will be min(1st element, 2nd element).

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */