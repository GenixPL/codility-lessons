package com.company;

import java.util.Arrays;

public class FrogRiverOne {

    // TEST DATA
//    int X = 5;
//    int[] A = {1, 3, 1, 4, 2, 3, 5, 4};

    public int solution(int X, int[] A) {
        System.out.println("X: " + X);
        System.out.println("A: " + Arrays.toString(A));

        // init array of bools 'was' with false
        boolean[] alreadyPlaced = new boolean[X];

        // init int 'needed' equal to X
        int neededToBePlaced = X;

        // init int 'stepsNeeded' with -1
        int timeNeeded = -1;


        // go through each field of A
        for (int i = 0; i < A.length; i++) {
            // if field is true in 'was' then continue
            int currentLeafPosition = A[i] - 1;

            if (alreadyPlaced[currentLeafPosition] == true) {
                continue;
            }

            // if field is false, then mark it and decrement 'needed'
            neededToBePlaced--;
            alreadyPlaced[currentLeafPosition] = true;

            // if 'needed' == 0 { mark 'stepsNeeded' with i and break}
            if (neededToBePlaced == 0) {
                timeNeeded = i;
                break;
            }
        }

        // return 'steps' == i
        return  timeNeeded;
    }

}
