from fastapi import FastAPI
from db_init import init_database
from dal import get_customers_by_credit_limit_range, get_orders_with_null_comments, get_first_5_customers, \
    get_payments_total_and_average, get_employees_with_office_phone, get_customers_with_shipping_dates, \
    get_customer_quantity_per_order, get_customers_payments_by_lastname_pattern

app = FastAPI()

init_database()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/q1/customers-credit-limit-outliers")
def customers_credit_limit_outliers():
    result =  get_customers_by_credit_limit_range()
    return result

@app.get("/q2/orders-null-comments")
def orders_null_comments():
    result = get_orders_with_null_comments()
    return result

@app.get("/q3/customers-first-5")
def customers_first_5():
    result = get_first_5_customers()
    return result

@app.get("/q4/payments-total-average")
def payments_total_average():
    result = get_payments_total_and_average()
    return result

@app.get("/q5/employees-office-phone")
def employees_office_phone():
    result = get_employees_with_office_phone()
    return result

@app.get("/q6/customers-shipping-dates")
def customers_shipping_dates():
    result = get_customers_with_shipping_dates()
    return result

@app.get("/q7/customer-quantity-per-order")
def customer_quantity_per_order():
    result = get_customer_quantity_per_order()
    return result

@app.get("/q8/customers-payments-by-lastname-pattern")
def customers_payments_by_lastname_pattern():
    result = get_customers_payments_by_lastname_pattern()
    return result

