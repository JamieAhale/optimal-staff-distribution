import pandas as pd
from itertools import product

def simulate_financial_model_adjusted(sales_team, account_management_team, support_team):

    initial_customers = 1000
    baseline_churn_rate = 0.10  
    organic_growth = 25
    baseline_fee = 100
    account_manager_capacity = 25
    revenue_growth_rate = 0.20  
    max_growth_months = 6  

    total_customers = initial_customers
    cumulative_revenue = 0
    managed_customers = min(account_management_team * account_manager_capacity, initial_customers)

    for month in range(1, 25):
        
        new_customers_from_sales = sales_team * 5  
        new_customers = new_customers_from_sales + organic_growth

   
        adjusted_churn_rate = (0.85 ** support_team) * baseline_churn_rate

     
        churned_customers = int(total_customers * adjusted_churn_rate)

        total_customers = total_customers + new_customers - churned_customers

     
        monthly_revenue = total_customers * baseline_fee

        additional_revenue = 0
        if month <= max_growth_months:
            for i in range(1, month + 1):
                additional_revenue += managed_customers * baseline_fee * (revenue_growth_rate * i)
        else:
            additional_revenue = managed_customers * baseline_fee * (revenue_growth_rate * max_growth_months)

        monthly_revenue += additional_revenue

        cumulative_revenue += monthly_revenue

    return cumulative_revenue

team_distributions = [(sales, am, 20 - sales - am) for sales, am in product(range(21), repeat=2) if sales + am <= 20]

distribution_revenues = {}

for distribution in team_distributions:
    sales, am, support = distribution
    revenue = simulate_financial_model_adjusted(sales, am, support)
    distribution_revenues[distribution] = revenue


optimal_distribution = max(distribution_revenues, key=distribution_revenues.get)
optimal_revenue = distribution_revenues[optimal_distribution]


print(f"Optimal Distribution: Sales={optimal_distribution[0]}, AM={optimal_distribution[1]}, Support={optimal_distribution[2]}")
print(f"Cumulative Revenue: ${optimal_revenue}")
