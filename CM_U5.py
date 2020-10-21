import time
import smbus

channel = 0

address = 0x50


# Initialize I2C (SMBus)
bus = smbus.SMBus(channel)

data = [0x50,0x00,12,17,48,56,67,78,89]  #[slave_addr, reg_add,data....]
bus.write_i2c_block_data(address, 0, data)

time.sleep(1)

data = [0x51]
bus.write_i2c_block_data(address,0,data)

block = bus.read_i2c_block_data(address,0,32)
print(block)

bus.close()