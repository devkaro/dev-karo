Title: Tes Geo DNS dl.karo.or.id
Date: 2014-02-06 23:35
Author: Surbakti
Category: News
Tags: serper, dns
Slug: tes-geo-dns-dl.karo.or.id

Aku pe enda situhuna labo kuangka kai, saja mari sicubaken erbansa :) Sienda labo tutorial, tapi hasil tesna saja ngenca. Ceritana lit 5 serper si tes erban Geo DNS enda, man settingen DNS-na kupake dnsmadeeasy, aktifken Geo DNS-na, dung e tambahken kerina IP serper ta ndai. Siban contohna ipna : 
```
192.168.1.1 - Amerika
192.168.1.2 - Amerika
192.168.1.3 - Amerika
192.168.1.4 - Jerman
192.168.1.5 - Inggris
```

bas masing-masing serper enda, OS-na si kupake Debian 7. Tambahken 1 virtualhost, ras ban kerina seri path domain ras ingan file-na, gelahna la mesera copy pastena, misalken bas /var/www/dl.karo.or.id, dung e restart apache. 
Enggo kenca dung kerina, buka cubaken alamat http://dl.karo.or.id ndai bas browserndu, siapai si ndeherna ku kita emekap ip sidat. Adina la arah browser pe banci ka ketik perintah `host dl.karo.or.id` bas terminal Linux. 
```
host dl.karo.or.id
```
hasilna perintah sidatas
```
dl.karo.or.id has address 88.150.xx.xxx
dl.karo.or.id has IPv6 address 2607:xxxxxx:xxxxx:xxxxx
```

Perintah enda banci cubakenndu, adina kam pake Windows banci ketik `ping dl.karo.or.id`. Tulisen enda lenga fix, bagi draft denga, adina lit kari waktu ku edit mulihi. 

Tujunna Geo DNS enda emekap, apai serper si ndeherna ras user-ta eme si mbereken respon ras nampilken websiteta, mbue kurang ras lebihna cara si enda, adina kam erban blog statik (bagi blog enda), cocok kel pake cara si enda ;)
