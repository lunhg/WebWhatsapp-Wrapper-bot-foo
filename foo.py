__bot__ = os.path.abspath(os.join(os.getcwd(), '..', 'lib')
sys.append(__bot__)
import bot

# Implement a abstract bot,
# with setup and run functions,
# Like a Java Processing Art Framework
class Foo(bot.Bot):

  def __init__(self, **kwargs):
    super(Foo, self).__init__(**kwargs)
    
    # Open and loads configuration for each
    # plugin
    for dir in os.listdir(kwargs.plugins):
      p = "%s/%s" % (kwargs.plugins, dir)
      if os.path.exists(p):
        self.plugin(name=dir, path=p)

  # A simple implementation of setup
  # loaded form configuration readed by a json file
  def setup(self):  
    super.setup(self.config)
    for key, val in self.config.iteritems():
      print "%s: %s" % (key, val)

  # A simple implementation of run with 0.1 seconds
  # between a call and another call, with
  # implementation of handle methods of each plugin
  def run(self):
    handles = [] 
    for key, val in self.config.iteritems():
      handle = self.__getattribute__(key).handle
      handles.append(handle)
    super.run(frameTime=0.1, callbacks=handles)
