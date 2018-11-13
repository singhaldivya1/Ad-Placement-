# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 22:30:49 2018

@author: singh
"""

import pandas as pd
import datetime


class AdPlacement:

    # Constructor for the class
    def __init__(self):
        self.placements_data = 0
        self.delivery_data = 0
        self.placementsFile_path = None
        self.deliveryFile_path = None

    # Method to count all the impressions by placements.
    # Method will store the output to the file "report_byPlacement.txt"
    def get_impressions_by_placements(self):
        if not self.placements_file_path_is_set() or not self.delivery_file_path_is_set():
            print("ERROR!! You have to set path for the input files first. \n")
            return

        self.fetch_data()

        result = self.merge_data()

        result.final = (result.final.round())

        f = open("report_byPlacement.txt", "w")
        for index, row in result.iterrows():
            f.write(row[2] + " (" + row.start + "-" + row.end + "): " + str(row.impressions) + " impressions @ $" + str(
                row.cpm) + " CPM = " + str(int(row.final)) + "\n")
        f.close()


    # Method to count total impressions within given date range
    # Method writes the output to the file "report_total.txt"
    def total_impressions_within_date(self):
        if not self.placements_file_path_is_set() or not self.delivery_file_path_is_set():
            print("ERROR!! You have to set path for the input files first. \n")
            return
        print("To get number of impressions delivered and the cost for certain range of date. Please enter the start and end date as asked.\n")
        year_start = input("Enter the start year ")
        while not year_start.isnumeric():
            print("INVALID INPUT !!!! \n")
            year_start = input("Enter the start year: ")

        month_start = input("Enter the start month: ")
        while not month_start.isnumeric() or int(month_start) < 1 or int(month_start) > 12:
            print("INVALID INPUT !!! \n")
            month_start = input("Enter the start month: ")

        date_start = input("Enter the start day: ")
        while not date_start.isnumeric() or int(date_start) < 1 or int(date_start) > 31:
            print("INVALID INPUT !!! \n")
            date_start = input("Enter the start day")

        year_end = input("Enter the end year: ")
        while not year_end.isnumeric():
            print("INVALID INPUT !!!! \n")
            year_end = input("Enter the end year: ")

        month_end = input("Enter the end month: ")
        while not month_end.isnumeric() or int(month_end) < 1 or int(month_end) > 12:
            print("INVALID INPUT !!! \n")
            month_end = input("Enter the end month: ")

        date_end = input("Enter the end day: ")
        while not date_end.isnumeric() or int(date_end) < 1 or int(date_end) > 31:
            print("INVALID INPUT !!! \n")
            date_end = input("Enter the end day: ")

        self.fetch_data()
        self.delivery_data["date"] = pd.to_datetime(self.delivery_data["date"])
        self.delivery_data = self.delivery_data[
            (self.delivery_data['date'] >= datetime.date(int(year_start), int(month_start), int(date_start))) & (
                        self.delivery_data['date'] <= datetime.date(int(year_end), int(month_end), int(date_end)))]
        result = self.merge_data()
        impressions_total = result['impressions'].sum()
        dollar_total = round(result['final'].sum())

        f = open("report_total.txt", "w")
        f.write(
            "Total (" + date_start + "/" + month_start + "/" + year_start + "-" + date_end + "/" + month_end + "/" +
            year_end + "): " + str(impressions_total) + " impressions, $" + str(dollar_total))
        f.close()

    # Method to set the file path of the placements file
    def set_placements_file_path(self, placements_file_path):
        self.placementsFile_path = placements_file_path

    # Method to check if the placements file path has been set by the user
    def placements_file_path_is_set(self):
        return self.placementsFile_path is not None

    # Method to set the file path of the delivery file
    def set_delivery_file_path(self, delivery_file_path):
        self.deliveryFile_path = delivery_file_path

    # Method to check if the delivery file path has been set by the user
    def delivery_file_path_is_set(self):
        return self.deliveryFile_path is not None

    # Method to fetch the data from the files given by the user
    def fetch_data(self):
        self.placements_data = pd.read_csv(self.placementsFile_path)
        self.delivery_data = pd.read_csv(self.deliveryFile_path)

    # Method to store and merge data into the pandas data-frame read from fetch-data() method.
    def merge_data(self):
        self.delivery_data = self.delivery_data.groupby('placement_id', as_index=False)['impressions'].sum()
        self.placements_data.rename(columns={'id': 'placement_id'}, inplace=True)
        result = pd.merge(self.delivery_data,
                          self.placements_data[['placement_id', 'name', 'cpm', 'start', 'end']],
                          on='placement_id')
        result['final'] = ((result.impressions / 1000) * result.cpm)
        return result



if __name__ == "__main__":
    ad_placement_object = AdPlacement()
    ad_placement_object.set_placements_file_path("./placements.csv")
    ad_placement_object.set_delivery_file_path("./delivery.csv")
    ad_placement_object.get_impressions_by_placements()
    ad_placement_object.total_impressions_within_date()
