import unittest

from tax import DefaultIncomeTaxCalculator

class TestDefaultIncomeTaxCalculator(unittest.TestCase):
    """
    Test the default income tax calculator implementation.
    """
    
    def setUp(self):
        tax_brackets = [(2000, 4000,0.2),
                        (4000, 6000, 0.25), 
                        (6000, 10000, 0.30), 
                        (10000, None, 0.5)]
        self.tax_brackets = tax_brackets
        self.tax_calculator = DefaultIncomeTaxCalculator(tax_brackets)
    
    def test_is_applicable(self):
        tax_calculator = self.tax_calculator
        for tax_bracket in self.tax_brackets:
            is_tax_bracket_applicable = tax_calculator.is_applicable(1000, tax_bracket)
            self.assertFalse(is_tax_bracket_applicable, 
                             "Tax bracket must not be applicable.")
            
        first_tax_bracket = self.tax_brackets[0] 
        self.assertFalse(tax_calculator.
                         is_applicable(2000, first_tax_bracket), 
                         "Tax bracket is not applicable.")   
        self.assertTrue(tax_calculator.
                        is_applicable(2001, first_tax_bracket), 
                        "Tax bracket is applicable.")
        
    def test_calculate_bracket_tax(self):
        first_tax_bracket = self.tax_brackets[0]
        tax_calculator = self.tax_calculator
        self.assertTrue(tax_calculator.
                        calculate_bracket_tax(4000, first_tax_bracket) == 400, 
                        "Calculated tax does not match expected amount")
        
        second_tax_bracket = self.tax_brackets[1]
        self.assertTrue(tax_calculator.
                        calculate_bracket_tax(5000, first_tax_bracket) == 400, 
                        "Calculated tax does not match expected amount")
        self.assertTrue(tax_calculator.
                        calculate_bracket_tax(5000, second_tax_bracket) == 250, 
                        "Calculated tax does not match expected amount")
        
        third_tax_bracket = self.tax_brackets[2]
        fourth_tax_bracket = self.tax_brackets[3]
        self.assertTrue(tax_calculator.
                        calculate_bracket_tax(9000, third_tax_bracket) == 900,
                        "Calculated tax does not match expected amount")
        self.assertTrue(tax_calculator.
                        calculate_bracket_tax(9000, fourth_tax_bracket) == 0, 
                        "Calculated tax does not match expected amount")
        self.assertTrue(tax_calculator.
                        calculate_bracket_tax(11000, fourth_tax_bracket) == 500,
                        "Calculated tax does not match expected amount")
        self.assertTrue(tax_calculator.
                        calculate_bracket_tax(13000, fourth_tax_bracket) == 1500,
                        "Calculated tax does not match expected amount")
        
    def test_calculate_tax(self):
        tax_calculator = self.tax_calculator
        self.assertTrue(tax_calculator.
                        calculate_tax(4000) == 400, 
                        "Calculated tax does not match expected amount")
        self.assertTrue(tax_calculator.
                        calculate_tax(5000) == 650, 
                        "Calculated tax does not match expected amount")
        self.assertTrue(tax_calculator.
                        calculate_tax(15000) == 4600, 
                        "Calculated tax does not match expected amount")
        

if __name__ == '__main__':
    unittest.main()