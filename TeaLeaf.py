import re
import sys
import pygame
from configparser import ConfigParser


class TeaLeaf:
    def __init__(self):
        self.config: ConfigParser = ConfigParser()
        self.config.read("./Config/Frame.ini")

        self.surface = pygame.display.set_mode(
            [int(i) for i in re.findall(r"\d+", self.config["General"]["Resolution"])],
            self.get_flag(),
            0,
            0,
            "TRUE" in self.config["General"]["Vsync"]
        )
        self.update = pygame.display.flip
        self.clock = pygame.time.Clock()
        self.fps: int = int(self.config["General"]["Fps"])

        pygame.display.set_caption(self.config["General"]["Caption"])

    def get_flag(self) -> int:
        def add_flag(f1, f2):
            if "TRUE" in f2.upper():
                return f1 | flags
            else:
                return flags

        flags = 0
        flags = add_flag(pygame.FULLSCREEN, self.config["Flags"]["FullScreen"])
        flags = add_flag(pygame.DOUBLEBUF, self.config["Flags"]["DoubleBuf"])
        flags = add_flag(pygame.OPENGL, self.config["Flags"]["OpenGL"])
        flags = add_flag(pygame.RESIZABLE, self.config["Flags"]["ReSizeable"])
        flags = add_flag(pygame.NOFRAME, self.config["Flags"]["NoFrame"])
        flags = add_flag(pygame.SCALED, self.config["Flags"]["Scaled"])
        flags = add_flag(pygame.SHOWN, self.config["Flags"]["Shown"])
        flags = add_flag(pygame.HIDDEN, self.config["Flags"]["Hidden"])
        return flags

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.tick()
            self.update()

            self.clock.tick(self.fps)

    def tick(self):
        pass
        # pygame.display.set_caption("Fps: %.3f" % self.clock.get_fps())


if __name__ == "__main__":
    pygame.init()
    TeaLeaf().mainloop()
