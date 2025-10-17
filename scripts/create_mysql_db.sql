-- SQL to create database and a dedicated user for the TMS Django project
-- Edit the username/password as desired before running

CREATE DATABASE IF NOT EXISTS `uap_tms_db` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Recommended dedicated user (adjust host if you will connect differently)
CREATE USER IF NOT EXISTS 'tms_user'@'127.0.0.1' IDENTIFIED BY 'tms_password_here';
GRANT ALL PRIVILEGES ON `uap_tms_db`.* TO 'tms_user'@'127.0.0.1';

-- Optionally allow localhost host entry as well
CREATE USER IF NOT EXISTS 'tms_user'@'localhost' IDENTIFIED BY 'tms_password_here';
GRANT ALL PRIVILEGES ON `uap_tms_db`.* TO 'tms_user'@'localhost';

FLUSH PRIVILEGES;

-- Verify
SHOW DATABASES LIKE 'uap_tms_db';
SELECT user, host FROM mysql.user WHERE user = 'tms_user';
