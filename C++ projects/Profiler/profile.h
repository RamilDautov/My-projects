#pragma once

#include <chrono>
#include <iostream>


using namespace std;
using namespace std::chrono;

class LogDuration{
public:
    explicit LogDuration(const string& msg = "") : start(steady_clock::now()), message(msg + ": "){};
    ~LogDuration(){
        auto finish = steady_clock::now();
        auto dur = finish - start;
        cerr << message << duration_cast<microseconds>(dur).count() << " mcs" << endl;
    }
private:
    steady_clock::time_point start;
    string message;
};

#define UNIQ_ID_IMPL(lineno) _a_local_var##lineno
#define UNIQ_ID(lineno) UNIQ_ID_IMPL(lineno)

#define LOG_DURATION(message)\
    LogDuration UNIQ_ID(__LINE__)(message);
