-- settings.sql
	CREATE DATABASE todo_list;
	CREATE USER todo_list_user WITH PASSWORD 'todo_list';
	GRANT ALL PRIVILEGES ON DATABASE todo_list TO todo_list_user;
