create_user = """
  INSERT INTO users (name, email, username, password, date_of_birth, account_status)
  VALUES (%s, %s, %s, %s, %s, %s);
"""

create_car = """
  INSERT INTO cars (brand, model, year_of_manufacture, car_status)
  VALUES (%s, %s, %s, %s);
"""

create_rental = """
  INSERT INTO rentals (user_id, car_id, rental_date, rental_status)
  VALUES (%s, %s, %s, %s, %s);
"""

update_car_status = """
  UPDATE cars
  SET car_status = %s
  WHERE id = %s;
"""

update_user_account_status = """
  UPDATE users
  SET account_status = %s
  WHERE id = %s;
"""

complete_rental = """
  UPDATE rentals
  SET rental_status = 'completed'
  WHERE id = %s AND rental_status != 'completed';
"""

update_rental_status = """
  UPDATE rentals
  SET rental_status = %s
  WHERE id = %s;
"""

flag_user_late_payment = """
  UPDATE users
  SET account_status = 'late payment'
  WHERE id = %s;
"""

select_user = "SELECT * FROM users"

select_car = "SELECT * FROM cars"

select_rental = "SELECT * FROM rentals"