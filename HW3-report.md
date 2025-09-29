# Homework 3: Create Visualization Idioms from Real-World Data

Tara Seabolt  
CS 625, Fall 2025  
Due: September 28, 2025

## Bar Chart

### **Data**

- For my bar chart visualization, I utilized *Table 730* from **Section 14: Prices**, <https://www.census.gov/library/publications/2011/compendia/statab/131ed/prices.html>
- For this specific dataset, I decided to focus on the average price of fuel and electricity in the year 2010 to show the prices for each different element from one particular year, so I removed all other data. 

### **Chart Description**
- The visualization idiom of a bar chart was an appropriate choice for this dataset because it shows the total number of prices in the year 2010 for each element, providing a visualizstion of the differences in price.

- <img src="Ave Price Fuel Electricity.png" height="250" alt="Average Price of Fuel and Electricity in 2010">
- Idiom: Bar Chart / Mark: Line  
| Data: Attribute | Data: Attribute Type | Encode: Channel | 
| --- | --- | --- |
| type of fuel | key, categorical | separate, horizontal position (x-axis) |
| average price | value, quantitative | aligned vertical position (y-axis) |

- Link to Excel workbook: ([Average Price of Fuel & Electricity in 2010](https://github.com/odu-cs625-datavis/fall25-mcw-taseabolt/blob/e1f8c3b13d92b2760a74a60596b752aaea95ca8f/Avg%20Price%20Fuel%20Electricity.xlsx))
  
- The only customization that I did for this chart was making the bars blue to provide itnerest and draw attention to the attributes listed.


## Line Chart

### **Data**

- For my bar chart visualization, I utilized *Table 520* from **Section 10: National Security & Veterans Affairs**, <https://www.census.gov/library/publications/2011/compendia/statab/131ed/national-security-veterans-affairs.html>.
- For this specific dataset, I removed the District of Columbia and also removed the overall totals for the United States, focusing only on the number of Veterans during each period of service from each state.  

### **Chart Description**
- The visulzation idiom of a line chart was an appropriate choice for this dataset because it shows the total number of Veterans as a quantitative value on the y-axis and the ordered states on the x-axis along with allowing the categorical period of service to be representated on different lines, each being distingiuished by a different color.

- <img src="Number of Veterans by Period of Service and State.png" height="250" alt="Number of Veterans by Period of Service and State">
- Idiom: Multiple Line Chart / Mark: Points with connection marks   
| Data: Attribute | Data: Attribute Type  | Encode: Channel | 
| --- | --- | --- |
| state | key, ordered | seperate, horizontal position (x-axis) |
| number of veterans | value, quantitative | aligned vertical position (y-axis) |
| period of service | categorical | color hue |

- Link to Excel workbook: ([Number of Veterans by Period of Service and State](https://github.com/odu-cs625-datavis/fall25-mcw-taseabolt/blob/e1f8c3b13d92b2760a74a60596b752aaea95ca8f/Veterans%20by%20Period%20of%20Service%20State.xlsx))

- <img src="Veterans by Period of Service and State.png" height="250" alt="Number of Veterans by Period of Service and State">

- Link to Tableau workbook (for the recreated chart):([Number of Veterans by Period of Service and State](https://github.com/odu-cs625-datavis/fall25-mcw-taseabolt/blob/09c75707602c16660d8f81c0b0e3a911f4d5cb66/Veterans%20by%20Period%20of%20Service%20and%20State.twbx))

- For both my Excel and Tableau visualizations, I chose to customize the line colors to blue and red in order to distinguish between the two attributes but to provide consistency in both visualizations, so each color correlated to the same attribute in both. 


## Scatter Plot

### **Data**

- For my scatter plot visualization, I utilized *Table 78* from **Section 2: Births, Deaths, Marriages, and Divorce** <https://www.census.gov/library/publications/2011/compendia/statab/131ed/births-deaths-marriages-divorces.html>.
- For this specific dataset, I decided to focus in on the marriage and divorce values only for the years 1977 to 1997 so that I could compare the two values over the course of two decades.

### **Chart Description**

- The visualization idiom of a scatter plot was an appropriate choice for this dataset because it shows the relationship between marriange and divorce numbers from 1977 to 1997, highlighting trends over time and to see if there may be a correlation between the two values.

- <img src="Marriage and Divorce rate 1977 to 1997.png" height="250" alt="Marriage and Death numbers from 1977 to 1997 Scatter Plot">
Idiom: Scatterplot / Mark: Point  
| Data: Attribute | Data: Attribute Type  | Encode: Channel | 
| --- | --- | --- |
| marriage numbers | value, quantitative | horizontal spatial position (x-axis) |
| divorce numbers | value, quantitative | vertical spatial position  (y-axis) |

- Link to Excel workbook:([Marriage and Death numbers 1977 to 1997](https://github.com/odu-cs625-datavis/fall25-mcw-taseabolt/blob/7b70190f8ae835b02f431bad75d4b8bc67d3c8e5/Marriage%20and%20Death%20numbers%201977%20to%201997.xlsx))

- My only custimization that I did, aside from choosing the same colors and axis labels as my other visualizations, was utilizing data labels to incorporate the year for each point, to make it easier to understand and comprehend.

## Discussion
I recreated my Line Chart within Tableau, using the same dataset and thought that using this tool was quite eaiser than using Excel. Tableau allows for a more intuitive way to build visualizations through a more user firendly dashboard configuration, which made it easer to change out data for each axis and to quickly customize labels and colors as well.

## References
* Markdown Guide: Basic Syntax, <https://markdownguide.offshoot.io/basic-syntax/>
* Basic Writing & Formatting Syntax, <https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax>
* Section 14: Prices, <https://www.census.gov/library/publications/2011/compendia/statab/131ed/prices.html>
* Section 10: National Security & Veterans Affairs, <https://www.census.gov/library/publications/2011/compendia/statab/131ed/national-security-veterans-affairs.html>
* Section 2: Births, Deaths, Marriages, and Divorce, <https://www.census.gov/library/publications/2011/compendia/statab/131ed/births-deaths-marriages-divorces.html>
* Chart Redesigns, <https://github.com/odu-cs625-datavis/public-fall25-mcw/blob/main/Chart-Redesigns.md>
* Idiom-Mark-Data-Encode Table Examples, <https://github.com/odu-cs625-datavis/public-fall25-mcw/blob/main/idiom-mark-data-encode-Examples.md>
* Build Charts & Analyze Data, <https://help.tableau.com/current/pro/desktop/en-us/design_and_analyze.htm>

