package com.company;

public class Main {

    public static void main(String[] args) {
        int[] A = {1, 5, 2, 1, 4, 0};
        int[] A2 = {1, 2, 3, 4};
        int[] A3 = {2147483647, 2147483647};

        var frog = new NumberOfDiscIntersections();
        var resBrute = frog.brute(A);
        var res = frog.solution(A);

        System.out.println("SOLUTION: " + res);
        System.out.println("SOLUTION BRUTE: " + resBrute);
    }
}
