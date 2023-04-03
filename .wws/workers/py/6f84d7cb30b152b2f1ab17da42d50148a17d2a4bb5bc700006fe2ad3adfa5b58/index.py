from poly import *

message =  '.daed era meht fo owt fi ,terces a peek nac eerhT'
translated = ''

i = len(message) - 1
#print(i)
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)


res = worker(Request(json.loads(sys.stdin.read())))
print(res.to_json())
