# -*- coding: UTF-8 -*-

import MySQLdb
import sys

class TransferMoney(object):

    def __init__(self, conn):
        self.conn = conn

    def check_acct_available(self, acct_id):
        cursor = self.conn.cursor()
        try:
            sql = 'select * from accounts where account_id = %s' % acct_id
            cursor.execute(sql)
            print 'check_acct_available: ' + sql
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('Account %s has error' % acct_id)
        finally:
            cursor.close()

    def has_enough_money(self, acct_id, money):
        cursor = self.conn.cursor()
        try:
            sql = 'select * from accounts where account_id = %s and money >= %s' % (acct_id, money)
            cursor.execute(sql)
            print 'has_enough_money: ' + sql
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('money is not enough' % acct_id)
        finally:
            cursor.close()

    def reduce_money(self, acct_id, money):
        cursor = self.conn.cursor()
        try:
            sql = 'update accounts set money = money - %s where account_id = %s' % (money, acct_id)
            cursor.execute(sql)
            print 'reduce_money: ' + sql
            if cursor.rowcount != 1:
                raise Exception('account %s reduce failed' % acct_id)
        finally:
            cursor.close()

    def add_money(self, acct_id, money):
        cursor = self.conn.cursor()
        try:
            sql = 'update accounts set money = money + %s where account_id = %s' % (money, acct_id)
            cursor.execute(sql)
            print 'add_money: ' + sql
            if cursor.rowcount != 1:
                raise Exception('account %s add failed' % acct_id)
        finally:
            cursor.close()

    def transfer(self, source_acctid, target_acctid, money):
        try:
            self.check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            self.has_enough_money(source_acctid, money)
            self.reduce_money(source_acctid, money)
            self.add_money(target_acctid, money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e


if __name__ == '__main__':
    source_acctid = sys.argv[1]
    target_acctid = sys.argv[2]
    money = sys.argv[3]

    conn = MySQLdb.Connect(
        host='10.0.0.112',
        port=3306,
        user='root',
        passwd='123456',
        db='spider',
        charset='utf8'
    )

    tr_money = TransferMoney(conn)

    try:
        tr_money.transfer(source_acctid, target_acctid, money)
    except Exception as e:
        print e
    finally:
        conn.close()












