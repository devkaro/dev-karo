Title: File Log Galangsa Erban Server Menam Tunggaling
Date: 2014-03-13 22:46
Author: Surbakti
Category: News
Tags: server, radio karo
Slug: file-log-galangsa-erban-server-menam-tunggaling

Piga-piga wari enda salah sada server [dev.karo] sipake man streaming ras ingan hosting project-project internal rempet mengkap-engkap, cek memory, disk I/O ras memoryna lalit masalahna. Enca nggo piga-piga dekahna dungna dat si erbansa masalah emekap file log ;) nggo lewat limit arah si bereken per akun, ras <<code>/tmp</code> pe dem alu log-log si la penting.

```
[ndikkar@dev] ls -lah *.log
-rw-r--r-- 1 karo karo 3.6G Mar 13 09:14 nohup.out
-rw-r--r-- 1 karo karo 115M Mar 13 09:18 sc_serv.log
-rw-r--r-- 1 karo karo 2.0G Feb  1 22:04 sc_trans.log
-rw-r--r-- 1 karo karo 183M Mar 13 09:14 sc_w3c.log
```

hapus empatna file sidatas, dung masalah :) cara ngapussa
```
rm -f *.log *.out
```

Server sipake jenda Debian 7 64 Bit. 



[dev.karo]:http://dev.karo.or.id
