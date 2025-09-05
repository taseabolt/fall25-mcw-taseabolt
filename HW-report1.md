# Homework 1: Tool Setup

Tara Seabolt  
CS 625, Fall 2025  
Due: September 7, 2025

## Git, GitHub

### Q1 - URL of GitHub Repo

https://github.com/taseabolt/CS625_HW1.git

### Q2 - Pull Command

The pull command works by sending remote changes made on GitHub to the local machine. 

### Q3 - Local Commits

If you have committed a change on your local machine but do not see the update on GitHub, then you may have forgotten to push the changes back to the branch.

## Markdown

### Q1 - Bulleted List

#### ***Favorite Foods List*** ####
- Pizza
- Dal Makhani
- Burritos

A bulleted list is different from a numbered list due to it being unordered. 

### Q2 - Markdown Paragraph

This is an example of a paragraph within markdown. Within it, I will utilize the markdown language to show *italics*, **bold**, and ***bold italics***. I will also show how to specify `lines of code` within markdown as well, in addition to providing links to specific websites, like [GitHub Docs](https://docs.github.com/en).

### Q3 - Animal Image

![Photo of a Rhino from Conde Nast Traveler!](/rhinophoto.webp "Rhino")

## Tableau

### Q1 - Region Other Than the South

![Image of Sales in the East chart from Tableau](/salesintheeast.png "Sales in the East")

## Google Colab

### Q1 - URL of Google Colab Notebook

[Tara's copy of the notebook](https://colab.research.google.com/drive/1cZWRa-PQjnpkHzAuR35XgdDkYMn4uMEl?usp=sharing)

## Python/Seaborn

### Q1 - First Penguin Image

![Image of First Penguin Chart in GoogleCoLab](/firstpengiunimage.png "First image")

This figure is showing a plot of the penguin bill length on the x-axis vs bill size on the y-axis, both in millimeters.

### Q2 - Second Penguin Image

![Image of Second Penguin Chart in GoogleCoLab](/secondpenguinimage.png "Second image")

This figure is showing a bar graph of the body mass (in grams) on the x-axis for the three different penguin species listed on the y-axis.

### Q3 - Outer Parenthesis

When I removed the outer parenthesis and indentions, I received a syntax error since there was a line break in the code. However, once I combined the two lines of code to one line, I was able to successfully run the code and produce the expected plot / graph. 

## Observable and Vega-Lite

### Q1 - markCircle to markSquare

Changing markCircle to markSquare caused the individual plot points on the graph to change from a circle to a square.

### Q2 - markCircle to markPoint

Changing markCircle to markPoint caused the inddividual plot points on the graph to change from a fully colored in circle to the outline of a circle, with a hollow center.

### Q3 - Swap X and Y Axes on Scatterplot

In order to swap the x and y axes on the scatterplot, I changed vl.x().fieldQ("Horsepower") to vl.y().fieldQ("Horsepower") and changed vl.y().fieldQ("Miles_per_Gallon") to vl.x().fieldQ("Miles_per_Gallon").

### Q4 - Remove fieldN(Origin)

![Count of Car Records bar graph](/countofrecords.png "Count of Records")

This is the result of the code change because it completely removed the y-axis variable from the graph, resulting in only the x-axis count aggregation being displayed.

## References

* Cloning a Repository, <https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>
* Basic Writing & Formatting Syntax, <https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax>
* Markdown Guide: Basic Syntax, <https://markdownguide.offshoot.io/basic-syntax/>
* GitHub Docs, <https://docs.github.com/en>
* Rhino Photo from "This Baby Animal from India is the Cutest in the World", <https://www.cntraveller.in/story/this-baby-animal-from-india-is-the-cutest-in-the-world/>
* Tutorial: Getting Started with Tableau Desktop, <https://help.tableau.com/current/guides/get-started-tutorial/en-us/get-started-tutorial-home.htm>
* Google Colaboratory: Frequently Asked Questions, <https://research.google.com/colaboratory/faq.html>
* CS 523 Module 2 - Introduction to Python, <https://github.com/cci-web-science-security/web-science/blob/main/modules.md#module-2>
* Breaking Up Long Lines of Code in Python, <https://www.pythonmorsels.com/breaking-long-lines-code-python/>
* A Taste of Observable, <https://observablehq.com/@observablehq/a-taste-of-observable>
* Charting with Vega-Lite, <https://observablehq.com/@observablehq/vega-lite>
* Vega-Lite - Mark, <https://vega.github.io/vega-lite/docs/mark.html#types>
