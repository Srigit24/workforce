-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 08, 2024 at 12:43 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `touchmark_workforce`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
(25, 'Can add wf_ rolemenu', 7, 'add_wf_rolemenu'),
(26, 'Can change wf_ rolemenu', 7, 'change_wf_rolemenu'),
(27, 'Can delete wf_ rolemenu', 7, 'delete_wf_rolemenu'),
(28, 'Can view wf_ rolemenu', 7, 'view_wf_rolemenu'),
(29, 'Can add wf_ candidate', 8, 'add_wf_candidate'),
(30, 'Can change wf_ candidate', 8, 'change_wf_candidate'),
(31, 'Can delete wf_ candidate', 8, 'delete_wf_candidate'),
(32, 'Can view wf_ candidate', 8, 'view_wf_candidate'),
(33, 'Can add wf_users', 9, 'add_wf_users'),
(34, 'Can change wf_users', 9, 'change_wf_users'),
(35, 'Can delete wf_users', 9, 'delete_wf_users'),
(36, 'Can view wf_users', 9, 'view_wf_users'),
(37, 'Can add wf_ job post', 10, 'add_wf_jobpost'),
(38, 'Can change wf_ job post', 10, 'change_wf_jobpost'),
(39, 'Can delete wf_ job post', 10, 'delete_wf_jobpost'),
(40, 'Can view wf_ job post', 10, 'view_wf_jobpost'),
(41, 'Can add wf_ recruiter', 11, 'add_wf_recruiter'),
(42, 'Can change wf_ recruiter', 11, 'change_wf_recruiter'),
(43, 'Can delete wf_ recruiter', 11, 'delete_wf_recruiter'),
(44, 'Can view wf_ recruiter', 11, 'view_wf_recruiter'),
(45, 'Can add wf_ company', 12, 'add_wf_company'),
(46, 'Can change wf_ company', 12, 'change_wf_company'),
(47, 'Can delete wf_ company', 12, 'delete_wf_company'),
(48, 'Can view wf_ company', 12, 'view_wf_company'),
(49, 'Can add wf_create_job', 13, 'add_wf_create_job'),
(50, 'Can change wf_create_job', 13, 'change_wf_create_job'),
(51, 'Can delete wf_create_job', 13, 'delete_wf_create_job'),
(52, 'Can view wf_create_job', 13, 'view_wf_create_job');

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(8, 'TDS_wfapp', 'wf_candidate'),
(12, 'TDS_wfapp', 'wf_company'),
(13, 'TDS_wfapp', 'wf_create_job'),
(10, 'TDS_wfapp', 'wf_jobpost'),
(11, 'TDS_wfapp', 'wf_recruiter'),
(7, 'TDS_wfapp', 'wf_rolemenu'),
(9, 'TDS_wfapp', 'wf_users');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-04-04 05:00:11.260604'),
(2, 'auth', '0001_initial', '2024-04-04 05:00:11.708567'),
(3, 'admin', '0001_initial', '2024-04-04 05:00:11.821688'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-04-04 05:00:11.833072'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-04-04 05:00:11.846281'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-04-04 05:00:11.912256'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-04-04 05:00:11.963386'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-04-04 05:00:11.984383'),
(9, 'auth', '0004_alter_user_username_opts', '2024-04-04 05:00:11.996386'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-04-04 05:00:12.034572'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-04-04 05:00:12.037838'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-04-04 05:00:12.049903'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-04-04 05:00:12.067649'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-04-04 05:00:12.101729'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-04-04 05:00:12.137902'),
(16, 'auth', '0011_update_proxy_permissions', '2024-04-04 05:00:12.149166'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-04-04 05:00:12.169182'),
(18, 'sessions', '0001_initial', '2024-04-04 05:00:12.211567'),
(19, 'TDS_wfapp', '0001_initial', '2024-04-04 07:54:55.567545'),
(20, 'TDS_wfapp', '0002_wf_create_job', '2024-04-08 10:12:24.481042'),
(21, 'TDS_wfapp', '0003_delete_wf_jobpost', '2024-04-08 10:12:24.499154');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('ky0p85vgi63f58jsjw2aay6z5zz8vz1k', 'eyJ1c2VyX2lkIjoxfQ:1rtm2r:PJ6pvdeZSbWB3lB-4ShqWIGWdmTp4D5v9nnHEWw6FoI', '2024-04-22 10:16:09.534905'),
('tkl24z28sbflcy51kcus2r0pvb6e63sr', 'eyJ1c2VyX2lkIjoxfQ:1rsKO0:-310A_MWEv1MQt8vaPqM2_BnPbaBKza5nA6RCSe8Cs4', '2024-04-18 10:32:00.942416');

-- --------------------------------------------------------

--
-- Table structure for table `tds_wfapp_wf_create_job`
--

CREATE TABLE `tds_wfapp_wf_create_job` (
  `job_id` int(11) NOT NULL,
  `job_title` varchar(255) NOT NULL,
  `job_description_id` int(11) NOT NULL,
  `salary_range` varchar(100) NOT NULL,
  `priority` varchar(100) NOT NULL,
  `vacancies` int(11) NOT NULL,
  `skills` longtext NOT NULL,
  `job_deadline` date NOT NULL,
  `languages_known` varchar(255) NOT NULL,
  `qualification` varchar(255) NOT NULL,
  `job_description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `wf_candidate`
--

CREATE TABLE `wf_candidate` (
  `candidate_id` int(11) NOT NULL,
  `candidate_name` varchar(100) NOT NULL,
  `candidate_email` varchar(255) NOT NULL,
  `candidate_phone_number` varchar(15) NOT NULL,
  `candidate_experience` int(11) NOT NULL,
  `candidate_skillset` longtext NOT NULL,
  `candidate_working_hours` int(11) NOT NULL,
  `candidate_resume` varchar(100) NOT NULL,
  `candidate_image` varchar(100) DEFAULT NULL,
  `createby` int(11) NOT NULL,
  `createdon` datetime(6) NOT NULL,
  `updatedon` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  `deleted` int(11) NOT NULL,
  `role_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `wf_candidate`
--

INSERT INTO `wf_candidate` (`candidate_id`, `candidate_name`, `candidate_email`, `candidate_phone_number`, `candidate_experience`, `candidate_skillset`, `candidate_working_hours`, `candidate_resume`, `candidate_image`, `createby`, `createdon`, `updatedon`, `status`, `deleted`, `role_id_id`) VALUES
(1, 'Muthu', 'muthu@touchmarkdes.com', '7707707707', 10, 'fluuter,html,css', 9, '', NULL, 0, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000', 0, 0, 1),
(2, 'Muthu', 'muthu@touchmarkdes.com', '7707707707', 10, 'fluuter,html,css', 9, '', NULL, 0, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000', 0, 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `wf_company`
--

CREATE TABLE `wf_company` (
  `company_id` int(11) NOT NULL,
  `company_name` varchar(255) NOT NULL,
  `company_description` longtext NOT NULL,
  `company_location` longtext NOT NULL,
  `company_contact_person` varchar(255) NOT NULL,
  `company_contact_email` varchar(255) NOT NULL,
  `company_contact_phone_number` varchar(15) NOT NULL,
  `company_resources_needed` int(11) NOT NULL,
  `createby` int(11) NOT NULL,
  `createdon` datetime(6) NOT NULL,
  `updatedon` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  `deleted` int(11) NOT NULL,
  `role_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `wf_company`
--

INSERT INTO `wf_company` (`company_id`, `company_name`, `company_description`, `company_location`, `company_contact_person`, `company_contact_email`, `company_contact_phone_number`, `company_resources_needed`, `createby`, `createdon`, `updatedon`, `status`, `deleted`, `role_id_id`) VALUES
(1, 'tds', 'tds touchmarkdescience private limited is software service and solution providers', 'chennai', 'bharthi', 'info@touchmarkdes.com', '9090909092', 5, 0, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000', 0, 0, 1),
(2, 'tds', 'tds touchmarkdescience private limited is software service and solution providers', 'chennai', 'bharthi', 'info@touchmarkdes.com', '9090909092', 5, 0, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000', 0, 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `wf_recruiter`
--

CREATE TABLE `wf_recruiter` (
  `recruiter_id` int(11) NOT NULL,
  `recruiter_name` varchar(100) NOT NULL,
  `recruiter_email` varchar(255) NOT NULL,
  `recruiter_password` varchar(255) NOT NULL,
  `recruiter_qualification` varchar(100) NOT NULL,
  `recruiter_experience` varchar(100) NOT NULL,
  `recruiter_employee_since` date DEFAULT NULL,
  `createby` int(11) NOT NULL,
  `createdon` datetime(6) NOT NULL,
  `updatedon` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  `deleted` int(11) NOT NULL,
  `role_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `wf_recruiter`
--

INSERT INTO `wf_recruiter` (`recruiter_id`, `recruiter_name`, `recruiter_email`, `recruiter_password`, `recruiter_qualification`, `recruiter_experience`, `recruiter_employee_since`, `createby`, `createdon`, `updatedon`, `status`, `deleted`, `role_id_id`) VALUES
(4, 'janani', 'jnanai@hsg.com', 'janani@123', 'btech', '2', '2023-06-03', 0, '0000-00-00 00:00:00.000000', '0000-00-00 00:00:00.000000', 0, 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `wf_rolemenu`
--

CREATE TABLE `wf_rolemenu` (
  `role_id` int(11) NOT NULL,
  `role_name` varchar(50) NOT NULL,
  `createby` int(11) NOT NULL,
  `createdon` datetime(6) NOT NULL,
  `updatedon` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  `deleted` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `wf_rolemenu`
--

INSERT INTO `wf_rolemenu` (`role_id`, `role_name`, `createby`, `createdon`, `updatedon`, `status`, `deleted`) VALUES
(1, 'admin', 0, '2024-04-04 10:01:17.840613', '2024-04-04 10:01:17.840613', 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `wf_users`
--

CREATE TABLE `wf_users` (
  `userID` int(11) NOT NULL,
  `usertoken` varchar(100) DEFAULT NULL,
  `user_profile` varchar(200) DEFAULT NULL,
  `username` varchar(150) DEFAULT NULL,
  `useremail` varchar(350) DEFAULT NULL,
  `password` varchar(300) DEFAULT NULL,
  `userlogtime` varchar(50) DEFAULT NULL,
  `userlogkey` varchar(50) DEFAULT NULL,
  `last_loggedon` datetime(6) DEFAULT NULL,
  `createdby` int(11) NOT NULL,
  `createdon` datetime(6) DEFAULT NULL,
  `updatedon` datetime(6) NOT NULL,
  `status` int(11) NOT NULL,
  `deleted` int(11) NOT NULL,
  `role_id_id` int(11) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `wf_users`
--

INSERT INTO `wf_users` (`userID`, `usertoken`, `user_profile`, `username`, `useremail`, `password`, `userlogtime`, `userlogkey`, `last_loggedon`, `createdby`, `createdon`, `updatedon`, `status`, `deleted`, `role_id_id`) VALUES
(1, NULL, NULL, 'Admin', NULL, 'pbkdf2_sha256$720000$suEl3zy4nybfylZMLxAKsx$0lPkaTU3xQGnT4XHsZk1EwZgD9A+5MS+WhdDMV/dFFY=', NULL, NULL, NULL, 0, NULL, '2024-04-04 10:02:16.808167', 0, 0, 1);

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
-- Indexes for table `tds_wfapp_wf_create_job`
--
ALTER TABLE `tds_wfapp_wf_create_job`
  ADD PRIMARY KEY (`job_id`);

--
-- Indexes for table `wf_candidate`
--
ALTER TABLE `wf_candidate`
  ADD PRIMARY KEY (`candidate_id`),
  ADD KEY `wf_Candidate_role_id_id_504b1e7d_fk_wf_Rolemenu_role_id` (`role_id_id`);

--
-- Indexes for table `wf_company`
--
ALTER TABLE `wf_company`
  ADD PRIMARY KEY (`company_id`),
  ADD KEY `wf_Company_role_id_id_72899820_fk_wf_Rolemenu_role_id` (`role_id_id`);

--
-- Indexes for table `wf_recruiter`
--
ALTER TABLE `wf_recruiter`
  ADD PRIMARY KEY (`recruiter_id`),
  ADD KEY `wf_Recruiter_role_id_id_aa3ae6b0_fk_wf_Rolemenu_role_id` (`role_id_id`);

--
-- Indexes for table `wf_rolemenu`
--
ALTER TABLE `wf_rolemenu`
  ADD PRIMARY KEY (`role_id`),
  ADD UNIQUE KEY `role_name` (`role_name`);

--
-- Indexes for table `wf_users`
--
ALTER TABLE `wf_users`
  ADD PRIMARY KEY (`userID`),
  ADD KEY `wf_users_role_id_id_42ea8831_fk_wf_Rolemenu_role_id` (`role_id_id`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

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
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `tds_wfapp_wf_create_job`
--
ALTER TABLE `tds_wfapp_wf_create_job`
  MODIFY `job_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `wf_candidate`
--
ALTER TABLE `wf_candidate`
  MODIFY `candidate_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `wf_company`
--
ALTER TABLE `wf_company`
  MODIFY `company_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `wf_recruiter`
--
ALTER TABLE `wf_recruiter`
  MODIFY `recruiter_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `wf_rolemenu`
--
ALTER TABLE `wf_rolemenu`
  MODIFY `role_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `wf_users`
--
ALTER TABLE `wf_users`
  MODIFY `userID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

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
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `wf_candidate`
--
ALTER TABLE `wf_candidate`
  ADD CONSTRAINT `wf_Candidate_role_id_id_504b1e7d_fk_wf_Rolemenu_role_id` FOREIGN KEY (`role_id_id`) REFERENCES `wf_rolemenu` (`role_id`);

--
-- Constraints for table `wf_company`
--
ALTER TABLE `wf_company`
  ADD CONSTRAINT `wf_Company_role_id_id_72899820_fk_wf_Rolemenu_role_id` FOREIGN KEY (`role_id_id`) REFERENCES `wf_rolemenu` (`role_id`);

--
-- Constraints for table `wf_recruiter`
--
ALTER TABLE `wf_recruiter`
  ADD CONSTRAINT `wf_Recruiter_role_id_id_aa3ae6b0_fk_wf_Rolemenu_role_id` FOREIGN KEY (`role_id_id`) REFERENCES `wf_rolemenu` (`role_id`);

--
-- Constraints for table `wf_users`
--
ALTER TABLE `wf_users`
  ADD CONSTRAINT `wf_users_role_id_id_42ea8831_fk_wf_Rolemenu_role_id` FOREIGN KEY (`role_id_id`) REFERENCES `wf_rolemenu` (`role_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
