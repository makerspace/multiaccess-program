import unittest
from multi_access.dump import dump
from multi_access.dump import db_helper
import pickle
import json
import os


class Test(unittest.TestCase):
    
    def setUp(self):
        self.db = db_helper.create_default_engine()

    def test_table(self):
        dump.table(self.db, "Users")

    def test_tables(self):
        dump.tables(self.db)

    def test_to_file_pickle(self):
        out_file = "./dump.pkl"
        dump.to_file(out_file)
        print(f"Output file path: {os.path.realpath(out_file)}")
        dump.from_file(out_file)

    def test_to_file_json(self):
        out_file = "./dump.json"
        dump.to_file(out_file)
        print(f"Output file path: {os.path.realpath(out_file)}")
        dump.from_file(out_file)
