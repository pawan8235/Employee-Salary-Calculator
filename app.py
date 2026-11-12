def calculate_hra(basic):
    return 0.20 * basic
def calculate_da(basic):
    return 0.10 * basic
def calculate_pf(basic):
    return 0.12 * basic
def calculate_gross(basic, hra, da):
    return basic + hra + da
def calculate_tax(gross):
    if gross <= 25000:
        return 0.0
    elif gross <= 50000:
        # 5% on the amount above 25000, or typically 5% of gross depending on slab interpretation. 
        # Let's check Test Case 1: Gross = 39000, Tax = 1950 (which is 5% of 39000).
        # Test Case 4: Gross = 65000, Tax = 6500 (which is 10% of 65000).
        # Therefore, the tax rate applies to the entire gross based on the bracket.
        return 0.05 * gross
    else:
        return 0.10 * gross
def print_slip(emp_id, emp_name, basic, hra, da, gross, pf, tax, net_salary):
    print("\n" + "=" * 40)
    print(" " * 12 + "SALARY SLIP")
    print("=" * 40)
    print(f"Employee ID   : {emp_id}")
    print(f"Employee Name : {emp_name}")
    print("-" * 40)
    print(f"Basic Salary  : {basic:.2f}")
    print(f"HRA (20%)     : {hra:.2f}")
    print(f"DA (10%)      : {da:.2f}")
    print(f"Gross Salary  : {gross:.2f}")
    print("-" * 40)
    print(f"PF (12%)      : {pf:.2f}")
    print(f"Tax           : {tax:.2f}")
    print(f"Net Salary    : {net_salary:.2f}")
    print("=" * 40 + "\n")
def main():
    print("=== Employee Salary Calculator ===")
    while True:
        emp_id = input("Enter Employee ID: ")
        emp_name = input("Enter Employee Name: ")
        # Input validation for basic salary
        while True:
            raw_salary = input("Enter Basic Salary: ")
            try:
                basic = float(raw_salary)
                if basic < 0:
                    print("Invalid salary. Enter a positive number.")
                    continue
                break
            except ValueError:
                print("Invalid salary. Enter a positive number.")  

        # Calculations
        hra = calculate_hra(basic)
        da = calculate_da(basic)
        gross = calculate_gross(basic, hra, da)
        pf = calculate_pf(basic)
        tax = calculate_tax(gross)
        net_salary = gross - (pf + tax)  
        # Print Slip
        print_slip(emp_id, emp_name, basic, hra, da, gross, pf, tax, net_salary)
        #Loop option for more employees
        choice = input("Do you want to calculate for another emoloyees")
        if choice != 'y':
            print("Exiting Employee Salary Calculator. Thank you!")
            break
if __name__ == "__main__":
    main()
