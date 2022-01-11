from yet.test import Script
from yet.workbench import *

if __name__ == '__main__':
    wb = Workbench(args, instruments=['scope', 'spi', 'la'])
    tst = Script(brief='Button Test')
    tst.step('Configure the instruments')
    wb.scope.configure(class=Oscilloscope, channels=['VbatVdc', 'VbatIdc'])
    wb.scope.VbatVdc.set_y_range(min=-1.0, max=4.0)
    wb.scope.VbatIdc.set_y_units(AMPERES)
    wb.scope.VbatIdc.set_y_gain(0.05) #Volts per Ampere
    wb.scope.set_x_range(min=-1.0, max=10.0)
    wb.scope.set_trigger(mode=NORMAL_TRIGGER_MODE, source=MANUAL_TRIGGER_SOURCE)
    wb.spi.configure(class=SpiMaster, channels=['Switcher'])
    wb.spi.Switcher.configure(class=Max17432SwitchArray, channels=['', ''])
    wb.la.configure(class=LogicAnalyzer, channels=['RedPwm', 'GreenPwm', 'BluePwm', 'IrPwm'])
    tst.case('')
    tst.step('')
    wb.scope.setup()
    wb.meter.setup()
    tst.prompt('')
    tst.verify_step('')
    tst.end_case()
    tst.end()
