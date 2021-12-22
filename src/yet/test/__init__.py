
MARKDOWN_FORMAT = 0

class Script:
    def __init__(self, args, devices=[], output_format=MARKDOWN_FORMAT, output='stdout'):
        self.devices = devices
        self.output_format = output_format
        self.output = output
