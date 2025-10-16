# Homework 4: Arrange Tables

Tara Seabolt  
CS 625, Fall 2025  
Due: October 11, 2025

## Dataset 2: [Section 10. National Security and Veterans Affairs](https://www.census.gov/library/publications/2009/compendia/statab/129ed/national-security-veterans-affairs.html) / Table 498. Department of Defense Personnel: 1960 to 2008

### Question 1:  
Show how the number of the total number of personnel in each of the armed forces (Army, Navy, Marine Corps, Air Force) has changed over time.

<img src="Question 1 chart.png" height="500" alt="Total Number of Personnel for each Armed Forces Branch (1960-2008)">

Link to excel workbooks: ([Original Table 498: Department of Defense Personnel: 1960 to 2008](https://github.com/odu-cs625-datavis/fall25-mcw-taseabolt/blob/main/Original%20Table%20498.xlsx))
([Edited Long Format Table 498: Department of Defense Personnel: 1960 to 2008](https://github.com/odu-cs625-datavis/fall25-mcw-taseabolt/blob/main/Table%20498%20-%20Long%20Format.xlsx))

Link to Tableau workbook:([Number of Personnel for each Armed Forces Branch (1968-2008)](https://github.com/odu-cs625-datavis/fall25-mcw-taseabolt/blob/main/Number%20of%20U.S.%20Armed%20Forces%20Personnel%20by%20Branch.twbx))


Idiom: Multiple Line Chart / Mark: Points with connection marks  
| Data: Attribute | Data: Attribute Type  | Encode: Channel | 
|---|---|---|
| year | key, ordered | horizontal spatial position (x-axis) |
| number of armed forces personnel | value, quantitative | vertical spatial position  (y-axis) |
| branch of service | categorical | color hue |

I decided to utilize the multiple line chart idiom for my dataset because the question was specifically looking at how an attribute has changed over time. The multiple lines allowed me to incorporate the different branches of service categories as different lines while having the years on the x-axis and the quantitative number of personnel value on the y-axis. 

While working on creating my chart, I noticed that the number of personnel increased around the time of the Vietnam war, with a significant increase in Army personnel during 1968. This correlates with history since many service members joined or were drafted during this war-time period. In addition, I also gained insight into how the Army tends to have higher numbers of personnel over other branches and that the Marine Corps tend to have the lowest numbers of personnel over the four branches.

When creating my multiple line chart, I made a few different design decisions that I felt would make the visualization easy to interpret and understand, while still conveying the data presented. I added points for each data point so it is easier to see where each one falls within the overall line and because it makes it easier to see how the values change over time. In addition, I also ensured that I chose a color palette that complemented each line but also allowed for each line to be distinct from the others. I also added tick marks on both axes so it was easier to see where the data points fall within the attributes on each axis. 

The only special customization that I made was to the dataset. I isolated the total number of personnel from each branch and for each year. Then I utilized PowerQuery to transform the data into a long format table so that I could easily create a chart within Tableau. 


### Question 2
Compare the proportion of male to female enlisted for each of the armed forces in 2008.

<img src="Question 2 Chart.png" height="600" alt="Comparison of male to female enlisted for each Armed Forces Branch (2008)">

Link to excel workbooks: ([Original Table 498: Department of Defense Personnel: 1960 to 2008](https://github.com/odu-cs625-datavis/fall25-mcw-taseabolt/blob/main/Original%20Table%20498.xlsx))
([Edited Long Format Table 498: Department of Defense Personnel: 1960 to 2008](https://github.com/odu-cs625-datavis/fall25-mcw-taseabolt/blob/main/Table%20498%20-%20Long%20Format.xlsx))

Link to Tableau workbook:([Comparison of male to female enlisted for each Armed Services Branch (2008)](https://github.com/odu-cs625-datavis/fall25-mcw-taseabolt/blob/main/Comparison%20of%20proporition%20of%20male%20to%20female%20enlisted%20for%20each%20branch.twbx))

Idiom: Stacked Bar Chart / Mark: Line 
| Data: Attribute | Data: Attribute Type  | Encode: Channel | 
|---|---|---|
| branch of service | Key, categorical | horizontal spatial position (x-axis) |
| gender | secondary key, categorical | vertical region (y-axis) |
| number of personnel | value, quantitative | unaligned inner vertical spatial region (y-axis) |
| gender | categorical | color hue |

I decided to utilize the stacked bar chart idiom for my dataset because the question was looking to compare the number of male enlisted to number of female enlisted for each of the armed forces in 2008. The stacked bars allow me to show the proportions of both male enlisted and female enlisted in the same bar on for each of the branches of service on the x-axis, while also allowing the user to see the total of enlisted for each branch on the y-axis as well. 

While working on creating my chart, I noticed that the number of males enlisted is always higher than the number of females enlisted. The chart also provided insight into which branches of service each of the genders preferred, which actually ended up being the same for both: the Army. 

When creating my stacked bar chart, I made quite a few design decisions that I felt added to being able to understand what the data is trying to convey, while still making the visualization simple and easy to understand. I decided to add mark labels to each of the bars, so it was easier to see the difference in the number of males versus females for each branch of service. I also chose a color palette that correlated with traditional gender colors, making it easier to understand which bar / mark represents which gender.

The only special customization that I made was within the dataset, making sure to narrow down the data to only male and female personnel numbers in only the year 2008 for each of the branches of service. I utilized PowerQuery to transform the data into a long format table prior to uploading within Tableau for chart creation. 

### Extra Credit
Combine this table with Table 2 (Population: 1960 to 2008, from Section 1 - Population) to show the relationship between the total in armed forces service and the US population (use Resident population, including Armed Forces overseas) over time.

<img src="Question 3 - EC.png" height="500" alt="Percentage of Total Resident Population that Participated in U.S. Armed Forces, 1960 - 2008">

Link to Excel workbook with added sheet combining tables: ([Table 2: Population: 1960 to 2008](https://github.com/odu-cs625-datavis/fall25-mcw-taseabolt/blob/main/Table%202.xls))

Link to Tableau workbook: ([Percentage of Total Resident Population that Participated in U.S. Armed Forces, 1960 - 2008](https://github.com/odu-cs625-datavis/fall25-mcw-taseabolt/blob/main/Percentage%20of%20Total%20Resident%20Population.twbx))

Idiom: Line Chart / Mark: Points with connection marks  
| Data: Attribute | Data: Attribute Type  | Encode: Channel | 
|---|---|---|
| year | key, ordered | horizontal spatial position (x-axis) |
| percentage of total resident population that participated in armed forces | value, quantitative | vertical spatial position  (y-axis) |

I decided to utilize a line chart idiom for my dataset because the question was specifically looking at what percentage of the U.S. Resident Population has participated in the Armed Forces over time. I was able to add a calculated field with my two values, that divided the total number of armed services personnel that I obtained from Table 298 by the total U.S. resident population (including armed services overseas) from Table 2 for each year and them multiplying each value by 100 to obtain the percentage. 

While working on creating my chart, I was able to infer that the percentage of U.S. residents who participated in the Armed Forces has continued to go down over time, ever since 1968, which was during the height of the Vietnam war. Although the U.S. resident population has increased, the overall percentage of those who participate in the Armed Forces has continued to go down. 

When creating my line chart, I made quite a few design decisions that I felt helped to make my visualization easy to understand and read. I decided to add mark labels to each of the bars, so it was easier to see the actual percentages of U.S. residents who participated in the Armed Forces for each year. I also chose a color palette that was bright but easy to read, especially for the mark labels. I also added tick marks and chose intervals for the year that allowed the data to be presented for all years, but that didn't crowd the x-axis, allowing for minor ticks in between the regular ticks. 

The only special customizations that I made was within the dataset were merging data from Table 298 into Table 2 to allow for comparison and then adding the calculated field within Tableau, to calculate the actual percentage of U.S. residents who participated in the Armed Forces over time.  


## Further Questions
When reviewing the datasets for my assignment, multiple questions and hypotheses came to fruition. One particular question that I thought of when reviewing Table 298 for Question 1 was if changes in military participation align with other major historical or war-time events beyond the Vietnam War, when the Armed Forces became a volunteer force, such as during the Cold War, during post-Cold War peace-time, or during the early 2000s Iraq and Afghanistan conflicts post 9/11? My hypothesis regarding this question would be that there is likely a correlation in higher recruitment or enlistment rates at the beginning of conflicts, such as the Iraq War; but that enlistment then reduces & tapers off the longer the conflict goes on. I could likely look at other tables within the 2010 Statistical Abstract, such as Table 505, to check out active-duty enrollment numbers by location & year to see if there were more active-duty enlistees during times of conflict or I could also look at Veterans data, such as Table 508 to see the number of Veterans during specific periods of service. 

## References
* Markdown Guide: Basic Syntax, <https://markdownguide.offshoot.io/basic-syntax/>
* Basic Writing & Formatting Syntax, <https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax>
* Section 10: National Security & Veterans Affairs, <https://www.census.gov/library/publications/2011/compendia/statab/131ed/national-security-veterans-affairs.html>
* Chart Redesigns, <https://github.com/odu-cs625-datavis/public-fall25-mcw/blob/main/Chart-Redesigns.md>
* Idiom-Mark-Data-Encode Table Examples, <https://github.com/odu-cs625-datavis/public-fall25-mcw/blob/main/idiom-mark-data-encode-Examples.md>
* Build Charts & Analyze Data, <https://help.tableau.com/current/pro/desktop/en-us/design_and_analyze.htm>
* Build Common Charts in Data Views, <https://help.tableau.com/current/pro/desktop/en-us/dataview_examples.htm>
* Unpivot Tables, <https://learn.microsoft.com/en-us/power-query/unpivot-column>
