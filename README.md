# Google PageSpeed Insights for Python

[![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg)]()

`pagespeed` offers a convenient interface for the Google PageSpeed Insights API.
It is written in Python and provides an easy way to query a site's page speed.

## Quickstart
Execute a query with:

```python
import pagespeed

ps = pagespeed.PageSpeed()
response = ps.analyse('https://www.example.com', strategy='desktop')
print(response.speed)
```

## Note
This is for Version 2 of the Google PageSpeed Insights API. The most recent version
is Version 4.