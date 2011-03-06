import urllib2
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import re

class GetSong(webapp.RequestHandler):
    def get(self):
        song = re.search(r'(soundcloud.*)$', self.request.path)
        if(song and song.group(1)):
            url = "http://www." + song.group(1)
            song = urllib2.urlopen(url).read()
            count= 0
            self.response.out.write("<html><body style='background-image: url(/img/background.jpg);'>")

            for m in re.finditer(r'"name"[^"]+"([^"]+).+?streamUrl"[^"]+"([^"]+)', song):
                count = count + 1
                self.response.out.write("<a style='color: white' href='%s'>%s</a><br />"% (m.group(2),m.group(1)))
            self.response.out.write("</body></html>")
        else:
            self.response.out.write("<html><body style='background-image: url(/img/background.jpg);"+
            "'><h1 style='color:white'>Please enter a soundcloud URL.<br /> An example: <a href='http://adichatclient.appspot.com/soundcloud.com/akiva'>http://adichatclient.appspot.com/soundcloud.com/akiva</a>.<br /><br />Then, open the link and press CTRL+S to save the mp3!<br />Confused? Read this whole thing over again.</h1></body><html>")

apps_binding = []
apps_binding.append(('/.*', GetSong)) 
application = webapp.WSGIApplication(apps_binding, debug=False)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()