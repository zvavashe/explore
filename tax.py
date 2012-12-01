class DefaultIncomeTaxCalculator(object):
    """
    Income tax calculator based on a tax bands or brackets.  
    """
    
    def __init__(self, tax_brackets):
        """
        Initialise the calculator with the tax brackets used for performing
        income tax calculations. The tax brackets must be supplied in ascending
        order sorted by the lower limits. Each tax bracket must be a tuple of
        the form:
        (lower_limit, upper_limit, tax_rate)
        
        The highest income tax bracket has an upper limit value of None.
        """
        
        if tax_brackets:
            self.tax_brackets = tax_brackets
            
    def calculate_tax(self, taxable_income):
        """
        Calculates income tax payable based on the taxable income. Taxable
        income is income already adjusted for any allowable deductions.
        """
        
        income_tax = 0
        for tax_bracket in self.tax_brackets:
            income_tax += self.calculate_bracket_tax(taxable_income, 
                                                     tax_bracket) 
        
        return income_tax  
                
    def is_applicable(self, taxable_income, tax_bracket):   
        """
        A tax bracket is only applicable if the taxable income is above the tax
        bracket's lower limit.
        """
        lower_limit = tax_bracket[0]
        return taxable_income > lower_limit  
    
    def calculate_bracket_tax(self, taxable_income, tax_bracket):
        """
        Calculates payable income tax for a given tax bracket 
        """
        
        if self.is_applicable(taxable_income, tax_bracket):            
            lower_limit = tax_bracket[0]
            upper_limit = tax_bracket[1]
            tax_rate = tax_bracket[2]
            if upper_limit and upper_limit <= taxable_income:
                return (upper_limit - lower_limit) * tax_rate
            else:
                return (taxable_income - lower_limit) * tax_rate
        else:
            return 0                