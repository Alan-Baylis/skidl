from skidl import Pin, Part, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

bbd = SchLib(tool=SKIDL).add_parts(*[
        Part(name='MN3005',dest=TEMPLATE,tool=SKIDL,keywords='Matsushita Panasonic BBD',description='4096-STAGE LONG DELAY BBD (bucket brigade device), delay time 20.48ms to 204.8ms, S/N 75dB, clock frequency range 10KHz to 100KHz',ref_prefix='U',num_units=1,fplist=['DIP-8*'],do_erc=True,pins=[
            Pin(num='1',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='CP2',do_erc=True),
            Pin(num='3',name='OUT1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='4',name='OUT2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='5',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='6',name='CP1',do_erc=True),
            Pin(num='7',name='IN',do_erc=True),
            Pin(num='8',name='VGG',func=Pin.PWRIN,do_erc=True)]),
        Part(name='MN3007',dest=TEMPLATE,tool=SKIDL,keywords='Matsushita Panasonic BBD',description='1024-STAGE LOW NOISE BBD (bucket brigade device), delay time 5.12ms to 51.2ms, S/N 80dB, clock frequency range 10KHz to 100KHz',ref_prefix='U',num_units=1,fplist=['DIP-8*'],do_erc=True,pins=[
            Pin(num='1',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='CP1',do_erc=True),
            Pin(num='3',name='IN',do_erc=True),
            Pin(num='4',name='VGG',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='6',name='CP2',do_erc=True),
            Pin(num='7',name='OUT1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='8',name='OUT2',func=Pin.OUTPUT,do_erc=True)]),
        Part(name='MN3101',dest=TEMPLATE,tool=SKIDL,keywords='Matsushita Panasonic BBD CMOS',description='CMOS CLOCK GENERATOR/DRIVER FOR LOW VOLTAGE OPERATION BBD (bucket brigade device), for the MN3200 series BBD, self oscillation and separate exitation, two phase clock output, single supply source 4V to 10V',ref_prefix='U',num_units=1,fplist=['DIP-8*'],do_erc=True,aliases=['MN3102'],pins=[
            Pin(num='1',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='CP1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='3',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='CP2',func=Pin.OUTPUT,do_erc=True),
            Pin(num='5',name='OX3',do_erc=True),
            Pin(num='6',name='OX2',do_erc=True),
            Pin(num='7',name='OX1',do_erc=True),
            Pin(num='8',name='VGG_OUT',func=Pin.PWROUT,do_erc=True)]),
        Part(name='MN3207',dest=TEMPLATE,tool=SKIDL,keywords='Matsushita Panasonic BBD',description='1024-STAGE LOW VOLTAGE OPERATION LOW NOISE BBD (bucket brigade device), delay time 2.56ms to 51.2ms, S/N 73dB, clock frequency range 10KHz to 200KHz',ref_prefix='U',num_units=1,fplist=['DIP-8*'],do_erc=True,pins=[
            Pin(num='1',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='CP1',do_erc=True),
            Pin(num='3',name='IN',do_erc=True),
            Pin(num='4',name='VGG',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='6',name='CP2',do_erc=True),
            Pin(num='7',name='OUT1',func=Pin.OUTPUT,do_erc=True),
            Pin(num='8',name='OUT2',func=Pin.OUTPUT,do_erc=True)]),
        Part(name='RD5106A',dest=TEMPLATE,tool=SKIDL,keywords='EG&G RETICON BBD N-channel silicon-gate',description='Analog Delay Line 512 sample bucket brigade device, 1msec to more than 2seconds, input signal frequency range 0 to 170KHz, clock frequency range 500Hz to 1MHz',ref_prefix='U',num_units=1,fplist=['DIP-8*'],do_erc=True,aliases=['RD5107A'],pins=[
            Pin(num='1',name='Clock',do_erc=True),
            Pin(num='2',name='VSS',func=Pin.PWRIN,do_erc=True),
            Pin(num='3',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='4',name='Output',func=Pin.OUTPUT,do_erc=True),
            Pin(num='5',name='VBB',func=Pin.PWRIN,do_erc=True),
            Pin(num='6',name='Input',do_erc=True),
            Pin(num='7',name='Sync',do_erc=True),
            Pin(num='8',name='VDD',func=Pin.PWRIN,do_erc=True)]),
        Part(name='SAD1024',dest=TEMPLATE,tool=SKIDL,keywords='EG&G RETICON BBD N-channel silicon-gate',description='SAD-512 ANALOG DELAY LINE, bucket brigade device, 512 stages, signal frequency range 0 to 200KHz, clock frequency range 1.5KHz to 1.5MHz',ref_prefix='U',num_units=2,fplist=['DIP-16*'],do_erc=True,aliases=['SAD512'],pins=[
            Pin(num='1',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='4',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='7',name='Vdd',func=Pin.PWRIN,do_erc=True),
            Pin(num='9',name='Vbb',func=Pin.PWRIN,do_erc=True),
            Pin(num='13',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='16',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='2',name='IN_A',do_erc=True),
            Pin(num='3',name='02A',do_erc=True),
            Pin(num='5',name='OUT_A',func=Pin.OUTPUT,do_erc=True),
            Pin(num='6',name="OUT_A'",func=Pin.OUTPUT,do_erc=True),
            Pin(num='8',name='01A',do_erc=True),
            Pin(num='10',name='01B',do_erc=True),
            Pin(num='11',name="OUT_B'",func=Pin.OUTPUT,do_erc=True),
            Pin(num='12',name='OUT_B',func=Pin.OUTPUT,do_erc=True),
            Pin(num='14',name='02B',do_erc=True),
            Pin(num='15',name='IN_B',do_erc=True)]),
        Part(name='TDA1022',dest=TEMPLATE,tool=SKIDL,keywords='PHILIPS BBD MOS monolithic delay analogue',description='BUCKET BRIGADE DELAY LINE FOR ANALOGUE SIGNALS, 512 stages, delay time 0.512ms to 51.2ms, signal frequency range 0 to 45KHz, clock frequency range 5KHz to 500KHz',ref_prefix='U',num_units=1,fplist=['DIP-16*'],do_erc=True,pins=[
            Pin(num='1',name='CL1',do_erc=True),
            Pin(num='2',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='3',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='4',name='CL2',do_erc=True),
            Pin(num='5',name='Input',do_erc=True),
            Pin(num='6',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='7',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='8',name='Output513',func=Pin.OUTPUT,do_erc=True),
            Pin(num='9',name='VDD',func=Pin.PWRIN,do_erc=True),
            Pin(num='10',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='11',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='12',name='Output512',func=Pin.OUTPUT,do_erc=True),
            Pin(num='13',name='V13-16',func=Pin.PWRIN,do_erc=True),
            Pin(num='14',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='15',name='NC',func=Pin.NOCONNECT,do_erc=True),
            Pin(num='16',name='GND',func=Pin.PWRIN,do_erc=True)])])