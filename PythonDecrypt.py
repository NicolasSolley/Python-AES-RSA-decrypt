import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES

aeshash = '9101797ba6c5344' \
          '5ac4b703038ffd449'
mh = '4feca929a7bc7488a' \
     '47807ca719b1e77'
i = 0


iv = 16*b'\x00'
m = 0

for i in range(200):


    f = open("private_key_Directory" + str(i) + ".pem", "r")
    x = f.read()



    k = RSA.importKey(x)
    print(i)
    for m in range(200):



        message = open("session_key_Directory" + str(m) + ".eaes", "rb").read()
        try:
            n = PKCS1_OAEP.new(k)
            n2 = n.decrypt(message)


        except:

            pass
        else:
            print(i)
            key = hashlib.md5(n2).hexdigest()



            print(key)



            if key == aeshash:
                n3 = n2

                print("private_key" + str(i) + ".pem")


                print(key)
                print("session_key" + str(m) + ".eaes")



                break
for q in range(90001):

    f = open("Message_Directory" + str(q) + ".emsg", "rb").read()
    try:
        t = AES.new(n3, AES.MODE_CBC, iv)


        t2 = t.decrypt(f)
    except:
        pass
    else:
        key2 = hashlib.md5(t2).hexdigest()



        if key2 == mh:
            print("Correct Message:")


            print(t2)
            print("emessage" + str(q) + ".emsg")


            break

