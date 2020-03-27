package com.company;

import java.util.Arrays;

public class NumberOfDiscIntersections {

    // BRUTE

    public int brute(int[] A) {
        int intersections = 0;

        for (int i = 0; i < A.length; i++) {
            for (int j = i + 1; j < A.length; j++) {
                if (doesIntersect(i, A[i], j, A[j])) {
                    intersections++;

                    if (intersections > 10000000) {
                        return -1;
                    }
                }
            }
        }

        return intersections;
    }

    boolean doesIntersect(int i, long ri, int j, long rj) {
        long rightSideOfLeft = i + ri;
        long leftSideOfRight = j - rj;

        return leftSideOfRight <= rightSideOfLeft;
    }

    // PROPER

    public int solution(int[] A) {
//        long startTime = System.nanoTime();
        Event[] events = new Event[A.length * 2];

        for (int i = 0; i < A.length; i++) {
            events[i * 2] = new Event((long) i - A[i], 1);
            events[i * 2 + 1] = new Event((long) i + A[i], -1);
        }

        Arrays.sort(events, Event::compareTo);

        // count starts before 0
        int circlesStack = 0;
        int intersections = 0;

        for (int i = 0; i < events.length; i++) {
            if (events[i].value == 1) {
                intersections += circlesStack;
            }

            circlesStack += events[i].value;

            if (intersections > 10000000) {
                return -1;
            }
        }
//        long elapsedTime = System.nanoTime() - startTime;
//        System.err.println("TIME (millis): " + elapsedTime / 1000000);

        return intersections;
    }

    class Event implements Comparable<Event> {
        long position;
        int value;

        Event(long position, int value) {
            this.position = position;
            this.value = value;
        }

        @Override
        public int compareTo(Event event) {
            if (this.position == event.position) {
                if (this.value == event.value) {
                    return 0;
                }

                return (this.value < event.value) ? 1 : -1;
            }

            if (this.position < event.position) {
                // -1 here results in ascending order
                return -1;
            }

            return 1;
        }
    }
}
