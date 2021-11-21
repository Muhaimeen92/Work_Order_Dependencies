import unittest
import json

class TestWorkOrder(unittest.TestCase):

    def test_output(self):
        # Append corresponding lists of output and result files and run the unittest
        list_of_result_files = ["output.json"]
        list_of_output_files = ["text_data/output.json"]

        for result_path, output_path in zip(list_of_result_files, list_of_output_files):
            with open(output_path, "r") as output_file:
                output = json.load(output_file)
            with open(result_path, "r") as result_file:
                result = json.load(result_file)

            self.assertEqual(output, result)

if __name__ == "__main__":
    unittest.main()