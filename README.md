# Ad Placement



## Overview

Ad placement (or ad): The advertisement itself, in "place" on a website (or in an app, or on YouTube). An ad placement runs for a specific period of time, in a specific context. For example, the time period might be "labor day weekend" or "spring 2016". The context could be "the sports section of the Des Moines Register" or "during YouTube videos being displayed to women in Los Angeles between the ages of 21 and 35 who are interested in volleyball".

Cost per Mille (Thousand): (or CPM) The price paid by the buyer of an ad per 1,000 views of the ad, or "impressions".

Impressions one impression is one viewer seeing the ad in place


## Overview of design:
* The input files were smaller in size and because of the well known panda's library of python , which can create data frames like tables, I decided upon using python for the project.
* Used pandas to read delivery.csv and placements.csv and store it into dataframe. 
* Merged both the data frames on placement id's. Then calculated the sum of impressions per id and also the total cpm per id.

## Instructions to run the program
* Clone this repository
* Install python 3 
* This repo has 4 file - ad_placement.py , test_ad_placement.py, delivery.csv, placements.csv
* If using an IDE, open the project and run the "ad_placement.py". It imports all the necessary classes used for the project.
  Please make sure all the four files are in the same directory.
* If using command-line follow the instructions mentionded on the link: https://www.pythoncentral.io/execute-python-script-file-shell/. 
* Once you run the file, follow on screen instructions for user input to give the date range to calculate the total number of impressions and cost for that range.
* Output will be written in a `.txt` file in the same directory. There will be 2 files created 
  1) `report_byPlacement.txt` - This is a report containing the total number of impressions delivered and final cost of each placement.
  2) `report_total.txt` - This report calculates the number of impressions delivered and cost for an given range of days within the provided data set.

## Running the tests

This game has an automated test suite for unit testing . To run the test suite run `test_ad_placement.py` in your terminal/IDE to test all the methods.
