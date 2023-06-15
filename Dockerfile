# Use the official MySQL 8.0 image as the base image
FROM mysql:8.0

# Set the root password (change it to your desired password)
ENV MYSQL_ROOT_PASSWORD mysecretpassword

# Create a database and user (optional, modify as needed)
ENV MYSQL_DATABASE users_db
ENV MYSQL_USER myuser
ENV MYSQL_PASSWORD mypassword

# Copy custom SQL scripts to initialize the database (optional, modify as needed)
# COPY init.sql /docker-entrypoint-initdb.d/

# Expose the default MySQL port (change it if needed)
EXPOSE 3306

# Start the MySQL server when the container launches
CMD ["mysqld"]
