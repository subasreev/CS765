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
- Find correlation among pairs of attributes across all assignments and by student
- Each row in the data file represents an assignment entry for a student with grade score, lateness value for this assignment, number of posts by this student for this assignment, average post length (mean length of all the posts by this student for this assignment), default static category (same for all students to color the data points similarly)
  - Average post length vs Number of posts (per student)
  - Average post length vs Lateness
  - Average post length vs Score
  - Number of posts vs Lateness
  - Number of posts vs Score
  - Lateness vs Score
  
