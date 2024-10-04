CREATE DATABASE IF NOT EXISTS recetas;
USE recetas;

CREATE TABLE roles (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(255) UNIQUE,
  descripcion TEXT
);

CREATE TABLE usuarios (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(255),
  email VARCHAR(255) UNIQUE,
  contraseña VARCHAR(255),
  foto_perfil VARCHAR(255),
  tipo_cuenta VARCHAR(255),
  rol_id BIGINT,
  FOREIGN KEY (rol_id) REFERENCES roles(id)
);

CREATE TABLE recetas (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(255),
  descripcion TEXT,
  instrucciones TEXT,
  dificultad VARCHAR(50),
  tiempo_preparacion INT,
  publica BOOLEAN
);

CREATE TABLE categoria_ingredientes (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(255) UNIQUE,
  descripcion TEXT
);

CREATE TABLE ingredientes (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(255),
  categoria_id BIGINT,
  FOREIGN KEY (categoria_id) REFERENCES categoria_ingredientes(id)
);

CREATE TABLE unidades (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(255) UNIQUE
);

CREATE TABLE receta_ingredientes (
  receta_id BIGINT,
  ingrediente_id BIGINT,
  cantidad VARCHAR(50),
  unidad_id BIGINT,
  PRIMARY KEY (receta_id, ingrediente_id),
  FOREIGN KEY (receta_id) REFERENCES recetas(id),
  FOREIGN KEY (ingrediente_id) REFERENCES ingredientes(id),
  FOREIGN KEY (unidad_id) REFERENCES unidades(id)
);

CREATE TABLE inventario (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  usuario_id BIGINT,
  ingrediente_id BIGINT,
  cantidad VARCHAR(50),
  unidad_id BIGINT,
  fecha_caducidad DATE,
  FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
  FOREIGN KEY (ingrediente_id) REFERENCES ingredientes(id),
  FOREIGN KEY (unidad_id) REFERENCES unidades(id)
);

CREATE TABLE planificaciones (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  usuario_id BIGINT,
  fecha_inicio DATE,
  fecha_fin DATE,
  tipo_planificacion VARCHAR(50),
  FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE menus (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  planificacion_id BIGINT,
  nombre VARCHAR(255),
  FOREIGN KEY (planificacion_id) REFERENCES planificaciones(id)
);

CREATE TABLE menu_recetas (
  menu_id BIGINT,
  receta_id BIGINT,
  PRIMARY KEY (menu_id, receta_id),
  FOREIGN KEY (menu_id) REFERENCES menus(id),
  FOREIGN KEY (receta_id) REFERENCES recetas(id)
);

CREATE TABLE listas_compras (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  usuario_id BIGINT,
  fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  completada BOOLEAN,
  FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE lista_ingredientes (
  lista_id BIGINT,
  ingrediente_id BIGINT,
  cantidad VARCHAR(50),
  unidad_id BIGINT,
  estado VARCHAR(50),
  PRIMARY KEY (lista_id, ingrediente_id),
  FOREIGN KEY (lista_id) REFERENCES listas_compras(id),
  FOREIGN KEY (ingrediente_id) REFERENCES ingredientes(id),
  FOREIGN KEY (unidad_id) REFERENCES unidades(id)
);

CREATE TABLE notificaciones (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  usuario_id BIGINT,
  mensaje TEXT,
  fecha_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE grupos (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(255),
  descripcion TEXT
);

CREATE TABLE categorias (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(255) UNIQUE,
  descripcion TEXT
);

CREATE TABLE usuario_recetas (
  usuario_id BIGINT,
  receta_id BIGINT,
  es_propietario BOOLEAN,
  PRIMARY KEY (usuario_id, receta_id),
  FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
  FOREIGN KEY (receta_id) REFERENCES recetas(id)
);

CREATE TABLE receta_categorias (
  receta_id BIGINT,
  categoria_id BIGINT,
  PRIMARY KEY (receta_id, categoria_id),
  FOREIGN KEY (receta_id) REFERENCES recetas(id),
  FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

CREATE TABLE usuario_grupos (
  usuario_id BIGINT,
  grupo_id BIGINT,
  PRIMARY KEY (usuario_id, grupo_id),
  FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
  FOREIGN KEY (grupo_id) REFERENCES grupos(id)
);
