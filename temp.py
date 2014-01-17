import urllib2
import pdfkit

a = []
response = urllib2.urlopen('http://codeforces.com/problemset/problem/222/A')
html = response.read()
idx = html.find('<!-- Codeforces javascripts. -->')
orig = html[:idx]
idx = html.find('<div class="ttypography">')
orig +=html[idx:]
idx = orig.find('<script type="text/javascript">')
orig = orig[:idx]
orig+='</div></body></html>'
a.append(orig)

pdfkit.from_string(orig, 'outtemp.pdf')
