# Homework 4: Arrange Tables

Tara Seabolt  
CS 625, Fall 2025  
Due: October 11, 2025

## Dataset 2: [Section 10. National Security and Veterans Affairs](https://www.census.gov/library/publications/2009/compendia/statab/129ed/national-security-veterans-affairs.html) / Table 498. Department of Defense Personnel: 1960 to 2008

### Question 1:  
Show how the number of the total number of personnel in each of the armed forces (Army, Navy, Marine Corps, Air Force) has changed over time.

<img src="Question 1 chart.png" height="450" alt="Total Number of Personnel for each Armed Forces Branch (1960-2008)">

Link to excel workbooks: ([Original Table 498: Department of Defense Personnel: 1960 to 2008](https://github.com/odu-cs625-datavis/fall25-mcw-taseabolt/blob/main/Original%20Table%20498.xlsx))
([Edited Long Format Table 498: Department of Defense Personnel: 1960 to 2008](https://github.com/odu-cs625-datavis/fall25-mcw-taseabolt/blob/main/Table%20498%20-%20Long%20Format.xlsx))

Link to Tableau workbook:([Number of Personnel for each Armed Forces Branch (1968-2008)](https://github.com/odu-cs625-datavis/fall25-mcw-taseabolt/blob/main/Number%20of%20U.S.%20Armed%20Forces%20Personnel%20by%20Branch.twbx))


Idiom: Multiple Line Graph / Mark: Points with connection marks  
| Data: Attribute | Data: Attribute Type  | Encode: Channel | 
|---|---|---|
| year | Key, ordered | horizontal spatial position (x-axis) |
| number of armed forces personnel | value, quantitative | vertical spatial position  (y-axis) |
| branch of service | categorical | color hue |

I decided to utilize the multiple line chart idiom for my dataset because the question was specifically looking at how an attribute has changed over time. The multiple lines allowed me to incorproate the different branches of service categories as different lines while having the years on the x-axis and the quantiative number of personnel value on the y-axis. 

While working on creating my chart, I noticed that the number of personnel increased around the time of the Vietnam war, with a signifiant increase in Army personnel during 1968. This correlates with history since many service members joined or were drafted during this war-time period. In addition, I also gained insight into how the Army tends to have higher numbers of personnel over other branches and that the Marine Corps tend to have the lowest numbers of personnel over the four branches.

When creating my multiple line chart, I made a few different design decisions that I felt would make the visualization easy to interpret and understand, while still conveying the data presented. I added points for each data point so it is easier to see where each one falls within the overall line and because it makes it easier to see how the values change over time. In addition, I also ensured that I chose a color pallette that complemented each line but also allowed for each line to be distinct from the others. I also added tick marks on both axes so it was easier to see wheere the data points fall within the attributes on each axis. 

The only special customization that I made was to the dataset. I isolated the total number of personnel from each branch and for each year. Then I utilized PowerQuery to transform the data into a long format table so that I could easily create a chart within Tableau. 


explanation of how the idiom used in your chart is appropriate for your datasets and question/task
discussion of any insights gained about the data from your chart
discussion of any design decisions you made
discussion of any special customizations you used


### Question 2
Compare the proportion of male to female enlisted for each of the armed forces in 2008.



Idiom: Stacked Bar Chart / Mark: Line 
| Data: Attribute | Data: Attribute Type  | Encode: Channel | 
|---|---|---|
| branch of service | Key, categorical | horizontal spatial position (x-axis) |
| gender | secondary key, categorical | vertical region (y-axis) |
| number of personnel | value, quantitative | unaligned inner vertical spatial region (y-axis) |
| gender | categorical | color hue |

I decided to utilize the stacked bar chart idiom for my dataset because the question was looking to compare the number of male enlisted to number of female enlisted for each of the armed forces in 2008. The stacked bars allows me to show the proportions of both male enlisted and female enslisted in the same bar on for each of the braches of service on the x-axis, while also allowing the user to see the total of enlisted for each branch on the y-axis as well. 

While working on creating my chart, I noticed that the number of males enslisted is always higher than the number of females enlisted. The chart also provided insight into which branches of service each of the genders preferred, which actually ended up being the same for both: the Army. 

When creating my stacked bar chart, I made quite a few design decisions that I felt added to being able to understand what the data is trying to convey, while still making the visualization simple and easy to understand. I decided to add mark labels to each of the bars, so it was easier to see the difference in the number of males versus females for each branch of service. I also chose a color pallette that correlated with traditional gender colors, making it easier to understand which bar / mark represents which gender.

The only special customization that I made was within the dataset, making sure to narrow down the data to only male and female personnel numbers in only the year 2008 for each of the braches of service. I utilized PowerQuery to transform the data into a long format table prior to uploading within Tableau for chart creation. 

