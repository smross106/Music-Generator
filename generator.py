import wave,random,struct,math

SAMPLE_LEN = 5000

noise_output = wave.open('noise4.wav', 'w')
noise_output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

values = []

for i in range(0, SAMPLE_LEN):
        #value = random.randint(-32767, 32767)
        if i%2 == 0:
            value = math.sin(i) * 32767
        packed_value = struct.pack('h', value)
        values.append(packed_value)
        values.append(packed_value)
print("done")
value_str = ''.join(values)
noise_output.writeframes(value_str)

noise_output.close()
