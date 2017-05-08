# Tasks
The tool builds 2 types of visualizations, a heatmap and a scatterplot matrix.

### Tasks supported by Heatmap:
- Find assignments where more number of students performed poorly
- For a given assignment, find which grade score bucket range is highly filled or popular
- Find immediate trends in the grade distribution across assignments
  - Find assignments where more number of students scored below 10
  - Find assignments where students scored above 50
- Find assignments with smallest and largest number of posts
  - Find assignments which did not generate as many posts as any other assignment
  - Find assignments whihc generated more posts than most of the other assignments
- Find assignments where longer posts were frequent
- Find assignments where maximum post length is more than that of other assignments
- Find assignments where maximum post length does not exceed 2nd bin (or any lower bin)

### Tasks supported by Scatterplot matrix:
- Each row in the data file represents an assignment entry for a student with grade score, lateness value for this assignment, number of posts by this student for this assignment, average post length (mean length of all the posts by this student for this assignment), default static category (same for all students to color the data points similarly)
- Find correlation among pairs of attributes across all assignments and by student
  - Average post length vs Number of posts (per student)
    - Is there a correlation between students who post larger number of posts and length of posts? It is possible that students who post many posts tend to keep the lengths smaller. Or it is also possible that students post many number of larger posts.
  - Average post length vs Lateness
    - Is there a possibility that students who post late tend to keep the posts smaller because they were in a hurry?
    - Is is possible that students who post too early post smaller as they did not think through well or ehy posted for the sake of posting early?
    - Is it possible that students who posted late (positive lateness) tend to post longer posts as they freaked out that they were late and hence wanted to make a larger post?
  - Average post length vs Score
    - This may be a known fact that automatic grading is based on length of posts. But, this can help find anomalies where smaller posts had greater scores.
  - Number of posts vs Lateness
    - Is it possible that students who post late tend to have fewer posts?
  - Number of posts vs Score
    - Helps in observing trends in distribution of scores with respect to number of posts
  - Lateness vs Score
    - Helps to find anomalies where points were not deducted for positive lateness (turned in after due date)
  
