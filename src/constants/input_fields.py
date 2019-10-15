import us


BASIC_INFO = [{
        'field': "Tax Advisor",
        'type': 'text',
        'name': 'tax_advisor'
     }, {
        'field': "Client Name",
        'type': 'text',
        'name': 'client_name'
     }, {
        'field': "Business Name",
        'type': 'text',
        'name': 'business_name'
     }, {
        'field': "State",
        'type': 'text',
        'name': 'state'
     }, {
         'field': "Filing Status",
         'type': 'text',
         'name': 'filing_status'
     }, {
         'field': "Industry",
         'type': 'text',
         'name': 'industry'
     }, {
         'field': "Number of Qualified Children",
         'type': 'number',
         'name': 'num_of_children'
     }
]

FEDERAL_INCOME = [{
        'field': "W2 Income",
        'type': 'number',
        'name': 'w2_income'
     }, {
        'field': "Bank Interest",
        'type': 'number',
        'name': 'bank_interest'
     }, {
        'field': "Taxable IRA Distribution",
        'type': 'number',
        'name': 'taxable_ira_dist'
     }, {
        'field': "Ordinary Dividends",
        'type': 'number',
        'name': 'ordinary_dividends'
     }, {
         'field': "Qualified Dividends",
         'type': 'number',
         'name': 'qualified_dividends'
     }, {
         'field': "Short Term Cap Gains",
         'type': 'number',
         'name': 'short_term_cap_gains'
     }, {
         'field': "Long Term Cap Gains",
         'type': 'number',
         'name': 'long_term_cap_gains'
     }, {
         'field': "Other Income (Non-SE)",
         'type': 'number',
         'name': 'other_income'
     }
]

FEDERAL_INCOME_ADJUSTMENTS = [{
        'field': "Health Insurance Premium",
        'type': 'number',
        'name': 'health_insurance_premium'
    }, {
        'field': "SEP IRA Contribution",
        'type': 'number',
        'name': 'sep_ira_contribution'
    }, {
        'field': "IRA Deduction",
        'type': 'number',
        'name': 'ira_deduction'
    }, {
        'field': "401k Contribution",
        'type': 'number',
        'name': '401k_contribution'
    }, {
        'field': "Alimony Paid (Deductible Portion)",
        'type': 'number',
        'name': 'alimony_paid'
    }, {
        'field': "Other Deductions",
        'type': 'number',
        'name': 'other_deductions'
    }
]

BUSINESS_INCOME = [{
        'field': "S Corp Business Income (post wages)",
        'type': 'number',
        'name': 's_corp_business_income'
    }, {
        'field': "Schedule C Income",
        'type': 'number',
        'name': 'schedule_c_income'
    }, {
        'field': "S Corp Wages",
        'type': 'number',
        'name': 's_corp_wages'
    }
]

FEDERAL_DEDUCTIONS = [{
        'field': "Mortgage Interest",
        'type': 'number',
        'name': 'mortgage_interest'
    }, {
        'field': "State Income Taxes",
        'type': 'number',
        'name': 'state_income_taxes'
    }, {
        'field': "Local/City Income Taxes",
        'type': 'number',
        'name': 'local_city_income_taxes'
    }, {
        'field': "Property Taxes",
        'type': 'number',
        'name': 'property_taxes'
    }, {
        'field': "Personal Property Taxes",
        'type': 'number',
        'name': 'personal_property_taxes'
    }, {
        'field': "Cash Donations",
        'type': 'number',
        'name': 'cash_donations'
    }, {
        'field': "Noncash Donations",
        'type': 'number',
        'name': 'noncash_donations'
    }, {
        'field': "Other Donations",
        'type': 'number',
        'name': 'other_donations'
    }, {
        'field': "Medical and Dental",
        'type': 'number',
        'name': 'medical_and_dental'
    }, {
        'field': "Federal Tax Withheld",
        'type': 'number',
        'name': 'federal_tax_withheld'
    }
]

ESTIMATED_TAX_PAYMENTS = [{
        'field': "Federal Estimated Tax Payments",
        'type': 'number',
        'name': 'federal_estimated_tax_payments'
    }
]

STATES = [s.name for s in us.STATES]

FILING_STATUSES = [
    'Single',
    'Married Filing Jointly'
]

INDUSTRIES = [
    'Real Estate',
    'Food and Beverage',
    'Truckers',
    'Uber/Lyft/Rideshare Drivers',
    'Cannabis',
    'Entertainment',
    'Ecommerce'
]
