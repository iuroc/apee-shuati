import json
import os
import pymysql

_mysql = {
    'host': 'localhost',
    'username': 'root',
    'password': '123456',
    'database': 'ponconsoft',
    'table': 'xin_xi_ji_shu_zhi_shi_jing_sai_ti_ku'
}
conn = pymysql.connect(host=_mysql['host'], user=_mysql['username'],
                       password=_mysql['password'], database=_mysql['database'])
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS `%s`;' % _mysql['table'])
cursor.execute('''
CREATE TABLE `%s` (
    `id` INT AUTO_INCREMENT,
    `type` VARCHAR(1) COMMENT "题目类型",
    `topic` TEXT COMMENT "题目",
    `A` TEXT COMMENT "A选项",
    `B` TEXT COMMENT "B选项",
    `C` TEXT COMMENT "C选项",
    `D` TEXT COMMENT "D选项",
    `answer` VARCHAR(1) COMMENT "答案",
    `difficulty` INT COMMENT "难度",
    PRIMARY KEY (`id`)
);
''' % _mysql['table'])


def replaceSQL(row):  # 过滤特殊字符
    row = list(row)
    text = ''''",\\'''
    for i in range(0, len(row)):
        if not type(row[i]) is type(1):
            for j in text:
                row[i] = row[i].replace(j, '')
    return tuple(row)


data = json.load(open('data.json', 'r', encoding='utf-8'))
sql = "INSERT INTO `" + \
    _mysql['table'] + \
    "` (`type`, `topic`, `A`, `B`, `C`, `D`, `answer`, `difficulty`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', %s);"
for i in data:
    cursor.execute(sql % replaceSQL(i.values()))
conn.commit()
cursor.close()
conn.close()
print('存入数据库完成')
print('开始导出SQL文件，请输入数据库密码')
os.system('mysqldump -u root -p %s %s > %s.sql' %
          (_mysql['database'], _mysql['table'], _mysql['table']))
print('完成')
