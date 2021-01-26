import socket
from typing import Text
import requests

number = 0
target_ip = '10.10.72.148'
# initial_port = 3010
target_port = 1337
last_port = 9765

print('''
**************************************************************************************************************************************
   .dMMMb  .aMMMb  .aMMMb  dMP dMP dMMMMMP dMMMMMMP        .aMMMb  dMMMMb  .aMMMb dMMMMMP dMP dMP        .dMMMb  dMP dMP dMMMMMMMMb 
  dMP" VP dMP"dMP dMP"VMP dMP.dMP dMP        dMP          dMP"VMP dMP.dMP dMP"dMP  .dMP" dMP.dMP        dMP" VP dMP dMP dMP"dMP"dMP 
  VMMMb  dMP dMP dMP     dMMMMK" dMMMP      dMP          dMP     dMMMMK" dMMMMMP .dMP"   VMMMMP         VMMMb  dMP dMP dMP dMP dMP  
dP .dMP dMP.aMP dMP.aMP dMP"AMF dMP        dMP          dMP.aMP dMP"AMF dMP dMP.dMP"   dA .dMP        dP .dMP dMP.aMP dMP dMP dMP   
VMMMP"  VMMMP"  VMMMP" dMP dMP dMMMMMP    dMP           VMMMP" dMP dMP dMP dMPdMMMMMP  VMMMP"         VMMMP"  VMMMP" dMP dMP dMP    
BY allexdiass
v: 1.0
**************************************************************************************************************************************
\n''')

print('[*] Iniciando...')
while True:
    try:
        if target_port != last_port:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect_ex((target_ip, target_port))
            client.send(
                f'GET / HTTP/1.1\r\nHost: http://{target_ip}\r\n\r\n'.encode('utf-8'))
            response = client.recv(1096)
            if ('HTTP/1.0 200 OK' in repr(response)):
                print('\n[!] conexão estabelecida com sucesso!')
                r = requests.get(url=f'http://{target_ip}:{target_port}')
                response = r.text.split(' ')
                if r.text.lower() == 'stop':
                    client.close()
                    break
                else:
                    print(f'[portas] porta atual:   {target_port}')
                    print(f'[valor atual] valor:    {number}')
                    print(
                        f'[operações] operação:   {response[0]} {response[1]}')
                    print(f'[portas] próxima porta: {response[2]}')
                    if response[0] == 'add':
                        number += float(response[1])
                    elif response[0] == 'minus':
                        number -= float(response[1])
                    elif response[0] == 'divide':
                        number /= float(response[1])
                    elif response[0] == 'multiply':
                        number *= float(response[1])
                    target_port = int(response[2])
                    print('*'*134)
            client.close()
        else:
            break
    except Exception as e:
        continue
print(f'[!!!] Resultado: {round(number, 2)}!')
