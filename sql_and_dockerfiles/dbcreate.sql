-- Adminer 4.8.0 PostgreSQL 13.2 dump

<br />
<b>Warning</b>:  PDO::query(): SQLSTATE[42601]: Syntax error: 7 ERROR:  syntax error at or near &quot;STATUS&quot;
LINE 1: SHOW FUNCTION STATUS WHERE Db = 'postgres'
                      ^ in <b>/var/www/html/adminer.php</b> on line <b>185</b><br />
<br />
<b>Warning</b>:  PDO::query(): SQLSTATE[42601]: Syntax error: 7 ERROR:  syntax error at or near &quot;STATUS&quot;
LINE 1: SHOW PROCEDURE STATUS WHERE Db = 'postgres'
                       ^ in <b>/var/www/html/adminer.php</b> on line <b>185</b><br />
<br />
<b>Warning</b>:  PDO::query(): SQLSTATE[42703]: Undefined column: 7 ERROR:  column &quot;consrc&quot; does not exist
LINE 1: SELECT conname, consrc
                        ^
HINT:  Perhaps you meant to reference the column &quot;pg_constraint.conkey&quot; or the column &quot;pg_constraint.conbin&quot;. in <b>/var/www/html/adminer.php</b> on line <b>185</b><br />
DROP TABLE IF EXISTS "admin";
DROP SEQUENCE IF EXISTS admin_id_seq;
CREATE SEQUENCE admin_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."admin" (
    "id" integer DEFAULT nextval('admin_id_seq') NOT NULL,
    "name" character varying(255) NOT NULL,
    "admin_bip32_extended_public_key" text NOT NULL,
    "admin_bip32_key_index" bigint NOT NULL,
    "admin_bitcoin_address" text NOT NULL,
    "permissions" smallint NOT NULL,
    "isModerator" smallint,
    CONSTRAINT "admin_name_key" UNIQUE ("name"),
    CONSTRAINT "admin_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


<br />
<b>Warning</b>:  PDO::query(): SQLSTATE[42703]: Undefined column: 7 ERROR:  column &quot;consrc&quot; does not exist
LINE 1: SELECT conname, consrc
                        ^
HINT:  Perhaps you meant to reference the column &quot;pg_constraint.conkey&quot; or the column &quot;pg_constraint.conbin&quot;. in <b>/var/www/html/adminer.php</b> on line <b>185</b><br />
DROP TABLE IF EXISTS "products";
DROP SEQUENCE IF EXISTS products_id_seq;
CREATE SEQUENCE products_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."products" (
    "id" integer DEFAULT nextval('products_id_seq') NOT NULL,
    "name" character varying(255) NOT NULL,
    "description" text,
    "price" numeric NOT NULL,
    "user_id" character varying(255) NOT NULL,
    "tags" text,
    "is_hidden" smallint,
    "code" character varying,
    "images" bytea,
    "category" bigint,
    CONSTRAINT "products_name_key" UNIQUE ("name"),
    CONSTRAINT "products_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "products_user_id_key" UNIQUE ("user_id")
) WITH (oids = false);


<br />
<b>Warning</b>:  PDO::query(): SQLSTATE[42703]: Undefined column: 7 ERROR:  column &quot;consrc&quot; does not exist
LINE 1: SELECT conname, consrc
                        ^
HINT:  Perhaps you meant to reference the column &quot;pg_constraint.conkey&quot; or the column &quot;pg_constraint.conbin&quot;. in <b>/var/www/html/adminer.php</b> on line <b>185</b><br />
DROP TABLE IF EXISTS "user";
DROP SEQUENCE IF EXISTS user_id_seq;
CREATE SEQUENCE user_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 START 6 CACHE 1;

CREATE TABLE "public"."user" (
    "id" integer DEFAULT nextval('user_id_seq') NOT NULL,
    "name" character varying(255) NOT NULL,
    "PIN" character varying NOT NULL,
    "password" character varying NOT NULL,
    "pgp_public_key" text,
    "bip32_key" text,
    "bip32_key_integer" bigint,
    "is_vendor" smallint,
    "created" timestamp DEFAULT now() NOT NULL,
    "modified" timestamp DEFAULT now() NOT NULL,
    CONSTRAINT "user_name_key" UNIQUE ("name"),
    CONSTRAINT "user_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

INSERT INTO "user" ("id", "name", "PIN", "password", "pgp_public_key", "bip32_key", "bip32_key_integer", "is_vendor", "created", "modified") VALUES
(3,	'rocky',	'\x246172676f6e32696424763d3139246d3d36353533362c743d322c703d31246d53586d6679786f5266394e5973697a394b35714151245468613159466568465043614e794c6177487076694f486668414b372f32614337595a765733315877546b',	'\x246172676f6e32696424763d3139246d3d36353533362c743d322c703d31246e35667a44585950742f4f506558524375335341464124484755424c79695a6d58324a6830586c515a64494a49436f716b4e3172774948675a6b563471734f456f45',	NULL,	NULL,	NULL,	NULL,	'2021-02-27 13:38:40.212079',	'2021-02-27 13:38:40.212079'),
(4,	'rocky2',	'\x246172676f6e32696424763d3139246d3d36353533362c743d322c703d312471797466452f714b4665707770676f6a7130464c5067246f754a2f6375594d593977545a7a4a5267372b4569536364503743586268496757652b5838676133654577',	'\x246172676f6e32696424763d3139246d3d36353533362c743d322c703d3124663453536a6967474b2b734b62703755503148547177243769452b63425a666d70664f755159316c347652526b6437374a43574a66556d56616b333438494b7a4967',	NULL,	NULL,	NULL,	NULL,	'2021-02-27 13:44:35.820821',	'2021-02-27 13:44:35.820821'),
(5,	'overlord',	'\x246172676f6e32696424763d3139246d3d36353533362c743d322c703d31242b30454d434a71316148336e453241644e6c7254584124623556436176556e4b58736c314e2f6b436a424730454874517a344b57444673452b666e6b72664c775873',	'\x246172676f6e32696424763d3139246d3d36353533362c743d322c703d31245454346c432f316a4d3359457359636c59732b4b5577242f727431334d5765634e6747502b77597074613449513979677948514742386841716967706f3949347873',	NULL,	NULL,	NULL,	NULL,	'2021-02-27 13:46:18.573959',	'2021-02-27 13:46:18.573959'),
(6,	'rocky3',	'\x246172676f6e32696424763d3139246d3d36353533362c743d322c703d3124724c6e766445305565643552467334517150736f77672462467744496a352f44513579496a5a4f662f6c567a6276336a4f5955494b366f745a475263377041325555',	'\x246172676f6e32696424763d3139246d3d36353533362c743d322c703d312445694d47534d4f7669592f7941666a4472665a56386724394c6c77456735722b7a4d6f6849725a43354c2b79397831373938476e41755469693559335943514f4849',	NULL,	NULL,	NULL,	NULL,	'2021-02-27 14:41:33.227515',	'2021-02-27 14:41:33.227515');

-- 2021-02-27 22:50:57.117064+00
