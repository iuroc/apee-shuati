<?php

/**
 * 配置文件
 */

$config = [
    'title' => 'APEE 刷题工具', // 网站标题
    'description' => '支持组卷考试的刷题工具', // 网站描述
    'logo_url' => 'img/logo-blue.png', // 网站logo URL
    'mysql' => [
        'host' => 'localhost', // 数据库地址
        'user' => 'root', // 数据库用户名
        'pass' => '123456', // 数据库密码
        'db' => 'ponconsoft', // 数据库名称
    ],
    'table' => [
        'user' => 'poncon_user', // 用户表
        'topic' => 'xin_xi_ji_shu_zhi_shi_jing_sai_ti_ku', // 题库表
    ],
];
