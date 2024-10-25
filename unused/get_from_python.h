#pragma once
#include <fstream>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> audio_from_python(){
    ifstream file("../../../data/recording.bin", ios::binary);
    vector<int> arr;
    int value;
    while (file.read(reinterpret_cast<char*>(&value), sizeof(float64_t))) {
        arr.push_back(static_cast<float64_t> (value));
    }
    file.close();
    return arr;
}