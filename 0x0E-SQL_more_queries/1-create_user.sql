-- Log in as a MySQL user with sufficient privileges (e.g., root)
-- Replace 'your_username' and 'your_password' with your actual MySQL username and password.

-- Check if the user already exists and drop it if it does (to avoid conflicts)
DROP USER IF EXISTS 'user_0d_1'@'localhost';

-- Create the user with all privileges and set the password
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Apply the privileges
FLUSH PRIVILEGES;
