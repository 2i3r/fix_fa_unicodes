#!/usr/bin/env python

trans_table = {
	u'\u0643': u'\u06a9',
	u'\u0649': u'\u06cc',
	u'\u064a': u'\u06cc',
	u'\u0626': u'\u06cc',
}

def fa_unicode_correct(s):
    for k in trans_table.keys():
        s = s.replace(k, trans_table[k]);
