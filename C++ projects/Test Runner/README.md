# Test Runner

To test functionality of a particular unit create a separate void function implementing this unit (e.g `void TestMyUnit()`). 
Use macros `ASSERT_EQUAL(<result_of_unit>, <expected_result>)` to see if the unit works correctly. 

In `main` function create an object `TestRunner tr` and use macros `RUN_TEST(tr, TestMyUnit)` to run the unit test.

# Example
Here I provide example testing the functionality of `SplitIntoWords` function. This function splits string into words removing the spaces. Output of the function is the vector of words.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include "test_runner.h"

using namespace std;

vector<string> SplitIntoWords(string_view input){
    vector<string> result;

    while(true){
        if(input.empty()) break;
        size_t space = input.find(' ');
        if(space > 0){
            result.emplace_back(move(input.substr(0, space)));
        }

        if(space == input.npos){
            break;
        } else{
            input.remove_prefix(space + 1);
        }
    }

    return result;
}

void TestSplitIntoWords(){
    string str = "   My    name  is Alice      ";
    vector<string> result = SplitIntoWords(str);
    vector<string> expected = {"My", "name", "is", "Alice"};
    ASSERT_EQUAL(result, expected);
};

int main() {
    TestRunner tr;
    RUN_TEST(tr, TestSplitIntoWords);

    return 0;
}
```
