CREATE DATABASE control_tareas_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

CREATE USER 'usuario_tareas'@'localhost'
IDENTIFIED BY 'CAMBIAR_PASSWORD';

GRANT ALL PRIVILEGES
ON control_tareas_db.*
TO 'usuario_tareas'@'localhost';

FLUSH PRIVILEGES;