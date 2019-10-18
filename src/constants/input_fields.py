import us


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

BASIC_INFO = [{
    'range_pos': 0,
    'field': "Tax Advisor",
    'type': 'text',
    'name': 'tax_advisor'
}, {
    'range_pos': 0,
    'field': "Client Name",
    'type': 'text',
    'name': 'client_name'
}, {
    'range_pos': 0,
    'field': "Business Name",
    'type': 'text',
    'name': 'business_name'
}, {
    'range_pos': 0,
    'field': "State",
    'type': 'select',
    'name': 'state',
    'choices': STATES
}, {
    'range_pos': 0,
    'field': "Filing Status",
    'type': 'select',
    'name': 'filing_status',
    'choices': FILING_STATUSES
}, {
    'range_pos': 1,
    'field': "Industry",
    'type': 'select',
    'name': 'industry',
    'choices': INDUSTRIES
}, {
    'range_pos': 2,
    'field': "Number of Qualified Children",
    'type': 'number',
    'name': 'num_of_children'
}]

FEDERAL_INCOME = [{
    'range_pos': 0,
    'field': "W2 Income",
    'type': 'number',
    'name': 'w2_income',
    'currency': True
}, {
    'range_pos': 0,
    'field': "Bank Interest",
    'type': 'number',
    'name': 'bank_interest',
    'currency': True
}, {
    'range_pos': 0,
    'field': "Taxable IRA Distribution",
    'type': 'number',
    'name': 'taxable_ira_dist',
    'currency': True
}, {
    'range_pos': 0,
    'field': "Ordinary Dividends",
    'type': 'number',
    'name': 'ordinary_dividends',
    'currency': True
}, {
    'range_pos': 0,
    'field': "Qualified Dividends",
    'type': 'number',
    'name': 'qualified_dividends',
    'currency': True
}, {
    'range_pos': 0,
    'field': "Short Term Cap Gains",
    'type': 'number',
    'name': 'short_term_cap_gains',
    'currency': True
}, {
    'range_pos': 0,
    'field': "Long Term Cap Gains",
    'type': 'number',
    'name': 'long_term_cap_gains',
    'currency': True
}, {
    'range_pos': 0,
    'field': "Other Income (Non-SE)",
    'type': 'number',
    'name': 'other_income',
    'currency': True
}
]

FEDERAL_INCOME_ADJUSTMENTS = [{
    'range_pos': 0,
    'field': "Health Insurance Premium",
    'type': 'number',
    'name': 'health_insurance_premium',
    'currency': True
}, {
    'range_pos': 0,
    'field': "SEP IRA Contribution",
    'type': 'number',
    'name': 'sep_ira_contribution',
    'currency': True
}, {
    'range_pos': 0,
    'field': "IRA Deduction",
    'type': 'number',
    'name': 'ira_deduction',
    'currency': True
}, {
    'range_pos': 0,
    'field': "401k Contribution",
    'type': 'number',
    'name': '401k_contribution',
    'currency': True
}, {
    'range_pos': 0,
    'field': "Alimony Paid (Deductible Portion)",
    'type': 'number',
    'name': 'alimony_paid',
    'currency': True
}, {
    'range_pos': 0,
    'field': "Other Deductions",
    'type': 'number',
    'name': 'other_deductions',
    'currency': True
}
]

BUSINESS_INCOME = [{
    'range_pos': 0,
    'field': "S Corp Business Income (post wages)",
    'type': 'number',
    'name': 's_corp_business_income',
    'currency': True
}, {
    'range_pos': 0,
    'field': "Schedule C Income",
    'type': 'number',
    'name': 'schedule_c_income',
    'currency': True
}, {
    'range_pos': 0,
    'field': "S Corp Wages",
    'type': 'number',
    'name': 's_corp_wages',
    'currency': True
}
]

FEDERAL_DEDUCTIONS = [{
    'range_pos': 0,
    'field': "Mortgage Interest",
    'type': 'number',
    'name': 'mortgage_interest',
    'currency': True
}, {
    'range_pos': 0,
    'field': "State Income Taxes",
    'type': 'number',
    'name': 'state_income_taxes',
    'currency': True
}, {
    'range_pos': 0,
    'field': "Local/City Income Taxes",
    'type': 'number',
    'name': 'local_city_income_taxes',
    'currency': True
}, {
    'range_pos': 0,
    'field': "Property Taxes",
    'type': 'number',
    'name': 'property_taxes',
    'currency': True
}, {
    'range_pos': 0,
    'field': "Personal Property Taxes",
    'type': 'number',
    'name': 'personal_property_taxes',
    'currency': True
}, {
    'range_pos': 0,
    'field': "Cash Donations",
    'type': 'number',
    'name': 'cash_donations',
    'currency': True
}, {
    'range_pos': 0,
    'field': "Noncash Donations",
    'type': 'number',
    'name': 'noncash_donations',
    'currency': True
}, {
    'range_pos': 0,
    'field': "Other Donations",
    'type': 'number',
    'name': 'other_donations',
    'currency': True
}, {
    'range_pos': 0,
    'field': "Medical and Dental",
    'type': 'number',
    'name': 'medical_and_dental',
    'currency': True
}, {
    'range_pos': 1,
    'field': "Federal Tax Withheld",
    'type': 'number',
    'name': 'federal_tax_withheld',
    'currency': True
}
]

ESTIMATED_TAX_PAYMENTS = [{
    'range_pos': 0,
    'field': "Federal Estimated Tax Payments",
    'type': 'number',
    'name': 'federal_estimated_tax_payments',
    'currency': True
}
]
