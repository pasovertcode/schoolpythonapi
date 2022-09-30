-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-09-2022 a las 22:25:54
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `escuela`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `obtenerAllEstudiantes` ()   SELECT *
from estudiante$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `obtenerEstudiante` (IN `codigoEstudiante` VARCHAR(50))   SELECT *
FROM estudiante as e
WHERE e.nid_estudiante = codigoEstudiante$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `obtenerMateria` (IN `codigoMateria` VARCHAR(50))   SELECT * 
FROM asignatura as a 
WHERE a.codigo_asignatura = codigoMateria$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `obtenerNotasEstudiante` (IN `codigoEstudiante` VARCHAR(50))   SELECT n.codigo_notas as codigo_notas, n.periodo_notas as periodo_notas, concat(p.nombres_profesor," ", p.apellidos_profesor) as nombre_profesor, a.nombre_asignatura as asignatura, n.curso_notas as curso, concat(e.nombres_estudiante, " ", e.apellidos_estudiante) as nombre_estudiante, n.calificacion_notas as calificacion, n.anotacion_notas as anotacion, n.estado_notas as estado_notas 
FROM notas as n
INNER JOIN profesor as p ON p.nid_profesor = n.nid_profesor
INNER JOIN asignatura as a ON n.codigo_asignatura = a.codigo_asignatura
INNER JOIN estudiante as e ON n.nid_estudiante = e.nid_estudiante
WHERE n.nid_estudiante = codigoEstudiante$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `obtenerProfesor` (IN `codigoProfesor` VARCHAR(50))   SELECT *
FROM profesor as p
WHERE p.nid_profesor = codigoProfesor and p.estado_profesor = 'activo'$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `obtenerUsuario` (IN `codigoUsuario` VARCHAR(50))   SELECT *
FROM user
WHERE user.codigo_user = codigoUsuario and user.codigo_user = "activo"$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asignatura`
--

CREATE TABLE `asignatura` (
  `id_asignatura` int(11) NOT NULL,
  `codigo_asignatura` varchar(255) DEFAULT NULL,
  `nombre_asignatura` varchar(255) NOT NULL,
  `estado_asignatura` varchar(255) NOT NULL,
  `fecha_creacion_asignatura` datetime NOT NULL,
  `creador_codigo_user` varchar(255) NOT NULL,
  `nota_asignatura` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiante`
--

CREATE TABLE `estudiante` (
  `id_estudiante` int(11) NOT NULL,
  `tipoid_estudiante` varchar(255) NOT NULL,
  `nid_estudiante` varchar(255) NOT NULL,
  `nacionalidad_estudiante` varchar(255) NOT NULL,
  `nombres_estudiante` varchar(255) NOT NULL,
  `apellidos_estudiante` varchar(255) NOT NULL,
  `fecha_nac_estudiante` date NOT NULL,
  `fecha_creacion_estudiante` datetime NOT NULL,
  `creador_codigo_user` varchar(255) NOT NULL,
  `estado_estudiante` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estudiante`
--

INSERT INTO `estudiante` (`id_estudiante`, `tipoid_estudiante`, `nid_estudiante`, `nacionalidad_estudiante`, `nombres_estudiante`, `apellidos_estudiante`, `fecha_nac_estudiante`, `fecha_creacion_estudiante`, `creador_codigo_user`, `estado_estudiante`) VALUES
(1, 'TI', '15782030', 'COLOMBIANA', 'Juan Alfonso', 'Carrillo Aristisaval', '2008-09-09', '2022-09-30 22:07:23', 'ADMIN01', 'activo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `notas`
--

CREATE TABLE `notas` (
  `id_notas` bigint(20) NOT NULL,
  `codigo_notas` varchar(255) DEFAULT NULL,
  `periodo_notas` varchar(255) NOT NULL,
  `nid_profesor` varchar(255) NOT NULL,
  `codigo_asignatura` varchar(255) NOT NULL,
  `curso_notas` varchar(255) NOT NULL,
  `nid_estudiante` varchar(255) NOT NULL,
  `calificacion_notas` varchar(255) NOT NULL,
  `anotacion_notas` text DEFAULT NULL,
  `estado_notas` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesor`
--

CREATE TABLE `profesor` (
  `id_profesor` int(11) NOT NULL,
  `tipoid_profesor` varchar(255) NOT NULL,
  `nid_profesor` varchar(255) NOT NULL,
  `nacionalidad_profesor` varchar(255) NOT NULL,
  `nombres_profesor` varchar(255) NOT NULL,
  `apellidos_profesor` varchar(255) DEFAULT NULL,
  `fecha_nac_profesor` date NOT NULL,
  `fecha_creacion_profesor` datetime NOT NULL,
  `creador_codigo_user` varchar(255) NOT NULL,
  `estado_profesor` varchar(255) NOT NULL,
  `nota_profesor` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `profesor`
--

INSERT INTO `profesor` (`id_profesor`, `tipoid_profesor`, `nid_profesor`, `nacionalidad_profesor`, `nombres_profesor`, `apellidos_profesor`, `fecha_nac_profesor`, `fecha_creacion_profesor`, `creador_codigo_user`, `estado_profesor`, `nota_profesor`) VALUES
(1, 'CC', '124214555', 'COLOMBIANA', 'Karlim David', 'Urdaeta', '1998-08-20', '2022-09-30 20:53:58', 'ADMIN01', 'activo', 'Profesor de ingles');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id_user` int(11) NOT NULL,
  `tipo_user` char(20) NOT NULL,
  `codigo_user` varchar(255) NOT NULL,
  `username_user` varchar(255) NOT NULL,
  `password_user` varchar(255) NOT NULL,
  `fecha_creacion_user` datetime NOT NULL,
  `estado_user` varchar(255) NOT NULL,
  `nota_user` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id_user`, `tipo_user`, `codigo_user`, `username_user`, `password_user`, `fecha_creacion_user`, `estado_user`, `nota_user`) VALUES
(1, 'admin', 'ADMIN01', 'admin', 'admin123', '2022-09-30 20:52:44', 'activo', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_estudiante`
--

CREATE TABLE `user_estudiante` (
  `id_user_estudiante` int(11) NOT NULL,
  `codigo_user` varchar(255) NOT NULL,
  `nid_estudiante` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_profesor`
--

CREATE TABLE `user_profesor` (
  `id_user_profesor` int(11) NOT NULL,
  `codigo_user` varchar(255) NOT NULL,
  `nid_profesor` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `asignatura`
--
ALTER TABLE `asignatura`
  ADD PRIMARY KEY (`id_asignatura`),
  ADD UNIQUE KEY `codigo_asignatura` (`codigo_asignatura`),
  ADD KEY `creador_codigo_user` (`creador_codigo_user`);

--
-- Indices de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD PRIMARY KEY (`id_estudiante`),
  ADD UNIQUE KEY `nid_estudiante` (`nid_estudiante`),
  ADD KEY `creador_codigo_user` (`creador_codigo_user`);

--
-- Indices de la tabla `notas`
--
ALTER TABLE `notas`
  ADD PRIMARY KEY (`id_notas`),
  ADD UNIQUE KEY `codigo_notas` (`codigo_notas`),
  ADD KEY `nid_profesor` (`nid_profesor`),
  ADD KEY `codigo_asignatura` (`codigo_asignatura`),
  ADD KEY `nid_estudiante` (`nid_estudiante`);

--
-- Indices de la tabla `profesor`
--
ALTER TABLE `profesor`
  ADD PRIMARY KEY (`id_profesor`),
  ADD UNIQUE KEY `nid_profesor` (`nid_profesor`),
  ADD KEY `creador_codigo_user` (`creador_codigo_user`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id_user`),
  ADD UNIQUE KEY `codigo_user` (`codigo_user`),
  ADD UNIQUE KEY `username_user` (`username_user`);

--
-- Indices de la tabla `user_estudiante`
--
ALTER TABLE `user_estudiante`
  ADD PRIMARY KEY (`id_user_estudiante`),
  ADD KEY `codigo_user` (`codigo_user`),
  ADD KEY `nid_estudiante` (`nid_estudiante`);

--
-- Indices de la tabla `user_profesor`
--
ALTER TABLE `user_profesor`
  ADD PRIMARY KEY (`id_user_profesor`),
  ADD KEY `codigo_user` (`codigo_user`),
  ADD KEY `nid_profesor` (`nid_profesor`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `asignatura`
--
ALTER TABLE `asignatura`
  MODIFY `id_asignatura` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  MODIFY `id_estudiante` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `notas`
--
ALTER TABLE `notas`
  MODIFY `id_notas` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `profesor`
--
ALTER TABLE `profesor`
  MODIFY `id_profesor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `user_estudiante`
--
ALTER TABLE `user_estudiante`
  MODIFY `id_user_estudiante` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `user_profesor`
--
ALTER TABLE `user_profesor`
  MODIFY `id_user_profesor` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asignatura`
--
ALTER TABLE `asignatura`
  ADD CONSTRAINT `asignatura_ibfk_1` FOREIGN KEY (`creador_codigo_user`) REFERENCES `user` (`codigo_user`);

--
-- Filtros para la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD CONSTRAINT `estudiante_ibfk_1` FOREIGN KEY (`creador_codigo_user`) REFERENCES `user` (`codigo_user`);

--
-- Filtros para la tabla `notas`
--
ALTER TABLE `notas`
  ADD CONSTRAINT `notas_ibfk_1` FOREIGN KEY (`nid_profesor`) REFERENCES `profesor` (`nid_profesor`),
  ADD CONSTRAINT `notas_ibfk_2` FOREIGN KEY (`codigo_asignatura`) REFERENCES `asignatura` (`codigo_asignatura`),
  ADD CONSTRAINT `notas_ibfk_3` FOREIGN KEY (`nid_estudiante`) REFERENCES `estudiante` (`nid_estudiante`);

--
-- Filtros para la tabla `profesor`
--
ALTER TABLE `profesor`
  ADD CONSTRAINT `profesor_ibfk_1` FOREIGN KEY (`creador_codigo_user`) REFERENCES `user` (`codigo_user`);

--
-- Filtros para la tabla `user_estudiante`
--
ALTER TABLE `user_estudiante`
  ADD CONSTRAINT `user_estudiante_ibfk_1` FOREIGN KEY (`codigo_user`) REFERENCES `user` (`codigo_user`),
  ADD CONSTRAINT `user_estudiante_ibfk_2` FOREIGN KEY (`nid_estudiante`) REFERENCES `estudiante` (`nid_estudiante`);

--
-- Filtros para la tabla `user_profesor`
--
ALTER TABLE `user_profesor`
  ADD CONSTRAINT `user_profesor_ibfk_1` FOREIGN KEY (`codigo_user`) REFERENCES `user` (`codigo_user`),
  ADD CONSTRAINT `user_profesor_ibfk_2` FOREIGN KEY (`nid_profesor`) REFERENCES `profesor` (`nid_profesor`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
