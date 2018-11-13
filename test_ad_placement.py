# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 22:27:23 2018

@author: singh
"""


import unittest
import unittest.mock
from unittest.mock import patch
from ad_placement import AdPlacement

class Ad_placement(unittest.TestCase):
    def test_AdPlacementClass(self):
        ad_placement_object = AdPlacement()
        self.assertIsInstance(ad_placement_object,AdPlacement)
        
    def test_set_delivery_file_path(self):
        ad_placement_object = AdPlacement()
        ad_placement_object.set_delivery_file_path("./delivery.csv")
        self.assertEqual(ad_placement_object.deliveryFile_path, "./delivery.csv")
        
    def test_set_placement_file_path(self):
        ad_placement_object = AdPlacement()
        ad_placement_object.set_placements_file_path("./placements.csv")
        self.assertEqual(ad_placement_object.placementsFile_path, "./placements.csv")
        
    def test_placements_file_path_is_set(self):
        ad_placement_object = AdPlacement()
        ad_placement_object.set_placements_file_path("./placements.csv")
        self.assertTrue(ad_placement_object.placements_file_path_is_set())
    
    def test_delivery_file_path_is_set(self):
        ad_placement_object = AdPlacement()
        ad_placement_object.set_delivery_file_path("./delivery.csv")
        self.assertTrue(ad_placement_object.delivery_file_path_is_set())
        
    def test_get_impressions_by_placements(self):
        ad_placement_object = AdPlacement()
        ad_placement_object.set_placements_file_path("./placements.csv")
        ad_placement_object.set_delivery_file_path("./delivery.csv")
        ad_placement_object.get_impressions_by_placements()
        f = open("report_byPlacement.txt", "r")
        result_expected = "Sports (11/1/17-11/30/17): 1083576 impressions @ $5 CPM = 5418\n\
Business (12/1/17-12/31/17): 1607958 impressions @ $8 CPM = 12864\n\
Travel (11/1/17-11/30/17): 1035966 impressions @ $3 CPM = 3108\n\
Politics (12/1/17-12/31/17): 1529821 impressions @ $6 CPM = 9179\n"
        self.assertEqual(f.read() , result_expected)
        f.close()

            
    def test_total_impressions_within_date(self):
        ad_placement_object = AdPlacement()
        ad_placement_object.set_placements_file_path("./placements.csv")
        ad_placement_object.set_delivery_file_path("./delivery.csv")
        user_input = ["2017","11","22","2017","12","5"]
        result_expected = "Total (22/11/2017-5/12/2017): 1126785 impressions, $6061"
        
        with patch('builtins.input', side_effect=user_input):
            ad_placement_object.total_impressions_within_date()
        
        f = open("report_total.txt", "r")
        self.assertEqual(f.read(), result_expected)
        f.close()
        

            
        
        
        
        
        
        
        
if __name__ == "__main__":
    suit = unittest.TestLoader().loadTestsFromTestCase(Ad_placement)
    unittest.TextTestRunner(verbosity=2).run(suit)