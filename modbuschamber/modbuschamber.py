from pymodbus.client.sync import ModbusSerialClient

class WatlowF4Chamber(object):
    def __init__(self, port, baudrate=19200, addr=1, silent=False):
        self.addr = addr

        self.client = ModbusSerialClient(method='rtu', port=port, baudrate=baudrate)
        self.client.connect()

        self.diags = self.read_diagnostics()
        
        # Sanity check - do we have a Watlow F4 controller?
        if self.diags['model'] != 'F4':
            print(self.diags)
            raise IOError("Did not detect Watflow F4?")

        if silent is False:
            print("Found Watflow F4:")
            print("   Model: {}".format(self.diags['model']))
            print("      SN: {}".format(self.diags['sn']))
        
        # Check units & decimal points match expected
        regs = self.client.read_holding_registers(606, 3, unit=self.addr).registers

        # This needs to match
        if regs[0] != 1:
            raise IOError("606: Input 1 decimal point setting mismatch!")
        
        # Shouldn't latch input temp
        if regs[1] != 0:
            raise IOError("607: Input 1 error setting mismatch!")

        # Register 608 should be unit (F/C) - probably code works fine either way
        # but I've only tested it with C.
        if regs[2] != 0:
            raise IOError("608: Input 1 Unit mismatch [maybe ignorable?]")

    def read_diagnostics(self):
        """Read diagnostics registers"""
        regs = self.client.read_holding_registers(0, 6, unit=self.addr)
        model = str(regs.registers[0])
        # This register is '5270' decimal, where chr(70) chr(52) == F4
        modelascii = chr(int(model[2:])) + chr(int(model[0:2]))
        diags = {'model':modelascii, 
                 'sn':str(regs.registers[1]) + str(regs.registers[2]),
                 'dom':str(regs.registers[5])}
        return diags

    def read_temp(self):
        """Read input 100 (Input 1, temp)"""
        value = self.client.read_input_registers(100, 1, unit=self.addr).registers[0]
        return(self._conv_binary_to_temp(value))

    def get_process_temp(self):
        """Get process (setpoint) temp"""
        value = self.client.read_holding_registers(300, 1, unit=self.addr).registers[0]
        return(self._conv_binary_to_temp(value))

    def set_process_temp(self, temp):
        """Set process (setpoint) temp"""
        v = self._conv_temp_to_binary(temp)
        self.client.write_register(300, v, unit=self.addr)

    def _conv_binary_to_temp(self, value):
        """Covert raw int to floating temp value (internal usage)"""
        value = value-2**16 if value & 2**15 else value
        value = value / 10.0
        return value
    
    def _conv_temp_to_binary(self, value):
        """Convert floating temp value to raw int (internal usage)"""
        value = int(value * 10)
        if value < 0:
            value = (value + 2**16) | 2**15
        return value
    
    def dump_all_regs(self, end=5504, verbose=True):
        """Dumps all registers (even invalid ones) for debug/backup"""
        all = ""
        for i in range(0, end):
            reg = self.client.read_holding_registers(i, 1, unit=self.addr)
            s = "{}: {}".format(i, reg.registers[0])
            if verbose:
                print(s)
            all += s + "\n"
        return all

if __name__ == "__main__":
    import time
    chamber = WatlowF4Chamber("com3")

    chamber.set_process_temp(-22.1)

    print("Setpoint = {} °C".format(chamber.get_process_temp()))

    print("Actual = {} °C".format(chamber.read_temp()))

    #for i in range(-60, 200, 5):
    #    chamber.set_process_temp(i)
    #    print("Setpoint = {} °C".format(chamber.get_process_temp()))

    while(True):
        print("{} °C".format(chamber.read_temp()))
        time.sleep(2)

    #with open('register_settings.txt', "w") as file:
    #    regs = chamber.dump_all_regs()
    #    file.write(regs)
