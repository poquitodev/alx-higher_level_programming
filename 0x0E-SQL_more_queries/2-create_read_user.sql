-- Log in as a MySQL user with sufficient privileges (e.g., root)
-- Replace 'your_username' and 'your_password' with your actual MySQL username and password.

-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Check if the user already exists and drop it if it does (to avoid conflicts)
DROP USER IF EXISTS 'user_0d_2'@'localhost';

-- Create the user with SELECT privilege and set the password
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege in the hbtn_0d_2 database to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply the privileges
FLUSH PRIVILEGES;
