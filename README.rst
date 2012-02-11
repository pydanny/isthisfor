=========
isthisfor
=========

A way to validate your startup ideas. This project aids founders in the by prioritizing their helicopterization into the cloud!

Just seriously helicopterized the priorities of thousands of startups into the cloud at the http://www.ballmerpeakathon.com!!!

How it works
=============

* You create a pitch
* Others validate it by:

    * voting
    * comments

The crunchbase API
===================

https://gist.github.com/1226556::

    import requests
    r = requests.get('http://api.crunchbase.com/v/1/company/facebook.js')
    print(r.content)