#duck typing
class vscode:
    def execute(self):
        print("better night mode")


class myeditor:
    def execute(self):
        print("spell check")
        print('older gui')

class laptop:
    def code(self,ide):
        ide.execute()

ide=vscode()

l1=laptop()
l1.code(ide)
