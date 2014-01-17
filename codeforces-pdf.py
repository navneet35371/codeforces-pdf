import urllib2
import pdfkit

base_url = 'http://codeforces.com/problemset/problem/'
a = []
b = ['A','B','C','D','E']
for i in range(1,381):
	for j in range(0,5):
		ur = base_url+str(i)+'/'+b[j]
		response = urllib2.urlopen(ur)
		html = response.read()
		idx = html.find('<!-- Codeforces javascripts. -->')
		orig = html[:idx]
		idx = html.find('<div class="ttypography">')
		orig +=html[idx:]
		idx = orig.find('<script type="text/javascript">')
		orig = orig[:idx]
		orig+='</div></body></html>'
		a.append(orig)

pdfkit.from_file(a, 'out.pdf')
