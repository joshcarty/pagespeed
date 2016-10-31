import pagespeed

p = pagespeed.PageSpeed()

r = p.analyse('https://www.example.com', strategy='desktop')

print(r.speed)