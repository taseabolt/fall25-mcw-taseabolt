# Homework 2: Data Clearning

Tara Seabolt  
CS 625, Fall 2025  
Due: September 21, 2025

## OpenRefine

### **Part 1: Cleaning Data**
1. To begin my homework 2 assignment after uplaoding the Pet Names data and creating a new report within OpenRefine, I utilized the ***Cluster and Edit*** feature on various columns, including *What kind of pet is this*, *Pet's Full Name*, *Pet's Everyday Name* and *Pet's Breed*. I went through the different cluster features, including both *key collision* and *nearest neighbor* along with each keying function to locate different groups of cell values that refered to the same names or values. I reveiwed each and then merged clusters as indicated.
2. After completing my cluster review for each of the columns listed above, I utlized the ***Text Facet*** feature to further edit cell values that were similar. I made sure similar values were changed to the same values for continutity and good data practices. I also utilized other columns (such as the *Pet's Breed* column) to make deductions about what kind of pet should have been entered into the cell for the *What kind of pet is this* column. If there were multiple pets entered on the same line, I utilized the first kind of pet / pet name / pet breed for the cells and disregarded the second values so that each line only contains information about one pet. 
3. Next, I decided to tackle the *Pet's Age* column where I used a transform expression of `value.replace(/(\d+).*$/, "$1")` to remove text after a number for any non-numerical values. To get the non-numerical values, I opned the numerical facet and filtered to only the non-numerical values. After transforming the data, I then used the edit cells, common transforms, and the **to number** feature on the data to transform all the data entered into numbers (which is reprsented by the text in the columns converting to a green color form black, indicatin numerical values). For the remianing few columns that had text before values or values that were spelled out instead of utilizng a number, I used the ***Text Facet*** feature to edit the remaining cells manually and remove unncessary information from the cell that was not related to a numerical age and to convert the text answers to a number as well.
4. Finally, I utilized various GREL expressions such as `value.replace("(","").replace(")","")`, `value.replace(",","").replace(",","")`, and `value.toTitlecase()` on the *Pet's full name* and *Pet's everyday name* columns to remove any text with parentheiss and commas and to convert all words within the columns to *Title Case* for continuity.


### **Part 2: Analyze Cleaned Data **
1. How many **kinds of pets** are in your cleaned dataset?  
   There are 31 different types of pets within my cleaned dataset. I came to this conclusion after utilizing steps 1-2 in Part 1 to clean the column titled *What kind of pet is this?* through ***Cluster and Edit*** to merge similiar values together and by using the ***Text facet*** open to edit values manually that were similar as well. After cleaning my data, I searched for the requessted value by using the ***Text Facet*** option to show the different values for the *What kind of pet is this*.
<img src="HW2-%20Question%201.png" height="200" alt="Screenshot of my OpenRefine report for HW2 - Question 1">

2. How many **breeds of cats** are in your cleaned dataset?  
   There are about 58 different breeds of cats within my cleaned dataset. This was the result after I utilized the clenaing steps 1-2 within Part 1 to clean up the *Pet's Breed* and *What kind of pet is this* columns and then using the ***Text Facet*** option to select **Cats** from the *What kind of pet is this* column and then using the ***Text Facet*** option again for the *Pet's breed* column to show how many different types there are.
<img src="HW2%20-%20Question%202.png" height="200" alt="Screenshot of my OpenRefine report for HW2 - Question 2">

3. How many **guinea pigs** are in your cleaned dataset?  
   There are 13 guinea pigs within my cleaned dataset after cleaning each row utilizing the ***Cluster and Edit*** options for each column, as described in steps 1 and 2 of Part 1 of my clean up the *Pet's Breed* column. I was able to locate this information by using the ***Text Facet*** option to filter data in the *What kind of pet is this* column to only the **Guinea Pig** selection, which shows the total number.
<img src="HW2%20-%20Question%203.png" height="200" alt="Screenshot of my OpenRefine report for HW2 - Question 3">

4. Who is the **oldest dog** in your cleaned dataset? Give the dog's name, breed, and age. If there's a tie, list all oldest dogs.  
  The oldest dog within my cleaned dataset is ***Dino***, who is a Keeshound and is 30 years of age (wow!). By cleaning up the *Pet's age* column using steps 1 through 4 within Step 1, I was able to convert the column to numbers and remove any unnecessary characters or text within the column through GREL expressions. After cleaning the data, I then utlized the ***Text Facet*** feature to select **Dogs** as the filter option and then sorted the *Pet's Age* column from highest to lowest to see which dog had the highest age listed. 
<img src="HW2%20-%20Question%204.png" height="200" alt="Screenshot of my OpenRefine report for HW2 - Question 4">

5. What is the **most popular everyday name for a dog** in your cleaned dataset? If there's a tie, list all top names and number of occurrences.  
  The most popular everyday name for a dog within my cleaned dataset is ***Daisy***, with 12 dogs listed as having that as an everyday name. Cleaning up the *Pet's everyday name* column my steps in Part 1, I was able to merge many similar names and remove unnecessary text by transforming text within the columns using GREL expressions, including removing parentheisis and commas and converting all words with Title Case to ensure continuity. After cleaning my data, I utilized the ***Text Facet*** feature to filter for only **Dogs** on the *What kind of pet is this* column and then utilized the ***Text Facet*** feature for the *Pet's Name* column and clicking on *count* to get a count of each name from highest to lowest. 
<img src="HHW2%20-%20Question%205.png" height="200" alt="Screenshot of my OpenRefine report for HW2 - Question 5">


## References
* Markdown Guide: Basic Syntax, <https://markdownguide.offshoot.io/basic-syntax/>
* OpenRefine: General Refine Expression Language, <https://openrefine.org/docs/manual/grel>
* Hands on: GREL, <https://libjohn.github.io/openrefine/grel.html>
* Library Carpentry: Open Refine, <https://librarycarpentry.github.io/lc-open-refine/>
