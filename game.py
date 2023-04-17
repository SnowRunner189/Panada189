# напиши здесь код основного окна игры
from direct.showbase.ShowBase import ShowBase
from hero import Hero
from mapmanager import Mapmanager



class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.player = Hero()
base = Game()
base.camLens.setFov(90)
base.run()