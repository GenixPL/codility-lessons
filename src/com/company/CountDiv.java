package com.company;

public class CountDiv {
    public int solution(int A, int B, int K) {
        // determine first matching
        long first;
        long mod = A % K;
        if (mod == 0) {
            first = A;
        } else {
            first = A + (K - mod);
        }

        // determine last matching
        long last;
        mod = B % K;
        if (mod == 0) {
            last = B;
        } else {
            last = B - mod;
        }

        // determine those between
        if (last < first) {
            return 0;
        } else if (last == first) {
            return 1;
        } else {
            return (int) ((last - first) / K + 1);
        }
    }
}
