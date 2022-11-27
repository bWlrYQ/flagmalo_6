<?php
require_once('function_database.php');
$db = connectDB();

$db->query('CREATE TABLE IF NOT EXISTS challenges (
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	category TEXT NOT NULL,
	flag TEXT NOT NULL
);');

$db->query('INSERT INTO challenges(id,name,category,flag) VALUES (1,"SIP - CallMeMaybe","Network","FMCTF{2c95ae4adce93173faba3153e71c78c9}");');
$db->query('INSERT INTO challenges(id,name,category,flag) VALUES (2,"Python - SSTI","Web","FMCTF{ad2f030ceda6bbf9f3bea3a22627cbed}");');
$db->query('INSERT INTO challenges(id,name,category,flag) VALUES (3,"PwnMeIfYouCan","Pwn","FMCTF{e9b911050b8ed8ddfc4f7145c4b2bf7d}");');
$db->query('INSERT INTO challenges(id,name,category,flag) VALUES (4,"AperisolveIsntDaWay","Steganography","FMCTF{fe02013ca8518fde72af77682dd6296e}");');
$db->query('INSERT INTO challenges(id,name,category,flag) VALUES (5,"ELF x64 Easy Obfuscation","Cracking","FMCTF{6e0b1fa4ffa088aec64abff214545bf9}");');
$db->query('INSERT INTO challenges(id,name,category,flag) VALUES (6,"ChessSolver","Programming","FMCTF{f470a7a2b5f16d124d49cdb3d92c9bed}");');
$db->query('INSERT INTO challenges(id,name,category,flag) VALUES (7,"DoYouWannaCry?","Forensic","FMCTF{6f125731b9e0a72951653e4e9fa1fee6}");');
$db->query('INSERT INTO challenges(id,name,category,flag) VALUES (8,"TCP or Tears Control Policy","Network","FMCTF{cf5fdfa020f6c56edb9c72fab2207bfd}");');
$db->query('INSERT INTO challenges(id,name,category,flag) VALUES (9,"VerbTampering","Web","FMCTF{13340ccb84c05823bbbb4c5b94eabd50}");');
$db->query('INSERT INTO challenges(id,name,category,flag) VALUES (10,"TrickOrDDoS","Network","FMCTF{b8097d0e7410cfc64e9f9ff5b055e5aa}");');
$db->query('INSERT INTO challenges(id,name,category,flag) VALUES (11,"SEGFAULT","Pwn","FMCTF{ea09c99a93adc57b3ff8281f727fcbfd}");');
$db->query('INSERT INTO challenges(id,name,category,flag) VALUES (12,"DOM Based XSS","Web","FMCTF{4822e93cc742cf0cc7abf9efc5d0d3d6}");');
$db->query('INSERT INTO challenges(id,name,category,flag) VALUES (13,"RDP Replay","Network","FMCTF{895cb3e65a28d5c475503ad0a8b1092d}");');

$db->query('CREATE TABLE IF NOT EXISTS credentials (
	id INTEGER PRIMARY KEY,
	username TEXT NOT NULL,
	password TEXT NOT NULL,
	domain TEXT
);');

$db->query('INSERT INTO credentials (id,username, password, domain) VALUES (1,"Max3nce_Y0d4","8803bca23b52054117e8637fae45d4a40f26a9a72c049fe54bbe33b09c2bf53cb01353f9ae10b343c1c38787011a0e19a8933b86d617e91020305490f14ebaad","https://secure-notes-flagmalo-private.chall.flagmalo.fr")');
$db->query('INSERT INTO credentials (id,username, password, domain) VALUES (2,"Women x Coffee","5fb934474cd66a906c99c439d3773ac7a5f4fbea5ca5761bb5fd2f43effe0479aa95a0d6b2e254b0afc694dfc766d6346b30377f048f3e66b5ed7ca8b2004aed","discord.com")');
$db->query('INSERT INTO credentials (id,username, password, domain) VALUES (3,"Yoda","0d5ec267c43a98af7cad78127e4747780ce0c9b6314c5adffbe50f4be4d7eeaf4e7af93af1353b560120fc0731a2e76b62593e436481d44ea42e5c1a6d933b3a","twitter.fr")');
$db->query('INSERT INTO credentials (id,username, password, domain) VALUES (4,"Flag #5: FMCTF{N3v3r_Use_An_SQL_DB_aS_@_P4sswOrd_Man4ger...}","5994036dc2313d5de4b43a964165bc75a77c9eb157ddd0f8a88a6bc1e024494ff23e874befae8b6d518e27ee26bffbe3100036da785e3a674a745114bd331edb","easyflagz.net")');
$db->query('INSERT INTO credentials (id,username, password, domain) VALUES (5,"N3tw0rkingIsBae","506ed0743d34606265b0ed755bda885fbf47c5774a05d6c5740e390b3c7907de3e046d121e9d8fe4971b255641a6ff4f05badf56542c0151c461bbfb6f4967ac","cisco.com")');
$db->query('INSERT INTO credentials (id,username, password, domain) VALUES (6,"Maxence","9fff9718e96dcb3c6a491819f2f3b4908db8688dc2cd514ba06eafdb94c43cf27d2d8c6f33c3f91dc1a41991bbc25d2ab0146fe5d72458e47ab5b714f703c069","orange.fr")');

?>