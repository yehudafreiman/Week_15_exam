from typing import List, Dict, Any
import db

def get_customers_by_credit_limit_range():
    """Return customers with credit limits outside the normal range."""
    connection = db.get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
                    select customerName, creditLimit
                    from customers 
                    where creditLimit < 10000 
                    or creditLimit > 100000
                """)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return {"results": results}

def get_orders_with_null_comments():
    """Return orders that have null comments."""
    connection = db.get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
                    select orderNumber, comments
                    from orders
                    where comments is Null
                    order by orderDate
                """)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return {"results": results}

def get_first_5_customers():
    """Return the first 5 customers."""
    connection = db.get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
                    select customerName, contactLastName, contactFirstName
                    from customers
                    order by contactLastName
                    limit 5
                """)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return {"results": results}

def get_payments_total_and_average():
    """Return total and average payment amounts."""
    connection = db.get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
                    select sum(amount) totalAmount, 
                    avg(amount) averageAmount, 
                    min(amount) minAmount, 
                    max(amount) maxAmount
                    from payments
                """)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return {"results": results}

def get_employees_with_office_phone():
    """Return employees with their office phone numbers."""
    connection = db.get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
                    select employees.firstName,  
                    employees.lastName,  
                    offices.phone 
                    from employees 
                    inner join offices on employees.officeCode = offices.officeCode 
                """)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return {"results": results}

def get_customers_with_shipping_dates():
    """Return customers with their order shipping dates."""
    connection = db.get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
                    select customers.customerName, 
                    orders.orderDate
                    from customers
                    left join orders on customers.customerNumber = orders.customerNumber
                """)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return {"results": results}

def get_customer_quantity_per_order():
    """Return customer name and quantity for each order."""
    connection = db.get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
                    select customers.customerName, 
                    orderdetails.quantityOrdered
                    from customers
                    left join orders on customers.customerNumber = orders.customerNumber
                    left join orderdetails on orders.orderNumber = orderdetails.orderNumber
                    order by customers.customerName
                """)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return {"results": results}

def get_customers_payments_by_lastname_pattern():
    """Return customers and payments for last names matching pattern."""
    connection = db.get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
                    select customers.customerName, 
                    concat(employees.firstName, ' ', employees.lastName) salesRepName,
                    sum(amount) totalPayment
                    from customers
                    left join employees on customers.salesRepEmployeeNumber = employees.employeeNumber
                    left join payments on payments.customerNumber = customers.customerNumber
                    where employees.firstName like '%Mu%' or employees.firstName like '%ly%'
                    group by customers.customerName
                    order by sum(amount) desc 
                """)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return {"results": results}
