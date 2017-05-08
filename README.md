# CS765
**Data Challenge 3**
Files:
- d3_heatmap.html - This is the html file that contains d3 code to display the visualization for Challenge 3. It is interactive and displays heatmap of distribution of values of fields(score, number of posts, length of posts) over all the assignments. The buttons at the bottom of the webpage help the user select the field for displaying the appropriate heatmap. Each entry value in the heatmap grid is the frequency of the bin. When you hover the mouse on the grid, it displays the frequency value. There is also a color scale at the bottom of the webpage that maps frequency values to colors. There is a button for switching to another visualization (heatmap->scatterplot matrix and vice-versa). The scatterplot matrix displays scatterplots for 3 fields namely, avergae length of posts, lateness and number of posts. 

- file_processor.py - This script is used to read the input json file and generate an output.csv file in a format to render the scatterplot matrix. This iscript must be executed before we load the webpage.

- The input data is in the RealisticData folder
