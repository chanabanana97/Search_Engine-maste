class ConfigClass:

    def __init__(self):
        self.corpusPath = ""
        self.savedFileMainFolder = ""
        self.saveFilesWithStem = self.savedFileMainFolder + "\\WithStem"
        self.saveFilesWithoutStem = self.savedFileMainFolder + "\\WithoutStem"
        self.toStem = False

    def get__corpusPath(self):
        return self.corpusPath
