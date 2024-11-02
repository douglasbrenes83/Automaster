-- phpMyAdmin SQL Dump
-- version 5.2.1deb3
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 02-11-2024 a las 19:21:44
-- Versión del servidor: 8.0.39-0ubuntu0.24.04.2
-- Versión de PHP: 8.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `Automasterpro`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add cliente', 7, 'add_cliente'),
(26, 'Can change cliente', 7, 'change_cliente'),
(27, 'Can delete cliente', 7, 'delete_cliente'),
(28, 'Can view cliente', 7, 'view_cliente'),
(29, 'Can add facturas', 8, 'add_facturas'),
(30, 'Can change facturas', 8, 'change_facturas'),
(31, 'Can delete facturas', 8, 'delete_facturas'),
(32, 'Can view facturas', 8, 'view_facturas'),
(33, 'Can add gestion repuesto', 9, 'add_gestionrepuesto'),
(34, 'Can change gestion repuesto', 9, 'change_gestionrepuesto'),
(35, 'Can delete gestion repuesto', 9, 'delete_gestionrepuesto'),
(36, 'Can view gestion repuesto', 9, 'view_gestionrepuesto'),
(37, 'Can add mecanico', 10, 'add_mecanico'),
(38, 'Can change mecanico', 10, 'change_mecanico'),
(39, 'Can delete mecanico', 10, 'delete_mecanico'),
(40, 'Can view mecanico', 10, 'view_mecanico'),
(41, 'Can add detalle factura', 11, 'add_detallefactura'),
(42, 'Can change detalle factura', 11, 'change_detallefactura'),
(43, 'Can delete detalle factura', 11, 'delete_detallefactura'),
(44, 'Can view detalle factura', 11, 'view_detallefactura'),
(45, 'Can add registro vehiculo', 12, 'add_registrovehiculo'),
(46, 'Can change registro vehiculo', 12, 'change_registrovehiculo'),
(47, 'Can delete registro vehiculo', 12, 'delete_registrovehiculo'),
(48, 'Can view registro vehiculo', 12, 'view_registrovehiculo'),
(49, 'Can add asignacion mecanico', 13, 'add_asignacionmecanico'),
(50, 'Can change asignacion mecanico', 13, 'change_asignacionmecanico'),
(51, 'Can delete asignacion mecanico', 13, 'delete_asignacionmecanico'),
(52, 'Can view asignacion mecanico', 13, 'view_asignacionmecanico'),
(53, 'Can add reparaciones', 14, 'add_reparaciones'),
(54, 'Can change reparaciones', 14, 'change_reparaciones'),
(55, 'Can delete reparaciones', 14, 'delete_reparaciones'),
(56, 'Can view reparaciones', 14, 'view_reparaciones'),
(57, 'Can add recepcion vehiculo', 15, 'add_recepcionvehiculo'),
(58, 'Can change recepcion vehiculo', 15, 'change_recepcionvehiculo'),
(59, 'Can delete recepcion vehiculo', 15, 'delete_recepcionvehiculo'),
(60, 'Can view recepcion vehiculo', 15, 'view_recepcionvehiculo'),
(61, 'Can add repuesto factura', 16, 'add_repuestofactura'),
(62, 'Can change repuesto factura', 16, 'change_repuestofactura'),
(63, 'Can delete repuesto factura', 16, 'delete_repuestofactura'),
(64, 'Can view repuesto factura', 16, 'view_repuestofactura'),
(65, 'Can add reservas', 17, 'add_reservas'),
(66, 'Can change reservas', 17, 'change_reservas'),
(67, 'Can delete reservas', 17, 'delete_reservas'),
(68, 'Can view reservas', 17, 'view_reservas'),
(69, 'Can add repuesto reparacion', 18, 'add_repuestoreparacion'),
(70, 'Can change repuesto reparacion', 18, 'change_repuestoreparacion'),
(71, 'Can delete repuesto reparacion', 18, 'delete_repuestoreparacion'),
(72, 'Can view repuesto reparacion', 18, 'view_repuestoreparacion');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$870000$GCqEX6rZ865mdMH1ZEjS4h$xl4mIzPH0SaHDG/8w61TW4apltwRPbGxmQh2b8z7Kcc=', '2024-11-02 19:17:15.221135', 1, 'admin', '', '', 'admin@automasterpro.com', 1, 1, '2024-11-02 03:45:30.688849');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-11-02 03:48:46.495758', '1', 'María Elena Fernández López', 1, '[{\"added\": {}}]', 7, 1),
(2, '2024-11-02 03:54:07.339045', '2', 'José Antonio Martínez García', 1, '[{\"added\": {}}]', 7, 1),
(3, '2024-11-02 03:58:31.168281', '1', 'ZuZuki (My 2345)', 1, '[{\"added\": {}}]', 12, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(13, 'principal', 'asignacionmecanico'),
(7, 'principal', 'cliente'),
(11, 'principal', 'detallefactura'),
(8, 'principal', 'facturas'),
(9, 'principal', 'gestionrepuesto'),
(10, 'principal', 'mecanico'),
(15, 'principal', 'recepcionvehiculo'),
(12, 'principal', 'registrovehiculo'),
(14, 'principal', 'reparaciones'),
(16, 'principal', 'repuestofactura'),
(18, 'principal', 'repuestoreparacion'),
(17, 'principal', 'reservas'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-11-02 02:21:34.034246'),
(2, 'auth', '0001_initial', '2024-11-02 02:21:55.150435'),
(3, 'admin', '0001_initial', '2024-11-02 02:22:03.122409'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-11-02 02:22:03.599408'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-11-02 02:22:04.035317'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-11-02 02:22:07.037865'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-11-02 02:22:09.070369'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-11-02 02:22:09.459050'),
(9, 'auth', '0004_alter_user_username_opts', '2024-11-02 02:22:09.648772'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-11-02 02:22:11.926316'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-11-02 02:22:12.029118'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-11-02 02:22:12.146062'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-11-02 02:22:14.768688'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-11-02 02:22:17.961862'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-11-02 02:22:18.256378'),
(16, 'auth', '0011_update_proxy_permissions', '2024-11-02 02:22:18.459418'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-11-02 02:22:23.191399'),
(18, 'principal', '0001_initial', '2024-11-02 02:23:19.482011'),
(19, 'sessions', '0001_initial', '2024-11-02 02:23:20.863941');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0n0qwmb8jgk7ys0kk82730ykui46c81n', '.eJxVjDsOwjAQBe_iGlle_xJT0ucM1nrXwQHkSHFSIe5OIqWA9s28eYuI21ri1vISJxZXAeLyuyWkZ64H4AfW-yxprusyJXko8qRNDjPn1-10_wIFW9nfvlOcgIzjUQPYPrAN2rLmXnnizrDaW4rQGQMBQFkETZj96JxPpFh8vtKLN6o:1t7JcZ:ZRsGFKfqB_FgGV9dbUJaGfhPSdqtwtDY9naR4ogoGNY', '2024-11-16 19:17:15.344187'),
('lylxxlvbdwjtnnjvp9tane1kbdk9yphx', '.eJxVjDsOwjAQBe_iGlle_xJT0ucM1nrXwQHkSHFSIe5OIqWA9s28eYuI21ri1vISJxZXAeLyuyWkZ64H4AfW-yxprusyJXko8qRNDjPn1-10_wIFW9nfvlOcgIzjUQPYPrAN2rLmXnnizrDaW4rQGQMBQFkETZj96JxPpFh8vtKLN6o:1t755i:f_K3ICnmpU4gJYd1fd9Gy3vF5filrpZCn02hR5PaenA', '2024-11-16 03:46:22.539143'),
('on125igjfp1vwqwct97cmveqm9gp524n', '.eJxVjDsOwjAQBe_iGlle_xJT0ucM1nrXwQHkSHFSIe5OIqWA9s28eYuI21ri1vISJxZXAeLyuyWkZ64H4AfW-yxprusyJXko8qRNDjPn1-10_wIFW9nfvlOcgIzjUQPYPrAN2rLmXnnizrDaW4rQGQMBQFkETZj96JxPpFh8vtKLN6o:1t7IuX:4v3jIZ748fWyz2E4gTL1IaRp0mHz7rUCGwgYCjf7ii8', '2024-11-16 18:31:45.279449');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `principal_asignacionmecanico`
--

CREATE TABLE `principal_asignacionmecanico` (
  `id` bigint NOT NULL,
  `fecha_asignacion` date NOT NULL,
  `mecanico_id` bigint NOT NULL,
  `vehiculo_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `principal_cliente`
--

CREATE TABLE `principal_cliente` (
  `id` bigint NOT NULL,
  `dni` varchar(20) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `telefono` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `principal_cliente`
--

INSERT INTO `principal_cliente` (`id`, `dni`, `nombre`, `apellidos`, `direccion`, `telefono`) VALUES
(1, '041-230687-0004G', 'María Elena', 'Fernández López', 'San marcos , Carazo', '8888-8766'),
(2, '002-120799-0001Q', 'José Antonio', 'Martínez García', 'CIudad Jardin ,Managua', '8888-4567'),
(3, '001-121178-0001W', 'María Elena', 'Fernández López', 'Calle 1, Managua', '555-1234'),
(4, '002-234567-0001W', 'José Antonio', 'Martínez García', 'Calle 2, León', '555-2345'),
(5, '003-345678-0001W', 'Laura Isabel', 'Gómez Torres', 'Calle 3, Granada', '555-3456'),
(6, '004-456789-0001W', 'Carlos Eduardo', 'Pérez Díaz', 'Calle 4, Masaya', '555-4567'),
(7, '005-567890-0001W', 'Ana Lucía', 'Sánchez Romero', 'Calle 5, Estelí', '555-5678'),
(8, '006-678901-0001W', 'Jorge Luis', 'Ramírez Álvarez', 'Calle 6, Chinandega', '555-6789'),
(9, '007-789012-0001W', 'Sofía Patricia', 'Mendoza Castillo', 'Calle 7, Rivas', '555-7890'),
(10, '008-890123-0001W', 'Fernando Javier', 'Castillo Soto', 'Calle 8, Nueva Guinea', '555-8901');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `principal_detallefactura`
--

CREATE TABLE `principal_detallefactura` (
  `id` bigint NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `monto` decimal(10,2) NOT NULL,
  `factura_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `principal_facturas`
--

CREATE TABLE `principal_facturas` (
  `id` bigint NOT NULL,
  `fecha` date NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `iva` decimal(10,2) NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `total_dolares` decimal(10,2) NOT NULL,
  `reparacion_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `principal_gestionrepuesto`
--

CREATE TABLE `principal_gestionrepuesto` (
  `id` bigint NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `precio_unidad` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `principal_mecanico`
--

CREATE TABLE `principal_mecanico` (
  `id` bigint NOT NULL,
  `dni` varchar(20) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `especialidad` varchar(50) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `principal_mecanico`
--

INSERT INTO `principal_mecanico` (`id`, `dni`, `nombre`, `apellidos`, `especialidad`, `telefono`, `email`) VALUES
(1, '001-234567-0001W', 'Carlos Alberto', 'Pérez López', 'Motor', '555-1234', 'carlos.perez@example.com'),
(2, '002-345678-0001W', 'María Fernanda', 'Gómez Sánchez', 'Transmisión', '555-2345', 'maria.gomez@example.com'),
(3, '003-456789-0001W', 'José Luis', 'Martínez Ramírez', 'Frenos', '555-3456', 'jose.martinez@example.com'),
(4, '004-567890-0001W', 'Sofía Elena', 'Hernández Torres', 'Suspensión', '555-4567', 'sofia.hernandez@example.com'),
(5, '005-678901-0001W', 'Fernando Javier', 'Castillo Soto', 'Electrónica', '555-5678', 'fernando.castillo@example.com'),
(6, '006-789012-0001W', 'Ana Patricia', 'Sánchez Romero', 'Climatización', '555-6789', 'ana.sanchez@example.com'),
(7, '007-890123-0001W', 'Luis Miguel', 'Ramírez Álvarez', 'Chasis', '555-7890', 'luis.ramirez@example.com'),
(8, '008-901234-0001W', 'Isabel Cristina', 'Mendoza Castillo', 'Diagnóstico', '555-8901', 'isabel.mendoza@example.com'),
(9, '041-122589-0000L', 'julio Ramon', 'perez Olivares', 'frenos', '77889997', 'julioramon@automasterpro.com'),
(10, '041-122589-0025k', 'Pedro Antonio', 'Fuentes', 'Chasis', '77787865', 'pedrofuentes@automasterpro.com'),
(12, '002-120798-0001Q', 'andres', 'casanova ramires', 'Frenos', '78378778', 'andres@automaster.com'),
(13, '041-122589-0000L', 'Andrea Carolina', 'Gaitan Molina', 'frenos', '77889997', 'admin@automasterpro.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `principal_recepcionvehiculo`
--

CREATE TABLE `principal_recepcionvehiculo` (
  `id` bigint NOT NULL,
  `fecha_recepcion` date NOT NULL,
  `hora_recepcion` time(6) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `observaciones` varchar(255) DEFAULT NULL,
  `vehiculo_id` bigint NOT NULL,
  `reparacion_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `principal_registrovehiculo`
--

CREATE TABLE `principal_registrovehiculo` (
  `id` bigint NOT NULL,
  `matricula` varchar(20) NOT NULL,
  `modelo` varchar(50) NOT NULL,
  `color` varchar(30) NOT NULL,
  `fecha_entrada` date NOT NULL,
  `hora_entrada` time(6) NOT NULL,
  `cliente_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `principal_registrovehiculo`
--

INSERT INTO `principal_registrovehiculo` (`id`, `matricula`, `modelo`, `color`, `fecha_entrada`, `hora_entrada`, `cliente_id`) VALUES
(20, 'ABC123', 'Toyota Corolla', 'Rojo', '2024-11-01', '08:30:00.000000', 9),
(21, 'XYZ456', 'Honda Civic', 'Azul', '2024-11-02', '09:00:00.000000', 2),
(22, 'LMN789', 'Ford Fiesta', 'Negro', '2024-11-03', '10:15:00.000000', 3),
(23, 'DEF012', 'Chevrolet Spark', 'Blanco', '2024-11-01', '11:30:00.000000', 4),
(24, 'GHI345', 'Hyundai Elantra', 'Gris', '2024-11-02', '14:00:00.000000', 5),
(25, 'JKL678', 'Nissan Sentra', 'Verde', '2024-11-03', '16:45:00.000000', 6),
(26, 'MNO901', 'Volkswagen Golf', 'Amarillo', '2024-11-01', '12:00:00.000000', 7),
(28, 'STU567', 'Mazda 3', 'Morado', '2024-11-03', '10:45:00.000000', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `principal_reparaciones`
--

CREATE TABLE `principal_reparaciones` (
  `id` bigint NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date DEFAULT NULL,
  `total_mano_de_obra` decimal(10,2) DEFAULT NULL,
  `estatus` varchar(20) NOT NULL,
  `cliente_id` bigint NOT NULL,
  `vehiculo_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `principal_repuestofactura`
--

CREATE TABLE `principal_repuestofactura` (
  `id` bigint NOT NULL,
  `cantidad` int NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL,
  `factura_id` bigint NOT NULL,
  `repuesto_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `principal_repuestoreparacion`
--

CREATE TABLE `principal_repuestoreparacion` (
  `id` bigint NOT NULL,
  `cantidad` int NOT NULL,
  `reparacion_id` bigint NOT NULL,
  `repuesto_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `principal_reservas`
--

CREATE TABLE `principal_reservas` (
  `id` bigint NOT NULL,
  `fecha_reserva` date NOT NULL,
  `hora_inicio` time(6) NOT NULL,
  `hora_fin` time(6) NOT NULL,
  `especialidad` varchar(50) NOT NULL,
  `estado` varchar(20) NOT NULL,
  `cliente_id` bigint NOT NULL,
  `vehiculo_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `principal_asignacionmecanico`
--
ALTER TABLE `principal_asignacionmecanico`
  ADD PRIMARY KEY (`id`),
  ADD KEY `principal_asignacion_mecanico_id_0d7be128_fk_principal` (`mecanico_id`),
  ADD KEY `principal_asignacion_vehiculo_id_3b185e8b_fk_principal` (`vehiculo_id`);

--
-- Indices de la tabla `principal_cliente`
--
ALTER TABLE `principal_cliente`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `principal_detallefactura`
--
ALTER TABLE `principal_detallefactura`
  ADD PRIMARY KEY (`id`),
  ADD KEY `principal_detallefac_factura_id_c9cdfb88_fk_principal` (`factura_id`);

--
-- Indices de la tabla `principal_facturas`
--
ALTER TABLE `principal_facturas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `principal_facturas_reparacion_id_33813823_fk_principal` (`reparacion_id`);

--
-- Indices de la tabla `principal_gestionrepuesto`
--
ALTER TABLE `principal_gestionrepuesto`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `principal_mecanico`
--
ALTER TABLE `principal_mecanico`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `principal_recepcionvehiculo`
--
ALTER TABLE `principal_recepcionvehiculo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `principal_recepcionv_vehiculo_id_c23d0178_fk_principal` (`vehiculo_id`),
  ADD KEY `principal_recepcionv_reparacion_id_b84f64cb_fk_principal` (`reparacion_id`);

--
-- Indices de la tabla `principal_registrovehiculo`
--
ALTER TABLE `principal_registrovehiculo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `principal_registrove_cliente_id_a1c95a48_fk_principal` (`cliente_id`);

--
-- Indices de la tabla `principal_reparaciones`
--
ALTER TABLE `principal_reparaciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `principal_reparacion_cliente_id_dfe3ff6b_fk_principal` (`cliente_id`),
  ADD KEY `principal_reparacion_vehiculo_id_69692858_fk_principal` (`vehiculo_id`);

--
-- Indices de la tabla `principal_repuestofactura`
--
ALTER TABLE `principal_repuestofactura`
  ADD PRIMARY KEY (`id`),
  ADD KEY `principal_repuestofa_factura_id_350fbf12_fk_principal` (`factura_id`),
  ADD KEY `principal_repuestofa_repuesto_id_9f1efb2d_fk_principal` (`repuesto_id`);

--
-- Indices de la tabla `principal_repuestoreparacion`
--
ALTER TABLE `principal_repuestoreparacion`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `principal_repuestorepara_reparacion_id_repuesto_i_ad2afc6f_uniq` (`reparacion_id`,`repuesto_id`),
  ADD KEY `principal_repuestore_repuesto_id_e8b0bae3_fk_principal` (`repuesto_id`);

--
-- Indices de la tabla `principal_reservas`
--
ALTER TABLE `principal_reservas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `principal_reservas_cliente_id_cee8d99b_fk_principal_cliente_id` (`cliente_id`),
  ADD KEY `principal_reservas_vehiculo_id_92058adc_fk_principal` (`vehiculo_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `principal_asignacionmecanico`
--
ALTER TABLE `principal_asignacionmecanico`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `principal_cliente`
--
ALTER TABLE `principal_cliente`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `principal_detallefactura`
--
ALTER TABLE `principal_detallefactura`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `principal_facturas`
--
ALTER TABLE `principal_facturas`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `principal_gestionrepuesto`
--
ALTER TABLE `principal_gestionrepuesto`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `principal_mecanico`
--
ALTER TABLE `principal_mecanico`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `principal_recepcionvehiculo`
--
ALTER TABLE `principal_recepcionvehiculo`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `principal_registrovehiculo`
--
ALTER TABLE `principal_registrovehiculo`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT de la tabla `principal_reparaciones`
--
ALTER TABLE `principal_reparaciones`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `principal_repuestofactura`
--
ALTER TABLE `principal_repuestofactura`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `principal_repuestoreparacion`
--
ALTER TABLE `principal_repuestoreparacion`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `principal_reservas`
--
ALTER TABLE `principal_reservas`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `principal_asignacionmecanico`
--
ALTER TABLE `principal_asignacionmecanico`
  ADD CONSTRAINT `principal_asignacion_mecanico_id_0d7be128_fk_principal` FOREIGN KEY (`mecanico_id`) REFERENCES `principal_mecanico` (`id`),
  ADD CONSTRAINT `principal_asignacion_vehiculo_id_3b185e8b_fk_principal` FOREIGN KEY (`vehiculo_id`) REFERENCES `principal_registrovehiculo` (`id`);

--
-- Filtros para la tabla `principal_detallefactura`
--
ALTER TABLE `principal_detallefactura`
  ADD CONSTRAINT `principal_detallefac_factura_id_c9cdfb88_fk_principal` FOREIGN KEY (`factura_id`) REFERENCES `principal_facturas` (`id`);

--
-- Filtros para la tabla `principal_facturas`
--
ALTER TABLE `principal_facturas`
  ADD CONSTRAINT `principal_facturas_reparacion_id_33813823_fk_principal` FOREIGN KEY (`reparacion_id`) REFERENCES `principal_reparaciones` (`id`);

--
-- Filtros para la tabla `principal_recepcionvehiculo`
--
ALTER TABLE `principal_recepcionvehiculo`
  ADD CONSTRAINT `principal_recepcionv_reparacion_id_b84f64cb_fk_principal` FOREIGN KEY (`reparacion_id`) REFERENCES `principal_reparaciones` (`id`),
  ADD CONSTRAINT `principal_recepcionv_vehiculo_id_c23d0178_fk_principal` FOREIGN KEY (`vehiculo_id`) REFERENCES `principal_registrovehiculo` (`id`);

--
-- Filtros para la tabla `principal_registrovehiculo`
--
ALTER TABLE `principal_registrovehiculo`
  ADD CONSTRAINT `principal_registrove_cliente_id_a1c95a48_fk_principal` FOREIGN KEY (`cliente_id`) REFERENCES `principal_cliente` (`id`);

--
-- Filtros para la tabla `principal_reparaciones`
--
ALTER TABLE `principal_reparaciones`
  ADD CONSTRAINT `principal_reparacion_cliente_id_dfe3ff6b_fk_principal` FOREIGN KEY (`cliente_id`) REFERENCES `principal_cliente` (`id`),
  ADD CONSTRAINT `principal_reparacion_vehiculo_id_69692858_fk_principal` FOREIGN KEY (`vehiculo_id`) REFERENCES `principal_registrovehiculo` (`id`);

--
-- Filtros para la tabla `principal_repuestofactura`
--
ALTER TABLE `principal_repuestofactura`
  ADD CONSTRAINT `principal_repuestofa_factura_id_350fbf12_fk_principal` FOREIGN KEY (`factura_id`) REFERENCES `principal_facturas` (`id`),
  ADD CONSTRAINT `principal_repuestofa_repuesto_id_9f1efb2d_fk_principal` FOREIGN KEY (`repuesto_id`) REFERENCES `principal_gestionrepuesto` (`id`);

--
-- Filtros para la tabla `principal_repuestoreparacion`
--
ALTER TABLE `principal_repuestoreparacion`
  ADD CONSTRAINT `principal_repuestore_reparacion_id_03ef1d63_fk_principal` FOREIGN KEY (`reparacion_id`) REFERENCES `principal_reparaciones` (`id`),
  ADD CONSTRAINT `principal_repuestore_repuesto_id_e8b0bae3_fk_principal` FOREIGN KEY (`repuesto_id`) REFERENCES `principal_gestionrepuesto` (`id`);

--
-- Filtros para la tabla `principal_reservas`
--
ALTER TABLE `principal_reservas`
  ADD CONSTRAINT `principal_reservas_cliente_id_cee8d99b_fk_principal_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `principal_cliente` (`id`),
  ADD CONSTRAINT `principal_reservas_vehiculo_id_92058adc_fk_principal` FOREIGN KEY (`vehiculo_id`) REFERENCES `principal_registrovehiculo` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
