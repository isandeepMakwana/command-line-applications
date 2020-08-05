# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 19:02:07 2020

@author: Admin
"""
import imapclient, pyzmail
imapObj=imapclient.IMAPClient('imap.gmail.com',ssl=True)
imapObj.login('isandeepmakwana1@gmail.com', 'Vandnasharma94')
imapObj.select_folder('INBOX',readonly=True)
a=imapObj.search(['ALL'])
#b=imapObj.search(['ON 05-06-2020'])
c=imapObj.search(['UNSEEN'])
#d= imapObj.search(['BEFORE 01-jan-2015'])
#e=imapObj.search(['FROM vivekmakwanasjr@gmail.com'])

UIDs=imapObj.gmail_search('ibosamworldit1@gmail.com')
rawmsg=imapObj.fetch(UIDs,['BODY[]'])
message = pyzmail.PyzMessage.factory(rawmsg[4347]['BODY[]'])
print('Done',len(a)," " ,len(c))
print(a[0],a[-1],c[0],c[-1])