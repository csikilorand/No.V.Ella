import obd


#ports = obd.scan_serial()      # return list of valid USB or RF ports
#print (ports) 

#has_command = obd.commands.has_pid(1, 03) # True
#print(has_command)
#connection = obd.OBD()
connection= obd.OBD("/dev/rfcomm99")
#connection.status() == OBDStatus.CAR_CONNECTED
#print(connection.status)
rpm  = obd.commands.RPM
fuel = obd.commands.FUEL_STATUS
response = connection.query(rpm)
response2 = connection.query(fuel)

print(response.value)
print(response2.value)

connection.close()
