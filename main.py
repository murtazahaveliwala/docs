import webapp2
from webapp2_extras.routes import RedirectRoute

app = webapp2.WSGIApplication([
  RedirectRoute('/apps/topeka/', name='topeka', redirect_to='http://polymer-topeka.appspot.com/', strict_slash=True),
  RedirectRoute('/apps/designer/', name='designer', redirect_to='http://polymer-designer.appspot.com/', strict_slash=True),
  RedirectRoute('/tools/designer/', name='designer', redirect_to='http://polymer-designer.appspot.com/', strict_slash=True),
  RedirectRoute('/apps/polymer-tutorial/finished/', name='tutorial', redirect_to='http://polymer-tut.appspot.com/', strict_slash=True),
  RedirectRoute('/docs/elements/core-elements.html', name='core-elements', redirect_to='/docs/elements/', strict_slash=True),
  RedirectRoute('/docs/elements/paper-elements.html', name='paper-elements', redirect_to='/docs/elements/', strict_slash=True)
], debug=False)
