# Profiler
To measure the execution time of a particular unit, wrap it with macros `LOG_DURATION("your comments here")`

## Example

```cpp
    int main() {

    {
        LOG_DURATION("Adding elements to a vector")
        vector<int> vec;
        for(int i = 0; i < 5'000'000; ++i){
            vec.push_back(i);
        }
    }

    {
        LOG_DURATION("Adding elements to a deque")
        deque<int> deq;
        for(int i = 0; i < 5'000'000; ++i){
            deq.push_back(i);
        }
    }

    return 0;
}
```

In console you can see execution time of units:

![изображение](https://user-images.githubusercontent.com/35171099/117927344-c157df00-b302-11eb-9eac-7fe410a44151.png)
