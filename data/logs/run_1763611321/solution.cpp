class MinStack {
private:
    std::stack<int> stk;
    std::stack<int> min_stk;
public:
    MinStack() {
        
    }
    
    void push(int val) {
        stk.push(val);
        if (min_stk.empty() || val <= min_stk.top()) {
            min_stk.push(val);
        }
    }
    
    void pop() {
        if (stk.top() == min_stk.top()) {
            min_stk.pop();
        }
        stk.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return min_stk.top();
    }
};