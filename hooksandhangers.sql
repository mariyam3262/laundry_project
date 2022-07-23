-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 14, 2022 at 08:43 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hooksandhangers`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
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
(25, 'Can add customer', 7, 'add_customer'),
(26, 'Can change customer', 7, 'change_customer'),
(27, 'Can delete customer', 7, 'delete_customer'),
(28, 'Can view customer', 7, 'view_customer'),
(29, 'Can add membership', 8, 'add_membership'),
(30, 'Can change membership', 8, 'change_membership'),
(31, 'Can delete membership', 8, 'delete_membership'),
(32, 'Can view membership', 8, 'view_membership'),
(33, 'Can add customer membership', 9, 'add_customermembership'),
(34, 'Can change customer membership', 9, 'change_customermembership'),
(35, 'Can delete customer membership', 9, 'delete_customermembership'),
(36, 'Can view customer membership', 9, 'view_customermembership'),
(37, 'Can add item price', 10, 'add_itemprice'),
(38, 'Can change item price', 10, 'change_itemprice'),
(39, 'Can delete item price', 10, 'delete_itemprice'),
(40, 'Can view item price', 10, 'view_itemprice'),
(41, 'Can add invoice', 11, 'add_invoice'),
(42, 'Can change invoice', 11, 'change_invoice'),
(43, 'Can delete invoice', 11, 'delete_invoice'),
(44, 'Can view invoice', 11, 'view_invoice'),
(45, 'Can add order', 12, 'add_order'),
(46, 'Can change order', 12, 'change_order'),
(47, 'Can delete order', 12, 'delete_order'),
(48, 'Can view order', 12, 'view_order'),
(49, 'Can add cart', 13, 'add_cart'),
(50, 'Can change cart', 13, 'change_cart'),
(51, 'Can delete cart', 13, 'delete_cart'),
(52, 'Can view cart', 13, 'view_cart'),
(53, 'Can add barcode', 14, 'add_barcode'),
(54, 'Can change barcode', 14, 'change_barcode'),
(55, 'Can delete barcode', 14, 'delete_barcode'),
(56, 'Can view barcode', 14, 'view_barcode'),
(57, 'Can add user', 15, 'add_user'),
(58, 'Can change user', 15, 'change_user'),
(59, 'Can delete user', 15, 'delete_user'),
(60, 'Can view user', 15, 'view_user'),
(61, 'Can add notification', 16, 'add_notification'),
(62, 'Can change notification', 16, 'change_notification'),
(63, 'Can delete notification', 16, 'delete_notification'),
(64, 'Can view notification', 16, 'view_notification'),
(65, 'Can add text', 17, 'add_text'),
(66, 'Can change text', 17, 'change_text'),
(67, 'Can delete text', 17, 'delete_text'),
(68, 'Can view text', 17, 'view_text'),
(69, 'Can add expense', 18, 'add_expense'),
(70, 'Can change expense', 18, 'change_expense'),
(71, 'Can delete expense', 18, 'delete_expense'),
(72, 'Can view expense', 18, 'view_expense');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(9, 'pbkdf2_sha256$320000$NlR7OVVIrqsXGZ99AOkzNF$rcYgOnNbfloNpsazTz4QGK+ItKIohhz9L8LMk2/MuvI=', '2022-06-11 06:11:37.289658', 0, 'Musimdcxsd', 'sdcAdmin Cretx', '', 'admin@cretxinc.com', 0, 1, '2022-05-18 12:25:07.934021');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `customer_customer`
--

CREATE TABLE `customer_customer` (
  `id` bigint(20) NOT NULL,
  `customer_name` varchar(40) NOT NULL,
  `mobile` varchar(15) NOT NULL,
  `address` longtext NOT NULL,
  `location` varchar(150) NOT NULL,
  `email` varchar(100) NOT NULL,
  `pincode` int(11) NOT NULL,
  `dob` date NOT NULL,
  `otp` int(11) NOT NULL,
  `customer_service` varchar(30) NOT NULL,
  `customer_status` tinyint(1) NOT NULL,
  `customer_type` varchar(20) NOT NULL,
  `register_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_customer`
--

INSERT INTO `customer_customer` (`id`, `customer_name`, `mobile`, `address`, `location`, `email`, `pincode`, `dob`, `otp`, `customer_service`, `customer_status`, `customer_type`, `register_date`) VALUES
(2, 'Admin Cretx', '9904073595', '1102, Siddhi Vinayak Towers, Makarba', 'bopal', 'musimshad98@gmail.com', 380051, '2022-05-06', 0, '0', 0, '0', '2022-05-13'),
(5, 'Musimshad Test', '9904073595', '1102, Siddhi Vinayak Towers, Makarba', 'Ahmedabad', 'musimshad98@gmail.com ', 380051, '2022-05-18', 0, '0', 0, '0', '2022-05-18');

-- --------------------------------------------------------

--
-- Table structure for table `cust_barcode_barcode`
--

CREATE TABLE `cust_barcode_barcode` (
  `id` bigint(20) NOT NULL,
  `bvalue` varchar(100) NOT NULL,
  `service` varchar(20) NOT NULL,
  `product` varchar(20) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `remarks` varchar(200) NOT NULL,
  `cust_id_id` bigint(20) NOT NULL,
  `inv_id_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cust_barcode_barcode`
--

INSERT INTO `cust_barcode_barcode` (`id`, `bvalue`, `service`, `product`, `status`, `remarks`, `cust_id_id`, `inv_id_id`) VALUES
(1, '1-1', 'STEAM IRON', 'T-SHIRT', 0, 'nkjb', 2, 1),
(2, '1-2', 'IO', 'Shirt', 0, 'nkjb', 2, 1),
(3, '2-1', 'IO', 'Shirt', 0, 'nkjb', 2, 2),
(4, '3-1', 'IO', 'Shirt', 0, 'nkjb', 2, 3),
(5, '4-1', 'STEAM IRON', 'T-SHIRT', 0, 'nkjb', 2, 4),
(6, '5-1', 'STEAM IRON', 'T-SHIRT', 0, 'nkjb', 2, 5);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'customer', 'customer'),
(14, 'cust_barcode', 'barcode'),
(18, 'expense', 'expense'),
(11, 'invoice', 'invoice'),
(10, 'invoice', 'itemprice'),
(9, 'membership', 'customermembership'),
(8, 'membership', 'membership'),
(16, 'notifications', 'notification'),
(17, 'notifications', 'text'),
(13, 'order', 'cart'),
(12, 'order', 'order'),
(6, 'sessions', 'session'),
(15, 'user', 'user');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-05-06 06:04:41.410738'),
(2, 'auth', '0001_initial', '2022-05-06 06:04:52.953848'),
(3, 'admin', '0001_initial', '2022-05-06 06:04:56.758979'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-05-06 06:04:56.813830'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-05-06 06:04:56.857133'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-05-06 06:04:57.638103'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-05-06 06:04:58.738188'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-05-06 06:04:59.049266'),
(9, 'auth', '0004_alter_user_username_opts', '2022-05-06 06:04:59.103147'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-05-06 06:04:59.906080'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-05-06 06:04:59.947747'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-05-06 06:05:00.060838'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-05-06 06:05:00.226556'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-05-06 06:05:00.379511'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-05-06 06:05:00.632380'),
(16, 'auth', '0011_update_proxy_permissions', '2022-05-06 06:05:00.728898'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-05-06 06:05:00.929303'),
(18, 'customer', '0001_initial', '2022-05-06 06:05:01.435886'),
(19, 'invoice', '0001_initial', '2022-05-06 06:05:03.847951'),
(20, 'invoice', '0002_rename_product_type_itemprice_cust_type_and_more', '2022-05-06 06:05:04.003599'),
(21, 'invoice', '0003_alter_invoice_due_date', '2022-05-06 06:05:04.045473'),
(22, 'invoice', '0004_alter_invoice_due_date_alter_invoice_payment_type', '2022-05-06 06:05:04.147855'),
(23, 'invoice', '0005_alter_invoice_due_date', '2022-05-06 06:05:04.380995'),
(24, 'invoice', '0006_alter_invoice_due_date', '2022-05-06 06:05:04.431841'),
(25, 'invoice', '0007_alter_invoice_due_date', '2022-05-06 06:05:04.483384'),
(26, 'invoice', '0008_alter_invoice_due_date', '2022-05-06 06:05:04.547872'),
(27, 'invoice', '0009_alter_invoice_due_date', '2022-05-06 06:05:04.647337'),
(28, 'invoice', '0010_alter_invoice_due_date', '2022-05-06 06:05:04.694590'),
(29, 'invoice', '0011_alter_invoice_date_alter_invoice_due_date', '2022-05-06 06:05:04.768583'),
(30, 'cust_barcode', '0001_initial', '2022-05-06 06:05:10.134744'),
(31, 'cust_barcode', '0002_alter_barcode_product_alter_barcode_service', '2022-05-06 06:05:21.084857'),
(32, 'cust_barcode', '0003_rename_b_val_barcode_bvalue', '2022-05-06 06:05:21.284008'),
(33, 'cust_barcode', '0004_remove_barcode_bvalue', '2022-05-06 06:05:21.869610'),
(34, 'cust_barcode', '0005_barcode_bvalue', '2022-05-06 06:05:22.314647'),
(35, 'cust_barcode', '0006_delete_barcode', '2022-05-06 06:05:22.616230'),
(36, 'cust_barcode', '0007_initial', '2022-05-06 06:05:25.453483'),
(37, 'membership', '0001_initial', '2022-05-06 06:05:25.881173'),
(38, 'membership', '0002_customermembership', '2022-05-06 06:05:29.989128'),
(39, 'order', '0001_initial', '2022-05-06 06:05:34.337791'),
(40, 'order', '0002_cart', '2022-05-06 06:05:36.858803'),
(41, 'sessions', '0001_initial', '2022-05-06 06:05:37.698279'),
(42, 'user', '0001_initial', '2022-05-11 13:07:51.037283'),
(43, 'notifications', '0001_initial', '2022-05-11 13:07:51.049055'),
(44, 'customer', '0002_alter_customer_register_date', '2022-05-16 04:56:39.127701'),
(45, 'customer', '0003_alter_customer_dob', '2022-05-16 04:56:39.138264'),
(46, 'customer', '0004_alter_customer_dob', '2022-05-16 04:56:39.149327'),
(47, 'customer', '0005_alter_customer_dob', '2022-05-16 04:56:39.159036'),
(48, 'invoice', '0003_alter_invoice_date_alter_invoice_due_date', '2022-05-16 04:56:39.180935'),
(49, 'membership', '0002_alter_customermembership_date_and_more', '2022-05-16 04:56:39.210983'),
(50, 'notifications', '0002_text', '2022-05-16 13:45:45.930626'),
(51, 'expense', '0001_initial', '2022-05-18 06:44:34.728495'),
(52, 'invoice', '0004_alter_invoice_status', '2022-05-18 06:44:34.734609'),
(53, 'order', '0003_alter_cart_remarks', '2022-05-18 06:44:34.770097'),
(54, 'expense', '0002_alter_expense_date', '2022-05-18 06:45:52.769234'),
(55, 'expense', '0003_expense_amount', '2022-05-18 06:53:27.873836');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('15n9aipu6zuc8bjjv58xg7sjzxw7peet', 'e30:1nrJJv:jKa-0dbyvJBMfPOaMAGXbxksV_cgE1DRvniDzYB0zg8', '2022-06-01 13:02:31.559684'),
('1jsdj3byz4u1mv8yr6114g4x59qdlxjv', 'e30:1nrIkR:fC7RfQSJdnpq6xkU1Vc8uw8PTf45XLDGyWGaa0ZLqnk', '2022-06-01 12:25:51.814564'),
('34djr2ukjwpaphu43vrbraa5zu2tiscw', 'e30:1nrJJ1:featWOoaSVgzsk77eHseErq7QSx702paxCwQ9QhvKts', '2022-06-01 13:01:35.114682'),
('3ob1macxwpwp1ww2jawmcihkhz6dafsc', '.eJxVjEEOwiAQRe_C2hCgMGVcuvcMZGBAqoYmpV0Z765NutDtf-_9lwi0rTVsPS9hYnEWKE6_W6T0yG0HfKd2m2Wa27pMUe6KPGiX15nz83K4fweVev3WdkAEIiQ2ZBCVL6iNdoXHIUHUNhfwBFGxImVdNB5yMnZM3pLTHpx4fwDYNzdP:1nrJLS:IBV5dR2PrJ54V5q2yCGn6inpZWZEy7mDxuzVw9O_6h8', '2022-06-01 13:04:06.515653'),
('9livjudiy3udu8px0vf5zbztajjhgmtl', '.eJxVjEEOwiAQRe_C2hCgMGVcuvcMZGBAqoYmpV0Z765NutDtf-_9lwi0rTVsPS9hYnEWKE6_W6T0yG0HfKd2m2Wa27pMUe6KPGiX15nz83K4fweVev3WdkAEIiQ2ZBCVL6iNdoXHIUHUNhfwBFGxImVdNB5yMnZM3pLTHpx4fwDYNzdP:1ntkXH:6K0F42Iq6RFsPhuNPN8vWRxeYfXsxh_-mK0JkLerYEg', '2022-06-08 06:30:23.414002'),
('p8lcxqpk3rj475a22mwgn1l5nsh4qnag', '.eJxVjEEOwiAQRe_C2hCgMGVcuvcMZGBAqoYmpV0Z765NutDtf-_9lwi0rTVsPS9hYnEWKE6_W6T0yG0HfKd2m2Wa27pMUe6KPGiX15nz83K4fweVev3WdkAEIiQ2ZBCVL6iNdoXHIUHUNhfwBFGxImVdNB5yMnZM3pLTHpx4fwDYNzdP:1nzuLR:4FY9xe_zc5YSx8FbswFHej-RPrE-DC0Rdp7jO0YS7C8', '2022-06-25 06:11:37.292558'),
('xtwkg26f4dd9qp151j663tx6o20fplu7', '.eJxVjEEOwiAQRe_C2hCgMGVcuvcMZGBAqoYmpV0Z765NutDtf-_9lwi0rTVsPS9hYnEWKE6_W6T0yG0HfKd2m2Wa27pMUe6KPGiX15nz83K4fweVev3WdkAEIiQ2ZBCVL6iNdoXHIUHUNhfwBFGxImVdNB5yMnZM3pLTHpx4fwDYNzdP:1nuT7V:YFBzl2c5zm2Z91R7mIXKefaTxX1yoMPIhEHcc6ym-O8', '2022-06-10 06:06:45.827796');

-- --------------------------------------------------------

--
-- Table structure for table `expense_expense`
--

CREATE TABLE `expense_expense` (
  `id` bigint(20) NOT NULL,
  `expense` longtext NOT NULL,
  `date` date NOT NULL,
  `remarks` longtext NOT NULL,
  `amount` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `expense_expense`
--

INSERT INTO `expense_expense` (`id`, `expense`, `date`, `remarks`, `amount`) VALUES
(2, 'Petrol', '2022-05-18', 'njkbj', '5000'),
(3, 'Petrol', '2022-05-18', 'njkbj', '5000');

-- --------------------------------------------------------

--
-- Table structure for table `invoice_invoice`
--

CREATE TABLE `invoice_invoice` (
  `id` bigint(20) NOT NULL,
  `total_piece` int(11) NOT NULL,
  `date` date NOT NULL,
  `due_date` date NOT NULL,
  `price` int(11) NOT NULL,
  `discount_type` varchar(10) NOT NULL,
  `discount` int(11) NOT NULL,
  `net` int(11) NOT NULL,
  `payment_due` int(11) NOT NULL,
  `paid` int(11) NOT NULL,
  `payment_type` int(11) NOT NULL,
  `payment_status` tinyint(1) NOT NULL,
  `status` varchar(30) NOT NULL,
  `cancel` tinyint(1) NOT NULL,
  `m_price` int(11) NOT NULL,
  `m_point` int(11) NOT NULL,
  `cust_id_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `invoice_invoice`
--

INSERT INTO `invoice_invoice` (`id`, `total_piece`, `date`, `due_date`, `price`, `discount_type`, `discount`, `net`, `payment_due`, `paid`, `payment_type`, `payment_status`, `status`, `cancel`, `m_price`, `m_point`, `cust_id_id`) VALUES
(1, 2, '2022-05-25', '2022-05-30', 150, 'Flat', 0, 150, 150, 0, 0, 0, 'Pending', 0, 0, 0, 2),
(2, 1, '2022-05-25', '2022-05-30', 100, 'Flat', 0, 100, 100, 0, 0, 0, 'Pending', 0, 0, 0, 2),
(3, 28, '2022-05-25', '2022-05-30', 100, 'Flat', 0, 2800, 2700, 2700, 2, 1, 'Delivered', 0, 0, 0, 2),
(4, 1, '2022-05-27', '2022-06-01', 50, 'Flat', 0, 50, 50, 50, 1, 1, 'Delivered', 0, 0, 0, 2),
(5, 1, '2022-06-11', '2022-06-16', 50, 'Flat', 0, 50, 50, 0, 0, 0, 'Pending', 0, 0, 0, 2);

-- --------------------------------------------------------

--
-- Table structure for table `invoice_itemprice`
--

CREATE TABLE `invoice_itemprice` (
  `id` bigint(20) NOT NULL,
  `cust_type` varchar(30) NOT NULL,
  `service` varchar(30) NOT NULL,
  `cloth_type` varchar(30) NOT NULL,
  `price` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `invoice_itemprice`
--

INSERT INTO `invoice_itemprice` (`id`, `cust_type`, `service`, `cloth_type`, `price`) VALUES
(1, 'MEN', 'STEAM IRON', 'T-SHIRT', '50'),
(2, 'Women', 'IO', 'Shirt', '100');

-- --------------------------------------------------------

--
-- Table structure for table `membership_customermembership`
--

CREATE TABLE `membership_customermembership` (
  `id` bigint(20) NOT NULL,
  `date` datetime(6) NOT NULL,
  `ex_date` datetime(6) NOT NULL,
  `avl_price` int(11) NOT NULL,
  `avl_point` int(11) NOT NULL,
  `day_ex` int(11) NOT NULL,
  `custid_id` bigint(20) NOT NULL,
  `msid_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `membership_membership`
--

CREATE TABLE `membership_membership` (
  `id` bigint(20) NOT NULL,
  `service` varchar(20) NOT NULL,
  `mbsp_amount` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `point` int(11) NOT NULL,
  `validity` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `membership_membership`
--

INSERT INTO `membership_membership` (`id`, `service`, `mbsp_amount`, `price`, `point`, `validity`) VALUES
(1, 'STEAM IRON', 1000, 1000, 100, '2-months');

-- --------------------------------------------------------

--
-- Table structure for table `notifications_notification`
--

CREATE TABLE `notifications_notification` (
  `id` bigint(20) NOT NULL,
  `Class` varchar(50) NOT NULL,
  `key` varchar(100) NOT NULL,
  `message` longtext NOT NULL,
  `route` varchar(200) NOT NULL,
  `user_id_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `notifications_text`
--

CREATE TABLE `notifications_text` (
  `id` bigint(20) NOT NULL,
  `text` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `notifications_text`
--

INSERT INTO `notifications_text` (`id`, `text`) VALUES
(1, 'xsxsa{0}{1}{2}{3}');

-- --------------------------------------------------------

--
-- Table structure for table `order_cart`
--

CREATE TABLE `order_cart` (
  `id` bigint(20) NOT NULL,
  `cust_type` varchar(30) NOT NULL,
  `service` varchar(30) NOT NULL,
  `product` varchar(30) NOT NULL,
  `ind_price` int(11) NOT NULL,
  `no_item` int(11) NOT NULL,
  `total_price` int(11) NOT NULL,
  `remarks` longtext NOT NULL,
  `cust_id_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `order_order`
--

CREATE TABLE `order_order` (
  `id` bigint(20) NOT NULL,
  `cust_type` varchar(30) NOT NULL,
  `service` varchar(30) NOT NULL,
  `product` varchar(30) NOT NULL,
  `ind_price` int(11) NOT NULL,
  `no_item` int(11) NOT NULL,
  `total_price` int(11) NOT NULL,
  `remarks` varchar(30) NOT NULL,
  `cust_id_id` bigint(20) NOT NULL,
  `inv_id_id` bigint(20) NOT NULL,
  `ip_id_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `order_order`
--

INSERT INTO `order_order` (`id`, `cust_type`, `service`, `product`, `ind_price`, `no_item`, `total_price`, `remarks`, `cust_id_id`, `inv_id_id`, `ip_id_id`) VALUES
(1, 'MEN', 'STEAM IRON', 'T-SHIRT', 50, 1, 50, 'nkjb', 2, 1, 1),
(2, 'Women', 'IO', 'Shirt', 100, 1, 100, 'nkjb', 2, 1, 2),
(3, 'Women', 'IO', 'Shirt', 100, 1, 100, 'nkjb', 2, 2, 2),
(4, 'Women', 'IO', 'Shirt', 100, 28, 2800, 'nkjb', 2, 3, 2),
(5, 'MEN', 'STEAM IRON', 'T-SHIRT', 50, 1, 50, 'nkjb', 2, 4, 1),
(6, 'MEN', 'STEAM IRON', 'T-SHIRT', 50, 1, 50, 'nkjb', 2, 5, 1);

-- --------------------------------------------------------

--
-- Table structure for table `user_user`
--

CREATE TABLE `user_user` (
  `id` bigint(20) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `password_confirm` varchar(255) NOT NULL,
  `email` varchar(200) NOT NULL,
  `m_number` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `customer_customer`
--
ALTER TABLE `customer_customer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cust_barcode_barcode`
--
ALTER TABLE `cust_barcode_barcode`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cust_barcode_barcode_cust_id_id_947d2015_fk_customer_customer_id` (`cust_id_id`),
  ADD KEY `cust_barcode_barcode_inv_id_id_975ce9bd_fk_invoice_invoice_id` (`inv_id_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `expense_expense`
--
ALTER TABLE `expense_expense`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `invoice_invoice`
--
ALTER TABLE `invoice_invoice`
  ADD PRIMARY KEY (`id`),
  ADD KEY `invoice_invoice_cust_id_id_fbb3d0bf_fk_customer_customer_id` (`cust_id_id`);

--
-- Indexes for table `invoice_itemprice`
--
ALTER TABLE `invoice_itemprice`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `membership_customermembership`
--
ALTER TABLE `membership_customermembership`
  ADD PRIMARY KEY (`id`),
  ADD KEY `membership_customerm_custid_id_88cad932_fk_customer_` (`custid_id`),
  ADD KEY `membership_customerm_msid_id_f35e8fdd_fk_membershi` (`msid_id`);

--
-- Indexes for table `membership_membership`
--
ALTER TABLE `membership_membership`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `notifications_notification`
--
ALTER TABLE `notifications_notification`
  ADD PRIMARY KEY (`id`),
  ADD KEY `notifications_notification_user_id_id_d11da299_fk_user_user_id` (`user_id_id`);

--
-- Indexes for table `notifications_text`
--
ALTER TABLE `notifications_text`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `order_cart`
--
ALTER TABLE `order_cart`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_cart_cust_id_id_83914cb8_fk_customer_customer_id` (`cust_id_id`);

--
-- Indexes for table `order_order`
--
ALTER TABLE `order_order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_order_cust_id_id_d4e4c77a_fk_customer_customer_id` (`cust_id_id`),
  ADD KEY `order_order_inv_id_id_4714249a_fk_invoice_invoice_id` (`inv_id_id`),
  ADD KEY `order_order_ip_id_id_cb4e3b51_fk_invoice_itemprice_id` (`ip_id_id`);

--
-- Indexes for table `user_user`
--
ALTER TABLE `user_user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customer_customer`
--
ALTER TABLE `customer_customer`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `cust_barcode_barcode`
--
ALTER TABLE `cust_barcode_barcode`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT for table `expense_expense`
--
ALTER TABLE `expense_expense`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `invoice_invoice`
--
ALTER TABLE `invoice_invoice`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `invoice_itemprice`
--
ALTER TABLE `invoice_itemprice`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `membership_customermembership`
--
ALTER TABLE `membership_customermembership`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `membership_membership`
--
ALTER TABLE `membership_membership`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `notifications_notification`
--
ALTER TABLE `notifications_notification`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `notifications_text`
--
ALTER TABLE `notifications_text`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `order_cart`
--
ALTER TABLE `order_cart`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `order_order`
--
ALTER TABLE `order_order`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `user_user`
--
ALTER TABLE `user_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `cust_barcode_barcode`
--
ALTER TABLE `cust_barcode_barcode`
  ADD CONSTRAINT `cust_barcode_barcode_cust_id_id_947d2015_fk_customer_customer_id` FOREIGN KEY (`cust_id_id`) REFERENCES `customer_customer` (`id`),
  ADD CONSTRAINT `cust_barcode_barcode_inv_id_id_975ce9bd_fk_invoice_invoice_id` FOREIGN KEY (`inv_id_id`) REFERENCES `invoice_invoice` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `invoice_invoice`
--
ALTER TABLE `invoice_invoice`
  ADD CONSTRAINT `invoice_invoice_cust_id_id_fbb3d0bf_fk_customer_customer_id` FOREIGN KEY (`cust_id_id`) REFERENCES `customer_customer` (`id`);

--
-- Constraints for table `membership_customermembership`
--
ALTER TABLE `membership_customermembership`
  ADD CONSTRAINT `membership_customerm_custid_id_88cad932_fk_customer_` FOREIGN KEY (`custid_id`) REFERENCES `customer_customer` (`id`),
  ADD CONSTRAINT `membership_customerm_msid_id_f35e8fdd_fk_membershi` FOREIGN KEY (`msid_id`) REFERENCES `membership_membership` (`id`);

--
-- Constraints for table `notifications_notification`
--
ALTER TABLE `notifications_notification`
  ADD CONSTRAINT `notifications_notification_user_id_id_d11da299_fk_user_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `user_user` (`id`);

--
-- Constraints for table `order_cart`
--
ALTER TABLE `order_cart`
  ADD CONSTRAINT `order_cart_cust_id_id_83914cb8_fk_customer_customer_id` FOREIGN KEY (`cust_id_id`) REFERENCES `customer_customer` (`id`);

--
-- Constraints for table `order_order`
--
ALTER TABLE `order_order`
  ADD CONSTRAINT `order_order_cust_id_id_d4e4c77a_fk_customer_customer_id` FOREIGN KEY (`cust_id_id`) REFERENCES `customer_customer` (`id`),
  ADD CONSTRAINT `order_order_inv_id_id_4714249a_fk_invoice_invoice_id` FOREIGN KEY (`inv_id_id`) REFERENCES `invoice_invoice` (`id`),
  ADD CONSTRAINT `order_order_ip_id_id_cb4e3b51_fk_invoice_itemprice_id` FOREIGN KEY (`ip_id_id`) REFERENCES `invoice_itemprice` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
