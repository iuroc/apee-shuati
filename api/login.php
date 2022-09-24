<?php

/**
 * 用户登录
 */
require 'Poncon.php';

use Poncon\Poncon;

$poncon = new Poncon;

$username = $poncon->GET('username', '', true);
$password = $poncon->GET('password', '', true);
$conn = $poncon->initDb();
$poncon->login($conn, $username, $password);
$poncon->success('登录成功');
