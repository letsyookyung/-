###  문제 이해
1. numCourses 개 만큼의 코스가 존재한다. 0 ~ numCourses-1 의 라벨이 매겨져 있다.
2. prerequisites[i] 는 int[2] 짜리 배열로, prerequisites[i][1] 은 prerequisites[i][0] 인 과목의 선수과목이다. 
   즉, prerequisites[i][1] 을 들어야만 prerequisites[i][0] 을 수강할 수 있다.
3. 이러한 정보들이 주어질 때, 모든 코스를 끝낼 수 있다면 true를 리턴, 그렇지 않으면 false를 리턴하라.
4. 즉, DFS -> cycle 이 생기면 => false  

