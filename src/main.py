from src.core.core import Core

if __name__ == '__main__':
   core = Core()

   while(core.mgr.Quit()):
      core.update()
      core.render()

