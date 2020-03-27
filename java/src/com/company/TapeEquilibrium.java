package com.company;

public class TapeEquilibrium {
    public int solution(int[] A) {
        int leftPart = A[0];
        int rightPart = A[1];

        // slits into two non-empty parts
        // 0 < P < A.length

        // count whole right side
        for(int i = 2; i < A.length; i++) {
            rightPart += A[i];
        }

        int minDif = Math.abs(leftPart - rightPart);

        for (int p = 1; p < A.length - 1; p++) {
            leftPart += A[p];
            rightPart -= A[p];

            int dif = Math.abs(leftPart - rightPart);

            if (dif < minDif) {
                minDif = dif;
            }
        }

        return minDif;
    }
}
