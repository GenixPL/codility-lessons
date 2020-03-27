package com.company;

public class Main {

    public static void main(String[] args) {
        int[] A = {4, 2, 2, 5, 1, 5, 8};

        var frog = new MinAvgTwoSlice();
        var res = frog.solution(A);

        System.out.println("SOLUTION: " + res);
    }
}
