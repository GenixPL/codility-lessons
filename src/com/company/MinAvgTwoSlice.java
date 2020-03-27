package com.company;

public class MinAvgTwoSlice {
    public int solution(int[] A) {
        // we have to check slices of length equal to 2 or 3
        double minAvg = Double.MAX_VALUE;
        int minP = Integer.MAX_VALUE;

        for (int i = 0; i < A.length; i++) {
            if (i <= A.length - 2) {
                //check length 2
                int first = A[i];
                int second = A[i + 1];
                double res = (double) (first + second) / 2;

                if (res < minAvg) {
                    minAvg = res;
                    minP = i;
                }
            }

            if (i <= A.length - 3) {
                //check length 3
                int first = A[i];
                int second = A[i + 1];
                int third = A[i + 2];
                double res = (double) (first + second + third) / 3;

                if (res < minAvg) {
                    minAvg = res;
                    minP = i;
                }

            }

        }

        return minP;
    }
}
