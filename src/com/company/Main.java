package com.company;

public class Main {

    public static void main(String[] args) {
        int A = 6;
        int B = 11;
        int K = 2;

        var frog = new CountDiv();
        var res = frog.solution(A, B, K);

        System.out.println("SOLUTION: " + res);
    }
}
