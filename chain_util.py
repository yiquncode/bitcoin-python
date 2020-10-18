import uuid
import hashlib
import ecdsa

class ChainUtil:
    @staticmethod
    def gen_key_pair():
        # More info: https://www.programcreek.com/python/example/81785/ecdsa.SECP256k1
        return ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

    @staticmethod
    def id():
        return str(uuid.uuid1())

    @staticmethod
    def to_hash(data):
        m = hashlib.sha256()
        data = bytes(data.encode('utf-8'))
        m.update(data)
        return m.digest()

    @staticmethod
    # To verify an existing signature with a public key
    def verify_sig(public_key, signature, data_hash):
        # https://stackoverflow.com/questions/34451214/how-to-sign-and-verify-signature-with-ecdsa-in-python
        # print(f'public_key: {public_key}')
        # print(f'signature: {signature}')
        # print(f'data_hash: {data_hash}')

        vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.SECP256k1)
        
        try:
            return vk.verify(signature, data_hash)
        except ecdsa.keys.BadSignatureError:
            return False
